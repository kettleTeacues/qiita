import pydantic

import dataclasses, typing

_primitive = int | str | bool

_dataclass = dataclasses.dataclass

_typedDict = typing.TypedDict

_Protocol = typing.Protocol

_pydantic_dataclass = pydantic.dataclasses.dataclass
