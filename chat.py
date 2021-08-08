import json
file = open('info.json', 'r')
info = json.load(file)
from linebot import LineBotApi
from linebot.models import TextSendMessage
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
def main():
    user_id = info['USER_ID']
    message = TextSendMessage(text='ふぇ～ん、漏れちゃったよ、、\n 気持ち悪いョ～(泣)')
    line_bot_api.push_message(user_id, messages = message)

if __name__ == "__main__":
    main()