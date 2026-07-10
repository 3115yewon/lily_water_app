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
</style>
""", unsafe_allow_html=True)

st.image(
    "https://user-gen-media-assets.s3.amazonaws.com/gpt4o_images/31680fa2-8316-49dc-aae4-ed8b2aeb45a1.png?AWSAccessKeyId=ASIA2F3EMEYEZJV3GD6M&Signature=hhbffapGNcBN%2FIZBjkUJ7le49%2Fg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIEld%2B6XUPUUWQ%2FsjywPtydbGGza4r5oerAEroo%2BJpTvAAiEAushM2Wsv3umN1E3k%2F3aJWAWYFTo3rFLhOdiuaW0jVP0q%2FAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE8KQ1OoGxKDeOv3NirQBG%2F6HUHTQ07XkB88X6YbuFSLGv1KLLQloN4wz22I40rReJ89ZU7PHxk1ww32Pj%2FDfc8obXKwaq6Rc1RLpO45cM0C8kBsAEsIIegYiymGxHNnxofMIFBbKWq8lTFIx5Ka9u0XaE6GDeG%2FRAQ%2F4XK8In4p6scOiz%2F2DXsdy9SiNdFt4RgDBkNRnlmCQ9RUH%2Bb6dBZsI4ZXuryjnKNfWyHsoiLNbZEoIOd0BsxN7Ph2h56Wa2AjEuCPhXDoyEe79tS1MU6bGfUxs%2BWJa3uirdIfz0L%2B%2BOkSARgc8n%2F%2FnEdl5KVNkC0YgM3ZW2ReJjMGu%2FOCj6NZ8k%2F%2B1HlsrOZ0r1vkzHGWRz7pHWnk0O5lZzEVWfnRL3smP3G%2BoJ9j2ldVfihBwVjnrCp98pLNhnatcjfS5eADF4hl%2FSyrr7%2Bs6CrJr9%2BjQl18rjCSL0eWJ8XPQsuT63kJjKww5Oyf9WmPn16qGvv%2FfsxfRaGoIIF9pVDKPZXHqlSXH4TwlAI1HRqgM257WyO1QnIE1hB46fD%2B4kVZVGr2psp%2BJwzyYL7avV7m%2BHHyaU8iS252eRexL7cJRcaLLfcgWnvBVlPlv7NKf7%2BndEWIrPmVMIemHGnssxaIFD%2FeLJ6ZkGk%2FVRJ4q3RsOjIuGs1BVONZsnNMZHoUbtbzkd5j2NZBTpNkeAxSpjh5yh861qDI7g3ao1xYO9YKlX%2BUo1GwVG7OSKV7g2lHPgChjYnTkZvIGoqRGsjUW3EQDDX9vR38KdhZhACSb%2FDZDYBUwLM9amYfIcsKkTLGApdXCrswo5nD0gY6mAGv%2B8BChOaIXnFnZYzdhDW%2BXoJS09Jz8lSlWBSVTzFPcx8KK3toK9nanPzialIzCIdza4bWaspIo%2F1UIr%2FVv%2Bw%2F%2Fzw6XyAymhqQT880n1Bm0lZ6vHAhAFM9l9AaRjNS7mlhQSdkoqSBNFl5A50JUvdm%2F%2FF%2B7NbqTSk5CfV%2BfUvbKWpQaxXpA20gPkRvfeE%2Bkcc9Zl2U3DZaHQ%3D%3D&Expires=1783683702",
    width=230
)

st.markdown('<div class="main-title">은방울꽃 관수 실험 체험</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">관수 주기와 관수 방식을 선택하고, 잎 색 변화 중심의 결과를 비교해 보세요.</div>',
    unsafe_allow_html=True
)

st.image(
    "https://user-gen-media-assets.s3.amazonaws.com/gpt4o_images/bae350bd-4253-47a4-9c49-11c343c192ff.png?AWSAccessKeyId=ASIA2F3EMEYE26FQZWBJ&Signature=0BS2sXedg4MBLoGVDOAP5ydDbHM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDnLvChg%2ByWogAOTjVXkwvJMqEXoZBJIjtSgGiDIFgTYQIgb1F57fFmoy5A%2BG0YFwKCXDywpWJjyz%2BqTmFNuJ3PDnUq%2FAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDLv5QzLSHpEnGuHh3yrQBJCCCN3XDpb4DRKZahFgQN3RDon0ICwOpeyDE%2FmBZ%2BP9cK9BIGjs2nQ88tEjtgCXs4zTxAKN%2FDVlH0RYaX%2BjyoWZdRpBIf7%2Ba5D%2BASShirB3D21VBFOyrnrLfWYfxWO0PWOuj3bMYo8C%2FtZMg57wSa2ks%2BkcvNgUwOp7OgwAgvkO4TbwDgBPoGuILZHTxC52eSdDFOxNyFZ6gQIy%2BLnIZn4iz1Cx967bJoTp32FCe94fAGyhcA73KZZEBmxX2Oc%2F7eHiJC%2FtnBV8s7drejGRAYp6J2gIy9AH8OWy6T0TmG8eAtHFe9I48Dhikuo3THM%2Fn06Gb9XBHJqVd5Juw%2Fggin6TbdfmLxToLBN7jSInwmtur6DKQuWl4W%2Bzvhbs5imBSwoBBsY8%2FAVVsyJgno5BgkW0xjGKu8TxuCf0MivYy07uOOfsQf9DGETUyvYdlcj7Z9e9tXhK33sVz8%2FyLfZ5VmD%2F%2Bfm%2FGRyZFRrDXVnDj%2F8I7MvypbLS6gVnnVA7pIcEOpuWLL0WAwMMYma76MKTNLW3dJIjVogTXT2bHfkbNMJUR3xKdxYAJo3TqGNrqxlouPvqkOGMn5EYR98E8qzybH2VvEmbpKiVypPuB%2BG2g7rz3rpjn4DT%2BHAI6K4i82YVcmSxU32V7gvTl3PttvUnmYYJUdAyuCqYOvbhysJzEfnRHJSWjBOnwgCSojxFI9ZveGz9ewaZJ7a5iu73sBgWXG9ihK2XagWZYR%2F2XODJSbzaOLt6Pzfb8Xpj%2B7A3APd%2Bj3Pkqk%2B%2FYm9h9cxVtRapDq0wqqDD0gY6mAH%2FQpz5sculWPKk3PosLwYAx%2FSdZu1ZV%2FlFty5VipBE%2F4Zp1I%2BZQGaO%2BJFEx6fUVoaIi5Wgtqr%2BQX9tbS9O1Nyx17j2l64E0yPWL8QqvR1Rf6ozQ87q38oS90fdIbSw0BGRlJ3Nuo%2BZtzEDakONOJ0PdU3FJ4Z0aNr6S9I4DF5kFYDscewL%2FHPKhnDrfl487L4mdhJKUQ%3D%3D&Expires=1783684605",
    use_container_width=True
)

left, right = st.columns([1, 1.2])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 실험 조건 선택")

    cycle = st.radio(
        "관수 주기를 고르세요",
        ["매일 물 주기", "주 2회 물 주기", "물을 주지 않음"]
    )

    if cycle == "주 2회 물 주기":
        method = "저면관수"
        st.radio(
            "물 주는 방식을 고르세요",
            ["저면관수", "관수 X"],
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
            ["두상관수", "저면관수", "관수 X"],
            index=0
        )
        if method == "관수 X":
            st.markdown(
                '<div class="rule-box">매일 물 주기와 관수 X는 서로 맞지 않는 선택이므로, 결과 해석 시 참고가 필요합니다.</div>',
                unsafe_allow_html=True
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

    elif cycle == "물을 주지 않음" or method == "관수 X":
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

st.info("이 웹앱은 실제 실험에서 관찰한 잎 색 변화를 바탕으로 만든 발표용 체험 페이지입니다.")
