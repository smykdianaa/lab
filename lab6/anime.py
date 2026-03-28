from flask import Flask
from jikanpy import Jikan

# Ініціалізація клієнта Jikan (API для MyAnimeList)
jikan = Jikan()
app = Flask(__name__)

# Отримуємо дані про епізоди аніме (ID 54595 - це аніме "Frieren")
# extension='episodes' дозволяє отримати саме список серій
try:
    j = jikan.anime(54595, extension='episodes')
except Exception as e:
    print(f"Помилка отримання даних: {e}")
    j = {"data": []}

@app.route('/')
def home():


    a ="<h1>Список епізодів аніме</h1>"
    # Проходимо циклом по отриманим даним
    for episode in j["data"]: 
        title = episode.get('title', 'Назва відсутня')
        score = episode.get('score', 'немає оцінки')
        a += f"<p><b>Епізод {episode['mal_id']}</b>: {title} — Оцінка: {score}</p>"
    return a

if __name__ == '__main__':
    # Запуск локального сервера
    app.run(debug=True)