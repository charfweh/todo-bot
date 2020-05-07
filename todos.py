import json
import sqlite3
import discord
from discord.ext import commands
bot = discord.Client()
prefix = "td!"
con = sqlite3.connect('todo.db')
#reading token
f = open('configs.json')
data = json.load(f)
#events on ready
@bot.event
async def on_ready():  
    print("working")
    
    # try:
    #     con = sqlite3.connect('todo.db')
    #     print('connection established')
    #     cursor = con.cursor()
    #     cursor.execute('''
    #         CREATE TABLE IF NOT EXISTS users(
    #             auth_id TEXT,
    #             auth_name TEXT
    #         )
    #     ''')
    # except:
    #     print("Exception occured")

#messages event MAIN MODULE
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'yo':
        await message.channel.send("working")
    #USER ADD COMMAND
    if message.content.startswith(prefix+'entry'):
        await message.channel.send("checking")
        cursor = con.cursor()
        val = (message.author.id,message.author.name)
        cursor.execute('''
            SELECT auth_id from USERS WHERE auth_id = ?
        ''',(message.author.id,))
        result = cursor.fetchone()
        if result:
            await message.channel.send("You are already added")
        else:
            await message.channel.send("Adding user...")
            cursor.execute(''' 
            INSERT INTO USERS(auth_id,auth_name) VALUES(?,?)
            ''',val)
            con.commit()
            await message.channel.send("You were added!")
    #USER TODOLIST INFO
    if message.content.startswith(prefix+'list'):
        #fetch user's todo list and display it in embed
        pass
    #HELP EMBED
    if message.content.startswith(prefix+'help'):
        #help embed
        await message.channel.send('under development')
#logging in
bot.run(data['bot_token'])