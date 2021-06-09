class Translation(object):


#This will be appeared when anyone use start command

      START = """**Hello {0} !!!**

I Am A Converter Bot.I can convert file to video or video to file with custom thumbnail support.

__For More Details check Help 📜__
"""


#This will be appeared when anyone use help command

      HELP = """**Hey you need help 🤔 ?**

1. Send me the telegram file or video which you wanted to convert.

2. Send me the thumbnail(photo) optional.

3. Reply to video /convtofile for converting into file.

4. Reply to file /convtovideo for converting into video.
"""


#Please don't change this about command 🙏

      ABOUT = """
**Creator:** [Vivek](https://t.me/Vivektvp)
**Credits:** Dan for his awesome pyrogram library 🔥
**Library:** [Pyrogram 1.1.13](https://docs.pyrogram.org/)
**Updates:** [vk projects](https://t.me/VkProjects)
**Server:** [Heroku](https://heroku.com)

**NB:** EveryOne Can Use Me.So Don't Worry🤗

"""

####################################################################################################################################################
####################################################################################################################################################



#If you set the password for the bot if anyone use the bot without logging in this text will appear

      NOT_LOGGED_TEXT = """ This bot was a private bot you need to login using the password.
For logging in use command <code>/login BotPassword</code>. And then use me 🥰"""


#This will be sent to the user when the user logged successfully

      SUCESS_LOGIN = """You are successfully logged in. So you can use me for today.
You access will be revoke by tomorrow"""


# This will be show when an user send wrong password

      WRONG_PWD = """This is a wrong password 🔐 please try with correct password"""


# This will appear if the user is already logged

      EXISTING_USER = "You are already logged in you can use me"

####################################################################################################################################################
####################################################################################################################################################


#DON'T CHANGE THE NUMBERS IN THE FLOWER BRACKETS AND THE ORDER OF PERCENTAGE, DONE, TOTAL, SPEED, ETA ONLY CHANGE THE THEME 

      PROGRESS = """
**Percentage :{0}%**
**Done: {1}**
**Total: {2}**
**Speed: {3}/s**
**ETA: {4}**
"""
       
      DOWNLOAD_PROGRESS = "▪️"
      UPLOAD_PROGRESS = "▫️"

####################################################################################################################################################
####################################################################################################################################################



      DOWNLOAD_START = "Trying to Download 📥"
      DOWNLOAD_COMPLETE = "✅ Media Downloaded successfully\nPreparing for upload"
      UPLOAD_START = "Trying to Upload 📤"
      UPLOAD_COMPLETE = "THANKS FOR USING ME"
      SAVED_CUSTOM_THUMB_NAIL = "✅ Saved Thumbnail Successfully. This will be deleted in 24hrs"
      BANNED_TEXT = "YOU ARE BANNED. SO YOUR ARE NOT ABLE TO USE ME 🐒"
      REPLY_TEXT = "👩‍✈️ Reply to the media which you need to convert"
      DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Deleted Successfully ✅"
