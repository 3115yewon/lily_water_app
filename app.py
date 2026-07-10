import streamlit as st

st.set_page_config(
    page_title="은방울꽃 관수 실험 체험",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.main-title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #245c3a;
    margin-bottom: 0.3rem;
}
.sub-text {
    font-size: 1.05rem;
    color: #4d5b52;
    margin-bottom: 1.2rem;
}
.card {
    background-color: #f7fbf7;
    padding: 1.2rem;
    border-radius: 18px;
    border: 1px solid #dbe9dc;
    margin-bottom: 1rem;
}
.result-box {
    padding: 1.4rem;
    border-radius: 20px;
    color: #1f2a1f;
    font-weight: 600;
    border: 1px solid #d3dfd4;
}
.badge {
    display: inline-block;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    background-color: #e7f4ea;
    color: #245c3a;
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 0.7rem;
}
.small {
    color: #5f6f65;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">은방울꽃 관수 실험 체험</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">관수 주기와 물 주는 방식을 직접 선택하고, 잎 색 변화 중심의 실험 결과를 체험해 보세요.</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 실험 조건 선택")

    cycle = st.radio(
        "관수 주기를 고르세요",
        ["매일 물 주기", "주 2회 물 주기", "물을 주지 않음"]
    )

    method = st.radio(
        "물 주는 방식을 고르세요",
        ["두상관수", "저면관수"]
    )

    st.markdown(
        """
        <div class="small">
        실험 설정: 물은 1회 120mL로 고정<br>
        비교 요소: 관수 주기, 관수 방식
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if cycle == "주 2회 물 주기":
        leaf_color = "#6fbf73"
        title = "가장 건강한 상태"
        summary = "잎 색이 가장 안정적이고 건강하게 유지되었습니다."
        detail = "실험에서 주 2회 관수한 은방울꽃이 매일 물을 준 경우보다 더 건강한 잎 색을 보였습니다."
        explain = "너무 자주 물을 주는 것보다, 일정 간격을 두고 수분을 공급하는 것이 은방울꽃의 건강 유지에 더 적절했음을 보여줍니다."
    elif cycle == "매일 물 주기" and method == "저면관수":
        leaf_color = "#9ccc65"
        title = "비교적 건강한 상태"
        summary = "매일 물을 준 조건 중에서는 더 좋은 결과였습니다."
        detail = "실험에서 매일 물을 준 식물들끼리 비교했을 때, 저면관수한 개체가 두상관수한 개체보다 더 건강했습니다."
        explain = "같은 매일 관수 조건이어도, 저면관수는 물이 비교적 고르게 흡수되어 잎 상태가 덜 나빠졌을 가능성이 있습니다."
    elif cycle == "매일 물 주기" and method == "두상관수":
        leaf_color = "#c5e1a5"
        title = "다소 약해진 상태"
        summary = "건강은 유지되지만 가장 좋은 결과는 아니었습니다."
        detail = "매일 관수는 주 2회 관수보다 잎 색이 덜 건강했고, 위로 물 주기는 매일 관수 조건 중에서도 상대적으로 덜 건강했습니다."
        explain = "과한 수분 공급이 반복되면 은방울꽃에 스트레스를 줄 수 있다는 점을 보여줍니다."
    else:
        leaf_color = "#f1d36b"
        title = "가장 스트레스가 큰 상태"
        summary = "잎 색이 가장 누렇게 변한 조건입니다."
        detail = "물을 주지 않은 은방울꽃은 잎 색이 가장 노랗게 변했습니다."
        explain = "수분 부족이 지속되면 잎이 누렇게 변하고 전체 건강 상태가 크게 떨어집니다."

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 결과 보기")
    st.markdown(
        f"""
        <div class="result-box" style="background-color:{leaf_color};">
            <div class="badge">{title}</div>
            선택한 조건: {cycle} + {method}<br><br>
            {summary}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"**해설:** {detail}")
    st.markdown(explain)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### 잎 색 변화 기준")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.color_picker("매우 건강함", "#6fbf73", disabled=True)
with c2:
    st.color_picker("비교적 건강함", "#9ccc65", disabled=True)
with c3:
    st.color_picker("약해짐", "#c5e1a5", disabled=True)
with c4:
    st.color_picker("누렇게 변함", "#f1d36b", disabled=True)

st.markdown("### 실험 핵심")
st.markdown(
    """
- 실험 대상: 은방울꽃  
- 관수 주기: 매일 / 주 2회 / 무관수  
- 관수 방식: 위로 물 주기 / 저면관수  
- 물의 양: 1회 120mL로 고정  
- 결과 지표: 잎 색 변화
"""
)

st.info("이 페이지는 실제 실험에서 관찰한 잎 색 변화를 바탕으로 만든 발표용 체험 웹앱입니다.")
