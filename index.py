# _*_ coding:utf-8 _*_


from wxpy import *
import config
bot = Bot(console_qr=2)
tuling = Tuling(api_key= config.CONFIG['tuling_api_key'])

# my_friend = ensure_one(bot.friends().search('大华'))

@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at == True:
        tuling.do_reply(msg, True)

@bot.register(bot.friends())
def reply_my_friend(msg):
    tuling.do_reply(msg)
embed()
