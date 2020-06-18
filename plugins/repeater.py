from nonebot import on_command, CommandSession,on_natural_language,NLPSession
from nonebot import get_bot
bot = get_bot()


repeaterList = [7600053]

@on_command('repeater', aliases=('复读',))
async def repeater(session: CommandSession):
    pass
    # daily_send = await get_daily()
    # await session.send(daily_send[0])
    # await session.send(daily_send[1])


# @on_natural_language()
# async def _(session: NLPSession):
#     print("###############",session)


# @on_natural_language()
# async def _(session: NLPSession):
#     print(session.ctx)


@bot.on_message("group")
async def group(ctx):
    userId = ctx["user_id"]
    try:
        if not repeaterList.index(userId) == -1:
            print(ctx["message"])
            await bot.send_group_msg(group_id=ctx["group_id"],message=ctx["message"])
    except:
        pass


