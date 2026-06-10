# ARRR Phase Checklist — MagicSquare

Export·세션 마감 전 점검. **magic-square-docs** Skill Step A~F와 함께 사용.

## Step A — 입력 수집

- [ ] `git status` 실행 (commit은 사용자 요청 시만)
- [ ] `python -m pytest tests/ -v` **실제 실행**
- [ ] Phase: `red` | `green` | `refactor` | `repeat`
- [ ] Test ID·RED 묶음 기록
- [ ] 사용 Command 목록

## Step B — 번호

- [ ] `report/` `^\d{2}\.` 스캔
- [ ] `prompt/` `^\d{2}\.` 스캔
- [ ] `NN = max + 1` 확정 (덮어쓰기 없음)

## Step C — Report (`report/NN.REPORT.md` 또는 `NN.<slug>.md`)

- [ ] [report-template.md](report-template.md) 적용
- [ ] Phase STEP 섹션 (RED/GREEN/REFACTOR)
- [ ] 산출물 표
- [ ] 미구현을 완료처럼 쓰지 않음

## Step D — Transcript (`prompt/NN.Export-Transcript.md`)

- [ ] [transcript-template.md](transcript-template.md) 적용
- [ ] User/Cursor 턴
- [ ] `_Exported on` 헤더
- [ ] 생성 파일 표

## Step E — README (선택)

- [ ] `report/README.md` 행 추가
- [ ] `prompt/README.md` 행 추가

## Step F — 완료 보고

- [ ] 보고서 경로
- [ ] Transcript 경로
- [ ] 순번 NN · 주제 한 줄

## TDD · ARRR (해당 시)

| Phase | 체크 |
|-------|------|
| **red (plan)** | C2C 4블록 · `/red-skeleton` 안내 |
| **red (skeleton)** | `tests/`만 · `pytest.fail` · FAILED |
| **green** | `src/` 최소 · 1묶음 · PASSED |
| **golden** | `UPDATE_GOLDEN=1` 생성 → matched |
| **refactor** | Budget · PASSED · golden 유지 |

## Mom Test (STEP 1 세션)

- [ ] 진짜 문제 한 문장
- [ ] 증거 3줄
- [ ] S1 D1/D2 · S2 암산 제거 · S3 즉시 특정

## 금지

- [ ] git commit 임의 없음
- [ ] UPDATE_GOLDEN 임의 없음
- [ ] 허위 pytest 결과 없음
