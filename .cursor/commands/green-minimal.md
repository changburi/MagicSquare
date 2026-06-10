# green-minimal — ARRR Respond (GREEN 최소 구현)

**ARRR·R 단계 (Respond = GREEN)** — RED **1묶음당** 최소 구현만 `src/`에 작성한다.  
**1커밋 = 1 RED 묶음** (commit·push는 사용자 요청 시만).

> SSOT: `.cursorrules` · `docs/PRD.md` · `tests/` · `/red-test-plan` 설계표  
> Skill: **magic-square-tdd** (있으면 자동 따름)

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: green | Layer: entity | Track: Logic
```

- **boundary / UI:** `Phase: green | Layer: boundary | Track: UI` — 절차 동일, 구현 경로만 `src/boundary/` 등으로 변경.
- 이어서 **한 문장**: 통과시키는 **Test ID**·RED 대상 테스트 경로.

---

## 자동 절차 (추가 질문 금지)

| 단계 | 행위 |
|------|------|
| 1 | `python -m pytest … -v` → **RED 재확인** (FAILED / ERROR / `pytest.fail`) |
| 2 | 실패 0건이면 **「GREEN 불필요」** 보고 후 종료 |
| 3 | **이번 RED 묶음 Test ID 1개**만 통과시키는 **최소** 코드를 `src/`에 작성 |
| 4 | `tests/`에서 `pytest.fail("RED: …")` **제거** → 설계표 Then과 일치하는 **assert**로 교체 |
| 5 | `pytest` 재실행 → 대상 **PASS** + 기존 통과 테스트 **회귀 없음** |
| 6 | 회귀 실패 시 **즉시 수정** 후 5번 반복 |

### RED 유형별 최소 조치

| RED 증상 | 최소 조치 |
|----------|-----------|
| `pytest.fail` | `src/` 구현 + assert 교체 |
| `ModuleNotFoundError` (`entity.location` 등) | `src/entity/` 패키지·대상 모듈 **생성** |
| `TypeError` / `None` (`validate_lines` `...`) | 함수 본문 **최소** 구현 |
| assert 실패 | 이번 Test ID 범위만 코드 보강 (**assert 완화 금지**) |

### 최소 구현 원칙

| 원칙 | 내용 |
|------|------|
| **YAGNI** | 이번 RED 묶음 1개만 해결 |
| **SSOT** | `34`/`16`/`4`/`0` → `entity/constants.py` 또는 `validate_lines.MAGIC_SUM`. **리터럴 하드코딩·매직넘버 금지** |
| **incomplete 우선** | `validate_lines`: `0` 존재 시 합 검사 전 `incomplete` (PRD §4) |
| **10선** | `R1`~`R4`, `C1`~`C4`, `D1`, `D2` — `LINE_IDS` SSOT |
| **ECB** | **entity** → `boundary`·`control` **import 금지** |
| **에러 코드** | **E001~E005** raise/return·테스트 기대 **금지** |

### `validate_lines` 10선 좌표 (해당 시)

```
R1: grid[0][*]  R2: grid[1][*]  R3: grid[2][*]  R4: grid[3][*]
C1: grid[*][0]  C2: grid[*][1]  C3: grid[*][2]  C4: grid[*][3]
D1: (0,0)(1,1)(2,2)(3,3)  D2: (0,3)(1,2)(2,1)(3,0)
```

### assert 교체 예 (D-LOC-01)

```python
# RED skeleton 제거 후
coords = find_blank_coords(grid_g1)
assert coords == [(2, 4), (3, 3)]
```

---

## 구현 스코프

| 허용 | 금지 |
|------|------|
| `src/` 본문·패키지 추가 (`entity/`, `validate_lines.py` 등) | 이번 RED 묶음 **외** Test ID 동시 해결 |
| `tests/` — `pytest.fail` → assert **만** | assert 완화·삭제·skip·xfail |
| 같은 파일 내 private helper (필요 최소) | **REFACTOR** (구조 개편·Budget extract) |
| | Solver·UI·ECB 통합 (Boundary 밖) |
| | `pyproject.toml`, `.cursorrules` 수정 |
| | **Git commit·push** (사용자 요청 시만) |

---

## pytest 명령 예시

```bash
# 단일 테스트
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v

# 파일 전체
python -m pytest tests/test_validate_lines.py -v
```

---

## GREEN 완료 보고 형식

```
Phase: green | Layer: entity | Track: Logic

## PASS Test ID
- {ID} — (한 줄)

## 변경 파일
- src/…
- tests/… (pytest.fail → assert 교체만)

## 실행 결과
- python -m pytest {target} -v → PASSED (N passed)

## 회귀
- (없음 / 즉시 수정한 내역)

## 다음
- RED 남음 → /red-skeleton (다음 ID 1개)
- 해당 트랙 전부 PASS → /golden-master (해당 시)
- 리팩터 필요·전 테스트 PASS → /refactor-smell
```

---

## 실행 예시

**Logic · validate_lines:**

```
/green-minimal
Phase: green | Layer: entity | Track: Logic
RED 대상: T2 (tests/test_validate_lines.py::test_t2_r2_c2_intersection_fail)
```

**Logic · entity:**

```
/green-minimal
Phase: green | Layer: entity | Track: Logic
RED 대상: D-LOC-01 (tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major)
```

**boundary:**

```
/green-minimal
Phase: green | Layer: boundary | Track: UI
RED 대상: U-IN-01 (tests/boundary/test_u_in_01.py::test_u_in_01_parse_g1_grid_text)
```
