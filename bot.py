import discord
import responses
import translators as ts
import langdetect
import emoji
import minesweeper_test

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.auther.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
def convert_regional_to_char(c):
    n = ord(c) - ord("🇦")
    return chr(ord('a') + n)
    
def run_discord_bot(): 
    intents = discord.Intents.default()
    intents.message_content = True

    TOKEN = 'MTE1NTU5MDg0MjcwMzE1OTQ2OQ.GP0fDS.4eestSpY-PVcjdTSIFM5dWkSIssQHH7MFQa_qQ'
    client = discord.Client(intents=intents)

    PREFIX = '!'

    @client.event
    async def on_ready():
        print(f'{client.user} (GOOD ONE!!!)')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0 : len(PREFIX) - 1] == PREFIX:
            user_message = user_message[len(PREFIX):]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)

    @client.event
    async def on_reaction_add(reaction, user):
        message = str(reaction.message.content)
        channel = reaction.message.channel
        try:
            language = convert_regional_to_char(reaction.emoji[0]) + convert_regional_to_char(reaction.emoji[1])
            if language in ['us', 'uk', 'au']:
                language = 'en'

            # if language in ['af', 'am', 'ar', 'as', 'az', 'ba', 'bg', 'bn', 'bo', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'dsb', 'dv', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fil', 'fj', 'fo', 'fr', 'fr-CA', 'ga', 'gl', 'gom', 'gu', 'ha', 'he', 'hi', 'hr', 'hsb', 'ht', 'hu', 'hy', 'id', 'ig', 'ikt', 'is', 'it', 'iu', 'iu-Latn', 'ja', 'ka', 'kk', 'km', 'kmr', 'kn', 'ko', 'ku', 'ky', 'ln', 'lo', 'lt', 'lug', 'lv', 'lzh', 'mai', 'mg', 'mi', 'mk', 'ml', 'mn-Cyrl', 'mn-Mong', 'mr', 'ms', 'mt', 'mww', 'my', 'nb', 'ne', 'nl', 'nso', 'nya', 'or', 'otq', 'pa', 'pl', 'prs', 'ps', 'pt', 'pt-PT', 'ro', 'ru', 'run', 'rw', 'sd', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr-Cyrl', 'sr-Latn', 'st', 'sv', 'sw', 'ta', 'te', 'th', 'ti', 'tk', 'tlh-Latn', 'tn', 'to', 'tr', 'tt', 'ty', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yo', 'yua', 'yue', 'zh-Hans', 'zh-Hant', 'zu']:
            response = ts.translate_text(
            message,
            translator = 'bing', 
            from_language = 'auto', 
            to_language = language, 
            if_use_preacceleration = False
            )

            await reaction.message.reply(f'{response} {user.mention}')
        except Exception as e:
            await message.send(f'{user.mention} uhm stupid idiot')
            print(e)

        
    client.run(TOKEN)