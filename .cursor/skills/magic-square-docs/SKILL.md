---
name: magic-square-docs
description: >-
  MagicSquare 세션 보고서·Transcript·ARRR 체크리스트를 report/prompt 번호 규칙에
  맞게 작성. export-session, save-report, ARRR 실습 마감, TDD 세션 정리, Mom
  Test 문서화 시 사용.
---

# MagicSquare Docs

## SSOT

| 문서 | 용도 |
|------|------|
| `.cursorrules` | API·TDD·Boundary |
| `docs/PRD.md` | 요구사항 (있을 때) |
| `.cursor/commands/export.md` | export-session (`NN.REPORT` + `NN.Export-Transcript`) |
| `.cursor/commands/save-report.md` | `NN.<slug>.md` + `NN.<slug>-transcript.md` |

## 번호 규칙

1. `report/`, `prompt/`에서 `^\d{2}\.` 파일 스캔
2. **max(NN) + 1** (없으면 `01`)
3. 같은 세션은 **동일 NN** — 보고서 1 + Transcript 1 (+ 체크리스트는 세션 메모)

### export-session (`/export-session` = `export.md`)

| 출력 | 경로 |
|------|------|
| 보고서 | `report/NN.REPORT.md` |
| Transcript | `prompt/NN.Export-Transcript.md` |

### save-report (`/save-report`)

| 출력 | 경로 |
|------|------|
| 보고서 | `report/NN.<slug>.md` |
| Transcript | `prompt/NN.<slug>-transcript.md` |

## 템플릿 (복사·채움)

- [report-template.md](templates/report-template.md) — `MagicSquare_1004` 메타·3섹션
- [transcript-template.md](templates/transcript-template.md) — User/Cursor 턴·파일 표
- [checklist-template.md](templates/checklist-template.md) — ARRR·S1~S3·T1~T6·금지

ARRR 실습 마감 시 checklist를 `report/NN.arr-checklist.md` 등으로 저장해도 됨 (사용자 요청 시).

## 작성 규칙

- **한국어**
- 확정·과거 사실만. 미구현을 완료처럼 쓰지 않음
- TDD 세션: Phase, `pytest` 결과, 변경 파일 경로
- Mom Test: 표면/진짜 문제·증거 3줄 (해당 시)
- 비밀·토큰 기록 금지
- `src/`·`tests/` — 문서 스킬만으로 **무단 수정 금지**

## Transcript 톤

- **User:** 원문·제약 유지
- **Cursor:** 경로·Phase·명령 결과만. 장황한 도구 로그 생략
- 시뮬레이션은 제목에 `[시뮬레이션]`

## 완료 보고 (export-session 형식)

```
## Export 완료

| 종류 | 경로 |
|------|------|
| 보고서 | report/NN.….md |
| Transcript | prompt/NN.….md |

**순번:** NN
**주제:** <한 줄>
```

## 금지

- 기존 `NN.` 파일 덮어쓰기
- 보고서·Transcript 쌍 중 하나만 생성
- Git commit·push (사용자 요청 시만)

## 연계 스킬

- TDD·ARRR: [magic-square-tdd](../magic-square-tdd/SKILL.md)
