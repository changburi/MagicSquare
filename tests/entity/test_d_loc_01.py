import pytest

from entity.location import find_blank_coords


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given — D-LOC-01: G1 격자 (0이 2개, row-major)
    grid = grid_g1

    # When — find_blank_coords(grid_g1) 호출
    coords = find_blank_coords(grid)

    # Then — [(2,4), (3,3)] (1-index, row-major); GREEN에서 assert 교체
    pytest.fail("RED: D-LOC-01 — [(2, 4), (3, 3)] row-major")
