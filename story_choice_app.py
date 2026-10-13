import streamlit as st

st.set_page_config(
    page_title="선택으로 만드는 이야기",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- 스타일 ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Noto+Serif+KR:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Gowun Dodum', sans-serif; }
.stApp {
    background: linear-gradient(180deg, #10182b 0%, #18243a 45%, #f4f0e8 45%, #f4f0e8 100%);
}
.block-container { max-width: 850px; padding-top: 2rem; padding-bottom: 4rem; }
.story-hero {
    padding: 2rem 1.8rem; border-radius: 24px; color: #f8f4e9;
    background: linear-gradient(135deg, rgba(29,42,66,.97), rgba(57,67,91,.95));
    border: 1px solid rgba(255,255,255,.16); margin-bottom: 1.25rem;
    box-shadow: 0 16px 40px rgba(0,0,0,.18);
}
.story-kicker { letter-spacing: .18em; color: #e7c98a; font-size: .76rem; font-weight: 700; }
.story-title { font-family: 'Noto Serif KR', serif; font-size: clamp(2rem, 5vw, 3.25rem); line-height: 1.25; margin: .65rem 0; }
.story-subtitle { color: #d4d9e3; font-size: 1.02rem; line-height: 1.8; }
.scene-card {
    background: #fffdf8; border: 1px solid #e7dfd1; border-radius: 20px;
    padding: 1.5rem 1.6rem; color: #292d36; margin: .7rem 0 1rem;
    box-shadow: 0 8px 24px rgba(35,35,35,.05);
}
.scene-label { color: #8a6d42; font-size: .75rem; font-weight: 700; letter-spacing: .12em; }
.scene-heading { font-family: 'Noto Serif KR', serif; font-size: 1.5rem; font-weight: 700; margin: .45rem 0 1rem; }
.scene-copy { font-size: 1.02rem; line-height: 2; white-space: pre-line; }
.small-muted { color: #7a7d85; font-size: .88rem; }
.ending-card {
    background: linear-gradient(135deg, #fffdf8, #f4ead8); border: 1px solid #dfcfaf;
    border-radius: 20px; padding: 1.5rem; margin: .8rem 0;
}
div.stButton > button {
    border-radius: 13px; min-height: 3.1rem; font-weight: 600;
    border: 1px solid #d8c7a8; transition: all .15s ease;
}
div.stButton > button:hover { border-color: #9c7a42; transform: translateY(-1px); }
hr { border-color: #e2d8c8; }
</style>
""", unsafe_allow_html=True)

# ---------- 이야기 데이터 ----------
SCENES = {
    "start": {
        "chapter": "CHAPTER 01 · 발견",
        "title": "책상 밑의 편지",
        "text": """방과 후, 텅 빈 교실에서 가방을 챙기던 너는 책상 밑에 끼워진 편지 한 통을 발견한다.

편지에는 짧은 문장이 적혀 있다.

“미안하다는 말을 꼭 하고 싶었어. 내일이면 너무 늦을지도 몰라.”

보낸 사람의 이름은 없다. 종이 한쪽에는 파란 잉크가 번져 있고, 봉투에는 학교 도서관 도장이 희미하게 찍혀 있다.

편지를 어떻게 할까?""",
        "choices": [
            ("ask", "편지의 주인을 찾아 직접 물어본다.", "상대와 직접 대화하는 길"),
            ("friend", "친한 친구에게 편지를 보여 주고 함께 추리한다.", "다른 관점을 빌리는 길"),
            ("alone", "아무에게도 알리지 않고 단서를 조사한다.", "혼자 진실을 좇는 길"),
        ],
    },
    "ask": {
        "chapter": "CHAPTER 02 · 대면",
        "title": "직접 묻는 용기",
        "text": """도서관에서 반납 도서를 정리하던 지우가 편지의 파란 잉크를 보더니 잠시 손을 멈춘다.

“그거 어디서 났어?”

지우는 편지에 대해 알고 있는 듯하지만, 더는 말하지 않는다. 표정에는 걱정과 망설임이 함께 떠 있다.

지우가 편지를 썼다고 단정할 수는 없다. 어떻게 할까?""",
        "choices": [
            ("gentle", "편지를 발견한 경위를 설명하고, 말하고 싶을 때 이야기해 달라고 한다.", "신뢰를 우선하는 선택"),
            ("press", "내일이면 늦는다는 말이 걱정된다며 지금 설명해 달라고 요구한다.", "빠른 확인을 우선하는 선택"),
        ],
    },
    "friend": {
        "chapter": "CHAPTER 02 · 함께 추리하기",
        "title": "두 사람의 단서",
        "text": """친구 민서는 편지를 한참 바라본다.

“파란 잉크는 도서부 애들이 자주 쓰는 펜이야. 그런데 이 문장, 누군가와 크게 다툰 사람 같아.”

민서는 편지를 다른 친구들에게 보여 주면 금방 주인을 찾을 수 있을 거라고 말한다. 하지만 편지에는 개인적인 사정이 담겨 있을지도 모른다.

어떻게 할까?""",
        "choices": [
            ("private", "편지 내용을 더 퍼뜨리지 않고 도서관 도장과 주변 단서를 확인한다.", "사생활을 지키며 조사하는 선택"),
            ("spread", "친구들에게 편지를 보여 주고 아는 사람이 있는지 묻는다.", "정보를 널리 모으는 선택"),
        ],
    },
    "alone": {
        "chapter": "CHAPTER 02 · 조용한 조사",
        "title": "남겨진 흔적",
        "text": """너는 편지를 다시 봉투에 넣고 도서관으로 향한다.

도서 반납대 옆에는 파란 잉크가 묻은 메모지가 놓여 있다. 메모지에는 ‘창가 자리, 마지막 종이 울린 뒤’라는 문장이 적혀 있다.

누군가를 만나야 할 수도 있다. 그러나 편지의 주인을 잘못 짚으면 엉뚱한 사람에게 상처를 줄 수 있다.

어떻게 할까?""",
        "choices": [
            ("wait", "창가 자리에서 기다리되, 먼저 상대를 단정하지 않는다.", "관찰과 신중함을 택하는 선택"),
            ("investigate", "도서관 기록과 메모를 더 확인해 주인을 특정하려 한다.", "증거 수집을 우선하는 선택"),
        ],
    },
    "gentle": {
        "chapter": "CHAPTER 03 · 마음의 문",
        "title": "말할 시간을 주다",
        "text": """지우는 한참 망설이다가 조용히 입을 연다.

“내가 쓴 건 아니야. 하지만 편지를 쓴 사람이 누구인지는 알아. 어제 내 친구 서윤이가 누군가와 다퉜거든. 대신 말해 주는 건 맞지 않는 것 같아.”

지우는 서윤이가 오늘도 혼자 남아 있었다고 덧붙인다. 이제 서윤이를 직접 찾아갈 수도 있고, 지우가 편지를 전해 주도록 부탁할 수도 있다.""",
        "choices": [
            ("meet", "서윤이를 직접 찾아가 편지에 대해 조심스럽게 묻는다.", "직접 마주하는 선택"),
            ("ask_help", "지우에게 편지를 전해 주고 서윤이가 원할 때 이야기해 달라고 부탁한다.", "중재를 부탁하는 선택"),
        ],
    },
    "press": {
        "chapter": "CHAPTER 03 · 서두른 질문",
        "title": "닫혀 버린 대화",
        "text": """지우는 어깨를 움츠린다.

“나도 잘 모른다니까.”

지우는 서둘러 자리를 떠난다. 네가 걱정한 마음은 진심이었지만, 상대에게는 추궁처럼 들렸을 수도 있다. 그래도 도서관 반납대에는 편지와 비슷한 파란 잉크 자국이 남아 있다.

이제 어떻게 할까?""",
        "choices": [
            ("apologize", "지우를 다시 만나 질문이 부담스러웠을 수 있다고 사과한다.", "관계를 회복하려는 선택"),
            ("evidence", "지우를 더 붙잡지 않고 남은 단서를 확인한다.", "증거를 따라가는 선택"),
        ],
    },
    "private": {
        "chapter": "CHAPTER 03 · 지켜야 할 비밀",
        "title": "도서관의 기록",
        "text": """도서관 도장을 확인한 민서는 최근 도서부에서 책갈피 만들기 활동을 했다는 사실을 떠올린다.

도서관 책상에는 같은 파란 잉크로 적힌 메모가 하나 더 있다. 이름은 없지만, ‘미안해. 네가 오해했을까 봐 무서웠어’라고 적혀 있다.

누군가의 사정을 함부로 공개하지 않으면서도 도울 방법을 찾아야 한다.""",
        "choices": [
            ("librarian", "사적인 내용을 공개하지 않고 사서 선생님에게 편지 전달 방법을 묻는다.", "안전한 도움을 요청하는 선택"),
            ("wait_private", "편지를 원래 자리에 두고 주인이 돌아오기를 기다린다.", "상대의 선택을 기다리는 선택"),
        ],
    },
    "spread": {
        "chapter": "CHAPTER 03 · 퍼져 버린 소문",
        "title": "말은 빠르게 번진다",
        "text": """친구 몇 명이 편지를 보고 각자 다른 추측을 내놓는다. 곧 편지의 내용은 원래 문장과 조금씩 다르게 전달된다.

한 친구는 특정 학생의 이름을 말하기 시작한다. 아직 확인된 사실은 없다. 편지를 찾는 일은 빨라질 수 있지만, 누군가가 상처를 입을 수도 있다.

지금 무엇을 해야 할까?""",
        "choices": [
            ("stop_rumor", "추측이 사실이 아님을 알리고 더 이상 편지를 공유하지 않는다.", "확산을 멈추는 선택"),
            ("follow_rumor", "이름이 나온 학생을 찾아가 사실인지 확인한다.", "의심을 직접 확인하는 선택"),
        ],
    },
    "wait": {
        "chapter": "CHAPTER 03 · 창가의 약속",
        "title": "기다림 끝에",
        "text": """마지막 종이 울리고 잠시 뒤, 서윤이가 창가로 다가온다. 서윤이는 네 손에 든 편지를 보고 걸음을 멈춘다.

“그걸 읽었어?”

서윤이는 편지를 빼앗으려 하지 않는다. 다만 무슨 말을 해야 할지 모르겠다는 듯 창밖을 바라본다.

너는 대화를 시작할 수 있지만, 먼저 어떤 태도를 보일지 결정해야 한다.""",
        "choices": [
            ("listen", "무슨 일이 있었는지 먼저 듣고 싶다고 말한다.", "경청을 선택"),
            ("solution", "문제를 해결할 방법부터 함께 찾자고 말한다.", "해결을 선택"),
        ],
    },
    "investigate": {
        "chapter": "CHAPTER 03 · 단서의 무게",
        "title": "확실한 것과 추측",
        "text": """도서관 기록에서 서윤이가 어제 늦게까지 남아 있었다는 사실을 알게 된다. 하지만 그것만으로 편지를 쓴 사람이 서윤이라고 확정할 수는 없다.

너는 기록을 더 확인할 수도 있고, 서윤이에게 단정하지 않은 질문을 건넬 수도 있다.""",
        "choices": [
            ("ask_seoyun", "추측을 사실처럼 말하지 않고 서윤이에게 조심스럽게 묻는다.", "확인과 배려를 함께하는 선택"),
            ("more_records", "추가 기록을 더 찾아본 뒤에야 말을 걸기로 한다.", "증거를 더 모으는 선택"),
        ],
    },
}

# 각 선택은 장면 키로 연결된다. 갈래는 중간에 합류하되 선택 기록은 보존한다.
NEXT = {
    "ask": "ask", "friend": "friend", "alone": "alone",
    "gentle": "gentle", "press": "press",
    "private": "private", "spread": "spread",
    "wait": "wait", "investigate": "investigate",
    "meet": "final", "ask_help": "final",
    "apologize": "final", "evidence": "final",
    "librarian": "final", "wait_private": "final",
    "stop_rumor": "final", "follow_rumor": "final",
    "listen": "final", "solution": "final",
    "ask_seoyun": "final", "more_records": "final",
}

CHOICE_LABELS = {
    "ask": "편지의 주인을 찾아 직접 물어본다.",
    "friend": "친한 친구에게 편지를 보여 주고 함께 추리한다.",
    "alone": "아무에게도 알리지 않고 단서를 조사한다.",
    "gentle": "상대가 말할 때까지 기다려 준다.",
    "press": "지금 설명해 달라고 요구한다.",
    "private": "편지를 퍼뜨리지 않고 단서를 확인한다.",
    "spread": "친구들에게 편지를 보여 주고 묻는다.",
    "wait": "창가에서 기다리되 상대를 단정하지 않는다.",
    "investigate": "기록과 메모를 더 확인한다.",
    "meet": "서윤이를 직접 찾아가 조심스럽게 묻는다.",
    "ask_help": "지우에게 편지를 전해 달라고 부탁한다.",
    "apologize": "지우에게 사과하고 다시 대화한다.",
    "evidence": "남은 단서를 확인한다.",
    "librarian": "사서 선생님에게 안전한 전달 방법을 묻는다.",
    "wait_private": "편지를 두고 주인이 돌아오기를 기다린다.",
    "stop_rumor": "추측이 사실이 아님을 알리고 공유를 멈춘다.",
    "follow_rumor": "이름이 나온 학생에게 사실인지 확인한다.",
    "listen": "먼저 이야기를 듣겠다고 말한다.",
    "solution": "해결 방법을 함께 찾자고 말한다.",
    "ask_seoyun": "단정하지 않고 서윤이에게 묻는다.",
    "more_records": "추가 기록을 더 확인한다.",
}

ENDINGS = {
    "trust": {
        "title": "마음의 문을 연 결말",
        "subtitle": "ENDING 01 · 신뢰",
        "body": "서윤이는 네가 자신의 말을 기다려 주었다는 사실에 조금씩 마음을 연다. 편지를 쓴 사람과 서윤이 사이의 오해는 한 번에 해결되지 않지만, 두 사람은 직접 이야기할 기회를 얻는다. 진실을 알아내는 일만큼이나 누군가가 말할 수 있는 자리를 마련하는 일이 중요하다는 것을 너는 배운다.",
        "theme": "신뢰는 답을 서둘러 얻는 것보다 상대가 말할 수 있는 조건을 만드는 데서 시작될 수 있다.",
    },
    "truth": {
        "title": "단서를 연결한 결말",
        "subtitle": "ENDING 02 · 진실",
        "body": "너는 여러 단서를 비교해 편지의 주인을 찾는 데 가까워진다. 하지만 기록과 흔적만으로는 마음속 사정까지 모두 알 수 없었다. 마지막으로 당사자에게 확인했을 때, 네가 사실이라고 생각했던 일부는 오해였다는 것을 알게 된다. 근거를 모으는 일과 그 근거를 해석하는 일은 다르다.",
        "theme": "증거는 판단의 출발점이지만, 충분한 근거와 당사자의 설명 없이 추측을 사실로 단정해서는 안 된다.",
    },
    "care": {
        "title": "소문을 멈춘 결말",
        "subtitle": "ENDING 03 · 책임",
        "body": "편지의 내용이 더 퍼지기 전에 너는 친구들에게 확인되지 않은 추측을 멈추자고 말한다. 진실이 곧바로 밝혀지지는 않았지만, 누군가가 근거 없는 소문 때문에 상처받을 가능성은 줄어든다. 너는 정보를 전달하는 행동에도 책임이 따른다는 사실을 깨닫는다.",
        "theme": "정보를 빠르게 전달하는 것보다 그 정보가 정확한지, 다른 사람에게 어떤 영향을 주는지 살피는 것이 중요하다.",
    },
    "open": {
        "title": "답을 남겨 둔 결말",
        "subtitle": "ENDING 04 · 여지",
        "body": "너는 편지의 주인을 확실하게 알아내지 못한 채 학교를 나선다. 하지만 편지를 발견한 순간보다 더 많은 가능성을 이해하게 되었다. 누군가에게는 직접 묻는 것이 도움이 되지만, 다른 누군가에게는 기다릴 시간이 필요할 수 있다. 이야기는 끝났지만, 네 판단은 다음 만남에서 계속될 것이다.",
        "theme": "모든 문제에 즉시 답을 내릴 수 있는 것은 아니며, 판단을 유보하는 것 또한 책임 있는 선택이 될 수 있다.",
    },
}

def init_state():
    defaults = {
        "page": "home",
        "scene": "start",
        "history": [],
        "choices": [],
        "ending": None,
        "player_name": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_state()

def restart():
    st.session_state.page = "home"
    st.session_state.scene = "start"
    st.session_state.history = []
    st.session_state.choices = []
    st.session_state.ending = None

def pick_ending():
    chosen = [c for c in st.session_state.choices]
    if any(c in chosen for c in ("spread", "follow_rumor")):
        return "care" if "stop_rumor" in chosen else "truth"
    if any(c in chosen for c in ("gentle", "listen", "ask_help", "wait_private", "librarian")):
        return "trust"
    if any(c in chosen for c in ("investigate", "evidence", "ask_seoyun", "more_records")):
        return "truth"
    if any(c in chosen for c in ("press", "solution")):
        return "open"
    return "open"

def show_header():
    st.markdown("""
    <div class="story-hero">
      <div class="story-kicker">INTERACTIVE STORY · 국어 탐구 웹앱</div>
      <div class="story-title">선택으로 만드는 이야기</div>
      <div class="story-subtitle">작은 선택 하나가 인물의 관계를 바꾸고, 이야기의 결말과 의미를 바꿉니다.<br>당신만의 이야기를 만들어 보세요.</div>
    </div>
    """, unsafe_allow_html=True)

def show_scene(scene_key):
    scene = SCENES[scene_key]
    st.markdown(f"""
    <div class="scene-card">
      <div class="scene-label">{scene['chapter']}</div>
      <div class="scene-heading">{scene['title']}</div>
      <div class="scene-copy">{scene['text']}</div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(min((len(st.session_state.choices) + 1) / 4, 1.0), text=f"이야기 진행 · 선택 {len(st.session_state.choices) + 1}")
    st.markdown("#### 어떻게 할까요?")
    for idx, item in enumerate(scene["choices"]):
        key, label, hint = item
        if st.button(f"{label}\n\n{hint}", key=f"{scene_key}_{key}", use_container_width=True):
            st.session_state.history.append(scene_key)
            st.session_state.choices.append(key)
            next_scene = NEXT.get(key, "final")
            if next_scene == "final":
                st.session_state.ending = pick_ending()
                st.session_state.page = "ending"
            else:
                st.session_state.scene = next_scene
            st.rerun()

def show_ending():
    ending = ENDINGS[st.session_state.ending or pick_ending()]
    st.markdown(f"""
    <div class="ending-card">
      <div class="scene-label">{ending['subtitle']}</div>
      <div class="scene-heading">{ending['title']}</div>
      <div class="scene-copy">{ending['body']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 나의 선택 기록")
    for i, choice in enumerate(st.session_state.choices, 1):
        label = CHOICE_LABELS.get(choice, choice)
        st.markdown(f"**{i}.** {label}")

    st.markdown("### 이야기의 주제 발견하기")
    st.info(ending["theme"])
    st.markdown("### 돌아보기")
    prompts = [
        "가장 고민했던 선택은 무엇이었나요? 그 이유는 무엇인가요?",
        "다른 선택을 했다면 인물의 관계나 사건은 어떻게 달라졌을까요?",
        "이야기의 결말은 처음에 생각했던 주제와 같았나요, 달랐나요? 근거를 들어 설명해 보세요.",
    ]
    for i, prompt in enumerate(prompts, 1):
        st.markdown(f"**{i}. {prompt}**")
        st.text_area("나의 생각", key=f"reflection_{i}", height=90, placeholder="선택과 이야기 속 장면을 근거로 적어 보세요.")
    if st.button("성찰 답안 저장용 텍스트 만들기", use_container_width=True):
        reflection_text = "선택으로 만드는 이야기 - 성찰 기록\n\n"
        reflection_text += "나의 선택:\n" + "\n".join(
            f"{i}. {CHOICE_LABELS.get(c, c)}" for i, c in enumerate(st.session_state.choices, 1)
        )
        reflection_text += f"\n\n결말: {ending['title']}\n주제: {ending['theme']}\n\n"
        reflection_text += "\n\n".join(
            f"{i}. {prompts[i-1]}\n{st.session_state.get(f'reflection_{i}', '')}"
            for i in range(1, 4)
        )
        st.download_button(
            "성찰 기록 다운로드 (.txt)",
            data=reflection_text,
            file_name="선택으로_만드는_이야기_성찰기록.txt",
            mime="text/plain",
            use_container_width=True,
        )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("다른 결말 상상하기", use_container_width=True):
            st.session_state.page = "alternate"
            st.rerun()
    with col2:
        if st.button("처음부터 다시 하기", use_container_width=True):
            restart()
            st.rerun()

def show_alternate():
    st.markdown("## 다른 선택을 했다면?")
    st.write("이번에는 가장 고민했던 순간에 다른 선택을 한다고 상상해 보세요.")
    st.markdown("아래에서 바꾸고 싶은 선택을 골라, 그 선택이 이야기의 주제에 어떤 영향을 주는지 적어 보세요.")
    options = list(CHOICE_LABELS.items())
    selected = st.selectbox("다르게 해 보고 싶은 선택", options, format_func=lambda x: x[1])
    imagined = st.text_area(
        "새로운 결말 상상하기",
        placeholder="이 선택을 했다면 어떤 사건이 생기고, 인물의 관계와 이야기의 주제는 어떻게 달라질까요?",
        height=140,
    )
    if st.button("상상 기록 저장", use_container_width=True):
        if imagined.strip():
            st.session_state.alternate_text = f"다르게 선택하기: {selected[1]}\n\n새로운 결말:\n{imagined}"
            st.success("상상 기록이 준비되었습니다.")
            st.download_button(
                "상상 기록 다운로드 (.txt)",
                data=st.session_state.alternate_text,
                file_name="다른_결말_상상하기.txt",
                mime="text/plain",
                use_container_width=True,
            )
        else:
            st.warning("새로운 결말을 먼저 작성해 주세요.")
    if st.button("결말 화면으로 돌아가기"):
        st.session_state.page = "ending"
        st.rerun()

# ---------- 앱 ----------
show_header()

if st.session_state.page == "home":
    st.markdown("### 오늘의 이야기")
    st.markdown("""
    <div class="scene-card">
      <div class="scene-label">MYSTERY · FRIENDSHIP · GROWTH</div>
      <div class="scene-heading">사라진 편지</div>
      <div class="scene-copy">방과 후 교실에서 발견한 익명의 편지. 누군가 사과하고 싶어 하지만, 내일이면 늦을지도 모른다.

    편지의 주인을 찾는 과정에서 당신은 진실, 신뢰, 사생활 사이에서 선택해야 한다.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**플레이 방법**")
    st.write("1. 장면을 읽고 가장 적절하다고 생각하는 행동을 선택하세요.")
    st.write("2. 선택에 따라 다른 단서와 인물의 반응을 만나게 됩니다.")
    st.write("3. 결말을 확인한 뒤 자신의 선택과 이야기의 주제를 돌아보세요.")
    if st.button("이야기 시작하기", type="primary", use_container_width=True):
        st.session_state.page = "story"
        st.session_state.scene = "start"
        st.rerun()
    st.caption("예상 소요 시간: 5~8분 · 학습 주제: 추론, 인물의 심리, 선택과 서사, 주제 해석")

elif st.session_state.page == "story":
    show_scene(st.session_state.scene)
    if st.button("처음 화면으로 돌아가기", key="back_home"):
        restart()
        st.rerun()

elif st.session_state.page == "ending":
    show_ending()

elif st.session_state.page == "alternate":
    show_alternate()

st.markdown("---")
st.markdown('<div class="small-muted">학습용 인터랙티브 스토리 프로토타입 · 이야기는 선택과 해석에 따라 여러 의미로 읽힐 수 있습니다.</div>', unsafe_allow_html=True)
