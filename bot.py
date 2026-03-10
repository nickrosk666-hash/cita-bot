import requests
import time
import re

TOKEN = "8585687977:AAEErCSoRixgv7hvn3E7YLb8vVbfMfBAYaQ"  # вставь свой токен
CHAT_ID = "525629073"
URL = "https://icp.administracionelectronica.gob.es/icpplus/index.html"

# Настройка SOCKS4 прокси
proxies = {
    "http": "socks4://149.34.2.39:8080",
    "https": "socks4://149.34.2.39:8080"
}

def send(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": msg}
        )
    except Exception as e:
        print("Ошибка отправки Telegram:", e)

print("Bot started")

while True:
    for attempt in range(3):  # повторим до 3 раз, если прокси упадёт
        try:
            r = requests.get(URL, timeout=20, proxies=proxies)
            text = r.text

            if "No hay citas disponibles" not in text:
                # ищем название города
                cities = re.findall(r'Barcelona[^<]{0,40}', text)
                city = cities[0] if cities else "Barcelona (точный офис не найден)"
                send(f"🔥 Появилась CITA!\nГород / офис: {city}")

            print("checked")
            break  # если всё прошло успешно, выходим из цикла повторов

        except Exception as e:
            print(f"Ошибка подключения (попытка {attempt+1}/3):", e)
            time.sleep(5)  # ждём перед повтором

    # Ждём 4 минуты перед следующей проверкой
    time.sleep(240)
