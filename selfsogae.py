import streamlit as st

if "theme" not in st.session_state:
    st.session_state.theme = "라이트"

st.sidebar.title("⚙️ 설정")

menu = st.sidebar.radio("메뉴", ["메인 화면", "프로필", "취미/관심사", "연락처"])

st.session_state.theme = st.sidebar.radio(
    "테마 선택", ["라이트", "다크"]
)

if st.session_state.theme == "라이트":
    background_color = "#ffffff"
    text_color = "#000000"
else:
    background_color = "#1e1e1e"
    text_color = "#ffffff"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {background_color};
            color: {text_color};
        }}
        .css-18e3th9, .css-1d391kg, .css-1v3fvcr, .css-1dp5vir {{
            color: {text_color};
        }}
        a, a:link, a:visited, a:hover, a:active {{
            color: {text_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

if menu == "메인 화면":
    st.title(":blue[자기소개 페이지]")
    st.header("안녕하세요! 저는 :orange[김주원]입니다.")
    st.markdown(
        "이 페이지는 **Streamlit**과 **HTML,CSS**을 활용해 만든 간단한 자기소개입니다.\n"
        "왼쪽 사이드바에서 테마와 메뉴를 선택해보세요!"
    )
    st.caption("다크 모드를 추천합니다.")
    st.markdown("---")
    st.write("아래에 이름을 입력해주세요!")
    name = st.text_input("")
    if name:
        st.write(f"👋 반가워요! **{name}** 님")

elif menu == "프로필":
    st.subheader("👤 프로필")
    st.write(
        "- 학교 : 한양대학교\n"
        "- 전공 : 데이터사이언스\n"
        "- 관심 분야 : 머신러닝, 웹 개발, 통계"
    )
    st.video("https://www.youtube.com/watch?v=xC-c7E5PK0Y")

elif menu == "취미/관심사":
    st.subheader("🎨 취미 & 관심사")
    st.write(
        "- 여행\n"
        "- 사진\n"
        "- 음악 감상"
    )
    st.subheader("📸 최근 찍은 사진")
    col1 , col2 = st.columns(2)
    with col1:
        st.image("https://imgur.com/RtjgJRh.jpg",width= 317, caption ="서울숲 앞")
    with col2:
        st.image("https://imgur.com/i43Odo3.jpg",width= 300, caption ="새벽 중랑천")

    st.subheader("🎶 요즘 듣는 음악")

    music_rank = [
        ("🐟", "한로로 - 금붕어", "https://www.youtube.com/watch?v=dAgY7zUqd8E"),
        ("🖤", "검정 치마 - Ling Ling", "https://www.youtube.com/watch?v=gjQwwWjxPaQ"),
        ("🌻", "Post Malone - Sunflower", "https://www.youtube.com/watch?v=0-q1KafFCLU"),
    ]

    for icon, title, link in music_rank:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{icon}** : {title}")
        with col2:
            st.link_button("▶️ YouTube", link)

elif menu == "연락처":
    st.subheader("📧 연락처")
    st.write("이메일: **kjw051217@gmail.com**")
    st.write("인스타: [**ju.won1217**](https://www.instagram.com/ju.won1217/)")

st.markdown("---") 
from datetime import datetime
col1, col2 = st.columns([4, 1])

with col1:
    st.caption("2025 Kim Juwon.")
with col2:
    st.caption(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
