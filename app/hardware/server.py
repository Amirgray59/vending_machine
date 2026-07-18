import json
import asyncio 
from app.core.config import config 

from typing import Dict


class HardwareGateway : 

    def __init__(self, host: str = config.TCP_HOST , port : int = config.TCP_PORT) : 

        self.host = host 
        self.port = port 

        self.server = None 
        self.sessions : Dict[int, dict] = {} 


    async def start(self) : 
        self.server = await asyncio.start_server(
            self.handle_connection, 
            self.host, 
            self.port
        ) 

    async def handle_connection(self, reader: asyncio.StreamReader, writer : asyncio.StreamWriter) : 
        client_ip = writer.get_extra_info("peername")[0] 

        try  : 
            while True  : 
                data = await reader.readline() 
                if not data : 
                    break 

                try : 
                    # TODO -> dectription 
                    json_str = json.loads(data)

                except Exception as ex : 
                    print(ex)

        except Exception as ex : 
            print(ex)

    async def shutdownD(self) : 
        if self.server : 
            self.server.close() 
            await self.server.wait_closed() 

    
            
            
    