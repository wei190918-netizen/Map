import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'機器人已成功上線：{bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"已同步 {len(synced)} 個斜線指令")
    except Exception as e:
        print(f"同步指令失敗: {e}")

@bot.tree.command(name="map", description="顯示地圖資訊")
async def show_map(interaction: discord.Interaction):
    # Map 1: 維京灣
    embed1 = discord.Embed(
        title="Map 1: 維京灣 Viking Bay",
        color=discord.Color.dark_gray()
    )
    # 貼上第一張地圖的圖片網址
    embed1.set_image(url="https://your-image-url-1.png")

    # Map 2: 岩峰
    embed2 = discord.Embed(
        title="Map 2: 岩峰 Stone Peaks",
        color=discord.Color.dark_gray()
    )
    # 貼上第二張地圖的圖片網址
    embed2.set_image(url="https://your-image-url-2.png")

    await interaction.response.send_message(embeds=[embed1, embed2])

# 從系統環境變數讀取 Token
TOKEN = os.getenv("BOT_TOKEN")
bot.run(TOKEN)
