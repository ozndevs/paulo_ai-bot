print('Iniciando o bot...')


import amanobot
from amanobot.loop import MessageLoop
import time
import aiml
import config


bot = amanobot.Bot(config.TOKEN)

k = aiml.Kernel()
k.learn('aiml/*.aiml')


def handle(msg):
	if msg.get('text'):
		response = k.respond(msg['text'])
		if response:
			response = response.replace('$nome', msg['from']['first_name']).replace('#', '\n')
			bot.sendChatAction(msg['chat']['id'], 'typing')
			time.sleep(1)
			bot.sendMessage(msg['chat']['id'], response)


MessageLoop(bot, handle).run_as_thread()

print('Bot iniciado!')

while True:
	time.sleep(10)