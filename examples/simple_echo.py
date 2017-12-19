from kakaobot import KakaoBot

bot = KakaoBot()

@bot.on_message
async def handle_message(message, **args):
    if args['type'] == 'text':
        return 'Echoing: %s' % message
    else:
        return 'Cannot understand'

if __name__ == '__main__':
    bot.run(host='0.0.0.0', port=8080)
