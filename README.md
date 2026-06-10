# MagicSquare_1004

4×4 부분 마방진의 **행·열·대각선 10선 합(34)** 을 판정하고, 틀린 축을 식별하는 TDD 프로젝트 (세션 3).

**요구사항 SSOT:** [docs/PRD.md](docs/PRD.md)

---

## 문제·목표

Mom Test에서 도출한 진짜 문제: 부분 마방진을 채운 뒤 **모든 합 조건(특히 대각선)을 빠짐없이 검증했는지 확신하기 어렵고**, 틀린 줄을 모른 채 진행하다 **암산으로 다시 확인할 때까지 시간을 낭비**한다.

세션 3 목표는 앱이나 자동 풀이가 아니라, **10개 축 판정을 Test Loop로 고정**하는 것이다.

---

## API (`validate_lines`)

```python
validate_lines(grid) -> {"status": str, "failed_lines": list[str]}
```

| `status` | 의미 | `failed_lines` |
|----------|------|----------------|
| `incomplete` | 빈칸(`0`) 존재 — 합 검사 생략 | `[]` |
| `pass` | 10선 모두 합 `MAGIC_SUM`, 빈칸 없음 | `[]` |
| `fail` | 빈칸 없고 한 선 이상 합 ≠ `MAGIC_SUM` | 틀린 선 ID 목록 |

- 검사 선 ID: `R1`~`R4`, `C1`~`C4`, `D1`(주대각), `D2`(역대각)
- 구현: [src/validate_lines.py](src/validate_lines.py) · 테스트: [tests/test_validate_lines.py](tests/test_validate_lines.py)

---

## 빠른 시작

```bash
# Python 3.10+
pip install pytest
python -m pytest tests/test_validate_lines.py -v
```

---

## TDD · ARRR (Dual-Track)

| Track | Layer | 예시 Test ID | 커맨드 흐름 |
|-------|-------|--------------|-------------|
| **B — Logic** | `entity` | T1~T6, D-LOC-01~03 | `/red-test-plan` → `/red-skeleton` → `/green-minimal` |
| **A — UI** | `boundary` | U-IN-01, U-IN-02 | 동일 (Layer·Track만 변경) |

| ARRR | Cursor 커맨드 |
|------|----------------|
| Ask (RED ③④) | `/red-test-plan`, `/red-skeleton` |
| Respond (GREEN) | `/green-minimal`, `/golden-master` |
| Refine | `/refactor-smell`, `/refactor-safe` |
| 문서 | `/export`, `/save-report` |
| 레거시 RED | `/tdd-red` |

- **RED:** `tests/`만 · **GREEN:** `src/` 최소 구현 · **REFACTOR:** Budget 내 행위 보존
- 규칙: [.cursorrules](.cursorrules)
- 스킬: [.cursor/skills/magic-square-tdd/](.cursor/skills/magic-square-tdd/) · [.cursor/skills/magic-square-docs/](.cursor/skills/magic-square-docs/)

---

## 저장소 구조

| 경로 | 내용 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 요구사항·도메인·API·테스트 큐 (SSOT) |
| [src/validate_lines.py](src/validate_lines.py) | `MAGIC_SUM`, `LINE_IDS`, `validate_lines` |
| [tests/test_validate_lines.py](tests/test_validate_lines.py) | `validate_lines` pytest |
| [report/](report/README.md) | Mom Test·세션·번호 보고서 (`NN.*`) |
| [prompt/](prompt/README.md) | 인터뷰 프롬프트·Transcript (`NN.*`) |
| [.cursor/commands/](.cursor/commands/) | ARRR·export 커맨드 |
| [.cursor/skills/](.cursor/skills/) | TDD·문서 스킬 |

---

## 테스트 큐 (요약)

### Logic — `validate_lines` (PRD §5)

| ID | 시나리오 | 기대 `status` |
|----|----------|---------------|
| T1 | `GOLDEN_GRID` 완성 | `pass` |
| T2 | (2,2) 교차셀 변경 → R2·C2 fail | `fail` |
| T3 | D1만 깨짐 | `fail` |
| T4 | D2만 깨짐 | `fail` |
| T5 | 빈칸(0) 존재 | `incomplete` |
| T6 | 열 1개만 틀림 | `fail` |

### Entity · Boundary (설계·후속 RED)

| ID | 대상 | 상태 |
|----|------|------|
| D-LOC-01~03 | `find_blank_coords` (G1 빈칸 좌표) | planned |
| U-IN-01~02 | `InputHandler.parse_grid_lines` | planned |

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| `validate_lines` 본문 | 미구현 (`...`) |
| 테스트 | T2 RED (`test_t2_r2_c2_intersection_fail`) |
| `pytest` | T2 **FAILED** — GREEN 대기 |
| ARRR 커맨드·스킬 | 6종 + `magic-square-tdd` / `magic-square-docs` |
| Git | `origin/staging` · 로컬 `spec` |

---

## 읽는 순서

1. [docs/PRD.md](docs/PRD.md) — 요구사항·API·테스트 큐
2. [report/mom-test-step1.md](report/mom-test-step1.md) — Mom Test 인터뷰
3. [report/session3-workbook-1004.md](report/session3-workbook-1004.md) — R-G-I-O·성공 기준 S1~S3
4. [report/01.session3-harness-cursor-commands.md](report/01.session3-harness-cursor-commands.md) — 하네스·커서룰 구축
5. [report/02.REPORT.md](report/02.REPORT.md) — T2 RED·export
