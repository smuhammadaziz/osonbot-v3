from typing import List

from aiogram import types, F, Router

from aiogram.types import Message, ContentType

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types.callback_query import CallbackQuery

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, jihozlarButton, valyutaButton, borYoq
from loader import bot
from states.KvartiraState.JizzaxState import JizzaxHomeSotish

from transliterate import to_cyrillic

from utils.QuestionKvartira.kvartiraqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, channel_id, check_text, jizzaxregion, data2, data32, data33, \
    data34, data35, success_text, nechanchiqavatyoz


from keyboards.inline.data import JizzaxKvartiraData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData


mode = "Markdown"


jizzax_kv_router = Router()

@jizzax_kv_router.callback_query(JizzaxKvartiraData.filter(F.word=="jizzaxkv"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: JizzaxKvartiraData):
    await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(JizzaxHomeSotish.images)



# @jizzax_kv_router.message(JizzaxHomeSotish.images)
# async def starter(message: Message, album: List[Message], state: FSMContext):
#     file_ids = []

#     for photo in album:
#         if photo:
#             file_id = photo.photo[-1].file_id
#             file_ids.append(file_id)
#             print(file_id)
    
#     print(file_ids)

#     await state.update_data(images=file_ids)


#     await message.answer(umumiyMaydonyoz, parse_mode="HTML")
#     await state.set_state(JizzaxHomeSotish.umumiyMaydon)
    
@jizzax_kv_router.message(JizzaxHomeSotish.images)
async def starter(message: Message, state: FSMContext):
    text = message.text


    await state.update_data({
        "images": text
    })


    await message.answer(umumiyMaydonyoz, parse_mode="HTML")
    await state.set_state(JizzaxHomeSotish.umumiyMaydon)



@jizzax_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    JizzaxHomeSotish.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@jizzax_kv_router.message(JizzaxHomeSotish.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await state.set_state(JizzaxHomeSotish.xonalar)

    await bot.send_message(chat_id=message.chat.id, text=xonalaryoz, parse_mode="HTML")


@jizzax_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    JizzaxHomeSotish.xonalar)
async def check_xonalar(message: Message):
    await message.reply(faqatRaqamyoz)


@jizzax_kv_router.message(JizzaxHomeSotish.xonalar)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "xonalar": text
    })

    await bot.send_message(chat_id=message.chat.id, text=nechaQavatyoz, parse_mode="HTML")
    await state.set_state(JizzaxHomeSotish.qavat)


@jizzax_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    JizzaxHomeSotish.qavat)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@jizzax_kv_router.message(JizzaxHomeSotish.qavat)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavat": text
    })

    await bot.send_message(chat_id=message.chat.id, text=nechanchiqavatyoz, parse_mode="HTML")
    await state.set_state(JizzaxHomeSotish.qavatlik)


@jizzax_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    JizzaxHomeSotish.qavatlik)
async def check_qavat(message: types.Message):
    await message.reply(faqatRaqamyoz)


@jizzax_kv_router.message(JizzaxHomeSotish.qavatlik)
async def umumiymaydon(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data({
        "qavatlik": text
    })

    await bot.send_message(chat_id=message.chat.id, text=remontyoz, parse_mode="HTML", 
                           reply_markup=remontButton)
    await state.set_state(JizzaxHomeSotish.remont)


# ====================================================================
@jizzax_kv_router.callback_query(YevroremontData.filter(F.word=="yevroremont"), JizzaxHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YevroremontData):
    text = "Евроремонт"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton)
    await state.set_state(JizzaxHomeSotish.jihozlar)


@jizzax_kv_router.callback_query(TamirlangantData.filter(F.word=="tamirlangan"), JizzaxHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirlangantData):
    text = "Таъмирланган"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton)
    await state.set_state(JizzaxHomeSotish.jihozlar)


@jizzax_kv_router.callback_query(OrtachaData.filter(F.word=="ortacha"), JizzaxHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: OrtachaData):
    text = "Ўртача"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton)
    await state.set_state(JizzaxHomeSotish.jihozlar)


@jizzax_kv_router.callback_query(TamirsizData.filter(F.word=="tamirsiz"), JizzaxHomeSotish.remont)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: TamirsizData):
    text = "Таъмирсиз"
    await callback_query.answer("Pressed")
    await state.update_data({
        "remont": text
    })


    await bot.send_message(chat_id=callback_query.message.chat.id, text=jihozlaryoz,
                           reply_markup=jihozlarButton)
    await state.set_state(JizzaxHomeSotish.jihozlar)


# ===============================================================
@jizzax_kv_router.callback_query(MavjudData.filter(F.word=="mavjud"), JizzaxHomeSotish.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: MavjudData):
    text = "бор"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq)
    await state.set_state(JizzaxHomeSotish.gaz)


