from typing import List

from aiogram import types, F, Router

from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types.callback_query import CallbackQuery

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, documentButton, valyutaButton, borYoq
from loader import bot
from states.YerSotish.NamanganState import NamanganYerSotish

from transliterate import to_cyrillic

from utils.QuestionYer.yerqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, namangan_id, check_text, namanganregion, data2, data32, data33, \
    data34, data35, success_text, hujjatlaribormiyoz


from keyboards.inline.data import NamanganYerData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import DocumentHaveData, DocumentNotData
from keyboards.inline.data import USDData, SUMData


mode = "Markdown"

from aiogram_media_group import media_group_handler

from aiogram.utils.media_group import MediaGroupBuilder


namangan_yer_router = Router()

@namangan_yer_router.callback_query(NamanganYerData.filter(F.word=="namanganyer"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: NamanganYerData):
    await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(NamanganYerSotish.images)


@namangan_yer_router.message(NamanganYerSotish.images, F.media_group_id, F.content_type.in_({'photo'}))
@media_group_handler
async def album_handler(messages: List[types.Message], state: FSMContext):
    file_ids = []

    for message in messages:
        photos = message.photo

        first_photo_size = photos[0]
        first_file_id = first_photo_size.file_id

        file_ids.append(first_file_id)

    await state.update_data({
        "images": file_ids
    })

    await messages[-1].answer(umumiyMaydonyoz, parse_mode="HTML")
    await state.set_state(NamanganYerSotish.umumiyMaydon)


@namangan_yer_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    NamanganYerSotish.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@namangan_yer_router.message(NamanganYerSotish.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(NamanganYerSotish.gaz)


# ================================================================

@namangan_yer_router.callback_query(BorData.filter(F.word=="bor"), NamanganYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(NamanganYerSotish.svet)


@namangan_yer_router.callback_query(YoqData.filter(F.word=="yoq"), NamanganYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(NamanganYerSotish.svet)

# ========================================================================
    
@namangan_yer_router.callback_query(BorData.filter(F.word=="bor"), NamanganYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Свет ✔️"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(NamanganYerSotish.suv)


@namangan_yer_router.callback_query(YoqData.filter(F.word=="yoq"), NamanganYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(NamanganYerSotish.suv)

# ============================================================================

@namangan_yer_router.callback_query(BorData.filter(F.word=="bor"), NamanganYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Сув ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq)

    await state.set_state(NamanganYerSotish.kanal)


@namangan_yer_router.callback_query(YoqData.filter(F.word=="yoq"), NamanganYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq)

    await state.set_state(NamanganYerSotish.kanal)

# ============================================================================

@namangan_yer_router.callback_query(BorData.filter(F.word=="bor"), NamanganYerSotish.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Канализация  ✔️"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(NamanganYerSotish.qoshimchaMalumot)
    else:
        await state.set_state(NamanganYerSotish.qoshimchaMalumot)


@namangan_yer_router.callback_query(YoqData.filter(F.word=="yoq"), NamanganYerSotish.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton)

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(NamanganYerSotish.qoshimchaMalumot)
    else:
        await state.set_state(NamanganYerSotish.qoshimchaMalumot)

# ==============================================================

@namangan_yer_router.message(NamanganYerSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=hujjatlaribormiyoz, reply_markup=documentButton)

    await state.set_state(NamanganYerSotish.hujjatlar)


# =================================================================
    
@namangan_yer_router.callback_query(DocumentHaveData.filter(F.word=="dokumentbor"), NamanganYerSotish.hujjatlar)
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = " Бор,  қонуний"
    await callback_query.answer("Dokument bor")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=valyutayoz,
                           reply_markup=valyutaButton)

    await state.set_state(NamanganYerSotish.valyuta)


@namangan_yer_router.callback_query(DocumentNotData.filter(F.word=="dokumentyoq"), NamanganYerSotish.hujjatlar)
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = " Тайёр эмас"
    await callback_query.answer("Dokument Yo'q")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=valyutayoz,
                           reply_markup=valyutaButton)

    await state.set_state(NamanganYerSotish.valyuta)    

# =================================================================
    

@namangan_yer_router.callback_query(USDData.filter(F.word=="usd"), NamanganYerSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz)

    await state.set_state(NamanganYerSotish.narxi)


@namangan_yer_router.callback_query(SUMData.filter(F.word=="sum"), NamanganYerSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz)

    await state.set_state(NamanganYerSotish.narxi)


# ===============================================================

@namangan_yer_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    NamanganYerSotish.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@namangan_yer_router.message(NamanganYerSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz)

    await state.set_state(NamanganYerSotish.manzil)


@namangan_yer_router.message(NamanganYerSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz)

    await state.set_state(NamanganYerSotish.moljal)


@namangan_yer_router.message(NamanganYerSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz)

    await state.set_state(NamanganYerSotish.telNumberOne)


@namangan_yer_router.message(NamanganYerSotish.telNumberOne)
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
        await state.set_state(NamanganYerSotish.telNumberTwo)
    else:
        await state.set_state(NamanganYerSotish.telNumberTwo)


@namangan_yer_router.message(NamanganYerSotish.telNumberTwo)
async def telNumbertwo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = MediaGroupBuilder()

    data = await state.get_data()

    photos = data['images']

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(NamanganYerSotish.check)
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(NamanganYerSotish.check)

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(NamanganYerSotish.check)

    else:
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = "бор \n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = " ".join(array)
        cyrillic_text = to_cyrillic(stringify)

        media_group.add_photo(photos[0], caption=cyrillic_text)

        for file_id in photos[1:]:
            media_group.add_photo(f"{file_id}")

        await bot.send_media_group(chat_id=chat_id, media=media_group.build())
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn)
        await state.set_state(NamanganYerSotish.check)


@namangan_yer_router.message(NamanganYerSotish.check)
async def check(message: types.Message, state: FSMContext):
    mycheck = message.text
    chat_id = message.chat.id

    media_group = MediaGroupBuilder()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            await bot.send_media_group(chat_id=namangan_id, media=media_group.build())
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            await bot.send_media_group(chat_id=namangan_id, media=media_group.build())
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            await bot.send_media_group(chat_id=namangan_id, media=media_group.build())
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()
        else:
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = "бор \n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал:  " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [namanganregion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = " ".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            media_group.add_photo(photos[0], caption=cyrillic_text, parse_mode="HTML")

            for file_id in photos[1:]:
                media_group.add_photo(f"{file_id}")

            await bot.send_media_group(chat_id=namangan_id, media=media_group.build())
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start)
            await state.clear()

    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="❌ Эълон қабул қилинмади")
        await bot.send_message(chat_id=chat_id, text="Еълон бериш учун қайтадан уриниб кўринг", reply_markup=start)
        await state.clear()
