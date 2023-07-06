from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from cread import TOKEN
from menu import main_menu_keyboard, cours_menu_keyboard
from key_buttons import tele_button, button

def start(update:Update, context: CallbackContext):
    update.message.reply_text(
        f"Welcome {update.effective_user.username}",
        reply_markup=main_menu_keyboard()
    )

def we_on_maps(update:Update, context: CallbackContext):
    update.message.reply_text(
        f'📍 Наш адрес: Ибраимова 115/1 (Напротив Bishkek centrum hotel)]\n⌛ График работы: \nРабочие дни с 10:00-19:00',
    reply_markup=main_menu_keyboard()
    )

def we_info(update:Update, context: CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать в Ogogo Academy! Мы являемся академией, специализирующейся на изучении программирования и развитии навыков в сфере информационных технологий. Наша миссия - помочь студентам достичь успеха в сфере технологий, предоставляя высококачественное образование и практические навыки. \nВ Ogogo Academy мы предлагаем разнообразные курсы, охватывающие популярные языки программирования, такие как Python и JavaScript. Независимо от вашего уровня подготовки - от начинающего до опытного программиста, наши экспертные преподаватели помогут вам освоить фундаментальные концепции и техники программирования, а также научат вас применять их на практике. Мы также предлагаем обучение в сфере UX UI (пользовательский опыт и интерфейс), чтобы помочь студентам создавать удобные и привлекательные веб-приложения и веб-сайты.\n Наши курсы UX/UI позволяют студентам изучить принципы дизайна, навыки прототипирования и тестирования, а также понять потребности и предпочтения пользователей. \nКроме того, в Ogogo Academy вы найдете наши курсы по английскому языку. Мы понимаем, что знание английского языка является ключевым фактором для успешной карьеры в IT-индустрии. Поэтому мы предлагаем специальные программы, которые помогут вам улучшить ваши навыки чтения, письма, говорения и аудирования на английском языке, специфически нацеленные на термины и контекст IT-сферы. \nПрисоединяйтесь к Ogogo Academy и откройте для себя захватывающий мир программирования, дизайна и языковых навыков. Наша команда экспертов исключительно мотивирована помочь вам достичь успеха и реализовать ваши профессиональные цели. Давайте вместе создавать будущее в технологической индустрии!"',
    reply_markup=main_menu_keyboard()
    )

def resive_courses_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        f"Выберите курс",
        reply_markup=cours_menu_keyboard()
    )

def back_to_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        f'Вы успешно вернулись назад на главное меню',
        reply_markup=main_menu_keyboard()
    )



def python_courses(update:Update, context: CallbackContext):
    update.message.reply_text(
        f'Курс по пайтон, мы обучим вас языку Python за 4 месяца',
        reply_markup=cours_menu_keyboard()
    )

def js_courses(update:Update, context: CallbackContext):
    update.message.reply_text(
        f'Курс по джава скрипт, мы обучим вас языку JS',
        reply_markup=cours_menu_keyboard()
    )

def uxui_courses(update:Update, context: CallbackContext):
    update.message.reply_text(
        f'Курс UX UI скрипт, мы обучим вас языку UX UI',
        reply_markup=cours_menu_keyboard()
    )

WE = tele_button[0]
MAPS = tele_button[2]
COURS_MENU = tele_button[1]

BACK = button[3]
PYTHON = button[0]
JS = button[1]
UXUI = button[2]

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(WE),
    we_info
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MAPS),
    we_on_maps
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURS_MENU),
    resive_courses_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back_to_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UXUI),
    uxui_courses
))

updater.start_polling()
updater.idle()

