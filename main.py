import telebot
import json
from random import choice
import pyfiglet
resi = pyfiglet.figlet_format('SUM NIGGA', font='banner3-d')
print(resi)
bot = telebot.TeleBot('6793222950:AAGn8q4z0gDeCAre1_tYnK5R35TswCSwUq8')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Бот находится в разработке и не выполняет базовые функции')


@bot.message_handler(commands=['start'])
def start(message):

    with open('users.json') as json_file:
        data = json.load(json_file)
    # Проверка наличия пользователя в файле
    user_exists = False
    for user in data['users']:
        if user['id'] == message.from_user.id:
            user_exists = True
            break
    # Если пользователь уже есть в файле
    if user_exists:
        questionnaire(message)
    else:
        return begin_registration(message)


def begin_registration(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 1
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    butt1 = telebot.types.InlineKeyboardButton(text='Регистрация', callback_data='butt1')
    keyboard.add(butt1)
    bot.send_message(message.chat.id, text=f'\
                                                        \nПривет {message.from_user.first_name}!\
                                                        \n➖➖➖➖➖➖➖➖➖➖➖➖\
                                                        \n SUM|neigbour предназначен для поиска сожителя\
                                                        \n в университете, для начала зарегестрируйтесь\
                                                        \n➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=keyboard)


def menu(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    but1 = telebot.types.InlineKeyboardButton(text='Скрыть анкету', callback_data='1')
    but2 = telebot.types.InlineKeyboardButton(text='Лайки', callback_data='2')
    but3 = telebot.types.InlineKeyboardButton(text='Моя анкета', callback_data='3')
    markup.add(but1, but2, but3)
    bot.send_message(message.chat.id, 'Меню', reply_markup=markup)


def registration(message):
    # Задайте вопрос о поле пользователя
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 2
    button1 = telebot.types.KeyboardButton('Муж')
    button2 = telebot.types.KeyboardButton('Жен')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Укажите ваше пол', reply_markup=markup)
    bot.register_next_step_handler(message, process_gender_step)


def process_gender_step(message):
    # Введите код для обработки ответа пользователя о поле
    gender = message.text

    # Задайте вопрос о возрасте пользователя
    bot.send_message(message.chat.id, 'Укажите ваш возраст (от 18 до 30)', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, Name_user, gender)


def Name_user(message, gender):
    # Введите код для обработки ответа пользователя о поле
    name_user = message.text

    # Задайте вопрос о возрасте пользователя
    bot.send_message(message.chat.id, 'Укажите ваше имя')
    bot.register_next_step_handler(message, process_age_step, gender, name_user)


def process_age_step(message, gender, name_user):
    # Введите код для обработки ответа пользователя о возрасте
    age = message.text

    # Задайте вопрос об институте
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 2
    button1 = telebot.types.KeyboardButton('ИЭФ')
    button2 = telebot.types.KeyboardButton('ИМ')
    button3 = telebot.types.KeyboardButton('ИОМ')
    button4 = telebot.types.KeyboardButton('ИИС')
    button5 = telebot.types.KeyboardButton('ИГУиП')
    button6 = telebot.types.KeyboardButton('ИУПСиБК')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, 'Укажите ваш институт', reply_markup=markup)
    bot.register_next_step_handler(message, process_institute_step, age, gender, name_user)


def process_institute_step(message, age, gender, name_user):
    # Введите код для обработки ответа пользователя об институте
    institute = message.text

    # Задайте вопрос о курсе обучения
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 2
    button1 = telebot.types.KeyboardButton('1')
    button2 = telebot.types.KeyboardButton('2')
    button3 = telebot.types.KeyboardButton('3')
    button4 = telebot.types.KeyboardButton('4')
    button5 = telebot.types.KeyboardButton('магистратура')
    button6 = telebot.types.KeyboardButton('аспирантура')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, 'Укажите ваш курс обучения', reply_markup=markup)
    bot.register_next_step_handler(message, process_yourself_step, institute, age, gender, name_user)


def process_yourself_step(message, age, gender, name_user, institute):
    course = message.text
    bot.send_message(message.chat.id, f'\
                                                    \n{gender}, расскажите о себе, а именно\
                                                    \n➖➖➖➖➖➖➖➖➖➖➖➖\
                                                    \n Поддерживаете ли вы порядок? Во сколько ложитесь?\
                                                    \n Как часто зовете гостей? Какое отношение к алкоголю/курению?\
                                                    \n➖➖➖➖➖➖➖➖➖➖➖➖\
                                                    \n Предпочтения по сьему\
                                                    \n Сколько готов платить (30-40)? Пожелания по ремонту?\
                                                    \n➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, process_course_step, institute, age, gender, name_user, course)


def process_course_step(message, institute, age, gender, name_user, course):
    # Введите код для обработки ответа пользователя о курсе обучения
    yourself = message.text
    # Сохраните данные пользователя в users.json
    user_data = {
        'id': message.from_user.id,
        'Nickname в телеграмме': f"@{message.from_user.username}",
        'Возраст': institute,
        'Пол': name_user,
        'Имя': gender,
        'Институт': age,
        'Курс': course,
        'О себе': yourself,
    }
    with open('users.json', 'r+', encoding='utf-8') as file:
        try:
            existing_data = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_data = {'users': []}
        existing_data['users'].append(user_data)
        file.seek(0)
        json.dump(existing_data, file, indent=4, ensure_ascii=False)
        file.truncate()
        file.write('\n')
    keyboard = telebot.types.InlineKeyboardMarkup()
    butt1 = telebot.types.InlineKeyboardButton(text='Добавить фотографию', callback_data='butt1')
    keyboard.add(butt1)
    bot.send_message(message.chat.id, 'Для того чтобы завершить регистрацию отправьте фотографию',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Проверяем, что сообщение содержит фотографию
    if message.content_type == 'photo':
        # Сохраняем фотографию в папку 'photos'
        photo = message.photo[-1]  # Берем последнюю фотографию (с наивысшим разрешением)
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = f'photos/{message.from_user.id}.jpg'  # Путь для сохранения фотографии
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Обновляем информацию о пользователе в файле JSON
        with open('users.json', 'r+') as file:
            data = json.load(file)
            users = data['users']
            for user in users:
                if user['id'] == message.from_user.id:
                    user['Фотография'] = file_path
                    break
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.truncate()

        questionnaire(message)
    else:
        bot.reply_to(message, 'Пожалуйста, отправьте фотографию')


def remove_user(message):
    with open('users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    user_id = message.from_user.id
    found_user = None
    for user in data['users']:
        if user['id'] == user_id:
            found_user = user
            break
    if found_user:
        data['users'].remove(found_user)
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)


def questionnaire(message):
    # Загружаем данные пользователя из users.json
    with open('users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Инициализируем переменную, отвечающую за количество попыток поиска
    attempts = 0

    # Ищем анкету пользователя по ID
    user_id = message.from_user.id
    user_data = None
    while attempts < 5:  # Проверяем до 5 раз
        for user in data['users']:
            if user['id'] == user_id:
                user_data = user
                break
        if user_data:
            break
        attempts += 1
    if user_data:
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        one = telebot.types.InlineKeyboardButton(text='Просмотр Анкет', callback_data='one')
        three = telebot.types.InlineKeyboardButton(text='настройка профиля', callback_data='three')
        markup.add(one, three)

        # Загружаем и отправляем фотографию
        image_path = user_data.get("Фотография")  # Путь к фотографии
        if image_path:
            with open(image_path, 'rb') as photo:
                # Отправляем фотографию в сообщении
                bot.send_photo(message.chat.id, photo, caption=f'''
                Ваша анкета:
                Имя: {user_data["Имя"]}
                Возраст: {user_data["Возраст"]}
                Пол: {user_data["Пол"]}
                Институт: {user_data["Институт"]}
                О себе: {user_data["О себе"]}
                ''', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Отсутствует фотография в анкете')

    else:
        bot.send_message(message.chat.id, 'Ошибка в поиске анкеты')


def options_questionnaire(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    b1 = telebot.types.InlineKeyboardButton(text='Поменять фотографию', callback_data='b1')
    b3 = telebot.types.InlineKeyboardButton(text='Заново пройти регистрацию', callback_data='b3')
    keyboard.add(b1, b3)
    bot.send_message(message.chat.id, text="Выберете что хотите изменить", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if call.data == 'butt1':
        bot.send_message(call.message.chat.id, text='Отправте фотографию')
    elif call.data == 'butt3':
        bot.send_message(call.message.chat.id, text="А все уже")
    elif call.data == 'three':
        return options_questionnaire(call.message)
    elif call.data == 'b1':
        bot.send_message(call.message.chat.id, text='Отправте фотографию!')
    elif call.data == 'b3':
        return registration(call.message)
    elif call.data == 'one':
        random_questionnaire(call.message)
    elif call.data == 'cnopka1':
        random_questionnaire(call.message)
    elif call.data == 'cnopka3':
        questionnaire(call.message)
    else:
        bot.send_message(call.message.chat.id, text="ERROR HANDLE CALLDATA")


@bot.message_handler(func=lambda message: True)
def handle_question(message):
    if message.text:
        if "Регистрация" in message.text:
            registration(message)
        else:
            bot.send_message(message.chat.id, text="Ошибка options_questionnaire")
    else:
        bot.send_message(message.chat.id, text='Ошибка в блоке обрабочика кнопок')
    if message.content_type == 'photo':
        bot.send_message(message.chat.id, text='Фотография успешно обновлена')
        questionnaire(message)
    else:
        print('ошибка message.content_type == photo')


def random_questionnaire(message):
    try:
        # Загружаем данные пользователя из users.json
        with open('users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Получаем случайный ID пользователя
        random_user_id = choice(data['users'])['id']

        # Ищем анкету пользователя по ID
        user_data = None
        for user in data['users']:
            if user['id'] == random_user_id:
                user_data = user
                break

        if user_data:
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            but1 = telebot.types.InlineKeyboardButton(text='Далее', callback_data='cnopka1')
            markup.add(but1)
            # Загружаем и отправляем фотографию
            image_path = user_data["Фотография"]  # Путь к фотографии
            with open(image_path, 'rb') as photo:
                # Отправляем фотографию в сообщении
                bot.send_photo(message.chat.id, photo, caption=f'''
                Имя: {user_data["Имя"]}
                Возраст: {user_data["Возраст"]}
                Пол: {user_data["Пол"]}
                Институт: {user_data["Институт"]}
                Телеграмма: {user_data["Nickname в телеграмме"]}
                О себе: {user_data["О себе"]}
                ''', reply_markup=markup)
        else:
            # Если анкета пользователя не найдена
            bot.send_message(message.chat.id, 'Ошибка в поиске анкеты не найдена.')
    except KeyError:
        bot.send_message(message.chat.id, "повторите попытку")


bot.polling(none_stop=True)