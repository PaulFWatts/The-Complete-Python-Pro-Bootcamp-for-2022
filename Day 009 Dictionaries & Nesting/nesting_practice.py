""" Nesting """

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lyon", "Marseille"],
    "Germany": ["Berlin", "Munich", "Frankfurt"],
}

# Nesting a List in a List

["A", "B", ["C", "D"]]

# Nesting a Dictionary in a Dictionary

travel_log_enhanced = {
    "France": {"cities_visited": ["Paris", "Lyon", "Marseille"], "total_visits": 3},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Frankfurt"], "total_visits": 5},
}

# Nesting a Dictionary in a List

travel_log_final = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lyon", "Marseille"],
        "total_visits": 3},
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Frankfurt"],
        "total_visits": 5},
]
