import requests
import os
# import senhas
import logging
import time

logging.basicConfig(
    filename='log.log', 
    encoding='utf-8', 
    level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s'
)
logging.info(50*'*' + '\nIniciando script telegram.')

if __name__ == '__main__':

    try:
        chat_id = os.environ['CHAT_ID']
    except:
        chat_id = None
        logging.warning('CHAT_ID não existe nas variávies de ambiente.')

    try:
        bot_token = os.environ['BOT_TOKEN']
    except:
        bot_token = None
        logging.warning('BOT_TOKEN não existe nas variávies de ambiente.')
    
    if (not(chat_id) and not(bot_token)):
        logging.error('Não foi possível executar script por não possuir as variáveis de ambiente.')
    else:
        texto = f'Mensagem enviada do python com o seguinte numero: {str(time.time()).replace(".","")}'
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={texto}'
        resposta = requests.get(url)
        logging.info(resposta.json())