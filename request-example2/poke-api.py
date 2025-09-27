import requests  # HTTP istekleri yapmak için kullanılır

pokemon_name = input("Bir Pokemon adı girin: ")  # Kullanıcıdan Pokemon adını al
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"  # API adresini oluştur

response = requests.get(url)  # API'ye istek gönder
if response.status_code == 200:  # Eğer istek başarılıysa
    data = response.json()  # Yanıtı JSON olarak al
    print(f"Adı: {data['name'].title()}")  # Pokemon'un adını yazdır
    print(f"Boyu: {data['height']}")  # Pokemon'un boyunu yazdır
    print(f"Kilosu: {data['weight']}")  # Pokemon'un kilosunu yazdır
    print("Tipleri:")  # Pokemon'un tiplerini yazdır
    for t in data['types']:
        print("-", t['type']['name']) #Pokemon’un tipi (örneğin: elektrik, ateş, su)
else:
    print("Pokemon bulunamadı!")  # Hatalı isim girilirse uyarı ver