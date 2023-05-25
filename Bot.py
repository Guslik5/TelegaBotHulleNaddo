import time
import logging

from aiogram import Bot, Dispatcher, executor, types

from db import Database
import AllTextMusic
import InformationAboutMusician

logging.basicConfig(level=logging.INFO)
TOKEN = "5824921460:AAFzNlAZcumMRl4vVz2XUUiM6g9gXC_v57c"
Id_First_Administrator = 1913377793

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = Database('database.db')


@dp.message_handler(commands=['start'])
async def start_handler(messege: types.Message):
    user_id = messege.from_user.id
    user_full_name = messege.from_user.full_name
    print("Инфомация о только что подключившемся пользователе:")
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')

    await messege.answer(f"Привет, {user_full_name}!")
    time.sleep(1)
    await messege.answer("Мы банда реперов и трахаем телечек 	🔞 \n"
                         "Чтобы узнать, что я могу напиши или нажми /help и пользуйся простой менюшкой\n"
                         "Подписывайся на нас в вк https://vk.com/hlnaddo181411502 🌐")

    if messege.chat.type == 'private':
        if not db.user_exists(user_id):
            db.add_user(user_id, user_full_name)


@dp.message_handler(commands="help")
async def help_handler(message: types.Message):
    await message.answer(
        "Мы очень рады, что ты за нами следишь, мы за тобой тоже, надеюсь ты уже подписался на нашу группу")
    kb = [
        [
            types.KeyboardButton(text="Список всех песен 🎵"),
            types.KeyboardButton(text="Список участников группы 👪"),
            types.KeyboardButton(text="Информация о группе 📜"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Я люблю тебя"
    )
    keyboard.add(types.KeyboardButton(text="Стикерпак группы 😊"))
    keyboard.add(types.KeyboardButton(text="Перейти к группе вконтакте 🌐", url='https://vk.com/hlnaddo181411502'))
    await message.answer("Ну что, приступим 😍", reply_markup=keyboard)

    @dp.message_handler(text="Список всех песен 🎵")
    async def with_puree(message: types.Message):
        InlineKeyboardForTrack = types.InlineKeyboardMarkup(row_width=2)

        button1 = types.InlineKeyboardButton(text="TATAR11IN - INTRO", callback_data="TATAR11IN - INTRO")
        button2 = types.InlineKeyboardButton(text="TATAR11IN feat. WHATDISLUV - КТО ДОМА",
                                             callback_data="TATAR11IN feat. WHATDISLUV - КТО ДОМА")
        button3 = types.InlineKeyboardButton(text="TATAR11IN - БЛОК НОМЕР 11",
                                             callback_data="TATAR11IN - БЛОК НОМЕР 11")
        button4 = types.InlineKeyboardButton(text="TATAR11IN feat. WHATDISLUV - РАМА",
                                             callback_data="TATAR11IN feat. WHATDISLUV - РАМА")
        button5 = types.InlineKeyboardButton(text="TATAR11IN - СЛУЧАЙНО", callback_data="TATAR11IN - СЛУЧАЙНО")

        InlineKeyboardForTrack.add(button1)
        InlineKeyboardForTrack.add(button2)
        InlineKeyboardForTrack.add(button3)
        InlineKeyboardForTrack.add(button4)
        InlineKeyboardForTrack.add(button5)
        await message.answer("<b>Тут список наших песен,</b> выбери и я скину тебе текст и песню",
                             reply_markup=InlineKeyboardForTrack, parse_mode="HTML")

    @dp.callback_query_handler(text="TATAR11IN - INTRO")
    async def send_music(call: types.CallbackQuery):
        await call.message.answer(f"🎧TATAR11IN - INTRO🎧\n {AllTextMusic.AllText[0]}")
        audio = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\music\TATAR11IN - INTRO.mp3', 'rb')
        await bot.send_audio(call.from_user.id, audio)
        audio.close()

    @dp.callback_query_handler(text="TATAR11IN feat. WHATDISLUV - КТО ДОМА")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer(f"🎧TATAR11IN feat. WHATDISLUV - КТО ДОМА🎧\n {AllTextMusic.AllText[1]}")
        audio = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\music\TATAR11IN feat. WHATDISLUV - КТО ДОМА.mp3', 'rb')
        await bot.send_audio(call.from_user.id, audio)
        audio.close()

    @dp.callback_query_handler(text="TATAR11IN - БЛОК НОМЕР 11")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer(f"🎧TATAR11IN - БЛОК НОМЕР 11🎧\n {AllTextMusic.AllText[2]}")
        audio = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\music\TATAR11IN - БЛОК НОМЕР 11.mp3', 'rb')
        await bot.send_audio(call.from_user.id, audio)
        audio.close()

    @dp.callback_query_handler(text="TATAR11IN feat. WHATDISLUV - РАМА")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer(f"🎧TATAR11IN feat. WHATDISLUV - РАМА🎧\n \n {AllTextMusic.AllText[3]}")

        audio = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\music\TATAR11IN feat. WHATDISLUV - РАМА.mp3', 'rb')
        await bot.send_audio(call.from_user.id, audio)
        audio.close()

    @dp.callback_query_handler(text="TATAR11IN - СЛУЧАЙНО")
    async def send_random_value(call: types.CallbackQuery):
        await call.message.answer(f"🎧TATAR11IN - СЛУЧАЙНО🎧 \n {AllTextMusic.AllText[4]}")
        audio = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\music\TATAR11IN - СЛУЧАЙНО.mp3', 'rb')
        await bot.send_audio(call.from_user.id, audio)
        audio.close()

    @dp.message_handler(lambda message: message.text == "Список участников группы 👪")
    async def InfoMusician(message: types.Message):
        InlineKeyboardForMusician = types.InlineKeyboardMarkup(row_width=2)
        buttonKirill = types.InlineKeyboardButton(text="Многосторонний TATAR11IN 👷", callback_data="TATAR11IN")
        buttonGuslik = types.InlineKeyboardButton(text="Звукорежиссер порно Guslik 👽", callback_data="Guslik")
        buttonOstap = types.InlineKeyboardButton(text="Владелец шаурмичной Ostap 💂", callback_data="Ostap")
        InlineKeyboardForMusician.add(buttonKirill)
        InlineKeyboardForMusician.add(buttonGuslik)
        InlineKeyboardForMusician.add(buttonOstap)

        await message.reply("Выбери кого-нибудь из нас, только никому не рассказывай что ты сейчас увидишь, <b>это тайная информация</b>", reply_markup=InlineKeyboardForMusician, parse_mode="HTML")

    @dp.callback_query_handler(text="TATAR11IN")
    async def send_music(call: types.CallbackQuery):
        await call.message.answer(f"👷TATAR11IN👷\n {InformationAboutMusician.InfoAboutMusician[0]}")
        photoKirill = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\Images\Kirill.jpg', 'rb')
        await bot.send_photo(call.from_user.id, photoKirill)
        photoKirill.close()

    @dp.callback_query_handler(text="Guslik")
    async def send_music(call: types.CallbackQuery):
        await call.message.answer(f"👽Guslik👽\n {InformationAboutMusician.InfoAboutMusician[1]}")
        photoGuslik = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\Images\Guslik.jpg', 'rb')
        await bot.send_photo(call.from_user.id, photoGuslik)
        photoGuslik.close()

    @dp.callback_query_handler(text="Ostap")
    async def send_music(call: types.CallbackQuery):
        await call.message.answer(f"💂Ostap💂\n {InformationAboutMusician.InfoAboutMusician[2]}")
        photoOstap = open(r'C:\Users\Guslik\Desktop\MyTelegramBot\Images\Ostap.png', 'rb')
        await bot.send_photo(call.from_user.id, photoOstap)
        photoOstap.close()

    @dp.message_handler(lambda message: message.text == "Информация о группе 📜")
    async def without_puree(message: types.Message):
        await message.reply("Наша группа самая крутая, потому что никто не сможет перепеть нас на лавке")

    @dp.message_handler(lambda message: message.text == "Стикерпак группы 😊")
    async def without_puree(message: types.Message):
        await message.reply(
            "Стекерпак Hule Naddo это лучшее, что есть на этом свете, пользуйся на здоровье ❤ \n https://t.me/addstickers/HULENADDO")

    @dp.message_handler(text="Перейти к группе вконтакте 🌐")
    async def with_puree(message: types.Message):
        await message.reply(
            "Мы очень рады, что ты хочешь следить за новостями в группе, теперь мы можем бахнуть пива на лавке 🍻 \n https://vk.com/hlnaddo181411502 🌐")



@dp.message_handler(commands=["ILoveBeer"])
async def cmd_answer(message: types.Message):
    await message.answer("Красава Брат, пиво лучшее что есть на этом свете")


@dp.message_handler(commands=["remove"])
async def cmd_dice(message: types.Message):
    if message.from_user.id == Id_First_Administrator:
        db.remove_all_users()
    await message.answer("Удаление из базы данных выполнено")
    await message.answer_dice(emoji="🎲")


@dp.message_handler(commands=["test"])
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")


@dp.message_handler(commands=["sendAll"])
async def send_all(messege: types.Message):
    if messege.chat.type == 'private':
        if messege.from_user.id == Id_First_Administrator:
            text = messege.text[9:]
            users = db.get_user()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(messege.from_user.id, "Рассылка выполнена")

@dp.message_handler(commands=["playGame"])
async def game_handler(messege: types.Message):
    game_rating = db.get_game_rating(messege.from_user.id)
    new_game_rating = db.set_game_rating(messege.from_user.id, game_rating+1)
    await bot.send_message(messege.from_user.id, f"Рассылка выполнена {game_rating}")


@dp.message_handler(commands=["defaultGame"])
async def default_game_handler(messege: types.Message):
     db.set_default_game_rating()
     await bot.send_message(messege.from_user.id, "Рейтинг обнавлен ")

if __name__ == '__main__':
    executor.start_polling(dp)



