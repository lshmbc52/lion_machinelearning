import streamlit as st
from pages import page2

# def page2():
#     st.title("Second page")

pg = st.navigation([
    st.Page(page2,title="Stock 데이터분석"),
    st.Page("page1.py",title="캘리포니아 집값 예측"),
    

])

pg.run()