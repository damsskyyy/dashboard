import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

st.title('Proyek Analisis Data: Bike-Sharing-dataset')
st.markdown('- Nama: Damar Bayu Krisna')
st.markdown('- Email: damarbkrisna@gmail.com')
st.markdown('- Id Dicoding: 1RXY09961ZVM')

# Mulai menyiapkan data
day_df = pd.read_csv("https://raw.githubusercontent.com/damsskyyy/analisis-data-python/main/Bike-sharing-dataset/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/damsskyyy/analisis-data-python/main/Bike-sharing-dataset/hour.csv")

# Cleaning Data
datetime_columns = ["dteday"]
for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])

# Eksplorasi Data
day_cnt = day_df.groupby('weekday')['cnt'].mean().reset_index()
hour_cnt = hour_df.groupby(['weekday', 'hr'])['cnt'].mean().reset_index()
hour_table = hour_cnt.pivot_table(values='cnt', index='weekday', columns='hr')
weather = ['temp', 'hum', 'windspeed', 'cnt']
weather_corr = hour_df[weather].corr()

# Visualisasi Pertanyaan 1
st.header('Pertanyaan 1: Pola Penggunaan Sepeda Berdasarkan Jam/Hari dalam Seminggu')
# Visualisasi Grafik 1 
st.subheader('Grafik Rata-rata Peminjaman Sepeda per Hari dalam Seminggu')
st.bar_chart(day_cnt.set_index('weekday'))

# Visualisasi Grafik 2
st.subheader('Grafik Rata-rata Peminjaman Sepeda per Jam dalam Seminggu')
plt.figure(figsize=(12, 8))
sns.barplot(x=hour_table.columns, y=hour_table.mean(axis=0), palette='viridis')
plt.xlabel('Jam (hr)')
plt.ylabel('Rata-rata total sewa sepeda')
plt.title('Rata-rata total sewa sepeda per Jam dalam Seminggu')
plt.xticks(rotation=45)
# Menyimpan plot ke dalam BytesIO
buffer_bar = BytesIO()
plt.savefig(buffer_bar, format='png')
buffer_bar.seek(0)
# Menampilkan plot dengan st.image()
st.image(buffer_bar)

# Visualisasi Pertanyaan 2
st.header('Pertanyaan 2: Korelasi Cuaca dengan Jumlah Pengguna Sepeda')
st.subheader('Tabel Korelasi Cuaca dengan Jumlah Pengguna Sepeda')
st.write(weather_corr)

# Menggunakan Matplotlib untuk scatter plot
fig, ax = plt.subplots()
ax.scatter(hour_df['temp'], hour_df['cnt'], alpha=0.5)
ax.set_xlabel('Suhu (Temperature)')
ax.set_ylabel('Total Sewa Sepeda')
ax.set_title('Scatter Plot: Hubungan antara Suhu dan Total Sewa Sepeda')
# Menyimpan plot ke dalam BytesIO
buffer = BytesIO()
fig.savefig(buffer, format='png')
buffer.seek(0)
# Menampilkan plot dengan st.image()
st.image(buffer)
