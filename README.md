## Dialogflow 챗봇

본 프로젝트는 Google Dialogflow CX를 사용하여 챗봇을 구축하는 방법을 보여줍니다. Streamlit을 사용하여 간단한 웹 인터페이스를 만들고 사용자와 챗봇 간의 대화를 시각화합니다.

### 1. 사전 준비

* Google Cloud Platform(GCP) 계정이 있어야 합니다.
* Dialogflow CX 에이전트를 생성해야 합니다.
* GCP 프로젝트에 필요한 환경 변수를 설정해야 합니다.

### 2. 환경 변수 설정

다음 환경 변수를 `.env` 파일에 설정합니다.

```
PROJECT_ID=YOUR_PROJECT_ID
LOCATION=YOUR_LOCATION
AGENT_ID=YOUR_AGENT_ID
```

* `PROJECT_ID`: GCP 프로젝트 ID
* `LOCATION`: Dialogflow CX 에이전트가 있는 위치
* `AGENT_ID`: Dialogflow CX 에이전트 ID

### 3. 실행

1. `pip install -r requirements.txt`를 사용하여 필요한 패키지를 설치합니다.
2. `streamlit run app.py`를 실행하여 챗봇을 시작합니다.

### 4. 사용 방법

* 웹 브라우저에서 `http://localhost:8501`을 열면 챗봇과 대화할 수 있습니다.
* 챗봇과 대화하려면 입력창에 메시지를 입력하고 "전송" 버튼을 클릭합니다.
* 챗봇의 응답이 채팅 창에 표시됩니다.

### 5. 코드 설명

* **`detect_intent()` 함수**: Dialogflow CX에 텍스트를 보내고 응답을 받는 함수입니다.
* **Streamlit**: 웹 인터페이스를 만들고 사용자 입력을 받는 데 사용됩니다.
* **`st.session_state`**: 사용자와 챗봇 간의 대화 기록을 저장하는 데 사용됩니다.

### 6. 주의 사항

* 본 프로젝트는 단순한 예시이며 실제 챗봇을 구축하는 데는 더 많은 코드와 설정이 필요합니다.
* Dialogflow CX를 사용하는 방법에 대한 자세한 내용은 [Dialogflow CX 문서](https://cloud.google.com/dialogflow/cx/docs)를 참조하십시오.

### 7. 추가 기능

* 챗봇의 응답에 이미지, 비디오, 오디오 등 다양한 미디어를 추가할 수 있습니다.
* 챗봇에 사용자 인증 기능을 추가할 수 있습니다.
* 챗봇의 응답을 개인화할 수 있습니다.
* 챗봇의 성능을 모니터링하고 개선할 수 있습니다.

### 8. 기여

본 프로젝트에 기여하고 싶으신 분들은 GitHub에 이슈를 제기하거나 pull request를 보내주시면 감사하겠습니다.

### 9. 라이선스

본 프로젝트는 Apache 2.0 라이선스로 배포됩니다.