import pydantic

import dataclasses, typing

_primitive = int | str | bool

_dataclass = dataclasses.dataclass

_typedDict = typing.TypedDict

_Protocol = typing.Protocol

_pydantic_dataclass = pydantic.dataclasses.dataclass

@dataclasses.dataclass
class Dataclass_Sample:
    sample_property: str
    def sample_method(self):
        return self.sample_property
dataclass_sample1 = Dataclass_Sample(
    sample_property='sample1'
)
dataclass_sample2 = Dataclass_Sample(
    sample_property=100
)
print('type(dataclass_sample):', type(dataclass_sample1)) # <class '__main__.Dataclass_Sample'>

class TypedDict_Sample(typing.TypedDict):
    sample_property: str
typedDict_sample1 = TypedDict_Sample(
    sample_property='sample1'
)
typedDict_sample2: TypedDict_Sample = {
    'sample_property': 'sample2'
}
typedDict_sample3: TypedDict_Sample = {
    'hello': 100
}
print('type(typedDict_sample1):', type(typedDict_sample1)) # <class 'dict'>
print('type(typedDict_sample2):', type(typedDict_sample2)) # <class 'dict'>

class Protocol_Sample(typing.Protocol):
    sample_property: str
    def sample_method(self) -> str:
        ...
sample_obj1 = Dataclass_Sample(
    sample_property='sample1'
)
sample_obj2 = Dataclass_Sample(
    sample_property=100
)
protocol_sample: Protocol_Sample = sample_obj1
print('type(protocol_sample):', type(protocol_sample)) # <class '__main__.Dataclass_Sample'>
def sample_function(obj: Protocol_Sample):
    print('type(obj):', type(obj)) # <class '__main__.Dataclass_Sample'>
sample_function(sample_obj1)
sample_function(sample_obj2)

## Protocolはインスタンス化できない。
# Error: Protocol クラス "Protocol_Sample" をインスタンス化できません
# protocol_sample = Protocol_Sample()

@pydantic.dataclasses.dataclass
class Pydantic_Dataclass_Sample:
    sample_property: str
    def sample_method(self):
        ...
pydantic_dataclass_sample1 = Pydantic_Dataclass_Sample(
    sample_property='sample',
)
try:
    pydantic_dataclass_sample2 = Pydantic_Dataclass_Sample(
        sample_property=100,
    )
except Exception as e:
    print(e)
print('type(pydantic_dataclass_sample):', type(pydantic_dataclass_sample1)) # <class '__main__.Pydantic_Dataclass_Sample'>
