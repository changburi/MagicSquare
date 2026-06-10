---
name: magic-square-docs
description: >-
  MagicSquare Report Export, Transcript, /export-session, Phase repeat, ARRR
  1사이클 완료 보고, 세션 N 보고서. Report/NN.REPORT.md, Prompting/NN.Export-Transcript.md
  형식. export-session·save-report 연동.
disable-model-invocation: true
---

# MagicSquare Docs Skill

Export·세션 보고 요청 시 로드. **Export 요청 시 magic-square-docs Skill 로드 후 checklist 수행.**

## SSOT 형식

| 종류 | 경로 |
|------|------|
| export-session | `report/NN.REPORT.md` + `prompt/NN.Export-Transcript.md` |
| save-report | `report/NN.<slug>.md` + `prompt/NN.<slug>-transcript.md` |

폴더: `Report/` → `report/`, `Prompting/` → `prompt/`

## 워크플로

### Step A — 입력 수집

| 항목 | 출처 |
|------|------|
| `git status` | 실제 실행 (commit 임의 금지) |
| `pytest` 결과 | **실제 실행** — 채팅에 없는 결과 기재 금지 |
| Phase | red / green / refactor / repeat |
| Test ID | T1~T6, D-LOC-01 등 |
| Command | /red-test-plan, /export 등 |

### Step B — 번호 결정

`NN = max(report/^\d{2}\./, prompt/^\d{2}\./) + 1` (없으면 `01`)

### Step C — Report

템플릿: [report-template.md](report-template.md)

- 제목: `# MagicSquare_1004 — {주제}`
- Phase별 STEP: RED / GREEN / REFACTOR / repeat
- 메타 표 · 3섹션 (요약 / 핵심 / 다음)

### Step D — Transcript

템플릿: [transcript-template.md](transcript-template.md)

- User / Cursor 턴
- `_Exported on {날짜} from Cursor_`
- `_Source uuid: {선택}` (agent transcript 있을 때)

### Step E — README 갱신

`report/README.md`·`prompt/README.md` 문서 표에 NN 행 추가 (**사용자 요청 또는 export 명시 시만**).

### Step F — 완료 보고

경로 2개 + 순번 + 주제 한 줄.

체크리스트: [phase-checklist.md](phase-checklist.md)

## /export-session 연동

`.cursor/commands/export.md` 실행 시 본 Skill 절차 Step A→F 수행.  
파일명은 `NN.REPORT.md` + `NN.Export-Transcript.md` 고정.

## 작성 규칙

- **한국어**
- 확정·과거 사실만
- TDD: Phase, pytest 결과, 변경 경로
- Mom Test: 표면/진짜 문제·증거 3줄 (해당 시)
- 비밀·토큰 금지

## 금지

| 금지 | 이유 |
|------|------|
| git commit 임의 | `.cursorrules` |
| `UPDATE_GOLDEN` 임의 | golden 우회 |
| 채팅에 없는 pytest 결과 | 사실 왜곡 |
| 기존 `NN.` 덮어쓰기 | 순번 충돌 |
| `src/`·`tests/` 무단 수정 | 문서 Skill |

## 연계

- TDD: [magic-square-tdd](../magic-square-tdd/SKILL.md)
- export: [export.md](../../commands/export.md)
- save-report: [save-report.md](../../commands/save-report.md)
