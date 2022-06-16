import requests

SENDER = 'Me'
END_MESSAGE = 'bye'

def send_message(sender, message):
    return requests.post('http://127.0.0.1:5002/webhooks/rest/webhook', json={'sender': sender, 'message': message})

def print_bot_reply(req_reply):
    should_quit = False
    
    print('Bot > ', end='')
    for i in req_reply.json():
        bot_message = i['text']
        print(bot_message)
        if bot_message.lower() == END_MESSAGE:
            should_quit = True
            
    return should_quit

def start_session_get_welcome_message():
    r = send_message(SENDER, '/session_start')
    print_bot_reply(r)

def main():
    start_session_get_welcome_message()

    while True:
        message = input('Me > ')
        r = send_message(SENDER, message)
        should_quit = print_bot_reply(r)
        
        if should_quit:
            break

if __name__ == '__main__':
    main()