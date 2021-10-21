import discord
from discord.ext import commands
import praw
import asyncio

reddit = praw.Reddit(client_id = "YOURCLIENTID", client_secret = "YOURCLIENTSECRET", username = "YOURUSERNAME", password = "YOURPASSWORD", user_agent = "pythonpraw")

bot = commands.Bot(command_prefix = '.')

master_list = [] #master list to reference all gathered deals. 

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def post_deals(ctx):
    while True:
        try:
            subreddit = reddit.subreddit("buildapcsales")

            new_gather = subreddit.new(limit = 20) #limit set to 20 becuase deals aren't posted that frequently

            gathered_list = [(submission.title, submission.url) for submission in new_gather] #list of post titles and urls in new_gather

            unique_post_list = [(title, url) for (title, url) in gathered_list if (title, url) not in master_list] #check if any unique posts in newly gathered posts, referenced against the master list of already collected posts

            [master_list.append(submission) for submission in gathered_list if submission not in master_list] #adds new values of scraped posts if they don't already exist in the master list


            monitor_list = "\n".join(str(title) + ' ' + str(url) for (title, url) in unique_post_list if '[Monitor]' in str(title) or '[MONITOR]' in str(title) and '1080' not in str(title))


            cpu_list = "\n".join(str(title) + ' ' + str(url) for (title, url) in unique_post_list if '[CPU]' in str(title) and '5600' in str(title))
            
        
            gpu_list = "\n".join(str(title) + ' ' + str(url) for (title, url) in unique_post_list if '[GPU]' in str(title) and 'EVGA' in str(title))
            

            ram_list = "\n".join(str(title) + ' ' + str(url) for (title, url) in unique_post_list if '[RAM]' in str(title) and 'G.SKILL' in str(title) and 'RGB' not in str(title))
           

            mobo_list = "\n".join(str(title) + ' ' + str(url) for (title, url) in unique_post_list if '[MOBO]' in str(title) or '[Motherboard]' in str(title) and 'B550' in str(title))
        

            keyboard_list = "\n".join(str(title) + ' ' + str(url) for (title, url) in unique_post_list if '[Keyboard]' in str(title))

            all_lists = str(cpu_list +'\n' + monitor_list + '\n' + gpu_list + '\n' + ram_list + '\n' + mobo_list + '\n' + keyboard_list)

            if unique_post_list is not None:
                await ctx.send(all_lists)


        except Exception:
            pass


        await asyncio.sleep(600)

bot.run('NzgwODQzMzU3NTM4MDkxMDI5.X70_Cw.Z68DvzwMviLpUS-emw3xQb_UVAM')

