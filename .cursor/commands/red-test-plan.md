# red-test-plan — ARRR Ask (RED ③ 테스트 설계)

**ARRR·A 단계** — C2C 설계표·테스트 플랜만 작성한다.  
**코드·파일 변경 없음** — 계획 출력만.

> SSOT: `.cursorrules` · `docs/PRD.md` · `report/session3-workbook-1004.md`  
> Skill: `magic-square-tdd` (있으면 자동 따름)

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: red | Layer: entity | Track: Logic
```

- **Track A (UI):** `Phase: red | Layer: boundary | Track: UI` — 본문 동일, Layer만 `boundary`로 바꾸면 재사용.
- 채팅·PRD·`tests/` 상태에서 **세션 주제·Test ID·RED 묶음**을 자동 추출한다. **추가 질문 금지.**

---

## 자동 절차

1. SSOT·`tests/test_validate_lines.py`(및 `tests/entity/` 등)를 읽는다.
2. 채팅 컨텍스트 또는 PRD §5 ARRR 큐에서 **이번 RED 묶음**·Test ID를 결정한다.
3. 미커버 우선순위 (Logic · `validate_lines`):

| 순위 | Test ID | PRD FR | Mom Test | Given→Then 요약 | 기대 status |
|------|---------|--------|----------|-------------------|-------------|
| 1 | T1 | FR-VAL-01 | S2 | GOLDEN_GRID → pass | `pass` |
| 2 | T2 | FR-VAL-02 | S3 | (2,2) 교차셀 변경 → R2·C2 fail | `fail` |
| 3 | T3 | FR-VAL-03 | S1 | D1만 깨짐 | `fail` |
| 4 | T4 | FR-VAL-04 | S1 | D2만 깨짐 | `fail` |
| 5 | T5 | FR-VAL-05 | — | 빈칸(0) 존재 | `incomplete` |
| 6 | T6 | FR-VAL-06 | S3 | 열 1개만 틀림 | `fail` |

4. 아래 **출력 4블록**을 표 형식으로만 출력한다.

---

## 출력 4블록 (필수)

### 1) C2C (Rule 1~3)

| Rule | 내용 |
|------|------|
| **Rule 1** | PRD FR 인용 → 이번 RED 묶음에 대응하는 **To-Do 1개** |
| **Rule 2** | Test ID · **Given** / **When** / **Then** (한 행) |
| **Rule 3** | Mom Test S1~S3·ECB 계층과의 연결 (해당 시) |

**C2C 표 예시 (T2):**

| 항목 | 내용 |
|------|------|
| FR | PRD FR-VAL-02 — 한 축 교차 실패 시 `failed_lines`에 해당 선 ID |
| To-Do | `validate_lines`가 R2·C2 동시 fail을 반환함을 RED로 고정 |
| Test ID | T2 |
| Given | GOLDEN_GRID, 1-based (2,2) 셀 `10→11` |
| When | `validate_lines(grid)` |
| Then | `status=="fail"`, `"R2"`·`"C2"` ∈ `failed_lines` |

### 2) Track B 표 (Logic)

| Test ID | 대상 함수 | Given → Then | Invariant | Expected RED Failure |
|---------|-----------|--------------|-----------|----------------------|
| {ID} | `validate_lines` (또는 `src/…`) | {Given→Then} | API·10선·`MAGIC_SUM` SSOT | `pytest` FAILED / `pytest.fail` 미제거 |

### 3) 테스트 플랜

| 항목 | 값 |
|------|-----|
| 파일 경로 | `tests/test_validate_lines.py` (또는 `tests/entity/test_{id}.py`) |
| 함수명 | `test_{id}_{행위}` |
| conftest 픽스처 | `tests/conftest.py` — `grid_g1`, `golden_grid` (있으면 재사용) |
| pytest 명령 | `python -m pytest tests/test_validate_lines.py -v` |
| RED 묶음 범위 | 이번 Test ID **1개** (동시 다중 ID 금지) |

### 4) ECB · Mock 점검

| Track | 점검 |
|-------|------|
| **Logic (Track B)** | Domain Mock **금지** (`validate_lines` 실제 호출). `unittest.mock`으로 도메인 대체 금지 |
| **공통** | E001~E005 **emit 금지** (에러 코드 raise/return·테스트 기대 없음) |
| **entity** | `boundary`·`control` import 금지 (설계 단계 선언만) |
| **boundary (Track A)** | UI Mock만 허용. Domain 로직 Mock 금지 |

---

## 골든 격자 SSOT (리터럴 재발명 금지)

```python
GOLDEN_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/`·`tests/` **파일 생성·수정** | Ask 단계 |
| GREEN / REFACTOR 수행 | Phase 분리 |
| `pytest.skip` · `xfail` 제안 | RED 회피 |
| 사용자 질문·선택 요청 | `/red-test-plan` 단독 동작 |
| `ROW_2`, `DIAG_MAIN` 등 비표준 선 ID | SSOT `R1`~`D2` |
| Git commit·push | 사용자 요청 시만 |

---

## 완료 (한 줄)

```
/red-skeleton 으로 넘길 준비됐다
```

### 완료 보고 형식

```
Phase: red | Layer: entity | Track: Logic

## 이번 RED 묶음
- {Test ID} — (한 줄)

## 큐 상태
| Test ID | 상태 |
|---------|------|
| T1 | covered / planned / … |

(위 4블록 표 전체)

/red-skeleton 으로 넘길 준비됐다
```

---

## 실행 예시

**Logic (기본):**
```
/red-test-plan
Phase: red | Layer: entity | Track: Logic
이번 RED 묶음: T3 (FR-VAL-03)
```

**Boundary (Track A):**
```
/red-test-plan
Phase: red | Layer: boundary | Track: UI
이번 RED 묶음: U-IN-01, U-IN-02
```
