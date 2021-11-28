from telebot import types


def button_start():
    markup = types.InlineKeyboardMarkup(row_width=2)
    subj = types.InlineKeyboardButton('Fanlar', callback_data='subjects')
    lang = types.InlineKeyboardButton('Tillar', callback_data='languages')
    markup.add(subj, lang)
    return markup


def buttons_subjects():
    markup = types.InlineKeyboardMarkup(row_width=4)
    python = types.InlineKeyboardButton('python', callback_data='python')
    js = types.InlineKeyboardButton('js', callback_data='js')
    math = types.InlineKeyboardButton('matem', callback_data='math')
    history = types.InlineKeyboardButton('Tarix', callback_data='history')
    smm = types.InlineKeyboardButton('smm🎯', callback_data='smm')
    literature = types.InlineKeyboardButton('literature', callback_data='literature')
    chemistry = types.InlineKeyboardButton('chemistry', callback_data='chemistry')
    java = types.InlineKeyboardButton('java', callback_data='java')
    graphic_design = types.InlineKeyboardButton('grafik design', callback_data='graphic_design')
    ai = types.InlineKeyboardButton('ai', callback_data='ai')
    ielts = types.InlineKeyboardButton('ielts', callback_data='ielts')
    frontend = types.InlineKeyboardButton('frontend', callback_data='frontend')
    php = types.InlineKeyboardButton('php', callback_data='php')
    ios = types.InlineKeyboardButton('ios', callback_data='ios')
    flutter = types.InlineKeyboardButton('flutter', callback_data='flutter')
    fizika = types.InlineKeyboardButton('fizika', callback_data='fizika')
    biology = types.InlineKeyboardButton('biology🧪', callback_data='biology')
    robototehnika = types.InlineKeyboardButton('🤖 tehnika', callback_data='robototehnika')
    mobile_developing = types.InlineKeyboardButton('📱 developing', callback_data='mobile_developing')
    markup.add(python, js, math, history, smm, fizika, flutter, php, ios, frontend, biology, robototehnika, literature,
               ielts, chemistry, ai, java, graphic_design, mobile_developing)
    return markup


def buttons_langs():
    markup = types.InlineKeyboardMarkup(row_width=3)
    english = types.InlineKeyboardButton('english🇬🇧', callback_data='english')
    russian = types.InlineKeyboardButton('russian🇷🇺', callback_data='russian')
    korean = types.InlineKeyboardButton('korean🇰🇷', callback_data='korean')
    japan = types.InlineKeyboardButton('japan🇯🇵', callback_data='japan')
    arabic = types.InlineKeyboardButton('arabic🇦🇪', callback_data='arabic')
    deutsch = types.InlineKeyboardButton('deutsch🇩🇪', callback_data='deutsch')
    french = types.InlineKeyboardButton('french🇫🇷', callback_data='french')
    chinese = types.InlineKeyboardButton('chinese🇨🇳', callback_data='chinese')
    markup.add(english, russian, korean, japan, arabic, deutsch, french, chinese)
    return markup
