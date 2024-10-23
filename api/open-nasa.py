
import requests


try:
    dd, mm, yyyy = map(int, input("Введите дату формата DD.MM.YYYY: ").split('.'))
except:
    print("""

    ===================
        NASA APOD
    ===================
    """)

    print("    Дата введена в другом формате. Перезапустите программу.")
    exit()


url=f'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={yyyy}-{mm}-{dd}'
response = requests.get(url).json()
date, explanation, media_type, title = response['date'], response['explanation'], response['media_type'], response['title']

print("""

    ===================
        NASA APOD
    ===================
""")

def photo_text(date, expl, mtype, title):
    if mtype == 'other':
        return rf"""    Дата: {date}
    Заголовок: {title}
    Описание: {expl}
"""
    if mtype == 'image':
        img = response['url']
        return rf"""    Дата: {date}
    Заголовок: {title}
    Описание: {expl}
    Изображение: {img}

"""

    if mtype == 'video':
            url = response['url']
            return rf"""    Дата: {date}
    Заголовок: {title}
    Описание: {expl}
    Видео: {url}
    """

print(
    photo_text(
        date,
        explanation,
        media_type,
        title
    )
)