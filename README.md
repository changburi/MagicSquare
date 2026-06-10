# MagicSquare

4×4 부분 마방진의 **행·열·대각선 10선 합(34)** 을 판정하고, 틀린 축을 식별하는 `validate_lines` TDD 프로젝트 (세션 3).

**요구사항 SSOT:** [docs/PRD.md](docs/PRD.md)

---

## 문제·목표

Mom Test에서 도출한 진짜 문제: 부분 마방진을 채운 뒤 **모든 합 조건(특히 대각선)을 빠짐없이 검증했는지 확신하기 어렵고**, 틀린 줄을 모른 채 진행하다 **암산으로 다시 확인할 때까지 시간을 낭비**한다.

세션 3 목표는 앱이나 자동 풀이가 아니라, **10개 축 판정을 Test Loop로 고정**하는 것이다.

---

## API

```python
validate_lines(grid) -> {"status": str, "failed_lines": list[str]}
```

| `status` | 의미 |
|----------|------|
| `incomplete` | 빈칸(`0`) 존재 — 합 검사 생략 |
| `pass` | 10선 모두 합 `34`, 빈칸 없음 |
| `fail` | 빈칸 없고 한 선 이상 합 ≠ `34` |

- 검사 선 ID: `R1`~`R4`, `C1`~`C4`, `D1`(주대각), `D2`(역대각)
- 구현: `src/validate_lines.py` · 테스트: `tests/test_validate_lines.py`

---

## 빠른 시작

```bash
# Python 3.10+
pip install pytest
pytest tests/test_validate_lines.py -v
```

---

## TDD · ARRR

| 단계 | Cursor 커맨드 |
|------|----------------|
| Arrange | `/red-test-plan` |
| RED | `/red-skeleton` |
| GREEN | `/green-minimal`, `/golden-master` |
| Refactor | `/refactor-smell`, `/refactor-safe` |

- RED: `tests/`만 수정 · GREEN: `src/` 최소 구현
- 규칙: [.cursorrules](.cursorrules) · 스킬: `.cursor/skills/magic-square-tdd/`

---

## 저장소 구조

| 경로 | 내용 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 요구사항·도메인·테스트 큐 (SSOT) |
| [src/validate_lines.py](src/validate_lines.py) | `MAGIC_SUM`, `LINE_IDS`, `validate_lines` |
| [tests/test_validate_lines.py](tests/test_validate_lines.py) | pytest |
| [report/](report/README.md) | Mom Test·세션 보고서 |
| [prompt/](prompt/README.md) | 인터뷰·워크북 프롬프트 |
| [.cursor/commands/](.cursor/commands/) | TDD·ARRR·export 커맨드 |

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| `validate_lines` 본문 | 미구현 (`...`) |
| 테스트 | T2 RED (`test_t2_r2_c2_intersection_fail`) |
| `pytest` | T2 FAILED — GREEN 대기 |

---

## 읽는 순서

1. [docs/PRD.md](docs/PRD.md) — 요구사항·API·테스트 큐
2. [report/mom-test-step1.md](report/mom-test-step1.md) — Mom Test 인터뷰
3. [report/session3-workbook-1004.md](report/session3-workbook-1004.md) — R-G-I-O·성공 기준 S1~S3

---

*작성자: 오창조의불 · 리뷰어: 홍길동*
