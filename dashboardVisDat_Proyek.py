import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset langsung dari sumber
@st.cache_data
def load_data():
    day_df = pd.read_csv("https://raw.githubusercontent.com/farisrizqi/Proyek-Visualisasi-Data/refs/heads/main/day.csv")
    hour_df = pd.read_csv("https://raw.githubusercontent.com/farisrizqi/Proyek-Visualisasi-Data/refs/heads/main/hour.csv")
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar dengan informasi proyek
st.sidebar.header("Informasi Proyek")
st.sidebar.write("**Nama:** Faris Nur Rizqiawan")
st.sidebar.write("**Email:** farisnur07@gmail.com")
st.sidebar.write("**ID Dicoding:** farisrizqiawan")
option = st.sidebar.selectbox("Pilih Data Visualisasi", ["Data Harian", "Data Per Jam"])

# Judul Dashboard
st.title("Bike Rental Analysis And Visualization")

# Menampilkan dataset
st.write("### Preview Dataset")
if option == "Data Harian":
    st.dataframe(day_df.head())
else:
    st.dataframe(hour_df.head())

# Visualisasi Data (update berdasarkan pilihan)
if option == "Data Harian":
    st.write("### Banyak pesepeda casual dan register (perhari)")
    fig, ax = plt.subplots()
    sns.barplot(x=["casual", "registered"], y=[day_df["casual"].sum(), day_df["registered"].sum()], ax=ax)
    ax.set_xlabel("Tipe Pengguna")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    st.pyplot(fig)
else:
    st.write("### Banyak pesepeda casual dan register (perjam)")
    fig, ax = plt.subplots()
    sns.barplot(x=["casual", "registered"], y=[hour_df["casual"].sum(), hour_df["registered"].sum()], ax=ax)
    ax.set_xlabel("Tipe Pengguna")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    st.pyplot(fig)

# Visualisasi Total Pengguna Berdasarkan Day & Hour
st.write("### Total Pengguna Berdasarkan Day & Hour")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Total Pengguna Berdasarkan Day
sns.barplot(ax=axes[0], x="season", y="cnt", data=day_df, palette="coolwarm", ci=None)
axes[0].set_xlabel("Season")
axes[0].set_ylabel("Total Pengguna")
axes[0].set_title("Total Pengguna Berdasarkan Day")
axes[0].set_xticks([0, 1, 2, 3])
axes[0].set_xticklabels(["Spring", "Summer", "Fall", "Winter"])

# Total Pengguna Berdasarkan Hour
sns.barplot(ax=axes[1], x="season", y="cnt", data=hour_df, palette="viridis", ci=None)
axes[1].set_xlabel("Season")
axes[1].set_ylabel("Total Pengguna")
axes[1].set_title("Total Pengguna Berdasarkan Hour")
axes[1].set_xticks([0, 1, 2, 3])
axes[1].set_xticklabels(["Spring", "Summer", "Fall", "Winter"])

plt.tight_layout()
st.pyplot(fig)

# Visualisasi Total Peminjaman Berdasarkan Registered (Day & Hour)
st.write("### Total Peminjaman Berdasarkan Registered (Day & Hour)")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Group data by 'registered' for Day
day_grouped = day_df.groupby("registered")["cnt"].sum().reset_index()
sns.barplot(ax=axes[0], x=day_grouped["registered"], y=day_grouped["cnt"], color="blue")
axes[0].set_xlabel("Jumlah Pengguna Terdaftar")
axes[0].set_ylabel("Total Peminjaman")
axes[0].set_title("Total Peminjaman berdasarkan Registered (Day)")

# Group data by 'registered' for Hour
hour_grouped = hour_df.groupby("registered")["cnt"].sum().reset_index()
sns.barplot(ax=axes[1], x=hour_grouped["registered"], y=hour_grouped["cnt"], color="red")
axes[1].set_xlabel("Jumlah Pengguna Terdaftar")
axes[1].set_ylabel("Total Peminjaman")
axes[1].set_title("Total Peminjaman berdasarkan Registered (Hour)")

plt.tight_layout()
st.pyplot(fig)

# Conclusion section
st.write("### Conclusion")

# Conclusion for question 1
st.write("#### Conclution Pertanyaan 1")
st.write("##### Bagaimana pola penggunaan sepeda di setiap musim?")
st.write("Pola Musim menunjukkan pengaruh besar terhadap penggunaan sepeda, dengan musim semi dan panas memiliki lebih banyak peminjaman daripada musim gugur dan dingin.")

# Conclusion for question 2
st.write("#### Conclution Pertanyaan 2")
st.write("##### Bagaimana pola jumlah total peminjaman berdasarkan jumlah pengguna terdaftar?")
st.write("Pola Pengguna Terdaftar vs Pemijaman menunjukkan korelasi positif antara jumlah pengguna terdaftar dengan total peminjaman, meskipun distribusinya bisa bervariasi tergantung pada faktor waktu dan kondisi lainnya.")
