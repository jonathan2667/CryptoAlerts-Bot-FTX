import telebot
import yfinance as yf

import ccxt
import json
import datetime
import requests
from ftx import FtxClient
import pandas as pd

from keep_alive import keep_alive

from AlertsCrossDown import CrossDown
from AlertsCrossUp import CrossUp

API_KEY = '5419960375:AAGMY3WE_RCaSt8Z4UghgQ026CUqlT2hWVQ'
chat_id = '5503700037'


keep_alive()

def Down() :
  markets_to_del = []

  for market, price in CrossDown.items():
    market_name = market.capitalize() + "/USD"
    url = 'https://ftx.com/api'
    path = f'/markets/{market_name}'
    url = url + path
    
    res = requests.get(url).json()
    df = pd.DataFrame(res)['result']['price']
  
    if df < price:
      txt = f'{market_name} price is under: ' +  str(price) + "$\nCurrent price is: " + str(df) + "$"
      bot.send_message(chat_id, txt)
      markets_to_del.append(market)

  for market in markets_to_del:
    del CrossDown[market]
    print("TO ERASE : " + market + "\n\n")

def Up() :
  markets_to_del = []

  for market, price in CrossUp.items():
    market_name = market.capitalize() + "/USD"
    url = 'https://ftx.com/api'
    path = f'/markets/{market_name}'
    url = url + path
    
    res = requests.get(url).json()
    df = pd.DataFrame(res)['result']['price']
  
    if df > price:
      txt = f'{market_name} price is over: ' +  str(price) + "$\nCurrent price is: " + str(df) + "$"
      bot.send_message(chat_id, txt)
      markets_to_del.append(market)

  for market in markets_to_del:
    del CrossUp[market]
    print("TO ERASE : " + market + "\n\n")
    
while (1):
  bot = telebot.TeleBot(API_KEY)

  Down()
  Up()
  
keep_alive()



"""

keep_alive()

API_KEY = '5419960375:AAGMY3WE_RCaSt8Z4UghgQ026CUqlT2hWVQ'
bot = telebot.TeleBot(API_KEY)
chat_id = '5503700037'


@bot.message_handler(commands=['price'])
def greet(message):
  market_name = message.text.split()[1]+ "/USD"
  url = 'https://ftx.com/api'
  path = f'/markets/{market_name}'
  url = url + path
  
  res = requests.get(url).json()
  df = pd.DataFrame(res)['result']['price']

  txt = "The current price is: " + str(df) + "$"
  
  bot.send_message(message.chat.id, txt)
  
    
@bot.message_handler(commands=['alert'])
def send_price(message):
  market_name = message.text.split()[1]+ "/USD"
  symbol = message.text.split()[2] 
  price = float(message.text.split()[3])

  url = 'https://ftx.com/api'
  path = f'/markets/{market_name}'
  url = url + path
  
  res = requests.get(url).json()
  df = pd.DataFrame(res)['result']['price']

  txt = "⌛ I will send you a message when the price of: " + market_name + " reaches: " + str(price) + "$.\nThe current price is: " + str(df) + "$"
  
  bot.send_message(message.chat.id, txt)
  
  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  bot.send_message(message.chat.id, "22s")

  
bot.send_message(chat_id, "323244")
bot.polling()

"""
