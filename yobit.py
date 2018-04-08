import requests





def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = (response['ticker']['avg'])
    return str(price)   +  '  USD'

def get_eth():
    url = 'https://yobit.net/api/2/eth_usd/ticker'
    response = requests.get(url).json()
    price = (response['ticker']['avg'])
    return str(price)   +  '  USD'



def get_ltc():
    url = 'https://yobit.net/api/2/ltc_usd/ticker'
    response = requests.get(url).json()
    price = (response['ticker']['avg'])
    return str(price)   +  '  USD'

def get_etc():
    url = 'https://yobit.net/api/2/etc_usd/ticker'
    response = requests.get(url).json()
    price = (response['ticker']['avg'])
    return str(price)   +  '  USD'


def get_dash():
    url = 'https://yobit.net/api/2/dash_usd/ticker'
    response = requests.get(url).json()
    price = (response['ticker']['avg'])
    return str(price)   +  '  USD'









