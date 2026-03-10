import requests
import time
import re

TOKEN = "PASTE_YOUR_TOKEN"
CHAT_ID = "525629073"

URL = "https://icp.administracionelectronica.gob.es/icpplus/index.html"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

print("Bot started")

while True:

    try:
        r = requests.get(URL, timeout=20)
        text = r.text

        if "No hay citas disponibles" not in text:

            # ищем названия городов
            cities = re.findall(r'Barcelona[^<]{0,40}', text)

            if cities:
                city = cities[0]
            else:
                city = "Barcelona (точный офис не найден)"

            send(f"🔥 Появилась CITA!\nГород / офис: {city}")

        print("checked")

    except Exception as e:
        print("error", e)

    time.sleep(10)
