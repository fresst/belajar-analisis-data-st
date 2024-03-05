import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_day = pd.read_csv('./Bike-sharing-dataset/day.csv')

df_day['dteday'] = pd.to_datetime(df_day['dteday'])

st.title('Total Bike Sharing Tahun 2011-2012 terhadap Musim')

fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='dteday', y='cnt', data=df_day, hue='season')

ax.set_xlabel('Date')
ax.set_ylabel('Count')
ax.legend()

st.pyplot(fig)

st.write(
        """Dari plot di atas, bisa dilihat bahwa tren bike sharing meningkat 
        mulai season 1, yaitu spring, dan menurun di season 4, yaitu winter.
        Musim-musim lain, yaitu 2 (summer) dan 3 (fall) memiliki jumlah bike sharing
        lebih banyak dibanding dua musim sebelumnya. Hal ini bisa dikaitkan dengan temperatur 
        musim tersebut. Selengkapnya bisa dilihat pada figure di bawah ini
        """
    )

st.subheader('Bike Sharing dengan Keterangan Temperatur')
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='dteday', y='cnt', data=df_day, hue='temp', palette='coolwarm')
ax.set_xlabel('Date')
ax.set_ylabel('Count')
ax.legend()

st.pyplot(fig)

with st.expander('Rasio Penggunaan Bike Sharing'):
    st.write(
        """Seperti yang sudah dijelaskan sebelumnya, pengguna bike sharing lebih
        banyak pada musim dengan temperatur yang hangat. Berikut keterangan jumlah
        pengguna di tiap musim
        """
    )
    
    sns.barplot(
        x='season',
        y='cnt',
        data=df_day,
    )
    ax.get_legend().remove()
    st.pyplot(fig)