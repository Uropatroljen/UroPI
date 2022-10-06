from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ["imei", "token"]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    imei: str
    token: str
    def __init__(self, token: _Optional[str] = ..., imei: _Optional[str] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ["client", "command", "light", "music", "network", "uro"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    LIGHT_FIELD_NUMBER: _ClassVar[int]
    MUSIC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    URO_FIELD_NUMBER: _ClassVar[int]
    client: Client
    command: str
    light: Light
    music: Music
    network: NetworkCre
    uro: Uro
    def __init__(self, command: _Optional[str] = ..., client: _Optional[_Union[Client, _Mapping]] = ..., music: _Optional[_Union[Music, _Mapping]] = ..., light: _Optional[_Union[Light, _Mapping]] = ..., uro: _Optional[_Union[Uro, _Mapping]] = ..., network: _Optional[_Union[NetworkCre, _Mapping]] = ...) -> None: ...

class Light(_message.Message):
    __slots__ = ["blue", "green", "red", "state"]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    blue: int
    green: int
    red: int
    state: bool
    def __init__(self, state: bool = ..., red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...

class Music(_message.Message):
    __slots__ = ["id", "title"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...

class NetworkCre(_message.Message):
    __slots__ = ["psw", "ssid"]
    PSW_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    psw: str
    ssid: str
    def __init__(self, ssid: _Optional[str] = ..., psw: _Optional[str] = ...) -> None: ...

class Uro(_message.Message):
    __slots__ = ["model"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str
    def __init__(self, model: _Optional[str] = ...) -> None: ...
