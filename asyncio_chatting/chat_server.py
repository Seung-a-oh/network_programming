import asyncio

async def handle_asyncclient(reader, writer):
    print('client :', writer.get_extra_info('peername'))
    while True:
        data = await reader.read(100)
        print('recv:'+data.decode())

        msg = input("메세지를 입력하세요: ")
        if msg == 'q':
            break
        writer.write(msg.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()
    print('connection was closed')

async def server_asyncmain():
    server = await asyncio.start_server(handle_asyncclient,'localhost',8000)
    print('server started')
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(server_asyncmain())
