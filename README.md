# LSTM 모델을 통한 영화 긍정/부정 비율 확인 서비스

# 강의실 개발 환경 설정
1. `mkdir C:\Github`
2. `winget install --id=Python.Python.3.13 -e` 또는 직접 설치
3. `git clone https://github.com/kbs-kbs/2025-1-AISP.git`
4. `configurator.bat`
5. `python3.13 -m venv venv` 및 편집기에서 가상환경 활성화
6. `venv\Scripts\activate`
7. `pip3.13 install -r requirements.txt`
8. `playwright install`
9. `scrapy startproject scrpy_plwrt_watchapedia`
10. `cd scrpy_plwrt_watchapedia`
11. `scrapy genspider watchapedia pedia.watcha.com`

## 서버 설정
1. `https://www.apachelounge.com/download/#google_vignette`
2. 다운로드 후 Apache24 파일을 c드라이브에 위치
3. 안의 bin-httpd.exe 파일을 실행하면 바로 로컬 서버가 실행됨
localhost 주소로 접속하면 확인가능
4. 시연 시 cmd-ipconfig-IPv4주소의 ip를 앞의 컴퓨터 주소창에 붙여넣고 실행

## scrapy-playwright setting.py




## 사용 언어
|언어|버전|
|---|---|
|Python|3.13.2|

## 사용 서버
|서버|버전|
|---|---|
|Apache|2.4.63|

## 사용 모델
|서버|설명|
|---|---|
|LSTM 모델|torch.nn.functional|

## 사용 라이브러리
|언어|라이브러리|버전|모듈/클래스|용도|
|---|---|---|---|---|
|Python|scrapy-playwright|0.0.43|page.PageMethod|왓챠피디아 리뷰 동적 데이터 크롤링|
||scikit-learn|1.6.1|sklearn.linear_model/LinearRegression|선형 회귀 모델 사용|
||||sklearn.neighbors/KNeighborsRegressor|k-최근접 이웃 회귀 모델 사용|
||pandas|2.2.3|pandas|데이터 불러오기|
||matplotlib|3.10.1|matplotlib.pyplot|데이터 시각화|

## 사용 외부 리소스/API
|외부 리소스|URI|API|
|---|---|---|
|왓챠피디아 코멘트|https://pedia.watcha.com|크롤링|

## 아키텍쳐 구성

## 🗃️ 디렉토리 구조
```bash
Apache24/
├── htdocs/
│   └── 2025-1-AISP/
│       ├── .venv/
│       ├── scrapy_plwrt_watchapedia/
│       │   ├── scrapy_plwrt_watchapedia/
│       │   │   ├── spiders/
│       │   │   ├── items.py
│       │   │   └── settings.py
│       │   └── scrapy.cfg
│       ├── web_app/
│       │   ├── static/
│       │   ├── templates/
│       │   └── app.py
│       ├── ai_model/
│       │   ├── model.py
│       │   └── train.py
│       ├── requirements.txt
│       └── wsgi.py
└── conf/
    └── httpd.conf
```

## 주요 구성 요소
htdocs/myproject/: 프로젝트 루트 디렉토리

.venv/: 가상환경 디렉토리

myapp/: 파이썬 애플리케이션 코드

static/ 및 templates/: 정적 파일과 HTML 템플릿

requirements.txt: 프로젝트 의존성 목록

wsgi.py: WSGI 애플리케이션 진입점


# 2025-1-AISP
2025학년도 1학기 인공지능서비스프로젝트

1주(3/6) : OT
2주(3/13) : 프로젝트 계획, Agile 방법론
3주(3/20) : 프로젝트 계획 세우기
4주(3/27) : 개발 계획 발표) 어떠한 AI 모듈 사용, 어떠한 기능을 구현, 웹 or 모바일? 
발표 내용에 대해 교수님의 단독 평가 (20점)
5주(4/3) ~ 6주(4/10) : 기본 기능 구현 (데모)
7주(4/17) :1차 결과 - 중간고사) 어느정도 동작하는 서비스 형태
수강생 전체 동료 평가 / 교수님 평가  (30점)
8주(4/24) : 중간고사기간
9주(5/8) ~ 11주(5/22) : 서비스 구현 
12주(5/29) ~ 13주(6/5) : 최종 결과- 기말고사) 서비스가 동작하는 데모 시연
수강생 전체 동료 평가 / 교수님 평가  (30점)
14주(6/12) : 논문(보고서) 작성 방법 /  논문(보고서) 작성
15주(6/19) : 기말고사 기간, 논문(보고서)제출
최종 결과- 기말고사) 논문/보고서 작성

교수님 평가  (기말고사 성적 합산)


기술 위주 디자인x

