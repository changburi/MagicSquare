---
name: magic-square-tdd
description: >-
  MagicSquare Dual-Track TDD·ARRR 워크플로. Phase red|green|refactor, Layer
  entity|boundary, Track Logic|UI. Commands /red-test-plan, /red-skeleton,
  /green-minimal, /golden-master, /refactor-smell, /refactor-safe. TDD, RED,
  GREEN, REFACTOR, Dual-Track, C2C, pytest.fail, validate_lines, 10선 R1~D2.
disable-model-invocation: true
---

# MagicSquare TDD Skill

명시 호출·슬래시 Command 실행 시에만 로드한다.

## SSOT (읽기 순서)

1. `.cursorrules`
2. `docs/PRD.md`
3. `report/session3-workbook-1004.md`
4. `src/validate_lines.py` — `MAGIC_SUM`, `LINE_IDS`

## 1. ARRR ↔ TDD 매핑

| ARRR | TDD | Command | 변경 |
|------|-----|---------|------|
| **Ask** (RED ③) | Arrange | `/red-test-plan` | 없음 (C2C·플랜) |
| **Ask** (RED ④) | RED | `/red-skeleton` | `tests/` only |
| **Respond** | GREEN | `/green-minimal` | `src/` 최소 |
| **Run** | GREEN | `/golden-master` | `tests/golden/` |
| **Refine** (⑦) | REFACTOR | `/refactor-smell` | 분석만 |
| **Refine** | REFACTOR | `/refactor-safe` | `src/` Budget 내 |

레거시: `/tdd-red` — RED 통합(플랜·skeleton 생략).

## 2. Phase 선언 (첫 줄)

```
Phase: red | Layer: entity | Track: Logic
Phase: green | Layer: entity | Track: Logic
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```

- **Track A:** `Layer: boundary | Track: UI`
- **Track B:** `Layer: entity | Track: Logic`

## 3. C2C Rule 1~3

| Rule | 내용 |
|------|------|
| **1** | PRD FR 인용 → RED 묶음당 **To-Do 1개** |
| **2** | Test ID · Given / When / Then |
| **3** | Mom Test S1~S3·ECB 계층 연결 |

## 4. RED 절대 금지

- `src/` 수정 (skeleton·plan 단계)
- `pytest.skip`, `xfail`, assert 완화·삭제
- Logic Track **Domain Mock** (`validate_lines` 대체 mock)
- E001~E005 emit
- 리터럴 `34` (→ `MAGIC_SUM` / `entity/constants.py`)
- 사용자 추가 질문 (슬래시 단독 동작)

## 5. GREEN

- **1 RED 묶음 = 1 GREEN** (1 commit = 1 묶음, commit은 사용자 요청 시)
- `pytest.fail` → assert 교체
- `MAGIC_SUM`, `LINE_IDS`, `GRID_SIZE` — constants SSOT
- entity → boundary/control import 금지
- E001~E005 raise/return 금지

## 6. REFACTOR

- **Change Budget:** 파일 ≤3 · 클래스 ≤1 · 메서드 ≤3
- pytest 전부 PASS 전제
- golden **matched** (`UPDATE_GOLDEN` 없이)
- API·incomplete 우선순위 불변

## 7. Track A vs Track B

| | Track A (UI) | Track B (Logic) |
|---|--------------|-----------------|
| Layer | `boundary` | `entity` |
| 테스트 | UI·입력·표시 | `validate_lines`·도메인 |
| Mock | UI만 허용 | **Domain Mock 금지** |
| 예시 ID | `U-IN-01` | `T1`~`T6`, `D-LOC-01` |

## 8. Command 체인

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
                                                      ↓
                              /refactor-smell → /refactor-safe
```

## 9. pytest 명령 패턴

```bash
python -m pytest tests/test_validate_lines.py -v
python -m pytest tests/test_validate_lines.py::test_t2_r2_c2_intersection_fail -v
UPDATE_GOLDEN=1 python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01 -v
python -m pytest tests/ -v
```

## 10. API 계약

```python
validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": list[str]}
```

| status | 조건 | failed_lines |
|--------|------|--------------|
| `incomplete` | `0` 존재 (우선) | `[]` |
| `pass` | 10선 == `MAGIC_SUM` | `[]` |
| `fail` | 합 ≠ `MAGIC_SUM` | 틀린 선 ID |

선 ID: `R1`~`R4`, `C1`~`C4`, `D1`, `D2`.

## 11. 테스트 큐 (Logic · validate_lines)

T1 pass → T2 R2·C2 → T3 D1 → T4 D2 → T5 incomplete → T6 열 단독 fail.

## 12. 완료 보고 형식

**RED (skeleton):** Test ID · FAIL 한 줄 · 변경 `tests/`만  
**GREEN:** PASS Test ID · 변경 `src/` · pytest PASSED  
**REFACTOR:** 스멜 · Budget · pytest · golden matched  

## 커맨드 경로

- [red-test-plan.md](../../commands/red-test-plan.md)
- [red-skeleton.md](../../commands/red-skeleton.md)
- [green-minimal.md](../../commands/green-minimal.md)
- [golden-master.md](../../commands/golden-master.md)
- [refactor-smell.md](../../commands/refactor-smell.md)
- [refactor-safe.md](../../commands/refactor-safe.md)
