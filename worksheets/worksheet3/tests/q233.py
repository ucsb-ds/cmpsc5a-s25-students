OK_FORMAT = True

test = {
    "name": "q233",
    "points": None,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> type(more_total_charges) == np.ndarray\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> sum(abs(more_total_charges - 1.2 * more_restaurant_bills)) < 1e-06\nTrue",
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
