from typing import Literal, TypedDict

MAGIC_SUM = 34

LINE_IDS = (
    "R1", "R2", "R3", "R4",
    "C1", "C2", "C3", "C4",
    "D1", "D2",
)

Status = Literal["pass", "fail", "incomplete"]


class ValidationResult(TypedDict):
    status: Status
    failed_lines: list[str]


def validate_lines(grid: list[list[int]]) -> ValidationResult:
    ...
