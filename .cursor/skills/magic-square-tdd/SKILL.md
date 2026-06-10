---
name: magic-square-tdd
description: >-
  MagicSquare validate_lines TDD·ARRR 워크플로. Arrange(테스트 계획)→RED(골격)→Run
  GREEN(최소 구현·골든 마스터)→Refactor(냄새·안전 리팩터)를 .cursorrules·PRD·Mom
  Test S1~S3에 맞춰 수행. TDD RED/GREEN/REFACTOR, validate_lines, ARRR, pytest,
  10선 R1~D2 작업 시 사용.
---

# MagicSquare TDD (ARRR)

## ARRR 사이클

| 단계 | 커맨드 | Phase | 변경 범위 |
|------|--------|-------|-----------|
| **A**rrange | `/red-test-plan` | RED (plan) | 없음 (계획만) |
| **R**ED | `/red-skeleton` | RED | `tests/`만 |
| **R**un GREEN | `/green-minimal` | GREEN | `src/validate_lines.py` |
| **R**un GREEN | `/golden-master` | GREEN | `tests/` SSOT |
| **R**efactor | `/refactor-smell` | REFACTOR (smell) | 없음 |
| **R**efactor | `/refactor-safe` | REFACTOR | `src/` (테스트 GREEN 유지) |

레거시: `/tdd-red` = RED 통합(계획+골격 생략 시). ARRR 실습은 위 6커맨드 순서 권장.

## SSOT (읽기 순서)

1. `.cursorrules` — API·TDD·Boundary
2. `docs/PRD.md` — 있으면 요구사항 최우선
3. `report/session3-workbook-1004.md` — Mom Test S1~S3·R-G-I-O
4. `src/validate_lines.py` — `MAGIC_SUM`, `LINE_IDS`

## API 계약

```python
validate_lines(grid) -> {"status": str, "failed_lines": list[str]}
```

| status | 조건 | failed_lines |
|--------|------|--------------|
| `incomplete` | `0` 빈칸 존재 (합 검사 전) | `[]` |
| `pass` | 10선 합 `MAGIC_SUM`, 빈칸 없음 | `[]` |
| `fail` | 빈칸 없고 한 선 이상 합 ≠ `MAGIC_SUM` | 틀린 선 ID |

선 ID: `R1`~`R4`, `C1`~`C4`, `D1`, `D2` only.

## 테스트 큐 (자동 진행)

`red-test-plan` 우선순위: T1 pass → T2 fail 교차 → T3 D1 → T4 D2 → T5 incomplete → T6 열 단독 fail.

- **S1:** T3·T4 대각선 필수
- **S2:** T1 한 호출로 전 축 pass
- **S3:** T2·T6 실패 축 즉시 특정

## Phase 선언

TDD 응답 **첫 줄**: `Phase: RED` | `GREEN` | `REFACTOR` (하위는 괄호 허용).

## RED·GREEN·REFACTOR 금지 (공통)

- assert 완화, `pytest.skip`, `xfail`, 테스트 삭제로 RED 회피
- 리터럴 `34` (→ `MAGIC_SUM`)
- Solver·UI·ECB 전 계층 통합
- Git commit·push (사용자 요청 시만)
- 슬래시 커맨드 실행 시 **추가 질문 금지** — 큐·파일 상태로 자동 결정

## 골든 마스터

```python
GOLDEN_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

fail/incomplete는 복사 후 최소 셀 변경.

## 커맨드 위치

- [.cursor/commands/red-test-plan.md](../../commands/red-test-plan.md)
- [.cursor/commands/red-skeleton.md](../../commands/red-skeleton.md)
- [.cursor/commands/green-minimal.md](../../commands/green-minimal.md)
- [.cursor/commands/golden-master.md](../../commands/golden-master.md)
- [.cursor/commands/refactor-smell.md](../../commands/refactor-smell.md)
- [.cursor/commands/refactor-safe.md](../../commands/refactor-safe.md)
