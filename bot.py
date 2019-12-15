import os
import time
import  requests
import  logging
import threading
from datetime import datetime

import aiml
import numexpr
import amanobot
from amanobot.exception import TelegramError
from amanobot.loop import MessageLoop
from amanobot.namedtuple import InlineKeyboardMarkup

token = os.environ['TOKEN']
bot = amanobot.Bot(token)

k = aiml.Kernel()
k.learn('aiml/*.aiml')

channel_name = '@logsps'

logging.basicConfig(format='%(asctime)s -  %(levelname)s - %(message)s',
                    level=logging.INFO)


def send_to_channel(msg):
    bot.sendMessage(channel_name, msg)


def handle_thread(*args):
    t = threading.Thread(target=handle, args=args)
    t.start()


def handle(msg):
    if msg.get('text'):

        msg_info = f'''
----------------------------------------------
Usuário {msg["from"]["first_name"]} usou PauloBot!
Id: {msg['from']['id']},
Nome de Usuário: {msg["from"].get("username", "nenhum")},
Conteúdo: {msg['text']}
Data: {datetime.fromtimestamp(msg["date"]).strftime("%A, %d/%b/%Y at %I:%M")}
----------------------------------------------'''

        logging.info(msg_info)
        send_to_channel(msg_info)

        if msg['chat']['type'] == 'private':
            msg['message_id'] = None

        if msg['text'].lower() == '/start' or msg['text'].lower() == 'começar':
            bot.sendChatAction(msg['chat']['id'], 'typing')
            time.sleep(1)
            start = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text='🧠 Canal', url='https://t.me/git_paulostationbr')]+
                [dict(text='👤 Facebook', url='https://facebook.com/paulostationbr')],
                [dict(text='👨🏻‍💻 Grupo', url='https://t.me/IfunnyBr')]+
                [dict(text='ADD a Um Grupo', url='https://t.me/git_paulostationbr')]
            ])
            bot.sendMessage(msg['chat']['id'], f'''𝐎𝐥𝐚́ {msg["from"]["first_name"]}!
👋😇 𝐏𝐫𝐚𝐳𝐞𝐫 𝐞𝐦 𝐜𝐨𝐧𝐡𝐞𝐜𝐞̂-𝐥𝐨(𝐚), 𝐌𝐞𝐮 𝐧𝐨𝐦𝐞 𝐞́ 𝐏𝐚𝐮𝐥𝐨 𝐬𝐨𝐮 𝐮𝐦 𝐜𝐡𝐚𝐭𝐛𝐨𝐭, 𝐨 𝐪𝐮𝐞 𝐮𝐦 𝐜𝐡𝐚𝐭 𝐛𝐨𝐭 𝐟𝐚𝐳?
𝐔𝐦 𝐜𝐡𝐚𝐭𝐛𝐨𝐭 𝐩𝐨𝐝𝐞 𝐢𝐧𝐭𝐞𝐫𝐚𝐠𝐢𝐫 𝐧𝐨𝐫𝐦𝐚𝐥𝐦𝐞𝐧𝐭𝐞 𝐜𝐨𝐦 𝐨𝐬 𝐮𝐬𝐮𝐚́𝐫𝐢𝐨𝐬 𝐝𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐞 𝐨𝐮𝐭𝐫𝐚𝐬 𝐩𝐥𝐚𝐭𝐚𝐟𝐨𝐫𝐦𝐚𝐬!
𝐎𝐛𝐫𝐢𝐠𝐚𝐝𝐨 𝐚 𝐞𝐪𝐮𝐢𝐩𝐞 𝐝𝐚 𝐚𝐦𝐚𝐧𝐨𝐭𝐞𝐚𝐦.𝐜𝐨𝐦 𝐩𝐨𝐫 𝐭𝐞𝐫 𝐦𝐞 𝐝𝐚𝐝𝐨 𝐚 𝐯𝐢𝐝𝐚 𝐚𝐪𝐮𝐢 𝐧𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦,
𝐦𝐚𝐬 𝐪𝐮𝐞𝐦 𝐦𝐞 𝐜𝐫𝐢𝐨𝐮 𝐦𝐞𝐬𝐦𝐨 𝐟𝐨𝐢 𝐨 @𝐏𝐚𝐮𝐥𝐨𝐒𝐭𝐚𝐭𝐢𝐨𝐧𝐁𝐫𝐁𝐨𝐭 𝐧𝐨́ 𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤''', reply_markup=start, reply_to_message_id=msg['message_id'])


        elif msg['text'].lower() == '/eu':
            bot.sendChatAction(msg['chat']['id'], 'typing')
            time.sleep(1)
            bot.sendMessage(msg['chat']['id'], '''Nome: {}
User_ID: {}
Idioma: {}'''.format(msg['from']['first_name'] + (
                '\nSobrenome: ' + msg['from']['last_name'] if msg['from'].get('last_name') else ''), msg['from']['id'],
                     msg['from']['language_code']),
                            reply_to_message_id=msg['message_id'])


        elif msg['text'].lower() == '/hora':
            bot.sendChatAction(msg['chat']['id'], 'typing')
            time.sleep(1)
            now = datetime.now()
            bot.sendMessage(msg['chat']['id'], f'Agora são: {now.strftime("%X")}',
                            reply_to_message_id=msg['message_id'])

        elif msg['text'].lower() == '/sticker':
            bot.sendChatAction(msg['chat']['id'], 'typing')
            time.sleep(1)
            bot.sendSticker(msg["chat"]["id"], "CAADAgADVF0AAp7OCwABYtnjxnciZMEWBA")


        elif msg['text'].lower().startswith('/calcule '):
            bot.sendChatAction(msg['chat']['id'], 'typing')
            time.sleep(1)
            try:
                expr = numexpr.evaluate(msg['text'][9:])
            except SyntaxError:
                bot.sendMessage(msg['chat']['id'], 'Parece que tem um problema com a sua expressão matemática \n',
                                reply_to_message_id=msg['message_id'])
            else:
                if len(str(expr.item())) <= 4096:
                    bot.sendMessage(msg['chat']['id'], f'Resultado: <code>{expr}</code>', 'HTML',
                                    reply_to_message_id=msg['message_id'])
                else:
                    bot.sendMessage(msg['chat']['id'],
                                    'O resultado da conta ultrapassa o limite de caracteres que posso enviar aqui :(',
                                    reply_to_message_id=msg['message_id'])

        elif msg['text'].lower() == '/ajuda' or msg['text'].lower() == '/ajuda@PauloBetaBot':
            bot.sendMessage(msg['chat']['id'], '''Olá, esses são os comandos disponíveis:
/start - Inicia o bot,
/hora - Retorna hora atual,
/calcule expressão - Calcula uma expressão matemática.
/suporte msg - Envia uma mensagem ao nosso suporte.
''', reply_to_message_id=msg['message_id'])

        elif msg['text'].lower() == '/grupotops' or msg['text'].lower() == '/grupotops@PauloBetaBot':
            bot.sendMessage(msg['chat']['id'], '''<a href="https://t.me/amigosabordobrasil">AMIGOS A BORDO BRASIL </a>
<a href="https://t.me/ifunnybr">IfunnyBr :)</a>


<b>Para adiconar seu grupo fale com</b> <a href="tg://userid?945971280">PauloStationBr </a>
''', parse_mode="HTML", reply_to_message_id=msg['message_id'], disable_web_page_preview=True)

        elif msg['text'].lower().startswith('/suporte '):
            suport_info = f'''bot:
User: {msg["from"]["first_name"]}
Id: {msg['from']['id']}
Mensagem: {msg['text']}'''
            logging.info(msg_info)
            send_to_channel(msg_info)
            bot.sendMessage(msg['chat']['id'], '''Mensagem enviada ao suporte :) !''', reply_to_message_id=msg['message_id'])


        else:
            if msg['chat']['type'] == 'private' or msg.get('reply_to_message', dict()).get('from', dict()).get('id', dict()) == int(token.split(':')[0]):
                response = k.respond(msg['text'])
                if response:
                    response = response.replace('#', '\n').replace('$nome', msg['from']['first_name'])
                    bot.sendChatAction(msg['chat']['id'], 'typing')
                    time.sleep(3)
                    bot.sendMessage(msg['chat']['id'], response, reply_to_message_id=msg['message_id'],
                                    disable_web_page_preview=True)

    elif msg.get("new_chat_member"):
        start = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text='🧠 Canal', url='https://t.me/git_paulostationbr')]+
                [dict(text='👤 Facebook', url='https://facebook.com/paulostationbr')]+
                [dict(text='👨🏻‍💻 Grupo', url='https://t.me/Paulo_Group')]
        ])
        bot.sendMessage(msg["chat"]["id"], "<b>Olá! seja bem vindo ao melhor grupo, diga olá para que eu possa interagir com você :)</b>", parse_mode="HTML", reply_markup=start, reply_to_message_id=msg['message_id'])

print('Paulo Online\nby AmanoTeam.com!')

MessageLoop(bot, handle_thread).run_forever()