애자일 기본 2주 최대 30일 마다 한번 -> 1스프린트 -> 실제 동작할 수 있는 기능 데모


## 🏛️ 프로젝트 소개
### 배경
오픈소스 프로젝트는 다양한 배경과 경험을 가진 개발자들이 협력하여 소프트웨어를 빠르고 효율적으로 개발할 수 있는 기회를 제공합니다. 그러나 기여자들이 오픈소스 개발에 대한 충분한 이해를 갖추지 못하거나, 프로젝트 관리자가 개발자들이 쉽게 기여할 수 있는 환경을 조성하지 못한다면 기여율은 저조해지고 프로젝트는 관성을 잃어버리게 됩니다. 따라서 오픈소스를 개발하기 위해서는 협업에 필요한 개념과 기술을 이해하고 활용하는 것이 중요합니다.

### 목표
영화의 리뷰 데이터를 긍정/부정으로 나누어 비율을 보여줌으로써 이용자에게 영화 선택의 고민을 줄여줌.

### 기능
1. **최신 개봉 영화 정보 확인**: 최신 영화의 정보를 사이트 상단에 보여줍니다.
2. **영화 검색 기능**: 찬반비율을 확인하고 싶은 영화를 검색할 수 있습니다.
2. **영화 리뷰 긍정/부정 비율 시각화**: 긍정/부정의 비율을 직관적인 그래프로 보여줍니다.
3. **긍정/부정에 속한 리뷰 확인**: 긍정/부정에 속한 상세 리뷰를 확인 가능합니다.

### 기대 효과
- 입문자들이 오픈소스 프로젝트에 기여할 수 있는 역량을 갖추게 될 것입니다.
- 오픈소스 프로젝트의 체계적이고 효율적인 관리가 가능해질 것입니다.
- 오픈소스 커뮤니티가 활발해지며 창의적인 아이디어와 솔루션을 발견할 수 있습니다.

### 프로젝트 기간
- 2024-11-11 ~ 2024-12-06

### 프로젝트 관리 및 협업 도구

- **GitHub Wiki**: 깃허브 위키를 통해 프로젝트의 개요, 추진 일정, 협업 규칙 등을 문서화합니다.
- **GitHub Projects**: 깃허브의 프로젝트 보드를 사용하여 작업 항목을 시각적으로 관리하고 추적합니다. 칸반 보드를 통해 작업 상태를 쉽게 파악하고, 팀원 간의 협업을 촉진합니다.
- **GitHub Milestones**: 프로젝트의 주요 목표와 일정을 관리하기 위해 마일스톤을 사용합니다. 각 마일스톤은 특정 기간 내에 달성해야 할 목표를 정의합니다.
- **GitHub Issues**: 이슈를 통해 작업을 관리합니다. 버그, 기능 요청, 개선 사항 등을 관리하기 위해 GitHub 이슈를 사용합니다. 이슈 템플릿을 사용하여 이슈를 체계적으로 작성하고, 라벨을 통해 우선순위를 설정합니다.깃
- **GitHub Actions**: 깃허브 액션을 사용하여 풀 리퀘스트가 생성될 때 자동으로 라벨링하여 반복적인 작업을 줄이고 이슈와 풀 리퀘스트를 체계적으로 관리합니다.

## 📆 애자일 프로젝트 추진 일정
<table>
  <tr>
    <td>스프린트 1 (3/20)</td>
    <td>주제 선정</td>
    <td>기능명세서 작성</td>
    <td>프로그래밍 언어/IDE/라이브러리/인공지능 모델/API/DBMS/서버 선정</td>
    <td>화면 설계/플로우 차트</td>
    <td>개발 계획서 작성</td>
  </tr>
  <tr>
   <td>스프린트 2 (3/27)</td>
   <td>개발 계획 발표</td>
   <td>개발 계획 발표</td>
  </tr>
  <tr>
   <td>스프린트 3 (4/3)</td>
  </tr>
  <tr>
   <td>스프린트 4 (4/10)</td>
  </tr>
</table>

기능 중점 두고
계획 개발 테스트


## 📦 설치 방법
프로젝트를 로컬 환경에 설치하려면 깃을 실행한 뒤 다음 명령어를 입력합니다:
```bash
git clone https://github.com/kbs-kbs/2025-1-AISP.git
```

## 🕯️ 기여 방법
프로젝트에 기여하려면 GitHub Wiki의 [기여 파이프라인](https://github.com/kbs-kbs/2024-OSS-Group-Project/wiki/협업-규칙#기여-파이프라인)을 참고해 주세요.

## 🖋️ 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](https://github.com/kbs-kbs/2024-OSS-Group-Project/blob/main/LICENSE) 파일을 참고해 주세요.


기술 검토
명확하게 제시