INITIAL_DATA = {
    'cafes': [
        {
            'name': 'banbeanzzle',
            'address': 'montreal',
            'features':{
                'wifi': "strong",
                'food': "fantastic",
                'outlets': "plenty"
            }
        },
                {
            'name': 'conors cafe',
            'address': 'oakville',
            'features':{
                'wifi': "weak",
                'food': "garbage",
                'outlets': "none"
            }
        },
                {
            'name': 'sarahs cafe',
            'address': 'delray',
            'features':{
                'wifi': "stronger",
                'food': "french",
                'outlets': "3"
            }
        }
    ]
}
def seed_table(target, connection, **kw):
    tablename = str(target)
