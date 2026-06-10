# golden-master — ARRR Run GREEN (골든 마스터 SSOT)

`validate_lines` **GREEN 보조** — 완성 4×4 마방진 **골든 마스터**를 테스트 SSOT로 고정한다.  
`pass` 기준 격자·변형 테스트의 **단일 진실 공급원**을 만든다.

> SSOT: `.cursorrules` · `docs/PRD.md`(있으면) · `report/session3-workbook-1004.md`

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: GREEN (golden master)
```

이어서 **한 문장**으로 골든 마스터를 어디에 두었는지 쓴다.

---

## 자동 절차 (추가 입력·질문 금지)

1. `tests/test_validate_lines.py`에 `GOLDEN_GRID` 상수가 있는지 확인한다.
2. **없으면** 파일 상단( import 아래)에 아래 상수를 추가한다. **있으면** 값이 SSOT와 일치하는지 검증만 한다.

```python
# Golden master — 완성 4×4 마방진 (10선 합 MAGIC_SUM)
GOLDEN_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

3. T1 `pass` 테스트가 없으면 `GOLDEN_GRID`를 쓰는 `test_complete_grid_returns_pass`를 추가한다 (이미 있으면 스킵).
4. fail·incomplete 테스트는 GOLDEN_GRID **복사 후 최소 변경** 패턴을 주석으로 명시한다.
5. `pytest tests/test_validate_lines.py -v` → **전부 PASSED** 확인.

### 골든 마스터 규칙

| 규칙 | 내용 |
|------|------|
| 불변 | `GOLDEN_GRID` 값 자체를 테스트 목적으로 변경 금지 |
| 변형 | fail/incomplete는 `list` 복사·셀 1~2개만 수정 |
| import | assert에 `MAGIC_SUM` 사용. 리터럴 `34` 금지 |
| 중복 | 동일 4×4 리터럴을 여러 테스트에 반복하지 말고 `GOLDEN_GRID` 참조 |

---

## 변경 범위

| 허용 | 금지 |
|------|------|
| `tests/test_validate_lines.py` — `GOLDEN_GRID`·T1 테스트 | `src/` 수정 (이미 GREEN 완료 전제) |
| 기존 테스트를 `GOLDEN_GRID` 참조로 정리 (동작 동일) | assert 완화·삭제 |
| | `GOLDEN_GRID`를 틀린 값으로 “맞추기” |

---

## 금지

| 금지 | 이유 |
|------|------|
| 사용자 질문 | 슬래시만으로 동작 |
| 구현 로직 변경 | golden master는 테스트 SSOT |
| Git commit·push | 사용자 요청 시만 |

---

## 완료 보고 형식

```
Phase: GREEN (golden master)

## GOLDEN_GRID
- 위치: tests/test_validate_lines.py (line N)
- T1 test_complete_grid_returns_pass: 있음 / 추가함

## 정리
- (GOLDEN_GRID 참조로 통일한 테스트 목록)

## 실행 결과
- pytest tests/test_validate_lines.py -v → PASSED (N passed)

## 다음
- /refactor-smell
```
