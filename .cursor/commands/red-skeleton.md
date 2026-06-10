# red-skeleton — ARRR RED (실패 테스트 골격)

`validate_lines` **ARRR·RED 단계** 전용. `/red-test-plan` 큐 기준으로 **실패하는 테스트 1개**를 `tests/`에 추가한다.

> SSOT: `.cursorrules` · `docs/PRD.md`(있으면) · `.cursor/commands/red-test-plan.md`

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: RED
```

이어서 **한 문장**으로 이번에 추가하는 `test_*` 이름·목표를 쓴다.

---

## 자동 절차 (추가 입력·질문 금지)

1. `tests/test_validate_lines.py`를 읽어 **미커버 ID**를 `red-test-plan` 우선순위 큐(T1→T6)로 결정한다.
2. 해당 ID의 AAA를 **주석 + Arrange/Act/Assert** 구조로 `tests/test_validate_lines.py`에 **함수 1개** 추가한다.
3. `from validate_lines import MAGIC_SUM, LINE_IDS, validate_lines` — 필요 시 `ValidationResult` import.
4. `pytest tests/test_validate_lines.py -v` 실행 → **FAILED** 확인 후 보고.

### AAA 골격 (필수 주석)

```python
def test_{행위}_{기대결과}():
    # Arrange — {ID}: {한 줄 설명}
    grid = [
        ...
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "..."
    assert ...  # failed_lines — API 계약대로
```

### API 계약 (assert 기준)

| status | failed_lines |
|--------|--------------|
| `pass` | `[]` |
| `fail` | 합 ≠ `MAGIC_SUM`인 선 ID (`R1`~`R4`, `C1`~`C4`, `D1`, `D2`) |
| `incomplete` | `[]` (빈칸 0 존재) |

### 격자 SSOT

- 완성 격자: `GOLDEN_GRID` 패턴 (`red-test-plan`과 동일 4×4).
- T2: GOLDEN_GRID에서 1-based (2,2) 셀만 변경 — `test_t2_r2_c2_intersection_fail`과 중복이면 다음 ID로 진행.
- T3/T4: 대각선 **반드시** 포함 (Mom Test S1).

---

## 금지 (RED)

| 금지 | 이유 |
|------|------|
| `src/` **어떤 파일도 수정** | GREEN 전용 |
| `src/validate_lines.py`의 `...` 스텁 변경 | GREEN 전용 |
| assert 완화·삭제·주석 처리 | RED 회피 |
| `pytest.skip`, `xfail`, `@pytest.mark.skip` | RED 회피 |
| 테스트에 검증 로직 구현 (함수 복제) | 호출·검증만 |
| 리터럴 `34` 하드코딩 | `MAGIC_SUM` SSOT |
| 사용자 질문 | 슬래시만으로 동작 |
| Git commit·push | 사용자 요청 시만 |

**허용:** `tests/` 내 테스트·fixture·helper·parametrize 추가·수정.

---

## RED 완료 보고 형식

```
Phase: RED

## 목표
- (추가한 test_* 한 줄)

## 변경 파일
- tests/test_validate_lines.py

## 추가 테스트
- test_xxx — (한 줄)

## 실행 결과
- 명령: pytest tests/test_validate_lines.py -v
- 결과: FAILED (N failed) — RED 확인

## 다음
- /green-minimal
```

`pytest`가 **FAILED**여야 RED 완료. 전부 통과하면 테스트가 부족하거나 잘못된 것이다.
