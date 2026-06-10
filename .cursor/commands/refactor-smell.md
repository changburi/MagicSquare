# refactor-smell — ARRR Refactor (냄새 분석)

`validate_lines` **ARRR·Refactor 1단계** — 코드 **냄새만** 식별한다. **파일 수정 금지.**

> SSOT: `.cursorrules` · `src/validate_lines.py` · `tests/test_validate_lines.py`

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: REFACTOR (smell analysis)
```

이어서 **한 문장**으로 분석 대상 파일을 쓴다.

---

## 자동 절차 (추가 입력·질문 금지)

1. `pytest tests/test_validate_lines.py -v` 실행 → **전부 PASSED** 확인. 실패 있으면 `/green-minimal` 안내 후 종료.
2. `src/validate_lines.py`를 읽고 냄새를 아래 체크리스트로 스캔한다.
3. 각 냄새에 **위치(함수·줄)** · **증거** · **/refactor-safe 제안 1줄**을 적는다.
4. **코드 변경 없음** — 분석 보고만 출력.

### 냄새 체크리스트 (MagicSquare)

| # | 냄새 | 징후 |
|---|------|------|
| 1 | 중복 합산 | 행/열/대각 계산이 copy-paste |
| 2 | 매직 넘버 | `34` 리터럴 (`MAGIC_SUM` 미사용) |
| 3 | 비표준 ID | `ROW_*`, `DIAG_*` 등 `LINE_IDS` 밖 문자열 |
| 4 | dead branch | unreachable 분기·미사용 변수 |
| 5 | 거대 함수 | `validate_lines` 한 함수에 10선+상태 전부 |
| 6 | 테스트 결합 | 구현 세부(내부 순서)에만 의존하는 assert |
| 7 | incomplete 역전 | 빈칸 검사가 합 검사 뒤에 실행 |

### 우선순위

1. 계약 위반 가능 (냄새 2·3·7)
2. 중복 (냄새 1·5)
3. 가독성 (냄새 4·6)

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/`·`tests/` **수정** | smell 단계는 분석만 |
| 사용자 질문 | 슬래시만으로 동작 |
| 범위 밖 제안 (Solver, UI) | `.cursorrules` Boundary |
| Git commit·push | 사용자 요청 시만 |

---

## 완료 보고 형식

```
Phase: REFACTOR (smell analysis)

## pytest
- PASSED (N passed)

## 냄새 목록
| # | 냄새 | 위치 | 제안 |
|---|------|------|------|
| 1 | … | validate_lines.py L… | … |

## 우선 리팩터
1. (한 줄)

## 다음
- /refactor-safe
```
