OK_FORMAT = True

test = {
    "name": "q31",
    "points": None,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> type(top_10_movies) == tables.Table\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> top_10_movies.select('Rating', 'Name').sort('Name')\nRating | Name\n8.9    | 12 Angry Men (1957)\n8.9    | Il buono, il brutto, il cattivo (1966)\n8.9    | Pulp Fiction (1994)\n8.9    | Schindler's List (1993)\n8.9    | The Dark Knight (2008)\n9.2    | The Godfather (1972)\n9      | The Godfather: Part II (1974)\n8.8    | The Lord of the Rings: The Fellowship of the Ring (2001)\n8.9    | The Lord of the Rings: The Return of the King (2003)\n9.2    | The Shawshank Redemption (1994)",
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
