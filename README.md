# Codyssey C1-2 · AI 브랜드 광고 영상 제작

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/deliverable-vertical%20export%20ready-22c55e)

> AI 개인비서 브랜드 **똑똑이(TTOKTTOK AI)**의 가치를 10초 안에 전달하는 생성형 AI 기반 광고 영상 프로젝트입니다.

## 한눈에 보기

| 항목 | 내용 |
|---|---|
| 브랜드 | 똑똑이 · 개인화 AI 비서 |
| 목표 | 업무 과부하를 AI 비서가 해결한다는 메시지 전달 |
| 서사 | 문제 제시 → AI 등장 → 업무 해결 → 브랜드 CTA |
| 제작 방식 | Text-to-Image → 검수 → Image-to-Video → 편집·오디오 통합 |
| 주요 도구 | 이미지 생성 AI, Kling/Runway, ElevenLabs, Suno, CapCut |
| 현재 산출물 | 스토리보드, 프롬프트 개선 비교, 최종 MP4, 상세 기획서 |

## 브랜드 메시지

> 할 일은 많고, 시간은 부족하다. 이제, 똑똑이에게 말하세요.

똑똑이는 일정 관리, 문서 작성, 세무 업무, 영어 학습, 영상 제작 등 사용자의 여러 업무를 하나의 흐름으로 지원하는 개인비서형 AI를 지향합니다.

## 광고 구조

```mermaid
flowchart LR
    A[업무 과부하] --> B[똑똑이 등장]
    B --> C[일정·세무·학습·영상·문서 해결]
    C --> D[브랜드 로고와 CTA]
```

| Scene | 시간 | 전달할 메시지 |
|---|---:|---|
| 01 | 0.0–2.5초 | 할 일은 많고 시간은 부족하다 |
| 02 | 2.5–5.0초 | 이제 똑똑이에게 말하세요 |
| 03 | 5.0–7.5초 | 일정부터 콘텐츠까지 한 번에 |
| 04 | 7.5–10.0초 | 생각보다 가까운 AI, 똑똑이 |

![4씬 스토리보드](assets/images/storyboard.png)

## 프롬프트 개선 사례

초기 휴머노이드 로봇 표현은 브랜드가 차갑고 기계적으로 보이는 문제가 있었습니다. 이를 푸른 홀로그램 빛과 미니멀 UI로 바꿔 친근함·신뢰감·미래성을 함께 표현했습니다.

![프롬프트 개선 비교](assets/images/prompt-iteration.png)

| 항목 | 초기안 | 개선안 |
|---|---|---|
| AI 비서 표현 | 실물 휴머노이드 로봇 | 푸른 홀로그램 빛과 UI |
| 인상 | 기계적·낯섦 | 친근함·신뢰감 |
| 브랜드 연결 | 범용 로봇 이미지 | 개인비서형 AI 정체성 |
| 시각 일관성 | 씬별 변형 위험 | 컬러·빛·UI 규칙으로 통제 |

## 제출물 상태

| 항목 | 상태 | 근거 |
|---|---|---|
| 브랜드 전략·스토리보드 | ✅ 완료 | [상세 기획서](docs/archive/production-report.md), 스토리보드 이미지 |
| 프롬프트 수정 전·후 | ✅ 완료 | 비교 이미지와 기획서 |
| AI 기반 제작 파이프라인 | ✅ 문서화됨 | 기획 → 생성 → 검수 → 편집 과정 |
| 가로형 원본 MP4 | ✅ 보존 | [`assets/video/ttokttok-ad-horizontal.mp4`](assets/video/ttokttok-ad-horizontal.mp4) |
| 세로형 9:16 납품본 | ✅ 완료 | [`assets/video/ttokttok-ad-vertical.mp4`](assets/video/ttokttok-ad-vertical.mp4) |
| 10초 이내 납품본 | ✅ 완료 | 9.916667초, H.264/AAC |

기존 MP4는 **10.03초, 1280×720**의 가로형 원본으로 그대로 보존합니다. 별도 납품본은 원본의 중심 장면과 오디오를 유지하고, 흐린 배경으로 세로 캔버스를 확장해 **1080×1920, 9.916667초, H.264/AAC**로 출력했습니다.

![세로형 납품본 실제 출력 프레임](assets/images/vertical-delivery-preview.png)

## 제작 규격

| 구분 | 제출 기준 | 현재 상태 |
|---|---|---|
| 화면 비율 | 9:16 세로형 | ✅ 9:16 |
| 해상도 | 1080×1920 권장 | ✅ 1080×1920 |
| 길이 | 10초 이내 | ✅ 9.916667초 |
| 영상 코덱 | H.264 권장 | ✅ H.264 |
| 오디오 | AI 음성·BGM·효과음 중 하나 이상 | ✅ AAC 오디오 포함 |
| 스톡·직접 촬영 | 사용 여부 명시 | 미사용으로 문서화됨 |

## 재출력 기록

1. 기존 가로형 원본과 오디오를 보존했습니다.
2. 원본 장면은 중앙에 유지하고, 동일 장면을 흐린 배경으로 확장해 세로 캔버스를 구성했습니다.
3. 마지막 프레임은 9.916667초로 제한했습니다.
4. 실제 출력 프레임을 `assets/images/vertical-delivery-preview.png`에 증빙으로 저장했습니다.
5. `evidence/manifest.toml`과 적합성 문서를 완료 상태로 갱신했습니다.

## 검증

```powershell
$env:PYTHONPATH = "src"
python -m c1_2_quality validate
python -m unittest discover -s tests -v
```

검증기는 매니페스트의 완료 항목이 실제 파일을 가리키는지 검사합니다. 영상의 재생시간·해상도는 내보내기 뒤 미디어 속성으로 다시 확인합니다.

## 저장소 구조

```text
.
├─ assets/
│  ├─ images/             # 스토리보드와 프롬프트 개선 이미지
│  └─ video/              # 현재본과 향후 세로형 납품본
├─ docs/
│  ├─ archive/            # 기존 상세 기획서 원문
│  ├─ mission/            # 미션 적합성 판정
│  └─ production/         # 납품·재출력 규격
├─ evidence/              # 요구사항 매니페스트
├─ src/c1_2_quality/      # 증빙 검증 CLI
├─ tests/
└─ .github/workflows/
```

## 관련 문서

- [미션 적합성 검토](docs/mission/compliance.md)
- [영상 납품 규격](docs/production/delivery-spec.md)
- [기존 상세 기획서](docs/archive/production-report.md)
- [기여·운영 규칙](CONTRIBUTING.md)
