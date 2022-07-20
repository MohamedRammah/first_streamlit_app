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


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)



# Display the table on the page.
streamlit.dataframe(my_fruit_list)




streamlit.data.frame(fruits_to_show)







# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

uit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
