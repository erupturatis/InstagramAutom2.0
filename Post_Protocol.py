from instabot import Bot
from Vars import usernames,passwords
from Vars import HostPages as Hp
import os


bot = Bot()

def Post(caption="Rate this 1-10",credit="Credit unkown dm me",hashtags="#", image="", batch=0 , nr=0):

    global bot
    image = 'Posts/post'+str(batch)+'.jpg'
    credit= "\n Reposted from:" + Hp[batch][nr]
    hashtags = "#"+usernames[batch][nr] + " " + hashtags
    bot.login(username=usernames[batch][nr], password=passwords[batch][nr], is_threaded=True )
    standardSpace="\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n"
    bot.upload_photo(image, caption=caption+standardSpace+credit+standardSpace+hashtags)
    os.remove('Posts/post'+str(batch)+'.jpg.REMOVE_ME')
    bot.logout()


