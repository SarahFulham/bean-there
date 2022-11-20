INITIAL_DATA = {
    'cafes': [
        {
            'name': 'Noble Café',
            'address': '430 Laurier Ave E',
            'features':{
                'wifi': "Not Available",
                'food': "Croissants, Ice Cream, Scones, Cookies",
                'outlets': "Not Available"
            },
            'images': [
                'frontend/public/images/noble_1.jpg',
                'frontend/public/images/noble_2.jpg',
            ]
        },
                {
            'name': 'Cafe Myriade - Le Plateau',
            'address': '4647 Saint Denis St',
            'features':{
                'wifi': "Spotty",
                'food': "Croissants, Scones, Muffins",
                'outlets': "Available at some tables"
            },
            'images': [
                'frontend/public/images/myriade_1.jpg',
                'frontend/public/images/myriade_2.jpg',
            ]
        },
        {
            'name': 'Caffè In Gamba',
            'address': '5263 Park Ave',
            'features':{
                'wifi': "Strong",
                'food': "Croissants, Scones, Danishes, Muffins, Cookies",
                'outlets': "Available at at all tables"
            },
            'images': [
                'frontend/public/images/gamba_1.jpg',
                'frontend/public/images/gamba_2.jpg',
            ]
        }
    ]
}
def seed_table(target, connection, **kw):
    tablename = str(target)
