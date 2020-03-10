import asyncio, discord, random

from discord.ext import commands

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

class Partner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60*10, type=commands.BucketType.user)
    async def partner(self, ctx, *, message):  
        def check(m):
            return m.author.id == ctx.message.author.id and m.channel.id == ctx.message.channel.id
        try:    
            await ctx.send("Alright, your message has been set, reply with yes/no")
            msg = await self.bot.wait_for("message", check=check, timeout=60)
            if msg.content == 'yes':
                await ctx.send("Alright, i'll pick a random server and send this message to everyone in it.")
                running = True
            else:
                await ctx.send("Alright, then i wont :wave:")
                running = False
        except asyncio.TimeoutError:     
            await ctx.send("Error, command timed out, try again later.") 
        await asyncio.sleep(5)
        if running == True:
            for guild in self.bot.guilds:
                for member in guild.members:
                    try:
                        await member.send(member.mention)
                        em = discord.Embed(title="JustPartner Bot", description=f"This message has been sent from {ctx.guild.name}", color=RandomColor())
                        em.add_field(name="Add me to your server!", value="[Click here to add me!](https://discordapp.com/oauth2/authorize?client_id=657917182650482718&scope=bot&permissions=8)")
                        em.set_footer(text="Created by Alucard | xanthe.#1337 https://discord.gg/BGu62Ha")
                        await member.send(embed=em)
                        await member.send(message)
                        await asyncio.sleep(5)
                    except:
                        pass    
            await ctx.send(f"{ctx.author.mention} | Finished sending messages to {guild.name} members!")
        else:   
            return                

def setup(bot):
    bot.add_cog(Partner(bot))
