from liplib.liplib import *
import time
import asyncio

loop = asyncio.get_event_loop()
srv = LipServer()

host_addr = "192.168.1.4"


def out(light, value, time=0.0):
    # connect to the bridge
    loop.run_until_complete(srv.open(host=host_addr))

    # send commands
    loop.run_until_complete(srv.write(LipServer.OUTPUT, light, 1, value, time))


out(37, 100, 2.0)

time.sleep(4)

out(37, 0)

loop.close()
