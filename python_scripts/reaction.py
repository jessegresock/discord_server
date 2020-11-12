import discord
import json

intents = discord.Intents().all()
client  = discord.Client(intents=intents)

with open('bot_token/token.json') as json_file:
    token = json.load(json_file)

@client.event
async def on_ready():
    print('Bot is logged on!')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == :
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        if payload.emoji.name == 'bois':
            role = discord.utils.get(guild.roles, name='bois')
        elif payload.emoji.name == 'league_bois':
            role = discord.utils.get(guild.roles, name='league_bois')
        elif payload.emoji.name == 'tft_bois':
            role = discord.utils.get(guild.roles, name='tft_bois')
        elif payload.emoji.name == 'movie_bois':
            role = discord.utils.get(guild.roles, name='movie_bois')
        elif payload.emoji.name == 'pjwinter_bois':
            role = discord.utils.get(guild.roles, name='pjwinter_bois')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print("Member not found.")
        else:
            print("Role not found.")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == :
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        if payload.emoji.name == 'bois':
            role = discord.utils.get(guild.roles, name='bois')
        elif payload.emoji.name == 'league_bois':
            role = discord.utils.get(guild.roles, name='league_bois')
        elif payload.emoji.name == 'tft_bois':
            role = discord.utils.get(guild.roles, name='tft_bois')
        elif payload.emoji.name == 'movie_bois':
            role = discord.utils.get(guild.roles, name='movie_bois')
        elif payload.emoji.name == 'pjwinter_bois':
            role = discord.utils.get(guild.roles, name='pjwinter_bois')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member not found.")
        else:
            print("Role not found.")

client.run(token['token'])