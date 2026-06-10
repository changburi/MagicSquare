# MagicSquare — Product Requirements Document (PRD)

| 항목 | 내용 |
|------|------|
| **프로젝트** | MagicSquare_1004 |
| **버전** | 세션 3 (validate_lines) |
| **작성일** | 2026-06-10 |
| **SSOT 순위** | 본 문서 → `.cursorrules` → `src/validate_lines.py` 상수 |
| **저장소** | https://github.com/changburi/MagicSquare |

---

## 1. 배경·문제

### 페르소나

4×4 **부분 마방진**을 손으로 또는 코드로 다루는 학습자. 빈칸 2개를 채우고 1~16을 배치하며 행·열·대각선 합 34를 맞추는 ECB( Entity–Control–Boundary ) 설계 과제 맥락.

### 진짜 문제 (Mom Test)

> 부분 마방진을 채운 뒤 **모든 합 조건(특히 대각선)을 빠짐없이 검증했는지 스스로 확신하기 어렵고**, 틀린 줄 모르고 진행하다 **암산으로 다시 확인할 때까지 수십 분의 작업 비용을 날린다.**

| 축 | 내용 |
|----|------|
| 불편 | 대각선 등 일부 조건을 놓친 채 “맞다”고 착각 |
| 비용 | 잘못된 가정 하에 **약 20분** 소요 (인터뷰 증거) |
| 판정 | “다 맞췄다”는 자기 판정이 틀릴 수 있음 |
| 재현 | 중간 **암산 검증**을 해야만 오류 발견 |

### Mom Test 증거 3줄

1. 「빈칸 2개 넣고 행·열·대각선 합 맞췄는데 **대각선 하나를 빼먹어서 20분 날렸다**」
2. 「**중간에 암산으로 검증해봤는데** 그때 알게 됐어」
3. 「**ECB 개념 분석·4×4 마방진** 작업을 했는데, 어려움이 있었어」

### 표면 문제 (스코프 밖)

「4×4 부분 마방진 **자동 검증 프로그램/완성 앱**을 만든다」— 제품 형태가 아니라 **판정 가능 여부**를 Test Loop로 고정하는 것이 세션 3 목표.

---

## 2. 목표·비목표

### 목표 (한 문장)

**4×4 부분 마방진에서 행·열·대각선 합(34)을 빠짐없이 판정하고, 틀린 축을 바로 알 수 있는지 검증한다.**

### R-G-I-O

| | 내용 |
|---|---|
| **Role** | **검증자(Validator)** — “맞다/틀리다” 대신 **어떤 축이 34인지·아닌지**만 판정 |
| **Goal** | **10개 축**(행 4 + 열 4 + 대각선 2) 누락 없이 검사, 실패 시 **축 ID** 식별 |
| **Input** | `int[4][4]` 격자 (`0` = 빈칸, `1~16` = 배치 값) |
| **Output** | `ValidationResult`: `status` + `failed_lines` |

### 성공 기준 (Mom Test S1~S3)

| # | 기준 | 증거 연결 |
|---|------|-----------|
| **S1** | 10축을 **한 번의 호출**로 검사. 테스트에 **D1·D2 대각선** 반드시 포함 | ① 대각선 누락이 20분 낭비의 핵심 |
| **S2** | **암산 없이** 즉시 `status` + 실패 축 이름 반환 | ② 암산 의존 제거 |
| **S3** | **한 축만 틀린** 격자에서 실패 축을 **즉시** 특정 (단위 테스트로 재현) | ① 20분 낭비 방지 + ECB 실패 조건 식별 |

### 비목표 (세션 3)

| 하지 않음 | 이유 |
|-----------|------|
| 빈칸 자동 채우기 / Solver | 증거는 “검증 누락”이지 풀이 알고리즘 부재가 아님 |
| GridUI · InputHandler · ResultDisplay | Boundary 전체는 후속 세션 |
| MissingFinder · ECB 전 계층 통합 | Control/Entity 통합은 후속 |
| 중복·범위 밖 값 검증 (1~16 중복 등) | 세션 3은 **10선 합 판정**에 집중. Rule 확장은 후속 |
| CLI `validate --file` | Command 계층 최소 단위는 `validate_lines` 함수 |

---

## 3. 도메인 규칙

### 격자

