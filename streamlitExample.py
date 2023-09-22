import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Ülkelere Göre Mutluluk Skorları")

st.sidebar.title("Grafik Ayarları")

grafik_genislik = st.sidebar.slider("Grafik Genişlik",min_value=6,max_value=12,value=8)
grafik_yuksekli = st.sidebar.slider("Grafik Yükseklikm",min_value=3,max_value=8, value= 4)



df = pd.read_csv("/Users/kadirdundar/Desktop/kaggleDeneme/WHR_2023.csv")

filtered_df = df[df['happiness_score'] < 5]

x = filtered_df["country"]
y = filtered_df["happiness_score"]

st.header("Mutluluk Skorlarının Dağılımı", divider='rainbow')
# İlk grafik
fig2, ax2 = plt.subplots(figsize=(grafik_genislik, grafik_yuksekli))
sns.histplot(data=df, x='happiness_score', bins=20, kde=True, ax=ax2)
plt.title('Distribution of happiness score')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')

st.pyplot(fig2)

years = range(2015,2023)
ort_mutluluk_butun_ulkeler = []

for i in range(15,23):
      path_name= "/Users/kadirdundar/Desktop/kaggleDeneme/WHR_20"+ str(i) +".csv"
      series_df = pd.read_csv(path_name)
      a = series_df["happiness_score"].mean()
      ort_mutluluk_butun_ulkeler.append(a)

neww_df = []
for i in range(15,23):
        path_name= "/Users/kadirdundar/Desktop/kaggleDeneme/WHR_20"+ str(i) +".csv"
        series_df = pd.read_csv(path_name)
        turkey_df = series_df[series_df["country"]== "Turkey"]
        happines_score = turkey_df["happiness_score"].values
        neww_df.append(happines_score)

# İkinci grafik
def enDusukUlkeler():

    
    st.header("Düşük Skorlu Ülkeler")
    plt.style.use('_mpl-gallery')
    fig1, ax1 = plt.subplots()
    ax1.stem(x, y)
    fig1.set_size_inches(12, 6)
    plt.xticks(rotation=90)
    st.pyplot(fig1)

##üçüncü grafik
def turkeyScore():
    st.header("Türkiye'nin Mutluluk Skoru")


    fig2, ax2 = plt.subplots()
    ax2.plot(years,neww_df)
    ax2.set(xlabel ="Yıllar",ylabel = "Mutluluk Skoru",title = "Türkiye Mutluluk Skoru ")
    fig2.set_size_inches(12, 6)

    st.pyplot(fig2)

##dördüncü grafik
def ortalamaScore():    
    st.header("Dünya Ülkelerinin Ortalama Skorları")


    fig3, ax3 = plt.subplots()

    ax3.plot(years,ort_mutluluk_butun_ulkeler)
    ax3.set(xlabel ="Yıllar",ylabel = "Mutluluk Skoru",title = "Tüm Ülkeler Ortalama Mutluluk Skoru ")
    fig3.set_size_inches(12, 6)

    st.pyplot(fig3)

## grafik 5 
def doviz():    
    st.header("Türkiye MutluluK Döviz İlişkisi")

    döviz_kuru = [2.7191,3.0181,3.6445,4.8301,5.6712,7.0034,8.8557,16.5512]
    developed_countries = ['Finland', 'Denmark', 'Iceland', 'Israel', 'Netherlands', 'Sweden', 'Norway', 'Switzerland', 'Luxembourg', 'New Zealand', 'Austria', 'Australia', 'Canada', 'Ireland', 'United States', 'Germany', 'Belgium', 'Czechia', 'United Kingdom', 'Lithuania', 'France', 'Slovenia', 'Singapore']
    mean_of_developed_countries_happnies = []
    for i in range(15,23):
       path_name= "/Users/kadirdundar/Desktop/kaggleDeneme/WHR_20"+ str(i) +".csv"
       series_df = pd.read_csv(path_name)
       developed_countries_data = series_df[series_df["country"].isin(developed_countries)]
       a = developed_countries_data["happiness_score"].values[0]
       mean_of_developed_countries_happnies.append(a)


    fig4, ax4 = plt.subplots(figsize=(10, 6))

    color = 'tab:grey'
    ax4.set_xlabel('Yıl')
    ax4.set_ylabel('Mutluluk Skoru', color=color)
    ax4.plot(years, mean_of_developed_countries_happnies, 'o--', color="blue", label="Gelişmiş Ülkeler")
    ax4.plot(years, ort_mutluluk_butun_ulkeler, 'o--', color="grey", label="Bütün Ülkelerin Ortalaması")
    ax4.plot(years, neww_df, 'o--', color="red", label="Türkiye")
    ax4.tick_params(axis='y', labelcolor=color)
    plt.legend()
    ax5 = ax4.twinx()  # İkinci y eksenini oluştur
    color = 'tab:green'
    ax5.set_ylabel('Döviz Kuru', color=color)
    ax5.plot(years, döviz_kuru, '--', color=color, label="Döviz Kuru")
    ax5.tick_params(axis='y', labelcolor=color)
    plt.legend()
    fig4.tight_layout()
    plt.title('Gelişmiş Ülkeler Mutluluk Skoru ve Döviz Kuru (2015-2022)')
    st.pyplot(fig4)


options = st.sidebar.multiselect(
    'Hangi Grafikleri Görmek İstersiniz?',
    ['Türkiye', 'Genel Dağılım', 'Dünya Ortalaması', 'Türkiye-Döviz İlişkisi'],
    [])


for option in options:
    if option == 'Türkiye':
        # Türkiye grafiklerini çizmek için ilgili fonksiyonu çağırın
        turkeyScore()
    elif option == 'Genel Dağılım':
        # Genel dağılım grafiklerini çizmek için ilgili fonksiyonu çağırın
        ortalamaScore()
    elif option == 'Dünya Ortalaması':
        # Dünya ortalaması grafiklerini çizmek için ilgili fonksiyonu çağırın
        enDusukUlkeler()
    elif option == 'Türkiye-Döviz İlişkisi':
        # Türkiye-döviz ilişkisi grafiklerini çizmek için ilgili fonksiyonu çağırın
        doviz()
