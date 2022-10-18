import discord
from discord.ext import commands
import asyncio

TOKEN = ''

#接続に必要なオブジェクトの作成
Intents = discord.Intents.all()
Intents.message_content = True
Intents.members = True
bot = commands.Bot(command_prefix="!", intents=Intents)

#ngワードのグローバル変数
ng_word =[""]*11 #11個の""の要素を作る（０は使わず１〜１０を使う）

#カテゴリのグローバル変数
Category =""

#メンションしたときに開始するかのボタンを出す関数(ver.ponkotuでは使ってないです)
#async def start_mention(ctx):
#    if bot.user.mentioned_in(ctx) and ctx.mention_everyone is False: #ボットにメンションしたとき
#        members =  ctx.author.voice.channel.members #botにメンションした人のいるvc内のメンバー情報の取得
#        embed = discord.Embed(title="メンバー")
#        i=0
#        for member in members:
#            i=i+1
#            embed.add_field(name=i,value=f"{member.mention}") #for文でメンバー全員のメンションを作成
#        views = yesbutton()
#        await ctx.channel.send(embed=embed, view=views)

#チャンネルを作る関数
async def mk_channel(ctx):
    if bot.user.mentioned_in(ctx) and ctx.mention_everyone is False:
        Guild = ctx.guild #ギルドIDの取得
        global Category 
        Category = await Guild.create_category("NGワードゲーム") #ギルドにカテゴリーを作る

        #メインルームを作る
        main_channel = await Category.create_text_channel("メインルーム")
        main_embed = discord.Embed(title="コマンドの使い方",description="このチャンネルはみんながNGワードを決め終わった後に使うよ\n!dm を使うとNGワードがdmに送信されるよ")
        await main_channel.send(embed=main_embed)
        #NGワードチャンネルを作る
        members =  ctx.author.voice.channel.members
        i=0
        for member in members:
            overwrites = {
             member: discord.PermissionOverwrite(read_messages=False) #自分のNGワードが見えないように
         }
            i=i+1
            embed = discord.Embed(title="コマンドの使い方",description = f"このチャンネルで使うコマンドは\n!ng{i} だよ\nコマンドを入力するとNGワードを入力できるようになるよ\n入力するときは20秒以内に入力してね\nNGワードをリセットしたいときはもう一回コマンドを使ってね")
            channel = await Category.create_text_channel(f'{member.display_name}のNGワード',overwrites=overwrites) #カテゴリー内にテキストチャンネルを作る
            await channel.send(embed=embed)
            await channel.send(f'{member.display_name}のNGワードをみんなで決めよう!\n※{member.display_name}にはこのチャンネルは見えてないよ') 
        


#class yesbutton(discord.ui.View): #ボタンを作る(わからないとこが多くて勉強中)
#    @discord.ui.button(
#        label = 'このメンバーで始める',
#        style = discord.ButtonStyle.gray,
#   )
#    async def make_channel(self, interaction: discord.Interaction, button: discord.ui.Button ):
#       await interaction.response.send_message(f'{interaction.user.display_name}は{button.label}を押しました',ephemeral=True)
        



#起動時の処理
@bot.event
async def on_ready():
    print("on_ready")
    await bot.change_presence(activity=discord.Game(name="NGワードゲーム")) #プレイ表示

#!ng1~!ng5まではほぼ処理が同じです
@bot.command()
async def ng1(ctx):
    def check(msg): 
        return msg.author is ctx.author
    await ctx.send("↓にNGワードを入力してね!")

    try:
        msg = await bot.wait_for('message',check=check, timeout=20) #メッセージ送信を待つcheck関数で送信者が入力しないと反応しないようにする
    except asyncio.TimeoutError:
        await ctx.send("入力が遅すぎるよ（T_T)\nもう一回コマンドを入力してNGワードを決めてね") #20秒以内に入力しないとコマンドの再入力を求める
        return
    global ng_word #グローバル変数の取得
    ng_word[1] = msg.content
    await ctx.send(f"{msg.content}をNGワードに登録したよ")

@bot.command()
async def ng2(ctx):
    def check(msg): 
        return msg.author is ctx.author
    await ctx.send("↓にNGワードを入力してね!")

    try:
        msg = await bot.wait_for('message',check=check, timeout=20) #メッセージ送信を待つcheck関数で送信者が入力しないと反応しないようにする
    except asyncio.TimeoutError:
        await ctx.send("入力が遅すぎるよ（T_T)\nもう一回コマンドを入力してNGワードを決めてね") #20秒以内に入力しないとコマンドの再入力を求める
        return
    global ng_word #グローバル変数の取得
    ng_word[2] = msg.content
    await ctx.send(f"{msg.content}をNGワードに登録したよ")