- 크기: **4×4** `list[list[int]]`
- `0`: 빈칸 (부분 마방진 허용)
- `1~16`: 배치된 값 (완성 마방진)

### 마법상수

- 목표 합: **34** (`MAGIC_SUM` in `src/validate_lines.py`)
- 테스트·문서에서 리터럴 `34` 하드코딩 금지 → `MAGIC_SUM` import

### 검사 선 (10개)

| ID | 의미 | 좌표 (0-based) |
|----|------|----------------|
| `R1` | 1행 | `grid[0][0..3]` |
| `R2` | 2행 | `grid[1][0..3]` |
| `R3` | 3행 | `grid[2][0..3]` |
| `R4` | 4행 | `grid[3][0..3]` |
| `C1` | 1열 | `grid[0..3][0]` |
| `C2` | 2열 | `grid[0..3][1]` |
| `C3` | 3열 | `grid[0..3][2]` |
| `C4` | 4열 | `grid[0..3][3]` |
| `D1` | 주대각 | `(0,0)(1,1)(2,2)(3,3)` |
| `D2` | 역대각 | `(0,3)(1,2)(2,1)(3,0)` |

- 선 ID는 **`R1`~`R4`, `C1`~`C4`, `D1`, `D2`만** 사용한다.
- 워크북 초안의 `ROW_2`, `DIAG_MAIN` 등 **비표준 ID 사용 금지**.

### 골든 마스터 (완성 4×4)

STEP 1 퍼즐을 채운 뒤의 완성 격자. `pass` 테스트·fail 변형의 SSOT.

```python
GOLDEN_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

STEP 1 퍼즐 (빈칸 2개, 채우기 전):

```
 16 |  3 |  2 | 13
  5 | 10 | 11 |  ?
  9 |  6 |  ? | 12
  4 | 15 | 14 |  1
```

---

## 4. 기능 요구사항 — `validate_lines`

### API

```python
validate_lines(grid: list[list[int]]) -> ValidationResult
```

```python
class ValidationResult(TypedDict):
    status: Literal["pass", "fail", "incomplete"]
    failed_lines: list[str]
