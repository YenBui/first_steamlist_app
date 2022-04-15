
import streamlit
import pandas


stramlit.dataframe(my_fruit_list)

streamlit.title('My Mom\'s New Healthy Diner')
                
streamlit.header('Breakfast Favorites')
streamlit.text('🫐 3 & Blueberry Oatmeal')
streamlit.text('🥬 Spinach & Rocket Smoothie')
streamlit.text('🥚 Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
