import pytest
from servicemon.cone import Cone


def validate_cone(num_points, min_radius, max_radius):
    gen = Cone.generate_random(num_points, min_radius, max_radius)
    prev = {'ra': 0, 'dec': 0, 'radius': 0}
    points = list(gen)
    assert len(points) == num_points
    for cone in gen:
        assert 0 <= cone['ra'] < 360
        assert -90 <= cone['dec'] < 90
        assert min_radius <= cone['radius'] <= max_radius

        assert cone['ra'] != prev['ra']
        assert cone['dec'] != prev['dec']
        assert cone['radius'] != prev['radius']

        prev = cone


def test_random():
    validate_cone(100, 0.01, 1.5)
    validate_cone(10000, 14.5, 102)


def test_errors():
    with pytest.raises(ValueError) as e_info:
        Cone.random_cone(2, 1)
    assert ('min-radius must be in the range [0,max_radius).'
            in str(e_info.value))

    with pytest.raises(ValueError) as e_info:
        Cone.generate_random(20, 3, 1)
    assert ('min-radius must be in the range [0,max_radius).'
            in str(e_info.value))

    with pytest.raises(ValueError) as e_info:
        Cone.generate_random(-14, 6, 7)
    assert ('num_points must be a positive number.'
            in str(e_info.value))
