
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))

inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')

inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)

inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Яндекс', url='https://www.yandex.ru'))

#42 урок
def get_simple_kb():
   kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
   btn1 = KeyboardButton(text='1')
   btn2 = KeyboardButton(text='2')
   kb.add(btn1)
   kb.add(btn2)
   return kb


def get_simple_kb1():
   kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
       KeyboardButton('Вы перешли с кнопки 1')).add(KeyboardButton('Закрыть'))
   return kb