```

구현: `src/validate_lines.py`  
테스트: `tests/test_validate_lines.py`

### `status` 판정 (우선순위)

| 순위 | status | 조건 | `failed_lines` |
|------|--------|------|----------------|
| 1 | `incomplete` | 격자에 `0`이 **하나라도** 있음 | `[]` (합 검사 생략) |
| 2 | `pass` | 빈칸 없음, 10선 **모두** 합 == `MAGIC_SUM` | `[]` |
| 3 | `fail` | 빈칸 없음, **한 선 이상** 합 ≠ `MAGIC_SUM` | 합이 틀린 선 ID 목록 |

- `fail`일 때만 `failed_lines`에 ID를 넣는다. `pass`·`incomplete`는 항상 `[]`.
- 여러 선이 동시에 틀리면 **모두** 목록에 포함 (예: R2·C2 교차셀 변경).

### 공개 상수 (SSOT)

| 이름 | 값 | 용도 |
|------|-----|------|
| `MAGIC_SUM` | `34` | 목표 합 |
| `LINE_IDS` | `R1`~`R4`, `C1`~`C4`, `D1`, `D2` | 선 ID 집합 |

---

## 5. 테스트 요구사항

### 프레임워크

- **pytest** (`pyproject.toml`: `testpaths=["tests"]`, `pythonpath=["src"]`)
- Python **≥ 3.10**

### TDD 사이클

1. **RED** — 실패 테스트만 `tests/`에 추가·수정. `src/` 수정 금지.
2. **GREEN** — 통과에 필요한 최소 구현만 `src/`.
3. **REFACTOR** — 동작 유지, 중복·이름 정리. 테스트 GREEN 유지.

**금지:** assert 완화, `pytest.skip`, `xfail`, 테스트 삭제로 RED 회피.

### ARRR 실습 큐 (권장 순서)

| ID | Mom Test | 시나리오 | 기대 `status` | 기대 `failed_lines` |
|----|----------|----------|---------------|---------------------|
| T1 | S2 | `GOLDEN_GRID` 완성 격자 | `pass` | `[]` |
| T2 | S3 | GOLDEN 변형: 1-based (2,2) 셀 변경 → R2·C2 동시 fail | `fail` | `R2`, `C2` 포함 |
| T3 | S1 | D1만 합 깨짐 | `fail` | `D1` 포함 |
| T4 | S1 | D2만 합 깨짐 | `fail` | `D2` 포함 |
| T5 | — | 빈칸(0) 1개 이상 | `incomplete` | `[]` |
| T6 | S3 | 행은 맞고 열 1개만 틀림 | `fail` | 해당 `C*` |

### 테스트 패턴 (AAA)

- **Arrange:** 4×4 `grid`, `MAGIC_SUM`·`LINE_IDS` import
- **Act:** `result = validate_lines(grid)`
- **Assert:** `result["status"]`, `result["failed_lines"]` — API 계약대로

### Cursor 커맨드·스킬

| 유형 | 경로 |
|------|------|
| ARRR | `.cursor/commands/red-test-plan.md` … `refactor-safe.md` |
| RED 통합 | `.cursor/commands/tdd-red.md` |
| 문서 | `.cursor/commands/export.md`, `save-report.md` |
| 스킬 | `.cursor/skills/magic-square-tdd/`, `magic-square-docs/` |

---

## 6. 8계층 로드맵

| 계층 | 세션 3 | 산출물·상태 |
|------|--------|-------------|
| **Rule** | ✅ | 합 34, 10선, `incomplete`/`pass`/`fail` — 본 PRD·`.cursorrules` |
| **Command** | ✅ | `validate_lines(grid)` |
| **(Skill)** | ⭕ | `check_all_sums` 등 — 선택·후속 |
| **Test Loop** | ✅ | pytest + ARRR 커맨드 |
| Entity | ❌ | `MagicSquare`, `Cell` — 후속 |
| Control | ❌ | `SquareValidator`, `Solver`, `MissingFinder` — 후속 |
| Boundary | ❌ | `GridUI`, `ResultDisplay` — 후속 |
| Integration | ❌ | E2E — 후속 |

---

## 7. 현재 구현 상태 (2026-06-10)

| 항목 | 상태 |
|------|------|
| `src/validate_lines.py` | 시그니처·상수·`ValidationResult` 정의. 본문 `...` (**미구현**) |
| `tests/test_validate_lines.py` | T2 `test_t2_r2_c2_intersection_fail`만 존재 (**RED**) |
| `pytest` | T2 **FAILED** — `validate_lines` 미구현 확인 |
| `.cursorrules` | API·TDD·Boundary 반영 |
| ARRR 커맨드 6종 + 스킬 2종 | 생성 완료 |
| Git | `origin/staging` 푸시됨. `spec` 로컬 브랜치 |

### T2 확정 사양

- 완성 격자에서 **1-based (2,2)** 교차셀 `10 → 11` (R2·C2 합 34→35)
- 기대: `status == "fail"`, `"R2"`·`"C2"` ∈ `failed_lines`

---

## 8. 협업·경계

- AI 응답 언어: **한국어**
- TDD 작업 시 응답 첫 줄: `Phase: RED` / `GREEN` / `REFACTOR`
- Git commit·push: **사용자 요청 시만**
- 슬래시 커맨드: **추가 입력·질문 없이** 저장소 상태로 자동 진행

---

## 9. 후속 세션 힌트

- Mom Test Q5 보완: 암산 시 실제로 확인한 축 기록 → 실패 축 리포트 UX
- `SquareValidator`(Control)로 Rule 승격
- `ResultDisplay`로 실패 축 시각화
- Rule 확장: 1~16 중복·범위 밖 값 검증
- `spec` 브랜치 원격 푸시 (요청 시)

---

## 10. 참고 문서

| 문서 | 내용 |
|------|------|
| [report/mom-test-step1.md](../report/mom-test-step1.md) | STEP 1 Mom Test 인터뷰 |
| [report/session3-workbook-1004.md](../report/session3-workbook-1004.md) | 세션 3 R-G-I-O·8계층 |
| [.cursorrules](../.cursorrules) | Entity·Control·Boundary (AI·TDD) |
| [report/01.session3-harness-cursor-commands.md](../report/01.session3-harness-cursor-commands.md) | 하네스·커맨드 구축 |
| [report/02.REPORT.md](../report/02.REPORT.md) | T2 RED·export |

---

*본 문서는 `docs/PRD.md` — MagicSquare 세션 3 요구사항 SSOT입니다.*
