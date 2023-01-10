import streamlit
streamlit.title('Welcome to Factspan Inc.')
streamlit.header('Services provided by us:')
streamlit.text('AI & ML')
streamlit.text('Cloud Data Build')
streamlit.text('Data Engineering')
streamlit.text('Bussiness Analytics')
streamlit.text('Others')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
