import requests              # İnternetten veri çekmek için kullanılır (API'den veri almak için)
import tkinter               # Grafik arayüz (pencere) oluşturmak için kullanılır
from PIL import Image, ImageTk  # Görsel işlemek ve tkinter'da göstermek için kullanılır
import io                    # İnternetten gelen görseli bellekte açmak için kullanılır

pokemon_name = input("Bir Pokemon adı girin: ")  # Kullanıcıdan bir Pokemon adı alır
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"  # API adresini oluşturur (küçük harfe çevirir)

response = requests.get(url)  # API'ye istek gönderir ve yanıtı alır
if response.status_code == 200:  # Eğer istek başarılıysa (Pokemon bulunduysa)
    data = response.json()       # API'den gelen yanıtı JSON formatında alır (Python sözlüğüne çevirir)
    img_url = data['sprites']['front_default']  # Pokemon'un görselinin URL'sini alır
    info = (                                    # Bilgileri bir string olarak hazırlar
        f"Adı: {data['name'].title()}\n"        # Pokemon'un adını ekler (ilk harfi büyük)
        f"Boyu: {data['height']}\n"             # Pokemon'un boyunu ekler
        f"Kilosu: {data['weight']}\n"           # Pokemon'un kilosunu ekler
        f"Tipleri: " + ", ".join([t['type']['name'] for t in data['types']])  # Tüm tiplerini ekler (ör: elektrik, su)
    )
    img_response = requests.get(img_url)         # Görselin URL'sine istek gönderir
    img_data = img_response.content              # Görselin ham verisini alır
    img = Image.open(io.BytesIO(img_data))       # Görseli bellekte açar (PIL ile)
    win = tkinter.Tk()                           # Yeni bir pencere oluşturur
    win.title(data['name'].title())              # Pencerenin başlığını Pokemon adı yapar
    win.geometry("350x400")                      # Pencere boyutunu ayarlar
    win.configure(bg="#e0f7fa")                  # Arka plan rengini ayarlar
    win.attributes('-topmost', True)             # Pencereyi en üstte tutar
    tk_img = ImageTk.PhotoImage(img)             # PIL görselini tkinter için uygun hale getirir
    img_label = tkinter.Label(win, image=tk_img, bg="#e0f7fa")  # Görseli pencereye ekler
    img_label.pack(pady=10)                      # Görseli yerleştirir
    info_label = tkinter.Label(win, text=info, bg="#e0f7fa", font=("Arial", 12), justify="left")  # Bilgileri ekler
    info_label.pack(pady=10)                     # Bilgileri yerleştirir
    btn = tkinter.Button(win, text="Tamam", command=win.destroy, bg="#522e8a", fg="white", font=("Arial", 11, "bold"))  # Tamam butonu
    btn.pack(pady=10)                            # Butonu yerleştirir
    win.mainloop()                               # Pencereyi çalıştırır (kapatılana kadar bekler)
else:                                            # Eğer Pokemon bulunamazsa (hatalı isim girilirse)
    win = tkinter.Tk()                           # Yeni bir hata penceresi oluşturur
    win.title("Hata")                            # Pencerenin başlığını "Hata" yapar
    win.geometry("350x150")                      # Pencere boyutunu ayarlar
    win.configure(bg="#ffe0e0")                  # Arka plan rengini ayarlar (kırmızımsı)
    win.attributes('-topmost', True)             # Pencereyi en üstte tutar
    label = tkinter.Label(win, text="Pokemon bulunamadı!", bg="#ffe0e0", font=("Arial", 12))  # Hata mesajı ekler
    label.pack(pady=30)                          # Mesajı yerleştirir
    btn = tkinter.Button(win, text="Tamam", command=win.destroy, bg="#c62828", fg="white", font=("Arial", 11, "bold"))  # Tamam butonu
    btn.pack(pady=10)                            # Butonu yerleştirir
    win.mainloop()                               # Pencereyi çalıştırır (kapatılana kadar bekler)