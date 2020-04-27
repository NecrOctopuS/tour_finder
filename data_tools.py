def get_departure_tours(departure, tours):
    departure_tours = {}
    for id, tour in tours.items():
        if tour['departure'] == departure:
            departure_tours[id] = tour
    return departure_tours


def get_base_data(data):
    base_data = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
    }
    return base_data


def get_tour_data(data, id):
    tour_data = data.tours[id]
    departure = tour_data['departure']
    tour_data['departure'] = data.departures[departure]
    stars_count = int(tour_data['stars'])
    tour_data['stars'] = '★' * stars_count
    return tour_data
