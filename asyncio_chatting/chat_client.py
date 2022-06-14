import asyncio

async def chat_client():
    reader, writer = await asyncio.open_connection(host='localhost',port=8000)
    
    while True:
        msg = input("메세지를 입력하세요: ")
        if msg == 'q':
            break
        writer.write(msg.encode())
        await writer.drain()

        data = await reader.read(100)      # read 안이 비어있는 경우 있는거 다 읽음
        print('recv:'+data.decode())

    writer.write(b'done')
    writer.close()
    await writer.wait_closed()
    print('connection was closed')

if __name__ == "__main__":
    asyncio.run(chat_client())