from telethon import TelegramClient
import os
from itertools import cycle
import asyncio

api_id = 20403628  # Замените на ваш
api_hash = 'a82bd42ad21f9790880449d637b6aec5'  # Замените на ваш
phone_number = '+797122301213'  # Ваш номер
images_folder = ''#путь к папке с фотками
recipients = ['@bebro228','@susic'] # Можно юзернейм# Или ID чата (число)# Или номер телефона (если в контактах)

client = TelegramClient('session_name', api_id, api_hash)

message_after_photo="Текст после фото"
message_before_photo="Текст в самом начале работ бота"

async def send_images():
    images = [
        f for f in os.listdir(images_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]

    if not images:
        print("❌ Нет изображений в папке!")
        return

    for recipient in recipients:
        await client.send_message(recipient, message_before_photo)

    image_cycle = cycle(images)
    for recipient in recipients:
        print(f"\n🔄 Начинаю отправку для {recipient}...")

        for i in range(50):
            img = next(image_cycle)
            img_path = os.path.join(images_folder, img)

            try:
                await client.send_file(recipient, img_path)
                print(f"✅ [{recipient}] Отправлено {i + 1}/50: {img}")

                await client.send_message(recipient, message_after_photo)
            except Exception as e:
                print(f"❌ Ошибка при отправке {img} для {recipient}: {e}")

            await asyncio.sleep(1)

with client:
    client.loop.run_until_complete(send_images())
