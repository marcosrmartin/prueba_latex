import genetic
import mock


def test_individual():
    config = genetic.individual()
    assert(len(config) == genetic.genes)


def test_initialize():
    population = genetic.initialize()
    assert(len(population) == genetic.individuals)


@mock.patch('genetic.fitness', return_value=1)
def test_selection_and_reproduction(function):

    population = [
        [1523, 42, 0, 1, 1, 2045, 537, 1, 1, 2, 2, 0, 0],
        [1971, 117, 0, 1, 0, 1140, 1737, 1, 1, 2, 2, 0, 0],
        [882, 101, 1, 0, 0, 986, 644, 0, 1, 1, 5, 0, 0],
        [1529, 70, 1, 1, 1, 1462, 1834, 0, 0, 1, 1, 1, 0],
    ]

    expected_result = [
        [1971, 117, 0, 1, 0, 1140, 1737, 1, 1, 2, 2, 0, 0],
        [1529, 70, 1, 1, 1, 1462, 1834, 0, 0, 1, 1, 1, 0],
        [1523, 42, 0, 1, 1, 2045, 537, 1, 1, 2, 2, 0, 0],
        [882, 101, 1, 0, 0, 986, 644, 0, 1, 1, 5, 0, 0]
    ]

    result = genetic.selection_and_reproduction(population)

    assert(result == expected_result)


@mock.patch('random.random', return_value=0.1)
@mock.patch('fitness.generate_random_config', return_value=[200, 39, 0, 1, 0, 1033, 1933, 1, 0, 2, 3, 0, 1])
def test_mutation(function1, function2):
    population = [
        [1523, 42, 0, 1, 1, 2045, 537, 1, 1, 2, 2, 0, 0],
        [1971, 117, 0, 1, 0, 1140, 1737, 1, 1, 2, 2, 0, 0],
        [882, 101, 1, 0, 0, 986, 644, 0, 1, 1, 5, 0, 0],
        [1529, 70, 1, 1, 1, 1462, 1834, 0, 0, 1, 1, 1, 0],
    ]
    expected_result = [
        [1523, 42, 0, 1, 1, 2045, 537, 1, 1, 2, 2, 0, 0],
        [1971, 117, 0, 1, 0, 1140, 1737, 1, 1, 2, 2, 0, 0],
        [882, 101, 1, 0, 0, 986, 644, 0, 1, 1, 5, 0, 0],
        [1529, 70, 1, 1, 1, 1462, 1834, 0, 0, 1, 1, 1, 0]
    ]
    result = genetic.mutation(population)
    assert(result == expected_result)