@jizzax_kv_router.callback_query(JihozlarsizData.filter(F.word=="jihozlarsiz"), JizzaxHomeSotish.jihozlar)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: JihozlarsizData):
    text = "йўқ"
    await callback_query.answer("Pressed")
    await state.update_data({
        "jihozlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=gazyoz, reply_markup=borYoq)
    await state.set_state(JizzaxHomeSotish.gaz)


# ================================================================

@jizzax_kv_router.callback_query(BorData.filter(F.word=="bor"), JizzaxHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(JizzaxHomeSotish.svet)


@jizzax_kv_router.callback_query(YoqData.filter(F.word=="yoq"), JizzaxHomeSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(JizzaxHomeSotish.svet)

# ========================================================================
    
@jizzax_kv_router.callback_query(BorData.filter(F.word=="bor"), JizzaxHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Свет ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(JizzaxHomeSotish.suv)


@jizzax_kv_router.callback_query(YoqData.filter(F.word=="yoq"), JizzaxHomeSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(JizzaxHomeSotish.suv)

# ============================================================================

@jizzax_kv_router.callback_query(BorData.filter(F.word=="bor"), JizzaxHomeSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Сув  ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(JizzaxHomeSotish.qoshimchaMalumot)
    else:
        await state.set_state(JizzaxHomeSotish.qoshimchaMalumot)


@jizzax_kv_router.callback_query(YoqData.filter(F.word=="yoq"), JizzaxHomeSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(JizzaxHomeSotish.qoshimchaMalumot)
    else:
        await state.set_state(JizzaxHomeSotish.qoshimchaMalumot)

# ==============================================================

@jizzax_kv_router.message(JizzaxHomeSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=valyutayoz, reply_markup=valyutaButton)

    await state.set_state(JizzaxHomeSotish.valyuta)


# =================================================================

@jizzax_kv_router.callback_query(USDData.filter(F.word=="usd"), JizzaxHomeSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz)

    await state.set_state(JizzaxHomeSotish.narxi)


@jizzax_kv_router.callback_query(SUMData.filter(F.word=="sum"), JizzaxHomeSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz)

    await state.set_state(JizzaxHomeSotish.narxi)


# ===============================================================

@jizzax_kv_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    JizzaxHomeSotish.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@jizzax_kv_router.message(JizzaxHomeSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz)

    await state.set_state(JizzaxHomeSotish.manzil)


@jizzax_kv_router.message(JizzaxHomeSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz)

    await state.set_state(JizzaxHomeSotish.moljal)


@jizzax_kv_router.message(JizzaxHomeSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz)

    await state.set_state(JizzaxHomeSotish.telNumberOne)


@jizzax_kv_router.message(JizzaxHomeSotish.telNumberOne)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    telNumber = message.text

    await state.update_data({
        "telNumberOne": telNumber
    })

    await message.answer(text=telraqam2yoz, reply_markup=otkazishButton)
    if message.text == "⏭️ Кейингиси":
        await state.update_data({
            "telNumberTwo": ""
        })
        await state.set_state(JizzaxHomeSotish.telNumberTwo)
    else:
        await state.set_state(JizzaxHomeSotish.telNumberTwo)


@jizzax_kv_router.message(JizzaxHomeSotish.telNumberTwo)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    # media_group = types.MediaGroup()

    data = await state.get_data()

    photos = data['images']

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        # media_group.attach_photo(photos[0], caption=cyrillic_text)

        # for file_id in photos[1:]:
        #     media_group.attach_photo(f"{file_id}")

        # await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(JizzaxHomeSotish.check)
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        # media_group.attach_photo(photos[0], caption=cyrillic_text)

        # for file_id in photos[1:]:
        #     media_group.attach_photo(f"{file_id}")

        # await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(JizzaxHomeSotish.check)

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n"
        data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        # media_group.attach_photo(photos[0], caption=cyrillic_text)

        # for file_id in photos[1:]:
        #     media_group.attach_photo(f"{file_id}")

        # await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(JizzaxHomeSotish.check)

    else:
        data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
        data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
        data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
        data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
        data7 = "🔶 Ремонти: " + data['remont'] + "\n"
        data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
        data9 = "🔶 "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        data10 = "бор \n"
        data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        # media_group.attach_photo(photos[0], caption=cyrillic_text)

        # for file_id in photos[1:]:
        #     media_group.attach_photo(f"{file_id}")

        # await bot.send_media_group(chat_id=chat_id, media=media_group)
        await bot.send_message(chat_id=chat_id, text=cyrillic_text)
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(JizzaxHomeSotish.check)


@jizzax_kv_router.message(JizzaxHomeSotish.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    # media_group = types.MediaGroup()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        # photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            # media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            # for file_id in photos[1:]:
            #     media_group.attach_photo(f"{file_id}")

            # await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            # media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            # for file_id in photos[1:]:
            #     media_group.attach_photo(f"{file_id}")

            # await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n"
            data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            # media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            # for file_id in photos[1:]:
            #     media_group.attach_photo(f"{file_id}")

            # await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()
        else:
            data3 = "🔶 Умумий майдон: " + data['umumiyMaydon'] + "m²" + "\n"
            data4 = "🔶 Хоналар сони: " + data['xonalar'] + " та" + "\n"
            data5 = "🔶 Қавати: " + data['qavat'] + "-қават" + "\n"
            data6 = "🔶 Неча қаватли: " + data['qavatlik'] + "-қаватли" + "\n"
            data7 = "🔶 Ремонти: " + data['remont'] + "\n"
            data8 = "🔶 Жиҳозлари: " + data['jihozlar'] + "\n"
            data9 = "🔶 "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            data10 = "бор \n"
            data11 = "🔶 Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💵 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [jizzaxregion, data2, data3, data4, data5, data6, data7, data8, data9, gaz, svet, suv, data10,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            # media_group.attach_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            # for file_id in photos[1:]:
            #     media_group.attach_photo(f"{file_id}")

            # await bot.send_media_group(chat_id=channel_id, media=media_group)
            await bot.send_message(chat_id=channel_id, text=cyrillic_text)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=start)
        await state.clear()