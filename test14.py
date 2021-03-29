import asyncio
import aiohttp

URL="https://captivateprime.adobe.com/primeapi/v2/badges"
headers=dict()
headers["Authorization"]="oauth 6401681362abe7350a7280a80ff73431"



async def task1(endpoint):
 print(f"Obtained end point {endpoint}")
 async with aiohttp.ClientSession() as session:
   async with session.get(URL,headers=headers) as response:
         print(response.status)
         return await response.json()


async def main():
   task_1=asyncio.create_task(task1("badges"))
   task_2=asyncio.create_task(task1("los"))
   task_3=asyncio.create_task(task1("certificate"))
   l=list()
   l.append(await task_1)
   l.append(await task_2)
   l.append(await task_3)
   return l

if __name__=="__main__":
  loop=asyncio.get_event_loop()
  collect=loop.run_until_complete(main())
  print(collect)