@bot.command()
async def ng3(ctx):
    def check(msg): 
        return msg.author is ctx.author
    await ctx.send("↓にNGワードを入力してね!")

    try:
        msg = await bot.wait_for('message',check=check, timeout=20) #メッセージ送信を待つcheck関数で送信者が入力しないと反応しないようにする
    except asyncio.TimeoutError:
        await ctx.send("入力が遅すぎるよ（T_T)\nもう一回コマンドを入力してNGワードを決めてね") #20秒以内に入力しないとコマンドの再入力を求める
        return
    global ng_word #グローバル変数の取得
    ng_word[3] = msg.content
    await ctx.send(f"{msg.content}をNGワードに登録したよ")

@bot.command()
async def ng4(ctx):
    def check(msg): 
        return msg.author is ctx.author
    await ctx.send("↓にNGワードを入力してね!")

    try:
        msg = await bot.wait_for('message',check=check, timeout=20) #メッセージ送信を待つcheck関数で送信者が入力しないと反応しないようにする
    except asyncio.TimeoutError:
        await ctx.send("入力が遅すぎるよ（T_T)\nもう一回コマンドを入力してNGワードを決めてね") #20秒以内に入力しないとコマンドの再入力を求める
        return
    global ng_word #グローバル変数の取得
    ng_word[4] = msg.content
    await ctx.send(f"{msg.content}をNGワードに登録したよ")

@bot.command()
async def ng5(ctx):
    def check(msg): 
        return msg.author is ctx.author
    await ctx.send("↓にNGワードを入力してね!")

    try:
        msg = await bot.wait_for('message',check=check, timeout=20) #メッセージ送信を待つcheck関数で送信者が入力しないと反応しないようにする
    except asyncio.TimeoutError:
        await ctx.send("入力が遅すぎるよ（T_T)\nもう一回コマンドを入力してNGワードを決めてね") #20秒以内に入力しないとコマンドの再入力を求める
        return
    global ng_word #グローバル変数の取得
    ng_word[5] = msg.content
    await ctx.send(f"{msg.content}をNGワードに登録したよ")

#確認用、ng_wordに入ってる要素をメッセージに送る
@bot.command()
async def check(ctx):
    await ctx.send(ng_word)

#DMに自分以外のNGワードをまとめて送るコマンドです。3人以上は試したことないのでバグる可能性あり。（forが複雑で自分でもどうなってるかわかってないです笑）
@bot.command()
async def dm(ctx):
    members =  ctx.author.voice.channel.members
    i=0
    for ng in ng_word: #ng_wordを全て表示させる
        member = members[i]
        await member.send("みんなのNGワードが決まったよ!")
        if len(members)==i:#メンバー数と上のfor文の実行回数が一致したら終了する
            break
        j=0
        k=0
        for ng in ng_word:#ng_wordを全て表示させる
            if ng_word[i+1]!=ng and ng_word[0]!=ng:#ngがi番目の要素でない,0番目でないとき
                await member.send(f"{members[k-1].display_name} : {ng}") #ngを表示,k-1は0番目が表示されない分を引いている
                j=j+1 #カウントを増やす,jはngが表示された分加算
            if len(members)==j+1:#一致すれば一人分終了させる
                break
            k=k+1#kはngが表示されたされないに関わらず加算
        
        await member.send("それじゃあ楽しんでね〜")
        i=i+1

#作ったカテゴリ、チャンネルを全て消すコマンドです    
@bot.command()
async def dele(ctx):
    global Category #作るときに取得したカテゴリ情報を持ってくる
    for channel in Category.channels: #カテゴリの中にあるすべてのチャンネルを
        await channel.delete() #消す
    await ctx.send("また遊んでね〜")
    await Category.delete() #カテゴリを削除


#全員のNGワードを表示させるコマンド
@bot.command()
async def result(ctx):
    members = ctx.author.voice.channel.members
    i=0
    for ng in ng_word:
        if ng_word[0]!=ng:
            await ctx.author.send(f"{members[i].display_name} : {ng}")
            i=i+1

@bot.event
async def on_message(message):
    if message.author.bot:
        return
   # await start_mention(message)
    await mk_channel(message) #メンションされてるかチェックする
    await bot.process_commands(message)
      
bot.run(TOKEN)
