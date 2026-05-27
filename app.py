import streamlit as st

from utils.live_search import web_search
from utils.llm import ask

st.set_page_config(
    page_title="Football Scout AI",
    page_icon="⚽",
    layout="wide"
)

st.markdown("""
<style>

.main {
background-color:#0e1117;
}

.big-title{
font-size:48px;
font-weight:700;
color:white;
}

.subtitle{
font-size:18px;
color:#9ca3af;
}

.answer-box{
padding:20px;
border-radius:15px;
background:#111827;
border:1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)

col1,col2=st.columns([4,1])

with col1:

    st.markdown(
    "<div class='big-title'>⚽ Football Scout AI</div>",
    unsafe_allow_html=True
    )

    st.markdown(
    "<div class='subtitle'>Live football intelligence + AI scouting</div>",
    unsafe_allow_html=True
    )

with col2:

    st.metric(
    "Mode",
    "LIVE"
    )

st.divider()

q=st.text_input(
"Search player / club / transfer target",
placeholder=
"Example: Harry Kane 2025 season"
)

c1,c2,c3=st.columns(3)

with c1:
    st.button("🔥 Form")

with c2:
    st.button("🎯 Scout")

with c3:
    st.button("📈 Stats")

if q:

    with st.spinner(
    "Scout analysing..."
    ):

        context=web_search(q)

        ans=ask(
        context,
        q
        )

    st.subheader(
    "Scout Report"
    )

    st.markdown(
    f"""
<div class="answer-box">

{ans}

</div>
""",
unsafe_allow_html=True
)

    with st.expander(
    "Retrieved Context"
    ):

        st.write(
        context
        )