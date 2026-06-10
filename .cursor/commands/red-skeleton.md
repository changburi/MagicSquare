# red-skeleton — ARRR Ask (RED ④ 실패 테스트 골격)

`/red-test-plan` 설계표 기준으로 **pytest.fail 스켈레톤**만 `tests/`에 작성한다.

> SSOT: `.cursor/commands/red-test-plan.md` · `.cursorrules` · `docs/PRD.md`  
> Skill: **magic-square-tdd** Skill이 있으면 자동 따름

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: red | Layer: entity | Track: Logic
```

이어서 **한 문장**: 추가하는 `test_*`·Test ID.

---

## 자동 절차 (추가 질문 금지)

1. `red-test-plan` 큐 또는 채팅에서 **Test ID 1개** 확정.
2. 설계표 없이 호출 시 — 채팅의 Given/When/Then으로 플랜을 내재 복원 후 진행.
3. `tests/`에 테스트 파일·`conftest` 픽스처를 **필요 시만** 추가.
4. **Then**은 `pytest.fail("RED: {Test ID} — …")` **한 줄만**. assert 본문·통과 더미 금지.
5. `python -m pytest … -v` 실행 → **FAILED** 확인 후 보고.

---

## AAA 주석 (Given / When / Then)

```python
def test_{test_id}_{행위}():
  # Given — {Test ID}: {한 줄}
  ...

  # When — {행위}
  ...

  # Then — RED skeleton (GREEN에서 assert로 교체)
  pytest.fail("RED: {Test ID} — {기대 한 줄}")
```

### validate_lines 패턴 (Logic Track)

```python
import pytest
from validate_lines import MAGIC_SUM, validate_lines


def test_t1_complete_grid_returns_pass():
    # Given — T1: GOLDEN_GRID 완성 4×4
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # When — validate_lines 호출
    result = validate_lines(grid)

    # Then
    pytest.fail("RED: T1 — status pass, failed_lines []")
```

### entity 패턴 (D-LOC-01 등)

```python
import pytest
# from entity.constants import GRID_SIZE, MAGIC_SUM  # 상수 SSOT
# from entity.location import find_blank_coords


def test_d_loc_01_blank_coords_row_major():
    # Given — D-LOC-01: G1 격자, 빈칸 2개 (row-major)
    grid_g1 = ...  # tests/conftest.py 픽스처

    # When — find_blank_coords(grid_g1)
    ...

    # Then — 1-index row-major [(2,3), (4,4)]
    pytest.fail("RED: D-LOC-01 — [(2,3), (4,4)]")
```

---

## 상수 · 픽스처 SSOT

| 항목 | 규칙 |
|------|------|
| `34` / `16` / `4` | `entity/constants.py` import (픽스처·Arrange 데이터만). 테스트 assert에 리터럴 `34` 금지 → `MAGIC_SUM` |
| `tests/conftest.py` | `grid_g1` — STEP 1 퍼즐, `0` 두 개, row-major |
| `golden_grid` | `GOLDEN_GRID`와 동일 값 (있으면 재사용) |

**grid_g1 예시 (STEP 1 빈칸 2개):**

```python
@pytest.fixture
def grid_g1():
    return [
        [16,  3,  2, 13],
        [ 5, 10, 11,  0],
        [ 9,  6,  0, 12],
        [ 4, 15, 14,  1],
    ]
```

---

## 금지 (RED)

| 금지 | 이유 |
|------|------|
| `src/` **어떤 파일도 수정** | GREEN 전용 |
| assert 본문 (Then에 `pytest.fail` 외) | skeleton 단계 |
| `pytest.skip` · `xfail` · 통과 더미 | RED 회피 |
| 테스트에 검증 로직 복제 | 호출·fail만 |
| 사용자 질문 | 슬래시 단독 동작 |
| Git commit·push | 사용자 요청 시만 |

**허용:** `tests/` 내 테스트·`conftest.py`·fixture 추가·수정.

---

## RED 완료 보고

```
Phase: red | Layer: entity | Track: Logic

## Test ID
- {ID} — FAIL: {pytest.fail 메시지 한 줄}

## 변경 파일
- tests/… (tests/만)

## 실행 결과
- python -m pytest {path} -v → FAILED (N failed)

## 다음
- /green-minimal
```

---

## 실행 예시

```
/red-skeleton
Phase: red | Layer: entity | Track: Logic
Test ID: T1
파일: tests/test_validate_lines.py
```

```
/red-skeleton
Phase: red | Layer: entity | Track: Logic
Test ID: D-LOC-01
Given: G1 격자 | When: find_blank_coords(grid_g1) | Then: [(2,3),(4,4)] (1-index row-major)
파일: tests/entity/test_d_loc_01.py
픽스처: tests/conftest.py (grid_g1)
```
