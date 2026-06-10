# refactor-safe — ARRR Refine (안전 리팩터)

`/refactor-smell` 표에서 **선택한 스멜 1개**만 Safe Refactor 실행.

> SSOT: `.cursor/commands/refactor-smell.md` · `.cursorrules`  
> Skill: **magic-square-tdd** (있으면 자동 따름)

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: refactor | Layer: entity | Track: Logic
```

이어서 **한 문장**: 제거하는 스멜·대상 파일.

---

## 원칙

| 원칙 | 내용 |
|------|------|
| 입출력 불변 | `validate_lines` API·`status`·`failed_lines` 규칙 변경 금지 |
| 좌표 | 1-based 문서·golden과 충돌 없게 |
| E001~E005 | emit 금지 |
| Budget | 파일 ≤3 · 클래스 ≤1 · 메서드 ≤3 |
| 범위 | 기능 추가·버그 수정 금지 (별도 GREEN) |

---

## 자동 절차 (추가 질문 금지)

1. `python -m pytest tests/ -v` → 시작 **PASSED** 확인.
2. smell 표 또는 채팅에서 **스멜 1개** 확정.
3. Budget 내 **행위 보존** 리팩터 1회.
4. `python -m pytest tests/ -v` → **PASSED** 유지.
5. golden 있으면 `UPDATE_GOLDEN` **없이** matched 확인.
6. golden diff: **의도적** → ISS 문서화 + `UPDATE_GOLDEN=1` / **비의도** → 롤백.

### 허용 패턴

- `_line_sum(cells) -> int`
- `LINE_SPECS` 튜플로 10선 좌표 데이터화
- `MAGIC_SUM`·`LINE_IDS` 단일 모듈 정리

---

## 금지

| 금지 | 이유 |
|------|------|
| `tests/` assert 완화 | RED 회피 |
| Budget 초과 | 안전 리팩터 |
| 동작·계약 변경 | 리팩터 아님 |
| Git commit·push | 사용자 요청 시만 |

---

## 완료 보고

```
Phase: refactor | Layer: entity | Track: Logic

## 제거한 스멜
- {한 줄}

## 변경 요약
- {파일·메서드 bullet}

## pytest
- python -m pytest tests/ -v → PASSED (N passed)

## golden matched
- yes / n/a / diff (의도·롤백 여부)

## 잔여
- (없음 / bullet)

## 다음
- 잔여 → /refactor-smell
- T1~T6 미커버 → /red-test-plan
```

---

## 실행 예시

```
/refactor-safe
Phase: refactor | Layer: entity | Track: Logic
스멜: Duplicated Code — 10선 합 계산 4곳 반복
대상: src/validate_lines.py
Budget: 파일 1개, 메서드 2개 extract
```
