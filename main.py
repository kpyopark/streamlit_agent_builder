import streamlit as st
from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import session
import os
import uuid
from dotenv import load_dotenv
import time

# Dialogflow 프로젝트 설정
load_dotenv()

PROJECT_ID = os.environ['PROJECT_ID']
LOCATION = os.environ['LOCATION']
AGENT_ID = os.environ['AGENT_ID']
SESSION_ID = str(uuid.uuid4())
LANGUAGE_CODE = "ko-KR"
agent = f"projects/{PROJECT_ID}/locations/{LOCATION}/agents/{AGENT_ID}"

def detect_intent(text):
    session_client = SessionsClient()
    session_path = session_client.session_path(
        project=PROJECT_ID, 
        location=LOCATION,
        agent=AGENT_ID,
        session=SESSION_ID)
    text_input = session.TextInput(text=text)
    query_input = session.QueryInput(text=text_input, language_code=LANGUAGE_CODE)
    request = session.DetectIntentRequest(
        session=session_path,
        query_input=query_input,
    )
    response = session_client.detect_intent(request=request)
    response_text = response.query_result.response_messages[0].text.text[0]
    return response_text

st.set_page_config(layout="wide")

# CSS 스타일링
st.markdown("""
    <style>
    .stApp {
        margin-bottom: 80px;
    }
    .fixed-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: white;
        padding: 10px;
        z-index: 999;
    }
    .chat-message {
        color: black;
    }
    .user-message {
        text-align: right;
    }
    .bot-message {
        text-align: left;
    }
    .message-container {
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Dialogflow 챗봇")

# 대화 기록을 저장할 세션 상태 초기화
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# 채팅 창 생성
chat_container = st.container()

# 메시지 표시 함수
def display_message(role, text, timestamp):
    message_time = time.strftime("%H:%M:%S", time.localtime(timestamp))
    if role == "user":
        st.markdown(f'<div class="message-container user-message"><span class="chat-message" style="background-color: #FFF5E6; padding: 5px 10px; border-radius: 15px;">{text}</span> <small>{message_time}</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-container bot-message"><span class="chat-message" style="background-color: #E6F3FF; padding: 5px 10px; border-radius: 15px;">{text}</span> <small>{message_time}</small></div>', unsafe_allow_html=True)

# 대화 기록 표시
#with chat_container:
#    for role, text, timestamp in st.session_state.conversation:
#        display_message(role, text, timestamp)

# 입력 폼 생성 (화면 하단에 고정)
st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
with st.form(key='message_form', clear_on_submit=True):
    user_input = st.text_input("메시지를 입력하세요:", key='input')
    submit_button = st.form_submit_button("전송")
st.markdown('</div>', unsafe_allow_html=True)

if submit_button and user_input:
    # 사용자 메시지를 즉시 표시
    current_time = time.time()
    st.session_state.conversation.append(("user", user_input, current_time))
    
    # 대화 기록 다시 표시
    chat_container.empty()
    for role, text, timestamp in st.session_state.conversation:
        display_message(role, text, timestamp)
    
    # 로딩 메시지 표시
    with st.spinner('응답을 생성 중입니다...'):
        # Dialogflow에 요청 보내기
        bot_response = detect_intent(user_input)
    
    # 봇 응답 추가 및 표시
    st.session_state.conversation.append(("bot", bot_response, time.time()))
    display_message("bot", bot_response, time.time())

# 스크롤을 항상 아래로 유지
st.markdown('<script>window.scrollTo(0,document.body.scrollHeight);</script>', unsafe_allow_html=True)