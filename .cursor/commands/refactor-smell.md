# refactor-smell — ARRR Refine (⑦ 스멜 탐지)

코드 **스멜만** 식별한다. **수정·commit 금지.**

> SSOT: `.cursorrules` · `src/` · `tests/`  
> Skill: **magic-square-tdd** (있으면 자동 따름)

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```

---

## 전제

```bash
python -m pytest tests/ -v
```

**전부 PASS** 아니면 중단 → `/green-minimal` 안내.

---

## 자동 절차 (추가 질문 금지)

1. `src/`·`tests/`를 읽고 스멜 체크리스트 스캔.
2. P0 → P1 → P2 우선순위로 표 작성.
3. **Change Budget** 대비 과대 리팩터 후보는 표시만.
4. `/refactor-safe`에 넘길 후보 **1~3개** bullet.
5. **코드 변경 없음.**

### 스멜 체크리스트

| 우선 | 스멜 | 징후 |
|------|------|------|
| **P0** | Magic Number | 리터럴 `34`·`4` (`MAGIC_SUM`·constants 미사용) |
| **P0** | ECB 위반 | entity가 boundary/control import |
| **P0** | incomplete 역전 | 빈칸 검사가 합 검사 뒤 |
| **P1** | Duplicated Code | 10선 합산 copy-paste |
| **P1** | Long Method | `validate_lines`에 10선+상태 전부 |
| **P1** | Mysterious Name | `ROW_*`, `DIAG_*` 비표준 ID |
| **P2** | Feature Envy | 테스트가 구현 내부 순서에만 의존 |
| **P2** | Dead branch | unreachable 분기 |

### Change Budget (refactor-safe용)

| 항목 | 한도 |
|------|------|
| 파일 | ≤ 3 |
| 클래스 | ≤ 1 |
| 메서드 | ≤ 3 |

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/`·`tests/` **수정** | 분석만 |
| commit | 사용자 요청 시만 |
| Solver·UI 제안 | Boundary 밖 |
| 사용자 질문 | 슬래시 단독 동작 |

---

## 완료 보고

```
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI

## pytest
- PASSED (N passed)

## 스멜 목록
| P | 스멜 | 위치 | 증거 |
|---|------|------|------|
| P0 | … | src/validate_lines.py L… | … |

## /refactor-safe 후보 (1~3)
1. {스멜} — {대상 파일} — Budget: 파일 N, 메서드 M
2. …

## 다음
- P0 1개만 골라 /refactor-safe 실행
```

---

## 실행 예시

```
/refactor-smell
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```
