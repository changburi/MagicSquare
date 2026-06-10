# TDD RED — `validate_lines`

`validate_lines` 세션 3 **RED 단계 전용** 커맨드. 실패하는 테스트만 추가한다.

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 적는다:

```
Phase: RED
```

이어서 **한 문장**으로 이번 RED 목표를 쓴다.  
예: *완성 격자에서 `status == "pass"`를 기대하는 테스트를 추가한다.*

---

## RED 절차 — AAA

테스트 1개당 아래 순서를 따른다.

| 단계 | 내용 |
|------|------|
| **Arrange** | 4×4 `grid` 준비. `0`=빈칸, `1~16` 배치. 기대값은 `MAGIC_SUM`·`LINE_IDS` import 사용 (리터럴 `34` 금지). |
| **Act** | `result = validate_lines(grid)` 호출. |
| **Assert** | `result["status"]`, `result["failed_lines"]`를 API 계약대로 검증. |

### API 계약 (assert 기준)

```python
validate_lines(grid) -> {"status": str, "failed_lines": list[str]}
```

| status | 의미 | failed_lines |
|--------|------|--------------|
| `pass` | 10선 합 `MAGIC_SUM`, 빈칸 없음 | `[]` |
| `fail` | 한 선 이상 합 ≠ `MAGIC_SUM` | 합 틀린 선 ID (`R1`~`R4`, `C1`~`C4`, `D1`, `D2`) |
| `incomplete` | 빈칸(0) 존재 | `[]` |

---

## pytest 예시

`tests/test_validate_lines.py`에 추가하는 패턴:

```python
from validate_lines import MAGIC_SUM, validate_lines


def test_complete_grid_returns_pass():
    # Arrange — STEP 1 완성 격자
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_wrong_diagonal_returns_fail_with_d1():
    # Arrange — D1만 합이 MAGIC_SUM이 아닌 격자
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  2],  # (4,4) 값 변경 → D1 깨짐
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "D1" in result["failed_lines"]
```

- 테스트 함수명: `test_<행위>_<기대결과>` (한글 주석 허용).
- **대각선 케이스(`D1`/`D2`)를 테스트 세트에 반드시 포함**한다 (Mom Test S1).

---

## 금지 (RED)

| 금지 | 이유 |
|------|------|
| `src/` **어떤 파일도 수정** | 구현은 GREEN |
| `src/validate_lines.py`의 `...` 스텁 변경 | GREEN 전용 |
| assert 완화·삭제·주석 처리 | RED 회피 |
| `pytest.skip`, `xfail`, `@pytest.mark.skip` | RED 회피 |
| 테스트에 검증 로직 구현 (함수 복제) | 테스트는 호출·검증만 |
| `pyproject.toml`, `.cursorrules` 수정 | RED 범위 밖 |
| 리터럴 `34` 하드코딩 | `MAGIC_SUM` SSOT |

**허용:** `tests/` 내 테스트·fixture·helper·parametrize 추가·수정.

---

## RED 완료 보고 형식

RED 작업 후 아래 형식으로 보고한다:

```
Phase: RED

## 목표
- (이번에 추가한 테스트가 검증하려는 행위 1줄)

## 변경 파일
- tests/test_validate_lines.py

## 추가 테스트
- test_xxx — (한 줄 설명)

## 실행 결과
- 명령: pytest tests/test_validate_lines.py -v
- 결과: FAILED (N failed) — RED 확인

## 다음
- GREEN에서 src/validate_lines.py 최소 구현
```

`pytest` 실행 결과가 **FAILED**여야 RED가 완료된 것이다. 통과하면 테스트가 부족하거나 잘못된 것이다.
