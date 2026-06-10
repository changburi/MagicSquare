from validate_lines import LINE_IDS, MAGIC_SUM, ValidationResult, validate_lines


def test_t2_r2_c2_intersection_fail():
    # Arrange — STEP 1 완성 격자, 1-based (2,2) R2·C2 교차셀 10→11 (합 34→35)
    grid = [
        [16,  3,  2, 13],
        [ 5, 11, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "R2" in result["failed_lines"]
    assert "C2" in result["failed_lines"]
