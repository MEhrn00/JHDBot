import discord 
from discord.ext import commands
import asyncio

class ModeratorCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #Clear Message Command..
    @commands.command() #a function to clear messages, if bot has perms to do that...
    async def clear(self, ctx, amount=2):     #amount=2 sets the default value to 2 basically command + the text above that
        try:
            if (ctx.message.author.guild_permissions.manage_messages):
                await ctx.channel.purge(limit=amount+1) #limit= number of messages going to be deleted !
                await ctx.channel.send(f"Deleted {amount} messages D:")
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
        except:
            await ctx.send("The bot is unauthorized to delete messages D:")



    #Kick Member Command..
    @commands.command() #a function to kick members
    async def kick(self, ctx, user: discord.Member, *, reason=None):                      #gets context user and reason, default being None
        try:
            if user.guild_permissions.manage_messages:                                  #check perms. if user has perms to manage message like if he mod he can't be kicked by the bot.
                await ctx.send(f"Sorry, can't kick {user} because of perms : (") 
            elif ctx.message.author.guild_permissions.kick_members:                     #checks if user who send the kick command is authorized to do it.
                await user.send("You were kicked from JHDiscord :"+reason)
                await ctx.guild.kick(user=user, reason=reason)                          #kicks that user
                await ctx.send(f'{user} has been kicked out from the server')
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
        except:
            await ctx.send("The bot is unauthorized to kick members D:")


    #Ban Member Command..
    @commands.command() #a function to ban members
    async def ban(self, ctx, user: discord.Member, *, reason=None): #gets context user and reason, default being None
        try:
            if user.guild_permissions.manage_messages:  #check perms. if user has perms to manage message like if he mod he can't be banned by the bot.
                await ctx.send(f"Sorry, can't ban {user} because of perms : (") 
            elif ctx.message.author.guild_permissions.ban_members: #checks if user who send the ban command is authorized to do it.
                await user.send("You were banned from JHDiscord :"+reason)
                await ctx.guild.ban(user=user, reason=reason)  #bans that user
                await ctx.send(f'{user} has been banned from the server')
            else:
                await ctx.send("Sorry, it seems like you are not authorized to do it")
        except:
            await ctx.sent("The bot is unauthorized to ban members D:")

def setup(bot):
    bot.add_cog(ModeratorCog(bot))
    print('Moderation cog loaded')