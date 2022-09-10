import hikari
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
bot = hikari.GatewayBot(token = TOKEN)
bot.run(
    asyncio_debug=True,             # enable asyncio debug to detect blocking and slow code.

    coroutine_tracking_depth=20,    # enable tracking of coroutines, makes some asyncio
                                    # errors clearer.

    propagate_interrupts=True,      # Any OS interrupts get rethrown as errors.
)