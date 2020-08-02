# -*- coding:utf-8 -*-

import asyncio
import time

async def hi(msg, sec):
    print('enter hi(). {} @{}'.format(msg,time.strftime('%H:%M:%S')))
    await asyncio.sleep(sec)
    print('exit hi{} @{}'.format(msg,time.strftime('%H:%M:%S')))
    return sec 

async def main():
    print('begin at {}'.format(time.strftime('%H:%M:%S')))
    tasks = []
    for i in range(1,5):
        t = asyncio.create_task(hi(i,i))
        tasks.append(t)
    print('main asyncio sleeping')
    await asyncio.sleep(2)
    # for t in tasks:
        # r = await t
        # print('r',r)
    print('end {}'.format(time.strftime('%H:%M:%S')))


asyncio.run(main())