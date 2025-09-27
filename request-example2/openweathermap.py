import requests  # HTTP istekleri yapmak için kullanılır

API_KEY = "76be3b1b00ce0012a7124bfb9fb0e750"  # OpenWeatherMap API anahtarınızı buraya yazın
city = input("Şehir adı girin: ")  # Kullanıcıdan şehir adını al
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"  # API adresini oluştur

response = requests.get(url)  # API'ye istek gönder
if response.status_code == 200:  # Eğer istek başarılıysa
    data = response.json()  # Yanıtı JSON olarak al
    print(f"{city.title()} için hava durumu:")
    print("Açıklama:", data["weather"][0]["description"])
    print("Sıcaklık:", data["main"]["temp"], "°C")
    print("Nem:", data["main"]["humidity"], "%")
    print("Rüzgar hızı:", data["wind"]["speed"], "m/s")
else:
    print("Şehir bulunamadı veya API anahtarı hatalı!")