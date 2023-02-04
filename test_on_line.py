import pytest


@pytest.mark.parametrize("coordinate1, coordinate2, x, y",
                         [((0, 0), (1, 1), 0.5, 0.5),
                          ((0, 0), (1, 2), 0.5, 1),
                          ((0, 5), (10, 0), 4, 3)])
def test_y_online(coordinate1, coordinate2, x, y):
    from on_line import y_online
    answer = y_online(coordinate1, coordinate2, x)
    assert answer == y
