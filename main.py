import telebot
import requests
import buttons

URL = 'http://18.191.130.122/apicentres/'
URL_LANGS = 'http://learningcourses.uz/apicentres/?lang__slugs={}&sub__slugs='
URL_SUBJS = 'http://learningcourses.uz/apicentres/?lang__slugs=&sub__slugs={}'
BOT_TOKEN = "2144753786:AAEVx-4NRLrj0cugcS6kPeMkuaFbv2Wm0rw"
bot = telebot.TeleBot(BOT_TOKEN)
users = []


def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f'{local_filename}', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def getCentres(message, data):
    for i in data:
        result = ''
        ln = ''
        image_url = i['img']
        more = f"http://learningcourses.uz/detailed/{i['id']}/"
        download_file(image_url)
        photo_text = image_url.split('/')[-1]
        photo = open(f'{photo_text}', 'rb')
        for lang in i['lang']:
            ln += f"🔷{lang['name']}\n"
        sb = ''
        for subj in i['sub']:
            sb += f"🔶{subj['name']}\n"
        result += f"🎓🎓🎓 {i['name']} 🎓🎓🎓 \n\n🚩Languages: \n{ln} \n\n📚Subjects: \n{sb} \n✅{i['additional']} \nMore info: {more} \n\n📲Tel: +998 {i['tel']} \n📥Sayt: {i['sayt']} \n🗺{i['addres']}\n\n Likes:👍🏻 {len(list(i['likes']))}\t Dislikes:👎🏻 {len(list(i['dis_likes']))} \n\n \n👉👉 @learning_courses_bot 👈👈 "
        bot.send_photo(message.from_user.id, photo, caption=result)


def centresbyslug(message, slug):
    try:
        centres = requests.get(URL_SUBJS.format(slug)).json()
        if centres:
            getCentres(message, centres)
        else:
            centres = requests.get(URL_LANGS.format(f'{slug}')).json()
            getCentres(message, centres)
    except:
        print('error')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Assalom aleykum qanaqa yonalishda O\'quv markaz izlayabsiz',
                     reply_markup=buttons.button_start())


@bot.message_handler(commands=['fanlar'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Qaysi yo\'nalishda kurslar qidiryabsiz \n📚📙📘💻📱',
                     reply_markup=buttons.buttons_subjects())


@bot.message_handler(commands=['tillar'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Qaysi Tildan kurslar qidiryabsiz \n🇬🇧 🇷🇺 🇰🇷 🇯🇵 🇦🇪 🇩🇪 🇫🇷 🇨🇳',
                     reply_markup=buttons.buttons_langs())

@bot.callback_query_handler(func=lambda m: True)
def StudyCentres(call):

    if call.data == 'subjects':
        bot.send_message(call.from_user.id, 'Qaysi yo\'nalishda kurslar qidiryabsiz \n📚📙📘💻📱',
                         reply_markup=buttons.buttons_subjects())
    elif call.data == 'languages':
        bot.send_message(call.from_user.id, 'Qaysi Tildan kurslar qidiryabsiz \n🇬🇧 🇷🇺 🇰🇷 🇯🇵 🇦🇪 🇩🇪 🇫🇷 🇨🇳',
                         reply_markup=buttons.buttons_langs())
    else:
        centresbyslug(call, call.data)


bot.polling()
