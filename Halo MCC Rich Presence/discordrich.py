from pypresence import Presence

def DiscordRPCInit():
    RPC = Presence(client_id)
    RPC.connect()
    return RPC

