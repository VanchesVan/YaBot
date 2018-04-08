# -*- coding: utf-8 -*-

import requests
import misc
from yobit import get_btc,get_dash,get_etc,get_ltc,get_eth
from time import sleep

token = misc.token

#  https://api.telegram.org/bot497084918:AAEPU7SohOv9NVKwbyJ813bYQ8IIZcTbtiU/sendmessage?chat_id=375030437&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0



def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()




def get_message():





    data = get_updates()

    last_object = data ['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id

    if last_update_id != current_update_id :
        last_update_id = current_update_id


        chat_id = last_object['message' ]['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                       'text': message_text}

        return  message
    return None

def send_message(chat_id, text='Подождите секундочку .....'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    # d = get_updates()

    while True :

        answer = get_message()

        if answer != None :
            chat_id = answer['chat_id']
            text = answer['text']


            if  text == '/btc' :
                send_message(chat_id, get_btc())

            if  text == '/eth' :
                send_message(chat_id, get_eth())

            if  text == '/ltc' :
                send_message(chat_id, get_ltc())

            if  text == '/etc' :
                send_message(chat_id, get_etc())

            if  text == '/dash' :
                send_message(chat_id, get_dash())

            if text == '/reminder' :
                send_message(chat_id, '1. Лучше начать с небольшой суммы.'
                                      '2. Помните о высоких комиссиях при переводе'
                                      '3. Чтобы перевести биткойн из кошелька в кошелек нужно время и немалое'
                                      '4. Не стоит держать деньги в кошельке на биржe'
                                      '5. Обратите внимание на другие валюты'
                                      '6. Чтобы купить альткоины, запаситесь биткойнами'
                                      '7.Транзакция - процесс не подлежащий оспариванию')

            if text == '/bubble':
                send_message(chat_id, 'Четыре причины, почему биткоин — не мыльный пузырь:                              '
                
                
                                      '1. Децентрализация.  Сила биткоина — децентрализация. Биткоин не принадлежит какой-либо централизованной банковской системе, поэтому стабилен.'
                                      '2. Поставка.  Поставка биткоина ограничена. Добыча биткоина становится сложнее, а ценность монеты будет расти.'
                                      '3. Безопасность.  Децентрализация и шифрование означают, что биткоин безопасен.'
                                      '4. Доказательство мошенничества.  Поскольку все транзакции записываются, возможность мошенничества минимальна и сразу отслеживается.')

            if text == '/end' :
               send_message(chat_id, 'В 2140 году будет добыт последний Биткоин')

            if text == '/father' :
               send_message(chat_id, 'Мой создатель это Иван Бонич , если я что-то делаю не так , не ругайтесь на него сильно , пожалуйста!')

            if text == '/btcfather' :
               send_message(chat_id, 'Сатоши Накамото — псевдоним создателя Биткоин. Весь мир теряется в загадках о его настоящейличности. Сатоши создал Биткоин в 2008-ом году. й первый миллион биткоинов был добыт лично Сатоши и, по всей видимости, до сих пор ему принадлежит. Исследователи до сих пор предпринимают попытки обнаружить кошельки Накамото, чтобы выйти на его след, но Сатоши сохраняет спокойствие')

            if text == '/language' :
                send_message(chat_id, 'Платежная система  Bitcoin Написана на C++')



        else:
            continue 


if __name__ == '__main__' :
    main( )
