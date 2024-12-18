
import requests

url = "http://178.233.128.84:12436"  # Sunucu adresi
#url = "http://localhost:11436/api/message"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Bağlantı başarılı! Sunucu çalışıyor.")
    else:
        print(f"Bağlantı başarısız: {response.status_code}")
except Exception as e:
    print(f"Sunucuya bağlanılamadı: {e}")
