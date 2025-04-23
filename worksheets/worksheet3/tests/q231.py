OK_FORMAT = True

test = {
    "name": "q231",
    "points": None,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> type(population_magnitudes) == np.ndarray\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> sum(abs(population_magnitudes - np.log10(population_amounts))) < 1e-06\nTrue",
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
