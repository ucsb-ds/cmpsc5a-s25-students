OK_FORMAT = True

test = {   'name': 'q1_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(model_proportions) % 2 == 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(np.unique(model_proportions)) == 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> sum(model_proportions) == 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(simulation_proportion_correct) == float or type(simulation_proportion_correct)==np.float64\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0 <= one_statistic <= 25\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
