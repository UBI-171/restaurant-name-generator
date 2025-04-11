import streamlit as st

from langchain_helper import generate_restaurant_name_and_menu

st.title("Restaurant Name & Menu Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Mughlai","Awadhi","Arabic","Italian","Mexican","American"))

if cuisine:
    response = generate_restaurant_name_and_menu(cuisine)
    restaurant_name = response["restaurant_name"]
    st.header(restaurant_name.strip())
    menu_items = response["menu_items"]
    st.write(menu_items)