#     "q211": {
#      "name": "q211",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> import math\n>>> np.isclose(sine_of_pi_over_four, 0.7071067811865475)\nTrue",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q32": {
#      "name": "q32",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> num_farmers_markets_columns == 59\nTrue",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q33": {
#      "name": "q33",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> sorted(farmers_markets_locations.labels) == ['MarketName', 'State', 'city', 'x', 'y']\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> farmers_markets_locations.num_rows == 8546\nTrue",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q34": {
#      "name": "q34",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> farmers_markets_without_fmid.num_columns == 57\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> print(sorted(farmers_markets_without_fmid.labels))\n['Bakedgoods', 'Beans', 'Cheese', 'Coffee', 'County', 'Crafts', 'Credit', 'Eggs', 'Facebook', 'Flowers', 'Fruits', 'Grains', 'Herbs', 'Honey', 'Jams', 'Juices', 'Location', 'Maple', 'MarketName', 'Meat', 'Mushrooms', 'Nursery', 'Nuts', 'Organic', 'OtherMedia', 'PetFood', 'Plants', 'Poultry', 'Prepared', 'SFMNP', 'SNAP', 'Seafood', 'Season1Date', 'Season1Time', 'Season2Date', 'Season2Time', 'Season3Date', 'Season3Time', 'Season4Date', 'Season4Time', 'Soap', 'State', 'Tofu', 'Trees', 'Twitter', 'Vegetables', 'WIC', 'WICcash', 'Website', 'WildHarvested', 'Wine', 'Youtube', 'city', 'street', 'x', 'y', 'zip']\n",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q35": {
#      "name": "q35",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> type(farmers_markets_locations_by_latitude) == tables.Table\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> list(farmers_markets_locations_by_latitude.column('y').take(range(3))) == [64.86275, 64.8459, 64.844414]\nTrue",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q36": {
#      "name": "q36",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> goleta_markets.num_rows == 2\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> list(goleta_markets.column('city')) == ['Goleta', 'Goleta']\nTrue",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q41": {
#      "name": "q41",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> type(above_eight) == tables.Table\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> above_eight.num_rows == 20\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> print(above_eight.sort(0).take([17]))\nTitle       | Rating\nToy Story 3 | 8.3\n",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     },
#     "q42": {
#      "name": "q42",
#      "points" : None,
#      "suites": [
#       {
#        "cases": [
#         {
#          "code": ">>> proportion_in_20th_century == 0.684\nTrue",
#          "hidden": False,
#          "locked": False
#         },
#         {
#          "code": ">>> proportion_in_21st_century == 0.316\nTrue",
#          "hidden": False,
#          "locked": False
#         }
#        ],
#        "scored": True,
#        "setup": "",
#        "teardown": "",
#        "type": "doctest"
#       }
#      ]
#     }
#    }
