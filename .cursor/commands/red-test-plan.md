# red-test-plan — ARRR Arrange (테스트 계획)

`validate_lines` **ARRR·A 단계** 전용. 실패 테스트를 쓰기 **전** Arrange·Act·Assert 계획만 수립한다.  
**코드·파일 변경 없음** — 계획 출력만.

> SSOT: `.cursorrules` · `docs/PRD.md`(있으면) · `report/session3-workbook-1004.md` · `.cursor/commands/export.md`

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: RED (Arrange — test plan)
```

이어서 **한 문장**으로 이번에 계획할 테스트 ID·목표를 쓴다.

---

## 자동 절차 (추가 입력·질문 금지)

1. SSOT를 읽어 API·10선·Mom Test S1~S3를 확인한다.
2. `tests/test_validate_lines.py`를 읽어 **이미 있는 테스트**를 파악한다.
3. 아래 **우선순위 큐**에서 첫 미커버 항목 1개를 고른다 (이미 있으면 스킵).

| 순위 | ID | Mom Test | 검증 행위 | 기대 status | 기대 failed_lines |
|------|-----|----------|-----------|-------------|-------------------|
| 1 | T1 | S2 | 완성 4×4 격자 | `pass` | `[]` |
| 2 | T2 | S3 | (2,2) 교차셀 변경 → R2·C2 동시 fail | `fail` | `R2`, `C2` 포함 |
| 3 | T3 | S1 | D1만 합 깨짐 | `fail` | `D1` 포함 |
| 4 | T4 | S1 | D2만 합 깨짐 | `fail` | `D2` 포함 |
| 5 | T5 | — | 빈칸(0) 1개 이상 | `incomplete` | `[]` |
| 6 | T6 | S3 | 행만 맞고 열 1개만 틀림 | `fail` | 해당 `C*` 1개 |

4. 골든 마스터 격자(완성 4×4)는 아래 SSOT를 쓴다 — 리터럴 재발명 금지.

```python
GOLDEN_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

5. 선택한 ID에 대해 **AAA 계획표**만 출력한다 (`tests/`·`src/` 수정 금지).

---

## AAA 계획표 형식 (출력)

```markdown
## 테스트 계획 — {ID}

**함수명(안):** `test_{행위}_{기대결과}`
**Mom Test:** S{n} — (한 줄 근거)

### Arrange
- grid: (4×4 값 또는 GOLDEN_GRID 변형 설명)
- 좌표: 1-based (행, 열) — 변경 셀 명시
- import: `MAGIC_SUM`, `LINE_IDS` from `validate_lines` (assert에 리터럴 34 금지)

### Act
- `result = validate_lines(grid)`

### Assert
- `result["status"] == "{pass|fail|incomplete}"`
- `result["failed_lines"]` — (정확한 기대 목록 또는 포함 관계)

### RED 예상
- `pytest tests/test_validate_lines.py -v` → FAILED (미구현 또는 의도적 실패)

### 다음 커맨드
- `/red-skeleton` — 위 계획대로 테스트 골격 작성
```

---

## 금지

| 금지 | 이유 |
|------|------|
| 사용자에게 질문·선택 요청 | 슬래시만으로 동작 |
| `tests/`·`src/` **어떤 파일도 수정** | 계획 단계 |
| `pytest` 실행 | skeleton·구현 전 |
| assert 완화·케이스 생략 제안 | RED 회피 |
| `ROW_2`, `DIAG_MAIN` 등 비표준 선 ID | SSOT `R1`~`D2`만 |
| Git commit·push | 사용자 요청 시만 |

---

## 완료 보고 형식

```
Phase: RED (Arrange — test plan)

## 선택 ID
- T{n} — (한 줄)

## 큐 상태
| ID | 상태 |
|----|------|
| T1 | covered / planned / … |

## 다음
- /red-skeleton
```
