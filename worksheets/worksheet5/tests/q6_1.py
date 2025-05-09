OK_FORMAT = True

test = {   'name': 'q6_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> fruits.sort(0).column(0).item(0) == 'apples'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> fruits.sort(0).column(1).item(0) == 4\nTrue', 'hidden': False, 'locked': False},
                                {'code': '>>> np.all(fruits.sort(0).column(0) == make_array("apples","oranges","pineapples"))\nTrue', 'hidden': False, 'locked': False},
                                {'code': '>>> np.all(fruits.sort(0).column(1) == make_array(4,3,2))\nTrue', 'hidden': False, 'locked': False}
                               ],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
