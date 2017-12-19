from kakaobot import KakaoBot, Message, Photo, MessageButton

bot = KakaoBot()

@bot.on_message
async def handle_message(message, **args):
    photo = Photo('http://t1.kakaocdn.net/kakaocorp/pw/kakao/ci_kakao.gif',
        width=320, height=320)
    button = MessageButton('Click it!', url='http://example.com')

    if args['type'] == 'text':
        if message == 'Text':
            return 'This is a text message'
        elif message == 'Photo':
            return Message('This is a message with a photo', photo=photo)
        elif message == 'Button':
            return Message('This is a message with a button', button=button)
        elif message == 'Altogether':
            return Message('Here are you', photo=photo, button=button)
        else:
            return 'What are you saying?'
    else:
        return 'I can understand only text messages'

if __name__ == '__main__':
    bot.run(host='0.0.0.0', port=8080)
