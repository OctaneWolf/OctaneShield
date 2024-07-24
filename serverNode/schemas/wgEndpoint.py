from typing import List, Optional
from pydantic import BaseModel, IPvAnyAddress, conint


class AllowedIP(BaseModel):
    ip: IPvAnyAddress
    cidr: conint(ge=0, le=32)


class Peer(BaseModel):
    public_key: str
    pre_shared_key: Optional[str] = None
    allowed_ips: List[AllowedIP]
    endpoint: Optional[str] = None
    persistent_keepalive: Optional[conint(ge=0)] = None


class Interface(BaseModel):
    private_key: str
    address: List[IPvAnyAddress]
    listen_port: Optional[conint(ge=1, le=65535)] = None
    mtu: Optional[conint(ge=576)] = None
    dns: Optional[List[IPvAnyAddress]] = None


class WireGuardClientConfig(BaseModel):
    interface: Interface
    peers: List[Peer]
