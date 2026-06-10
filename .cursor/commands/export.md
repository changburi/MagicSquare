# export-session — 세션 보고서 + Transcript Export

이번 대화를 정리해 두 폴더에 저장한다.

> 폴더 매핑: `Report/` → `report/`, `Prompting/` → `prompt/`

---

## 번호 규칙

1. `report/`와 `prompt/`에 있는 기존 `NN.*` 파일을 확인한다.
2. 가장 큰 번호 + 1을 다음 번호로 쓴다. (예: `04`까지 있으면 → `05`)
3. 번호는 **2자리** (`01`, `02`, … `05`).

---

## 생성 파일 (반드시 2개)

| 파일 | 설명 |
|------|------|
| `report/NN.REPORT.md` | 세션 요약 보고서 |
| `prompt/NN.Export-Transcript.md` | 대화 전문 Export |

---

## 보고서 형식 (`report/NN.REPORT.md`)

- 제목: `# MagicSquare_1004 — {세션 주제}`
- 상단 메타 표: 프로젝트, 단계, 보고서 생성일, 목적
- 섹션: **1. 요약** / **2. 핵심 결정·산출물** / **3. 다음 단계**
- 마지막 줄: `*본 문서는 report/NN.REPORT.md — …입니다.*`
- 관련 Transcript 링크: `prompt/NN.Export-Transcript.md`

---

## Transcript 형식 (`prompt/NN.Export-Transcript.md`)

- 제목 + `_Exported on {오늘 날짜} from Cursor_`
- **User** / **Cursor** 턴별로 대화 재구성 (요약이 아닌 전문)
- 마지막에 생성된 파일 목록 표
- 마지막 줄: `*본 문서는 prompt/NN.Export-Transcript.md — …입니다.*`

---

## 절차

1. `report/`, `prompt/`에서 다음 번호(NN)를 결정한다.
2. 위 형식으로 두 파일을 **직접 생성**한다.
3. 완료 후 생성 파일 경로·번호·한 줄 요약을 보고한다.

### 완료 보고 형식

```
## Export 완료

| 종류 | 경로 |
|------|------|
| 보고서 | report/NN.REPORT.md |
| Transcript | prompt/NN.Export-Transcript.md |

**순번:** NN
**주제:** <한 줄>
```

---

## 금지

| 금지 | 이유 |
|------|------|
| 기존 `01~04` 파일 덮어쓰기 | 순번 충돌 |
| 번호 없이 저장 (`REPORT.md` 단독명) | 명명 규칙 위반 |
| 보고서만 만들고 Transcript 생략 (또는 그 반대) | 쌍 저장 원칙 |
| `src/`, `tests/` 무단 수정 | 이 커맨드는 문서만 |
| Git commit·push | 사용자 요청 시만 (`.cursorrules`) |
