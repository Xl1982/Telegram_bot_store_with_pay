BOT_TOKEN = '5999451135:AAGAlBSdghuU45YZJr1NoHzkDjTurievm_M'
TOKEN = "5999451135:AAGAlBSdghuU45YZJr1NoHzkDjTurievm_M"

API_TOKEN = "5691041366:AAEqoonM9RxkJd0hEqX_NCXZ9WRWEzVoMUE"

WEATHER_API = '4fe671035ef5e6e022ec583b2f079f16'

TOKEN_KINO = "8Z6AZVK-MZCMTNB-JZBJ4MB-ZWVRZRD"
ADMINS = "1120233842"
url = 'https://api.kinopoisk.dev/'

PROVIDER_TOKEN = "1744374395:TEST:61e812a105321b23072b"

from contextlib import suppress  # ������ ������� suppress �� ������ contextlib - ��������� ������������ ������������� ����������
from aiogram.utils.callback_data import CallbackData  # ������ ������ CallbackData �� ������ aiogram.utils.callback_data - ��� �������� callback_data ��� inline-���������
from aiogram.utils.exceptions import MessageNotModified  # ������ ���������� MessageNotModified �� ������ aiogram.utils.exceptions - ��������� ��� ��������� ������� �������� ��� ���������� ���������
from aiogram import Bot, Dispatcher, executor, types  # ������ ������� Bot, Dispatcher, executor � types �� ������ aiogram - ���������� ��� ������ � Telegram API
import aiogram.utils.markdown as fmt  # ������ ������ aiogram.utils.markdown � ����������� fmt - ��� �������������� ������
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text, Command  # ������ �������� CommandHelp, CommandStart, Text � Command �� ������ aiogram.dispatcher.filters - ������������ ��� ���������� ���������
from aiogram.types import BotCommandScopeDefault, BotCommand, BotCommandScopeChat, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton # ������ ������� � �������� �� ������ aiogram.types - ������������ ��� �������� �������� Telegram API
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters, FSMContext  # ������ �������� � FSMContext �� ������ aiogram.dispatcher - ���������� ��� ���������� Finite State Machine
import logging  # ������ ������ logging - ��� ������� �����������
import os  # ������ ������ os - ��� ������ � ������������ ��������
import random  # ������ ������ random - ��� ��������� ��������� �����
import re  # ������ ������ re - ��� ������ � ����������� �����������
from keyboards import *  # ������ ���� ��������� �� ������ keyboards
import json  # ������ ������ json - ��� ������ � JSON-�������
from aiogram import types  # ������ ������ types �� ������ aiogram - ��������� ��� ������ � Telegram API
from aiogram.types import ReplyKeyboardRemove  # ������ ������ ReplyKeyboardRemove �� ������ aiogram.types - ��� �������� ���������� � ������������
from aiogram.dispatcher.filters import Command  # ������ ������� Command �� ������ aiogram.dispatcher.filters - ������������ ��� ���������� ������
from aiogram.dispatcher import FSMContext  # ������ ������ FSMContext �� ������ aiogram.dispatcher - ��� ���������� Finite State Machine
from aiogram.dispatcher.filters.state import State, StatesGroup  # ������ ������� State � StatesGroup �� ������ aiogram.dispatcher.filters.state - ��� ���������� Finite State Machine
