import pandas as pd
import streamlit as st

d_data = pd.read_excel("data/World_Bank_CO2.xlsx", sheet_name=3)

st.title("World Bank CO2")
st.write(d_data)

country = st.selectbox(
    'Select Country', d_data['Country Name'].unique(), index=1)
st.line_chart(data=d_data[d_data['Country Name'] == country][[
              "Year", "CO2 (kt)"]].set_index("Year"))
