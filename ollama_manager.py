import requests

class OllamaManager:
    def __init__(self, url="http://178.233.128.84:12436/api/message"):
        self.url = url

    def send_message(self, message):
        try:
            response = requests.post(self.url, json={"message": message})
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Ollama API hatası: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"Ollama API'ye bağlanılamadı: {e}")
            return None
