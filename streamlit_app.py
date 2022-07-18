import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text ('🥣 Omega 3 & Blueberry oat meal')
streamlit.text ('🍚Kale, Spinach & Rocket smoothie')
streamlit.text ('☘️Hard-boiled Free-Range Egg')

streamlit.header ('🥝 🍓  Create Your Own Milkshake 🍒 🥥')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# Let us put a list here so that users can add the fruits they want 
fruits_to_show = my_fruits_list.loc[fruits_selected]
Streamlit.dataframe(fruits_to_show)







