from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**สแดส, I'm {bn} ๐ต 
        แ แชแท แชแ แแชฮแแฌแ  แทแฎีแแ แขแแชแฝแฌแก แดฯดอฒ แกแฎฮ ฯดฮ ฯดแฮ ีแฌแกแแฌแก! แทฯดแกแฌ าแชีอฒแฌแก , ฮฯด แแ , แชแแ าแกแฌแฌ แชฮแ  แฮแแแฎแ แฌแ  แทฯดแกแฌ แฯดแทแทแชฮแ ี แฮ แอฒ.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ๐ฐ๐๐ ๐ผ๐ ๐๐ ๐ถ๐๐๐๐ ", url="https://t.me/CrystalMusicRobot?startgroup=new")
                  ],[
                    InlineKeyboardButton(
                        "๐ฌ ๐ฒ๐๐๐๐๐๐ ", url="https://t.me/crystalbots"
                    ),
                    InlineKeyboardButton(
                        "๐ฅ ๐ถ๐๐๐๐", url="https://t.me/Chatting_officials"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " Term & Condition ", url="https://t.me/crystalbots/14"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**๐ท๐๐๐๐ ๐ ๐๐ ๐๐๐๐๐ข!  ๐๐๐๐๐๐๐๐๐๐๐๐ข ๐๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel ", url="https://t.me/crystalbots")
                ]
            ]
        )
   )


