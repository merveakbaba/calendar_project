from ollama_manager import OllamaManager
from calendar_manager import CalendarManager

def main():
    calendar_manager = CalendarManager()
    ollama_manager = OllamaManager()

    while True:
        print("\n1. Randevu Ekle\n2. Randevuları Listele\n3. Randevu Sil\n4. Randevu Güncelle\n5. Doğal Dil Komutu\n6. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == '1':
            summary = input("Randevu Başlığı: ")
            location = input("Yer: ")
            description = input("Açıklama: ")
            start_time = input("Başlangıç Zamanı (YYYY-MM-DDTHH:MM:SS): ")
            end_time = input("Bitiş Zamanı (YYYY-MM-DDTHH:MM:SS): ")
            calendar_manager.add_event(summary, location, description, start_time, end_time)

        elif secim == '2':
            calendar_manager.list_events()

        elif secim == '3':
            event_id = input("Silmek istediğiniz randevunun ID'si: ")
            calendar_manager.delete_event(event_id)

        elif secim == '4':
            event_id = input("Güncellemek istediğiniz randevunun ID'si: ")
            summary = input("Yeni Başlık (boş bırakabilirsiniz): ")
            description = input("Yeni Açıklama (boş bırakabilirsiniz): ")
            start_time = input("Yeni Başlangıç Zamanı (YYYY-MM-DDTHH:MM:SS, boş bırakabilirsiniz): ")
            end_time = input("Yeni Bitiş Zamanı (YYYY-MM-DDTHH:MM:SS, boş bırakabilirsiniz): ")
            calendar_manager.update_event(event_id, summary, description, start_time, end_time)

        elif secim == '5':
            user_input = input("Doğal dilde bir komut girin: ")
            ollama_response = ollama_manager.send_message(user_input)
            if ollama_response:
                print("Ollama'nın cevabı:", ollama_response)

        elif secim == '6':
            print("Çıkılıyor... ")
            break

        else:
            print("Geçersiz seçim. Lütfen 1-6 arasında bir değer girin.")

if __name__ == '__main__':
    main()
