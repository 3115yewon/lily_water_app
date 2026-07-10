import streamlit as st

st.set_page_config(
    page_title="은방울꽃 관수 실험 체험",
    page_icon="🌼",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}
.main-title {
    font-size: 2.5rem;
    font-weight: 900;
    color: #1f5d3a;
    margin-bottom: 0.2rem;
}
.sub-text {
    font-size: 1.08rem;
    color: #526459;
    margin-bottom: 1rem;
}
.card {
    background: #f8fcf8;
    padding: 1.25rem;
    border-radius: 20px;
    border: 1px solid #d9e7da;
    margin-bottom: 1rem;
}
.result-hero {
    padding: 1.5rem;
    border-radius: 24px;
    border: 2px solid #d6dfd7;
    margin-bottom: 1rem;
}
.result-title {
    font-size: 1.7rem;
    font-weight: 900;
    margin-bottom: 0.4rem;
}
.result-grade {
    display: inline-block;
    padding: 0.45rem 0.85rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.7);
    font-weight: 800;
    margin-bottom: 0.9rem;
}
.info-chip {
    display: inline-block;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    background: #e7f5ea;
    color: #1f5d3a;
    font-size: 0.9rem;
    font-weight: 700;
    margin-right: 0.4rem;
    margin-bottom: 0.4rem;
}
.compare-box {
    padding: 1rem;
    border-radius: 18px;
    text-align: center;
    font-weight: 700;
    border: 1px solid #d7dfd7;
}
.small-note {
    color: #617065;
    font-size: 0.95rem;
}
.rule-box {
    background: #fffdf3;
    border: 1px solid #eee2a8;
    padding: 0.9rem 1rem;
    border-radius: 16px;
    color: #6c5a1b;
    font-weight: 600;
}
.method-box {
    background: #f4faf4;
    border: 1px solid #d6e6d7;
    padding: 0.95rem 1rem;
    border-radius: 16px;
    color: #36513d;
    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
    line-height: 1.6;
}
.section-title {
    font-size: 1.2rem;
    font-weight: 800;
    color: #214f35;
    margin-bottom: 0.6rem;
}
.top-box {
    background: linear-gradient(135deg, #f7fbf7, #eef7ef);
    border: 1px solid #dbe8dc;
    border-radius: 24px;
    padding: 1.4rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="top-box">', unsafe_allow_html=True)
st.markdown('<div class="main-title">은방울꽃 관수 실험 체험</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">관수 주기와 관수 방식을 선택하고, 잎 색 변화 중심의 결과를 비교해 보세요.</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<span class="info-chip">발표용 체험 웹앱</span><span class="info-chip">실험 결과 기반</span><span class="info-chip">은방울꽃 잎 색 변화</span>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

left, right = st.columns([1, 1.2])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">실험 조건 선택</div>', unsafe_allow_html=True)

    cycle = st.radio(
        "관수 주기를 고르세요",
        ["매일 물 주기", "주 2회 물 주기", "물을 주지 않음"]
    )

    st.markdown(
        """
        <div class="method-box">
        <b>관수 방식 설명</b><br>
        - <b>두상관수</b>: 위에서 흙 쪽으로 물을 주는 방법<br>
        - <b>저면관수</b>: 화분을 물에 담가 아래에서 물을 흡수하게 하는 방법<br>
        - <b>관수 X</b>: 물을 주지 않는 조건
        </div>
        """,
        unsafe_allow_html=True
    )

    if cycle == "주 2회 물 주기":
        method = "저면관수"
        st.radio(
            "물 주는 방식을 고르세요",
            ["두상관수", "저면관수", "관수 X"],
            index=0,
            disabled=True
        )
        st.markdown(
            '<div class="rule-box">주 2회 물 주기 조건에서는 관수 방식이 저면관수로 고정됩니다.</div>',
            unsafe_allow_html=True
        )

    elif cycle == "물을 주지 않음":
        method = "관수 X"
        st.radio(
            "물 주는 방식을 고르세요",
            ["두상관수", "저면관수", "관수 X"],
            index=2,
            disabled=True
        )
        st.markdown(
            '<div class="rule-box">물을 주지 않음 조건에서는 관수 방식이 자동으로 관수 X로 고정됩니다.</div>',
            unsafe_allow_html=True
        )

    else:
        method = st.radio(
            "물 주는 방식을 고르세요",
            ["두상관수", "저면관수"],
            index=0
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<span class="info-chip">물의 양: 1회 120mL</span>', unsafe_allow_html=True)
    st.markdown('<span class="info-chip">결과 지표: 잎 색 변화</span>', unsafe_allow_html=True)
    st.markdown(
        '<p class="small-note">실험에서는 관수 주기와 방식에 따라 은방울꽃 잎의 건강 상태 차이를 비교했습니다.</p>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if cycle == "주 2회 물 주기":
        leaf_color = "#4CAF50"
        title = "가장 건강한 상태"
        grade = "추천"
        emoji = "🌿"
        summary = "잎 색이 가장 선명하고 안정적으로 유지되었습니다."
        detail = "실험에서 주 2회 관수한 은방울꽃이 가장 건강한 잎 색을 보였습니다."
        explain = "너무 자주 물을 주는 것보다, 일정 간격을 두고 수분을 공급하는 방식이 더 적절했습니다."

    elif cycle == "매일 물 주기" and method == "저면관수":
        leaf_color = "#8BC34A"
        title = "비교적 건강한 상태"
        grade = "양호"
        emoji = "🍃"
        summary = "매일 물을 준 조건 중에서는 더 좋은 결과였습니다."
        detail = "매일 관수 조건에서는 저면관수가 두상관수보다 더 건강한 잎 색을 보였습니다."
        explain = "같은 물 양이어도, 아래에서 흡수되는 방식이 스트레스를 조금 덜 줄 수 있습니다."

    elif cycle == "매일 물 주기" and method == "두상관수":
        leaf_color = "#DCE775"
        title = "다소 약해진 상태"
        grade = "주의"
        emoji = "🪴"
        summary = "건강은 유지되지만 가장 좋은 결과는 아니었습니다."
        detail = "매일 관수는 주 2회 관수보다 잎 색이 덜 건강했고, 두상관수는 상대적으로 불리했습니다."
        explain = "잦은 관수는 은방울꽃에 과한 수분 스트레스를 줄 수 있습니다."

    elif cycle == "물을 주지 않음":
        leaf_color = "#FFD54F"
        title = "가장 스트레스가 큰 상태"
        grade = "비추천"
        emoji = "🥀"
        summary = "잎 색이 가장 누렇게 변한 조건입니다."
        detail = "물을 주지 않은 은방울꽃은 잎 색이 가장 노랗게 변했습니다."
        explain = "수분 부족이 지속되면 잎이 누렇게 변하고 전체 건강 상태가 크게 떨어집니다."

    else:
        leaf_color = "#E8F5E9"
        title = "조건 확인 필요"
        grade = "확인"
        emoji = "❓"
        summary = "선택한 조합을 다시 확인해 주세요."
        detail = "일반적인 실험 조합과 다른 선택입니다."
        explain = "왼쪽 조건을 다시 선택해 결과를 비교해 보세요."

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 결과 비교")

    st.markdown(
        f"""
        <div class="result-hero" style="background:{leaf_color};">
            <div class="result-title">{emoji} {title}</div>
            <div class="result-grade">판정: {grade}</div>
            <div style="font-size:1.08rem; font-weight:800; margin-bottom:0.5rem;">
                선택한 조건: {cycle} + {method}
            </div>
            <div style="font-size:1rem;">
                {summary}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            '<div class="compare-box" style="background:#4CAF50;">건강함<br><span style="font-size:1.6rem;">●</span></div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div class="compare-box" style="background:#DCE775;">보통<br><span style="font-size:1.6rem;">●</span></div>',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            '<div class="compare-box" style="background:#FFD54F;">나쁨<br><span style="font-size:1.6rem;">●</span></div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**해설:** {detail}")
    st.markdown(explain)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### 실험 핵심 정리")
st.markdown("""
- 실험 대상: 은방울꽃
- 관수 주기: 매일 / 주 2회 / 물 주지 않음
- 관수 방식: 두상관수 / 저면관수 / 관수 X
- 물의 양: 1회 120mL 고정
- 결과 지표: 잎 색 변화
""")

st.info(
    """
이 웹앱은 실제 실험에서 관찰한 잎 색 변화를 바탕으로 만든 발표용 체험 페이지입니다.
""",
    icon="ℹ️"
)
