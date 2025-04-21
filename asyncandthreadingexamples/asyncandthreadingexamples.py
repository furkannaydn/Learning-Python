import threading  # Çoklu iş parçacığı (thread) işlemleri için
import requests  # HTTP istekleri yapmak için
import time  # Zaman ölçümleri yapmak için
import asyncio  # Asenkron işlemleri yönetmek için
import aiohttp  # Asenkron HTTP istekleri yapmak için


def get_data_sync(urls):
    # Verilen URL'lere senkron olarak istek gönderir ve yanıtları toplar
    st = time.time()  # İşlem başlangıç zamanını kaydet
    json_array = []  # Yanıtları saklamak için bir liste
    for url in urls:
        json_array.append(requests.get(url).json())  # Her URL'ye istek gönder ve yanıtı listeye ekle
    et = time.time()  # İşlem bitiş zamanını kaydet
    elapsed_time = et - st  # Geçen süreyi hesapla
    print(f"Elapsed time for synchronous requests: {elapsed_time} seconds")  # Geçen süreyi yazdır
    return json_array  # Yanıtları döndür


class ThreadingDownloader(threading.Thread):
    # Bir URL'ye istek göndermek için bir iş parçacığı sınıfı
    jhson_array = []  # Yanıtları saklamak için bir sınıf seviyesi liste (hatalı kullanım, düzeltilmeli)

    def __init__(self, url):
        super().__init__()  # Üst sınıfın (Thread) __init__ metodunu çağır
        self.url = url  # İşlem yapılacak URL'yi sakla

    def run(self):
        # İş parçacığı çalıştırıldığında yapılacak işlemler
        response = requests.get(self.url)  # URL'ye istek gönder
        self.jhson_array.append(response.json())  # Yanıtı listeye ekle (hatalı kullanım, düzeltilmeli)
        print(self.jhson_array)  # Yanıtları yazdır
        return response.json()  # Yanıtı döndür


def get_data_threading(urls):
    # Verilen URL'lere iş parçacıkları kullanarak istek gönderir
    st = time.time()  # İşlem başlangıç zamanını kaydet
    threads = []  # İş parçacıklarını saklamak için bir liste
    for url in urls:
        t = ThreadingDownloader(url)  # Her URL için bir iş parçacığı oluştur
        t.start()  # İş parçacığını başlat
        threads.append(t)  # İş parçacığını listeye ekle

    for t in threads:
        t.join()  # Tüm iş parçacıklarının tamamlanmasını bekle
        print(t)  # İş parçacığını yazdır (anlamsız, düzeltilmeli)

    et = time.time()  # İşlem bitiş zamanını kaydet
    elapsed_time = et - st  # Geçen süreyi hesapla
    print(f"Elapsed time for threading requests: {elapsed_time} seconds")  # Geçen süreyi yazdır


async def get_data_async_but_as_wrapper(urls):
    # Verilen URL'lere asenkron olarak istek gönderir (sıralı şekilde)
    st = time.time()  # İşlem başlangıç zamanını kaydet
    json_array = []  # Yanıtları saklamak için bir liste

    async with aiohttp.ClientSession() as session:
        # Asenkron bir HTTP oturumu başlat
        for url in urls:
            async with session.get(url) as resp:
                # Her URL'ye istek gönder ve yanıtı al
                json_array.append(await resp.json())  # Yanıtı listeye ekle

    et = time.time()  # İşlem bitiş zamanını kaydet
    elapsed_time = et - st  # Geçen süreyi hesapla
    print(f"Elapsed time for async requests: {elapsed_time} seconds")  # Geçen süreyi yazdır
    return json_array  # Yanıtları döndür


async def get_data(session, url, json_array):
    # Tek bir URL'ye asenkron olarak istek gönderir ve yanıtı listeye ekler
    async with session.get(url) as resp:
        json_array.append(await resp.json())  # Yanıtı listeye ekle


async def get_data_async_concurrently(urls):
    # Verilen URL'lere asenkron olarak eş zamanlı istek gönderir
    st = time.time()  # İşlem başlangıç zamanını kaydet
    json_array = []  # Yanıtları saklamak için bir liste

    async with aiohttp.ClientSession() as session:
        # Asenkron bir HTTP oturumu başlat
        tasks = []  # Asenkron görevleri saklamak için bir liste
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
            # Her URL için bir asenkron görev oluştur ve listeye ekle
        await asyncio.gather(*tasks)  # Tüm görevleri eş zamanlı olarak çalıştır

    et = time.time()  # İşlem bitiş zamanını kaydet
    elapsed_time = et - st  # Geçen süreyi hesapla
    print(f"Elapsed time for async requests: {elapsed_time} seconds")  # Geçen süreyi yazdır
    return json_array  # Yanıtları döndür


urls = ["https://postman-echo.com/delay/3", ] * 10  # Test için 10 adet aynı URL
#get_data_sync(urls)  # Senkron istekleri çalıştır (yaklaşık 40 saniye sürer)
#get_data_threading(urls)  # İş parçacıkları ile istekleri çalıştır (yaklaşık 3 saniye sürer)
#asyncio.run(get_data_async_but_as_wrapper(urls))  # Asenkron sıralı istekleri çalıştır (yaklaşık 37 saniye sürer)
#asyncio.run(get_data_async_concurrently(urls))  # Asenkron eş zamanlı istekleri çalıştır (yaklaşık 5 saniye sürer)