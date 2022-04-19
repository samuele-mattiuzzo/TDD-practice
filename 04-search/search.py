DATABASE = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul"
]

WILDCARD_ALL = "*"

def search(text):
    # wildcard: return all
    if text == WILDCARD_ALL:
        return DATABASE

    # min 2 char per search term
    if len(text) < 2:
        return []

    # match
    return [
        city for city in DATABASE if (
            city.lower().startswith(text.lower()) or
            text.lower() in city.lower()
        )
    ]
