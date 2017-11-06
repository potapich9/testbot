import requests
import config
from time import sleep

token = config.token
URL = "https://api.telegram.org/bot"+ token+"/"
global last_update_id
last_update_id = 0

def get_updates():
	url = URL + "getupdates"
	params = {'timeout': 100, 'offset': None}
	r = requests.get(url,params)
	return r.json()

def main():	
	while True:
		sleep(3)
		answer = get_message()
		if answer!= None:
			chat_id = answer['chat_id']
			text = answer['text']
			if (text=='хуй'):
				send_message(chat_id,'привет2')



def get_message():
	data = get_updates()
	last_obj = data['result'][-1];
	curr_update_id = last_obj ['update_id']
	global last_update_id
	if (last_update_id!=curr_update_id): 
		last_update_id = curr_update_id
		chat_id = last_obj['message']['chat']['id']
		message_text = last_obj['message']['text']
		message = {'chat_id': chat_id,
					'text': message_text}
		return message
	return None

def send_message(chat_id, text='wait please..'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
	requests.get(url)


if __name__ == '__main__':
	main()

	
