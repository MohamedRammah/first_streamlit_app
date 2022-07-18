import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text ('🥣 Omega 3 & Blueberry oat meal')
streamlit.text ('🍚Kale, Spinach & Rocket smoothie')
streamlit.text ('☘️Hard-boiled Free-Range Egg')

streamlit.header ('🥝 🍓  Create Your Own Milkshake 🍒 🥥')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

