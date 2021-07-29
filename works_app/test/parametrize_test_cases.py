create_work_list_test_cases = {
    'correct_parameters': [
        {
            'title': 'Lagrimas Negras',
            'contributors':['El Cigala','Bebo Valdes'],
            'iswc': '1d3235'
        },
        {
            'title': 'La Vida Sale',
            'contributors':['Jose Merce'],
            'iswc': '1d3sadfs235'
        },
    ],

    'one_contributor_in_list': {
        'title': 'Imagine',
        'contributors':['Lennon'],
        'iswc': '1d3235'
    },

    'no_list_on_parameters': {
        'title': 'Raval Ruina',
        'contributors':'Ayax',
        'iswc': '1d3235'
    },

    'repeted_iswc': [
        {
            'title': 'No Logic',
            'contributors':['Wade'],
            'iswc': '1d3235'
        },
        {
            'title': 'No Logic',
            'contributors':['Wade'],
            'iswc': '1d3235'
        }
    ]
}