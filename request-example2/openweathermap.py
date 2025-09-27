import requests  # İnternetten veri çekmek için kullanılan popüler Python kütüphanesi
import tkinter   # Grafik arayüz (pencere) oluşturmak için kullanılan Python kütüphanesi

API_KEY = "76be3b1b00ce0012a7124bfb9fb0e750"  # OpenWeatherMap API anahtarın
city = input("Şehir adı girin: ")              # Kullanıcıdan şehir adını alır
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"  # API adresini oluşturur

response = requests.get(url)  # API'ye istek gönderir ve yanıtı alır

# Bilgileri veya hata mesajını gösterecek özel pencere fonksiyonu
def show_custom_info(title, message):
    win = tkinter.Tk()  # Yeni bir pencere oluşturur
    win.title(title)    # Pencerenin başlığını ayarlar
    win.geometry("500x300")  # Pencere boyutunu ayarlar
    win.configure(bg="#e0f7fa")  # Arka plan rengini ayarlar
    win.attributes('-topmost', True)  # Pencereyi en üstte tutar
    label = tkinter.Label(win, text=message, bg="#ffffff", font=("Arial", 12), justify="left")  # Bilgi veya hata mesajı için etiket
    label.pack(padx=50, pady=50)  # Etiketi pencereye yerleştirir
    btn = tkinter.Button(win, text="Tamam", command=win.destroy, bg="#522e8a", fg="white", font=("Arial", 11, "bold"))  # Tamam butonu
    btn.pack(pady=10)  # Butonu pencereye yerleştirir
    win.mainloop()  # Pencereyi çalıştırır (kapatılana kadar bekler)

# API isteği başarılıysa (şehir bulunduysa)
if response.status_code == 200:
    data = response.json()  # Yanıtı JSON formatında alır
    info = (
        f"{city.title()} için hava durumu:\n"  # Şehir adını başlık olarak ekler
        f"Açıklama: {data['weather'][0]['description']}\n"  # Hava durumu açıklaması
        f"Sıcaklık: {data['main']['temp']} °C\n"            # Sıcaklık bilgisi
        f"Nem: {data['main']['humidity']} %\n"              # Nem oranı
        f"Rüzgar hızı: {data['wind']['speed']} m/s"         # Rüzgar hızı
    )
    show_custom_info("Hava Durumu", info)  # Bilgileri pencere ile gösterir
else:
    error_msg = f"'{city}' adlı şehir bulunamadı veya API anahtarı hatalı!\n(Kod: {response.status_code})"  # Hata mesajı oluşturur
    show_custom_info("Hata", error_msg)  # Hata mesajını pencere ile gösterir