import streamlit as st
import pandas as pd
import plotly.express as px


# Import data
df = pd.read_csv('day.csv')

# Data Wrangling
df = df.drop(['dteday', 'instant', 'casual'], axis=1)

# Define season labels
season_labels = ['springer', 'summer', 'fall', 'winter']

# Set the title and description of your app
st.title('Bicycle Rental Analysis')
st.write('This app explores bicycle rental data.')

# Visualizations
st.header('Visualization & Explanatory Analysis')

st.write('Grafik ini menunjukkan jumlah peminjaman sepeda berdasarkan musim.')
season_sum = df.groupby('season')['cnt'].sum()
season_sum.index = season_labels

# Create an interactive bar chart with different colors
fig = px.bar(x=season_labels, y=season_sum, color=season_labels)
st.plotly_chart(fig)

st.write('Grafik ini membandingkan jumlah peminjaman sepeda pada hari libur dan hari kerja.')

holiday_labels = ['Weekday', 'Holiday']
holiday_sum = df.groupby('holiday')['cnt'].sum()
holiday_sum.index = holiday_labels

# Create an interactive bar chart with different colors
fig = px.bar(x=holiday_labels, y=holiday_sum, color=holiday_labels)
st.plotly_chart(fig)

st.write('Grafik ini menunjukkan pengaruh cuaca terhadap jumlah peminjaman sepeda.')

weather_labels = ['Clear', 'Mist', 'Light Snow']
weather_sum = df.groupby('weathersit')['cnt'].sum()
weather_sum.index = weather_labels

# Create an interactive bar chart with different colors
fig = px.bar(x=weather_labels, y=weather_sum, color=weather_labels)
st.plotly_chart(fig)
