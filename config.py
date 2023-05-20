BOT_TOKEN = '5999451135:AAGAlBSdghuU45YZJr1NoHzkDjTurievm_M'
TOKEN = "5999451135:AAGAlBSdghuU45YZJr1NoHzkDjTurievm_M"

API_TOKEN = "5691041366:AAEqoonM9RxkJd0hEqX_NCXZ9WRWEzVoMUE"

WEATHER_API = '4fe671035ef5e6e022ec583b2f079f16'

TOKEN_KINO = "8Z6AZVK-MZCMTNB-JZBJ4MB-ZWVRZRD"
ADMINS = "1120233842"
url = 'https://api.kinopoisk.dev/'

PROVIDER_TOKEN = "1744374395:TEST:61e812a105321b23072b"

from contextlib import suppress  # Импорт функции suppress из модуля contextlib - позволяет игнорировать выбрасываемые исключения
from aiogram.utils.callback_data import CallbackData  # Импорт класса CallbackData из модуля aiogram.utils.callback_data - для создания callback_data для inline-клавиатур
from aiogram.utils.exceptions import MessageNotModified  # Импорт исключения MessageNotModified из модуля aiogram.utils.exceptions - возникает при повторной попытке изменить уже измененное сообщение
from aiogram import Bot, Dispatcher, executor, types  # Импорт классов Bot, Dispatcher, executor и types из модуля aiogram - необходимы для работы с Telegram API
import aiogram.utils.markdown as fmt  # Импорт модуля aiogram.utils.markdown с псевдонимом fmt - для форматирования текста
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text, Command  # Импорт фильтров CommandHelp, CommandStart, Text и Command из модуля aiogram.dispatcher.filters - используются для фильтрации сообщений
from aiogram.types import BotCommandScopeDefault, BotCommand, BotCommandScopeChat, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton # Импорт классов и констант из модуля aiogram.types - используются для создания объектов Telegram API
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters, FSMContext  # Импорт фильтров и FSMContext из модуля aiogram.dispatcher - необходимы для реализации Finite State Machine
import logging  # Импорт модуля logging - для ведения логирования
import os  # Импорт модуля os - для работы с операционной системой
import random  # Импорт модуля random - для генерации случайных чисел
import re  # Импорт модуля re - для работы с регулярными выражениями
from keyboards import *  # Импорт всех клавиатур из модуля keyboards
import json  # Импорт модуля json - для работы с JSON-файлами
from aiogram import types  # Импорт класса types из модуля aiogram - необходим для работы с Telegram API
from aiogram.types import ReplyKeyboardRemove  # Импорт класса ReplyKeyboardRemove из модуля aiogram.types - для удаления клавиатуры у пользователя
from aiogram.dispatcher.filters import Command  # Импорт фильтра Command из модуля aiogram.dispatcher.filters - используется для фильтрации команд
from aiogram.dispatcher import FSMContext  # Импорт класса FSMContext из модуля aiogram.dispatcher - для реализации Finite State Machine
from aiogram.dispatcher.filters.state import State, StatesGroup  # Импорт классов State и StatesGroup из модуля aiogram.dispatcher.filters.state - для реализации Finite State Machine
