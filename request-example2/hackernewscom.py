import requests  # HTTP istekleri yapmak için kullanılır

# En üstteki 30 haberin ID'lerini al
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"  # Top haberlerin ID'lerini veren API adresi
top_ids = requests.get(top_stories_url).json()[:30]  # API'den gelen ID listesinin ilk 30 tanesini al

for idx, story_id in enumerate(top_ids, 1):  # Her haber ID'si için sırayla işle
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"  # Haber detaylarını veren API adresi
    story = requests.get(story_url).json()  # Haber detaylarını JSON olarak al
    print(f"{idx}. {story.get('title')} ({story.get('url', 'No URL')})")  # Haber başlığını ve varsa bağlantısını yazdır