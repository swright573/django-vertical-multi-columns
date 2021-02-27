"""
Simulate the data that would probably normally be returned in an API call

"""


def api_data_decoded_json():
    """Data to be displayed in a VMC view"""
    return [
        {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
        {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
        {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
        {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
        {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
        {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
        {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
        {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
        {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
        {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
        {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
        {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
        {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
        {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
        {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
        {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
        {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
        {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
        {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
        {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
        {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
        {"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False},
        {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
        {"id": 43, "name": "Okra", "colour": "green", "count": 4, "herb": False},
        {"id": 18, "name": "Onion", "colour": "white", "count": 5, "herb": False},
        {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
        {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
        {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
        {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
        {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
        {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
        {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
        {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
        {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
        {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
        {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
        {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
        {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
        {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
        {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
        {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
        {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
        {"id": 32, "name": "Turnips", "colour": "white", "count": 7, "herb": False},
        {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
        {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
    ]
    
def api_data_decoded_json_with_all_data_types():
    """Data to be displayed in a VMC view"""
    return [
        {'id': 1, 'string': 'Peter', 'number': 35, 'boolean': True, 'empty': None, 'object': {'a': 'abcde', 'b': 3}, 'array': [1, 2, 3]},
        {'id': 2, 'string': 'Susan', 'number': 42, 'boolean': False, 'empty': None, 'object': {'a': 'fghij', 'b': 32}, 'array': [11, 12, 13]},
        {'id': 3, 'string': 'Graham', 'number': 22, 'boolean': True, 'empty': None, 'object': {'a': 'klmno', 'b': 90}, 'array': [111, 112, 113]},
        {'id': 4, 'string': 'Lindsay', 'number': 22, 'boolean': False, 'empty': None, 'object': {'a': 'pqrst', 'b': 90}, 'array': [99, 102, 127]},
        {'id': 5, 'string': 'Indy', 'number': 22, 'boolean': False, 'empty': None, 'object': {'a': 'uvwyz', 'b': 90}, 'array': [59, 37, 111]},
    ]
   