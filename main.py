import asyncio
import random
from urllib import request
import urllib
import requests
import aiohttp
import revolt
from revolt.ext import commands
import json




class Client(commands.CommandsClient, revolt.Client):
    async def get_prefix(self, message: revolt.Message):
        return "-"
    async def on_ready(self):
        print(f"Ready as {self.user.name}")
        await self.edit_status(presence=revolt.PresenceType.online, text="Test")
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Bot reaction test command"""
        await ctx.send("pong")
    
    @commands.command()
    async def nsfw(self, ctx: commands.Context, category: str):
        """Generate a random NSFW picture"""
        if ctx.channel.nsfw == True:
            if category == "boobs":
                response = requests.get(f"https://www.reddit.com/r/boobs/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "pussy":
                response = requests.get(f"https://www.reddit.com/r/pussy/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "latina":
                response = requests.get(f"https://www.reddit.com/r/latinas/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "asian":
                response = requests.get(f"https://www.reddit.com/r/AsianNSFW/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "blowjob":
                response = requests.get(f"https://www.reddit.com/r/BlowJob/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "squirt":
                response = requests.get(f"https://www.reddit.com/r/squirting/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "lesbian":
                response = requests.get(f"https://www.reddit.com/r/lesbians/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "hentai":
                response = requests.get(f"https://www.reddit.com/r/hentai/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "nudes":
                response = requests.get(f"https://www.reddit.com/r/nudes/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "masturbation":
                response = requests.get(f"https://www.reddit.com/r/MasturbationGoneWild/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)
            elif category == "gay":
                response = requests.get(f"https://www.reddit.com/r/gayporn/hot.json", headers={"User-agent": "venady"})
                data = response.json()
                posts = data["data"]["children"]
                post = random.choice(posts)
                image_url = post["data"]["url"]
                await ctx.send(image_url)

            else:
                await ctx.send(embed=revolt.SendableEmbed(title="NSFW Command", description=f"More catogories: \n - nudes \n - pussy \n - boobs \n - masturbation \n - blowjob \n - squirt \n - lesbian \n - gay \n - hentai"))

        else:
            await ctx.send(embed=revolt.SendableEmbed(title="NSFW Command", description=f"⚠ This Command only works in NSFW Channels!"))


    @commands.command()
    async def neso(self, ctx: commands.Context):
        """Neso Help Menu"""
        await ctx.send(embed=revolt.SendableEmbed(title="Neso Help Menu", description=f"`-help` -> Shows u this message \n `-nsfw [catogory]` - Send u a random nsfw picture"))

async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, "token")
        await client.start()

asyncio.run(main())