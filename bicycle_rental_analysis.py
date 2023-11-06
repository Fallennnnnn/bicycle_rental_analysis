import streamlit as st
import pandas as pd

# Import data
df = pd.read_csv('day.csv')

# Data Wrangling
df = df.drop(['dteday', 'instant', 'casual'], axis=1)

# Define season labels
season_labels = ['springer', 'summer', 'fall', 'winter']

# Set the title and description of your app
st.title('Bicycle Rental Analysis')
st.write('This app explores bicycle rental data.')

# Add sections with descriptions
st.header('Data Description')
st.dataframe(df.head())

st.header('Data Summary')
st.dataframe(df.describe())

st.header('Correlation Matrix')
st.dataframe(df.corr())

# Visualizations
st.header('Visualization & Explanatory Analysis')

# Question 1: Jumlah Peminjaman Sepeda Berdasarkan Musim
st.subheader('Pertanyaan 1: Jumlah Peminjaman Sepeda Berdasarkan Musim')
st.write('Grafik ini menunjukkan jumlah peminjaman sepeda berdasarkan musim.')

season_sum = df.groupby('season')['cnt'].sum()
season_sum.index = season_labels
st.bar_chart(season_sum)
st.pyplot()

# Question 2: Perbandingan Peminjaman Sepeda pada Hari Libur dan Hari Kerja
st.subheader('Pertanyaan 2: Perbandingan Peminjaman Sepeda pada Hari Libur dan Hari Kerja')
st.write('Grafik ini membandingkan jumlah peminjaman sepeda pada hari libur dan hari kerja.')

holiday_labels = ['Weekday', 'Holiday']
holiday_sum = df.groupby('holiday')['cnt'].sum()
holiday_sum.index = holiday_labels
st.bar_chart(holiday_sum)
st.pyplot()

# Question 3: Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda
st.subheader('Pertanyaan 3: Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
st.write('Grafik ini menunjukkan pengaruh cuaca terhadap jumlah peminjaman sepeda.')

weather_labels = ['Clear', 'Mist', 'Light Snow']
weather_sum = df.groupby('weathersit')['cnt'].sum()
weather_sum.index = weather_labels
st.bar_chart(weather_sum)
st.pyplot()

# Conclusion
st.header('Conclusion')
st.write('- Pada pertanyaan 1 Berdasarkan visualisasi di atas, dapat dilihat bahwa jumlah peminjam sepeda berdasarkan musim sangat beragam. Pada musim 1 yang ditandai dengan "Springer" terdapat jumlah peminjam paling sedikit. Sebaliknya, pada musim 3 yang ditandai dengan "Fall" terdapat jumlah peminjam terbanyak. Hal ini menunjukkan bahwa musim memiliki pengaruh signifikan pada jumlah peminjaman sepeda.')

st.write('- Pada pertanyaan 2 Berdasarkan visualisasi di atas, dapat disimpulkan bahwa perbandingan jumlah peminjam pada saat hari libur (holiday) dan hari kerja (workingday) sangat signifikan. Hasil menunjukkan bahwa pada hari kerja (workingday) jumlah peminjam sepeda lebih besar dibandingkan dengan hari libur (holiday). Hal ini mengindikasikan bahwa faktor hari dalam seminggu (weekday) berpengaruh signifikan terhadap jumlah peminjaman sepeda, dengan hari kerja cenderung memiliki tingkat peminjaman yang lebih tinggi.')

st.write('- Pada pertanyaan 3 Berdasarkan visualisasi di atas, dapat disimpulkan bahwa perbandingan jumlah peminjam pada saat cuaca cerah "(1: Clear, Few clouds, Partly cloudy, Partly cloudy)" menduduki peringkat pertama dibandingkan dengan saat cuaca berkabut "(2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist)" dan saat ada sedikit salju "(3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds)". Hal ini menunjukkan bahwa cuaca cerah memiliki dampak positif terhadap jumlah peminjaman sepeda, sementara cuaca berkabut dan cuaca dengan sedikit salju cenderung memiliki tingkat peminjaman yang lebih rendah.')

# Run the app with streamlit
if __name__ == '__main__':
    st.set_page_config(page_title='Bicycle Rental Analysis', page_icon='🚲')
    st.run()