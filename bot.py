import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(message.content)
        
        print("Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
        print("Sentence Overall Rated As", end = " ")
    
        if sentiment_dict['compound'] >= 0.05: 
            print("Positive")
            await message.add_reaction("😊")
        elif sentiment_dict['compound'] <= - 0.05 :
            print("Negative")
            await message.add_reaction("😢")
        else :
            print("Neutral")
            await message.add_reaction("😐")
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
