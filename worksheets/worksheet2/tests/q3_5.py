OK_FORMAT = True

test = {
     "name": "q3_5",
     "points" : None,
     "suites": [
      {
       "cases": [
        {
         "code": ">>> type(farmers_markets_locations_by_latitude) == tables.Table\nTrue",
         "hidden": False,
         "locked": False
        },
        {
         "code": ">>> list(farmers_markets_locations_by_latitude.column('y').take(range(3))) == [64.86275, 64.8459, 64.844414]\nTrue",
         "hidden": False,
         "locked": False
        }
       ],
       "scored": True,
       "setup": "",
       "teardown": "",
       "type": "doctest"
      }
     ]
    }
