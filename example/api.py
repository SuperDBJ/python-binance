import sys
import asyncio
sys.path.append("..")
from binance.api import Api

client = Api()
loop = asyncio.get_event_loop()

task1 = asyncio.ensure_future(client.ping())
task2 = asyncio.ensure_future(client.get_server_time())

print(task1.result(), task2.result())

loop.close()