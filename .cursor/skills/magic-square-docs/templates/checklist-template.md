# MagicSquare ARRR · 세션 체크리스트

**순번:** NN  
**날짜:** YYYY-MM-DD  
**세션:** {주제}

---

## SSOT 확인

- [ ] `.cursorrules` — 10선·API·TDD 경계
- [ ] `docs/PRD.md` — (있을 때) 요구사항 반영
- [ ] `report/session3-workbook-1004.md` — S1~S3

## ARRR 진행

| 단계 | 커맨드 | 완료 | 비고 |
|------|--------|------|------|
| Arrange | `/red-test-plan` | [ ] | 테스트 ID: T |
| RED | `/red-skeleton` | [ ] | test_* |
| GREEN | `/green-minimal` | [ ] | pytest PASSED |
| GREEN | `/golden-master` | [ ] | GOLDEN_GRID |
| Refactor | `/refactor-smell` | [ ] | 냄새 N건 |
| Refactor | `/refactor-safe` | [ ] | GREEN 유지 |

## Mom Test S1~S3

- [ ] **S1** 대각선(D1·D2) 테스트 포함
- [ ] **S2** pass 한 호출·암산 불필요
- [ ] **S3** 실패 축 즉시 특정 (T2·T6류)

## 테스트 큐 T1~T6

- [ ] T1 pass (완성 격자)
- [ ] T2 fail R2·C2 교차
- [ ] T3 fail D1
- [ ] T4 fail D2
- [ ] T5 incomplete
- [ ] T6 fail 열 단독

## 문서 Export (선택)

- [ ] `report/NN.{slug}.md` — [report-template](report-template.md)
- [ ] `prompt/NN.{slug}-transcript.md` — [transcript-template](transcript-template.md)
- [ ] `/export-session` 또는 `/save-report` 완료

## 금지 준수

- [ ] RED에서 `src/` 미수정
- [ ] assert 완화·skip·xfail 없음
- [ ] Git commit·push — 사용자 요청 시만

---

*체크리스트 완료 시 report/ 또는 prompt/에 NN 번호로 보관.*
