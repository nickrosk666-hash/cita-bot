import requests
import time

TOKEN = "PASTE_TOKEN"
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

        if "No hay citas disponibles" not in r.text:
            send("🔥 Возможно появилась запись на CITA Barcelona!")

        print("checked")

    except Exception as e:
        print("error", e)

    time.sleep(10)
