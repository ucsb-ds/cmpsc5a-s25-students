OK_FORMAT = True

test = {   'name': 'q5_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> difference_from_expected.size == 272\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> difference_from_expected.item(271) == abs(60 * 272 - sum(waiting_times))\nTrue', 'hidden': False, 'locked': False},
                                
                                   {'code': '>>> np.all(np.isclose(difference_from_expected,np.abs(np.cumsum(waiting_times) - ((np.arange(len(waiting_times)) + 1 ) * 60))))\nTrue', 'hidden': False, 'locked': False}
                               
                               
                               ],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
