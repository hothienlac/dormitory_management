# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/gate_control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/gate_control.proto',
  package='gate_control',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x18proto/gate_control.proto\x12\x0cgate_control\"*\n\tGoRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\r\n\x05goOut\x18\x02 \x01(\x08\".\n\tGoRespond\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2G\n\x0bGateService\x12\x38\n\x02Go\x12\x17.gate_control.GoRequest\x1a\x17.gate_control.GoRespond\"\x00\x62\x06proto3'
)




_GOREQUEST = _descriptor.Descriptor(
  name='GoRequest',
  full_name='gate_control.GoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='gate_control.GoRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goOut', full_name='gate_control.GoRequest.goOut', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=84,
)


_GORESPOND = _descriptor.Descriptor(
  name='GoRespond',
  full_name='gate_control.GoRespond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accepted', full_name='gate_control.GoRespond.accepted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='gate_control.GoRespond.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['GoRequest'] = _GOREQUEST
DESCRIPTOR.message_types_by_name['GoRespond'] = _GORESPOND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GoRequest = _reflection.GeneratedProtocolMessageType('GoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GOREQUEST,
  '__module__' : 'proto.gate_control_pb2'
  # @@protoc_insertion_point(class_scope:gate_control.GoRequest)
  })
_sym_db.RegisterMessage(GoRequest)

GoRespond = _reflection.GeneratedProtocolMessageType('GoRespond', (_message.Message,), {
  'DESCRIPTOR' : _GORESPOND,
  '__module__' : 'proto.gate_control_pb2'
  # @@protoc_insertion_point(class_scope:gate_control.GoRespond)
  })
_sym_db.RegisterMessage(GoRespond)



_GATESERVICE = _descriptor.ServiceDescriptor(
  name='GateService',
  full_name='gate_control.GateService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=134,
  serialized_end=205,
  methods=[
  _descriptor.MethodDescriptor(
    name='Go',
    full_name='gate_control.GateService.Go',
    index=0,
    containing_service=None,
    input_type=_GOREQUEST,
    output_type=_GORESPOND,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATESERVICE)

DESCRIPTOR.services_by_name['GateService'] = _GATESERVICE

# @@protoc_insertion_point(module_scope)
