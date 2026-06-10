# golden-master — ARRR Run GREEN (Approval Test)

**GREEN PASS 후** Golden Master(Approval Test)를 구축·검증한다.

> SSOT: `.cursorrules` · `docs/PRD.md` · `tests/`  
> Skill: **magic-square-tdd** (있으면 자동 따름)

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: green | Layer: entity | Track: Logic
```

이어서 **한 문장**: 대상 Test ID·golden 파일 경로.

---

## 전제

- 대상 Test ID의 `pytest`가 **PASS** 상태.
- PASS 아니면 중단하고 보고:

```
Golden Master 진행을 위해 GREEN PASS 단계를 완료해 주세요.
```

---

## 자동 절차 (추가 질문 금지)

1. 대상 테스트·출력 스냅샷 형식을 확인한다.
2. `tests/_approval.py`에 `assert_matches_golden`이 **없으면 생성**.
3. `tests/golden/{test_id_lower}.approved.txt` 연결.
4. 기준 파일 생성: `UPDATE_GOLDEN=1 python -m pytest {target} -v`
5. 검증: `UPDATE_GOLDEN` **없이** `pytest` → **matched** 확인.
6. golden 파일 **수동 편집으로 통과 우회 금지**.

### assert_matches_golden (개요)

```python
# tests/_approval.py
import os
from pathlib import Path

GOLDEN_DIR = Path(__file__).parent / "golden"

def assert_matches_golden(actual: str, golden_name: str) -> None:
    path = GOLDEN_DIR / golden_name
    if os.environ.get("UPDATE_GOLDEN") == "1":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(actual, encoding="utf-8")
        return
    expected = path.read_text(encoding="utf-8")
    assert actual == expected, f"golden mismatch: {golden_name}\n{diff_hint}"
```

### 출력 포맷 고정

- 좌표·인덱스: **1-based** (문서·golden 일치)
- 에러 코드 문자열: `E001`~`E005` 형식 (세션 3 `validate_lines`는 status 문자열만)
- `validate_lines` golden 예: `status=pass\nfailed_lines=[]`

### validate_lines 단순 경로 (GOLDEN_GRID)

`tests/test_validate_lines.py`에 `GOLDEN_GRID` 상수가 없으면 PRD SSOT로 추가.  
T1이 PASS이면 approval 없이 `GOLDEN_GRID` SSOT만으로도 가능 — **D-SOL-01 등 다단계 출력**은 approval 필수.

---

## 금지

| 금지 | 이유 |
|------|------|
| golden 수동 편집으로 통과 | 우회 |
| `src/` 동작 변경으로 golden 맞추기 | 계약 변경은 GREEN |
| `UPDATE_GOLDEN` 없이 기준 파일 임의 생성 | 절차 위반 |
| Git commit·push | 사용자 요청 시만 |

---

## 완료 보고

```
Phase: green | Layer: entity | Track: Logic

## 대상
- {Test ID} — {test path}

## golden 경로
- tests/golden/{id}.approved.txt

## matched
- yes / no

## diff 요약
- (no diff / 한 줄)

## 실행 결과
- UPDATE_GOLDEN=1: (생성 여부)
- pytest {target} -v → PASSED, matched

## 다음
- /refactor-smell
```

---

## 실행 예시

```
/golden-master
Phase: green | Layer: entity | Track: Logic
대상: T1
```

```
/golden-master
대상: D-SOL-01 (tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success)
```
