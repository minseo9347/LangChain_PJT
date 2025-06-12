import streamlit as st
from report_service import investment_report
from stock_info import Stock
from search_index import search_company, SearchhResult
st.title("AI 투자 보고서 생성 서비스")
search_symbol = st.text_input("회사명", "AAPL")
# company_list = ["AAPL: Apple Inc",
#                "APLE: Apple Hospitality REIT Inc"]
hits = search_company(search_symbol)['hits']
result = [SearchhResult(hit) for hit in hits]

company_selected = st.selectbox("회사 선택", result, index=0)

# search_symbol = "PLTR"  # Palantir Technologies Inc
# company_selected = "Palantir Technologies Inc"

tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 차트로 시각화
with tab1:  
    st.header(f"{company_selected}의 6개월 주식 거래량")
    stock = Stock(search_symbol)
    volume = stock.get_stock_volume()
    st.line_chart(volume, use_container_width=True)


# LLM이 만든 투자 보고서 출력
with tab2:
    st.header(f"{search_symbol} 투자보고서 생성")


    if st.button("투자 보고서 생성"):
        with st.spinner(text="투자 보고서 생성 중..."):
            report = investment_report(company_selected, search_symbol)
            st.success("투자 보고서 생성 완료!")            
        st.write(report)