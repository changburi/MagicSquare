# refactor-safe — ARRR Refactor (안전 리팩터)

`validate_lines` **ARRR·Refactor 2단계** — `/refactor-smell`에서 **우선순위 1위** 냄새를 제거한다. 테스트는 **항상 GREEN** 유지.

> SSOT: `.cursorrules` · `.cursor/commands/refactor-smell.md`

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: REFACTOR
```

이어서 **한 문장**으로 이번에 제거하는 냄새·리팩터 행위를 쓴다.

---

## 자동 절차 (추가 입력·질문 금지)

1. `pytest tests/test_validate_lines.py -v` → 시작 시 **PASSED** 확인. 실패면 GREEN 복구 후 종료.
2. `src/validate_lines.py`를 읽고 smell 체크리스트로 **가장 심한 냄새 1개**를 스스로 선정 (smell 보고 없어도 동일 기준 적용).
3. **행위 보존** 리팩터 1회 수행 (이름 정리·중복 제거·helper 추출 등).
4. `pytest` 재실행 → **PASSED** 유지 확인. 실패 시 **즉시 롤백** 후 보고.
5. API 계약·`LINE_IDS`·`incomplete` 우선순위가 변하지 않았는지 자가 점검.

### 안전 리팩터 원칙

| 원칙 | 내용 |
|------|------|
| 한 번에 하나 | 냄새 1종류만 처리 |
| 테스트 불변 | `tests/` 수정 금지 (unless 버그 — 그때는 계약 명시 후 최소 수정) |
| 최소 추상화 | 1~2줄 helper 과도 추출 금지 |
| SSOT 유지 | `MAGIC_SUM`, `LINE_IDS` 단일 출처 |

### 허용 패턴 예

- `_line_sum(cells) -> int` private helper
- `LINE_SPECS` 튜플로 10선 좌표 데이터화
- 변수명 `total` → `line_sum` (의미 명확화)

---

## 금지 (REFACTOR)

| 금지 | 이유 |
|------|------|
| 동작 변경 (새 status·새 failed_lines 규칙) | 리팩터 아님 |
| `tests/` assert 완화 | RED 회피 |
| 기능 추가 (Solver, UI, ECB 통합) | Boundary 밖 |
| 사용자 질문 | 슬래시만으로 동작 |
| Git commit·push | 사용자 요청 시만 |

---

## REFACTOR 완료 보고 형식

```
Phase: REFACTOR

## 제거한 냄새
- (한 줄)

## 변경 파일
- src/validate_lines.py

## 실행 결과
- pytest tests/test_validate_lines.py -v → PASSED (N passed)

## 잔여 냄새
- (있으면 bullet, 없으면 "없음")

## 다음
- 잔여 있음 → /refactor-smell → /refactor-safe
- T1~T6 미커버 → /red-test-plan
```
