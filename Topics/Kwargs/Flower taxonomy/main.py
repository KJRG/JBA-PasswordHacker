iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    values = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    values.update(kwargs)
    iris[id_n] = values
