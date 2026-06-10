import pytest

# G1 — STEP 1 퍼즐, 빈칸(0) 2개, row-major (픽스처 데이터만; 상수는 GREEN 시 entity/constants.py)
G1_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  0],
    [ 9,  6,  0, 12],
    [ 4, 15, 14,  1],
]


@pytest.fixture
def grid_g1():
    return [row[:] for row in G1_GRID]
