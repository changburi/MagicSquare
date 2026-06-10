# Save Report — 보고서·Transcript 저장

이번 Cursor 세션의 **작업 보고서**와 **대화 Transcript**를 번호 규칙에 맞춰 저장한다.

> 폴더 매핑: `Report` → `report/`, `Prompting` → `prompt/`

---

## 파일명 규칙 — `01.XXX` 형식

| 항목 | 패턴 | 예시 |
|------|------|------|
| 보고서 | `report/NN.<slug>.md` | `report/04.tdd-red-validate-lines.md` |
| Transcript | `prompt/NN.<slug>-transcript.md` | `prompt/04.tdd-red-validate-lines-transcript.md` |

- `NN`: **2자리 순번** (`01`, `02`, …). `report/`·`prompt/` 각각 기존 `NN.` 파일을 스캔해 **다음 빈 번호**를 쓴다. 같은 세션은 **동일 NN**을 공유한다.
- `<slug>`: kebab-case 주제 (영문·숫자, 소문자). 이번 세션 핵심을 2~4단어로.
- **같은 NN으로 보고서 1개 + Transcript 1개**를 쌍으로 만든다.

### 순번 결정 절차

1. `report/`에서 `^\d{2}\.` 로 시작하는 파일 목록 확인.
2. `prompt/`에서 `^\d{2}\.` 로 시작하는 파일 목록 확인.
3. 두 폴더 중 **가장 큰 NN + 1**을 다음 번호로 사용. (없으면 `01`)

---

## 1) 보고서 생성 — `report/NN.<slug>.md`

### 포함 섹션 (순서 고정)

```markdown
# MagicSquare — <제목>

**작성일:** YYYY-MM-DD
**세션:** <STEP 1 | 세션 3 | TDD RED | …>
**순번:** NN

---

## 요약
(이번 세션에서 한 일 3~5줄)

## 산출물
| 파일/경로 | 변경 |
|-----------|------|
| … | 생성 / 수정 / 삭제 |

## 핵심 결정·계약
- (API, 규칙, 스코프 등 확정된 내용 bullet)

## 미완·다음 단계
- (후속 작업 bullet)

## 참고
- (관련 report·prompt 링크)
```

### 작성 규칙

- **과거 사실·확정 내용만** 기록. 추측·미구현을 완료처럼 쓰지 않는다.
- TDD 세션이면 Phase(RED/GREEN/REFACTOR), 테스트 수, pytest 결과를 포함한다.
- Mom Test 세션이면 표면/진짜 문제·증거 3줄을 포함한다.
- 기존 `report/README.md`는 **이 커맨드에서 수정하지 않는다** (사용자 요청 시만).

---

## 2) Transcript Export — `prompt/NN.<slug>-transcript.md`

### 헤더 (필수)

```markdown
# <제목> — Transcript
_Exported on M/D/YYYY at HH:MM:SS GMT+9 from Cursor_

---
```

### 본문 형식

대화를 **시간순**으로 옮긴다. 턴마다:

```markdown
**User**

<사용자 메시지 원문 또는 핵심 요약>

---

**Cursor**

<어시스턴트 응답 요약. 코드·파일 경로는 유지, 장황한 도구 로그는 생략>

---
```

### Transcript 규칙

- **User** 발화: 의도·제약(금지 사항)을 빠뜨리지 않는다.
- **Cursor** 발화: 생성·수정한 **파일 경로**, **핵심 결론**, **명령 실행 결과**만 남긴다.
- 비밀·토큰·API 키는 **기록하지 않는다**.
- 시뮬레이션·가상 인터뷰는 제목에 `[시뮬레이션]` 표기.

---

## 실행 절차

1. 이번 세션 주제에서 `<slug>`·`<제목>`을 정한다.
2. `report/`, `prompt/`에서 다음 `NN`을 결정한다.
3. `report/NN.<slug>.md` 작성·저장.
4. `prompt/NN.<slug>-transcript.md` 작성·저장.
5. 아래 **완료 보고**를 사용자에게 출력한다.

---

## 완료 보고 형식

```
## Save Report 완료

| 종류 | 경로 |
|------|------|
| 보고서 | report/NN.<slug>.md |
| Transcript | prompt/NN.<slug>-transcript.md |

**순번:** NN
**주제:** <한 줄>
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `01.XXX` 형식 없이 저장 | 명명 규칙 위반 |
| 보고서만 저장하고 Transcript 생략 | 쌍 저장 원칙 |
| 기존 `NN.` 파일 덮어쓰기 | 순번 충돌. 새 번호 사용 |
| `src/`, `tests/` 무단 수정 | 이 커맨드는 문서만 |
| Git commit·push | 사용자 요청 시만 (`.cursorrules`) |

---

## 예시 (첫 저장)

```
report/01.session-harness-cursorrules.md
prompt/01.session-harness-cursorrules-transcript.md
```
