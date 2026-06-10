# green-minimal — ARRR Run GREEN (최소 구현)

`validate_lines` **ARRR·GREEN 단계** 전용. 현재 **실패 중인 테스트**를 통과시키는 **최소** 구현만 `src/validate_lines.py`에 작성한다.

> SSOT: `.cursorrules` · `docs/PRD.md`(있으면) · `tests/test_validate_lines.py`

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: GREEN
```

이어서 **한 문장**으로 이번 GREEN이 통과시키는 테스트·행위를 쓴다.

---

## 자동 절차 (추가 입력·질문 금지)

1. `pytest tests/test_validate_lines.py -v` 실행 → **실패 목록** 확인.
2. 실패가 0이면: “GREEN 불필요 — /red-skeleton 또는 /golden-master” 보고 후 종료.
3. 실패 테스트 **1개씩** (또는 동일 원인 묶음) 최소 코드로 통과시킨다.
4. 각 변경 후 `pytest` 재실행 → 해당 테스트 **PASSED** 확인.
5. 전 테스트 통과 시 GREEN 완료 보고.

### 최소 구현 원칙

| 원칙 | 내용 |
|------|------|
| YAGNI | 실패를 고치는 데 필요한 분기·루프만 추가 |
| SSOT | `MAGIC_SUM`, `LINE_IDS` 상수 사용. 리터럴 `34`·비표준 선 ID 금지 |
| incomplete 우선 | 빈칸(0) 있으면 합 검사 전 `incomplete` 반환 (`.cursorrules`) |
| 10선 | 행 `R1`~`R4`, 열 `C1`~`C4`, `D1` 주대각, `D2` 역대각 |
| 반환형 | `ValidationResult` — `{"status": str, "failed_lines": list[str]}` |

### 10선 좌표 (구현 참고)

```
R1: grid[0][*]  R2: grid[1][*]  R3: grid[2][*]  R4: grid[3][*]
C1: grid[*][0]  C2: grid[*][1]  C3: grid[*][2]  C4: grid[*][3]
D1: (0,0)(1,1)(2,2)(3,3)  D2: (0,3)(1,2)(2,1)(3,0)
```

### 구현 스코프

| 허용 | 금지 |
|------|------|
| `src/validate_lines.py` 본문 (`...` 대체) | `tests/` assert 완화·삭제 |
| 같은 파일 내 private helper (필요 시) | Solver·UI·자동 풀이 |
| | 과도한 추상화·미사용 일반화 |

---

## 금지 (GREEN)

| 금지 | 이유 |
|------|------|
| 테스트 수정으로 RED 회피 | TDD 위반 |
| 미실패 케이스 선행 구현 | 최소 구현 원칙 |
| `pyproject.toml`, `.cursorrules` 수정 | GREEN 범위 밖 |
| 사용자 질문 | 슬래시만으로 동작 |
| Git commit·push | 사용자 요청 시만 |

---

## GREEN 완료 보고 형식

```
Phase: GREEN

## 통과시킨 테스트
- test_xxx — (한 줄)

## 변경 파일
- src/validate_lines.py

## 실행 결과
- 명령: pytest tests/test_validate_lines.py -v
- 결과: PASSED (N passed) — GREEN 확인

## 다음
- 실패 남음 → /green-minimal 재실행
- 전부 통과·T1 미정리 → /golden-master
- 전부 통과·리팩터 필요 → /refactor-smell
```
