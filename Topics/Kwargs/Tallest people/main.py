def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    tallest_people_names = (n for n, h in kwargs.items() if h == max_height)
    for name in sorted(tallest_people_names):
        print(name, ':', kwargs.get(name))
