OK_FORMAT = True

test = {
    "name": "q235",
    "points": None,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> all(powers_of_2 == 2 ** np.arange(30))\nTrue",
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
