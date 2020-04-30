from flask import Flask, render_template
import data
from data_tools import get_departure_tours, get_base_data, get_tour_data, get_tours_for_main_page

app = Flask(__name__)

NUMBER_OF_TOURS_ON_MAIN_PAGE = 6


@app.route('/')
def render_main():
    base_data = get_base_data(data)
    tours = get_tours_for_main_page(data, NUMBER_OF_TOURS_ON_MAIN_PAGE)
    return render_template('index.html', data=base_data, tours=tours)


@app.route('/departures/<departure>')
def render_departure(departure):
    base_data = get_base_data(data)
    departure_tours = get_departure_tours(departure, data.tours)
    return render_template('departure.html', data=base_data, tours=departure_tours, departure=departure)


@app.route('/tours/<int:id>/')
def render_tour(id):
    base_data = get_base_data(data)
    tour = get_tour_data(data, id)
    return render_template('tour.html', data=base_data, tour=tour)


if __name__ == '__main__':
    app.run()
