from jikanpy import Jikan

jikan = Jikan()

# Отримуємо аніме поточного сезону
print("Отримання даних про поточний сезон...")
season_now = jikan.seasons(extension='now')

print("-" * 50)
print(f"Аніме сезону: {season_now['data'][0]['season'].capitalize()} {season_now['data'][0]['year']}")
print("-" * 50)

# Виводимо перші 10 аніме
for anime in season_now['data'][:10]:
    title = anime.get('title')
    score = anime.get('score', 'Без оцінки')
    print(f"🎬 {title} — ⭐ Оцінка: {score}")