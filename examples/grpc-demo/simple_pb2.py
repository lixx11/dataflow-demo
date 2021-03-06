# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple.proto',
  package='simple',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0csimple.proto\x12\x06simple\"%\n\rsignalRequest\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x1a\n\x0bsignalReply\x12\x0b\n\x03sum\x18\x01 \x01(\x02\x32=\n\x06Signal\x12\x33\n\x03Sum\x12\x15.simple.signalRequest\x1a\x13.simple.signalReply\"\x00\x62\x06proto3'
)




_SIGNALREQUEST = _descriptor.Descriptor(
  name='signalRequest',
  full_name='simple.signalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='simple.signalRequest.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='simple.signalRequest.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=24,
  serialized_end=61,
)


_SIGNALREPLY = _descriptor.Descriptor(
  name='signalReply',
  full_name='simple.signalReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sum', full_name='simple.signalReply.sum', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=63,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['signalRequest'] = _SIGNALREQUEST
DESCRIPTOR.message_types_by_name['signalReply'] = _SIGNALREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

signalRequest = _reflection.GeneratedProtocolMessageType('signalRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNALREQUEST,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:simple.signalRequest)
  })
_sym_db.RegisterMessage(signalRequest)

signalReply = _reflection.GeneratedProtocolMessageType('signalReply', (_message.Message,), {
  'DESCRIPTOR' : _SIGNALREPLY,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:simple.signalReply)
  })
_sym_db.RegisterMessage(signalReply)



_SIGNAL = _descriptor.ServiceDescriptor(
  name='Signal',
  full_name='simple.Signal',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=91,
  serialized_end=152,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='simple.Signal.Sum',
    index=0,
    containing_service=None,
    input_type=_SIGNALREQUEST,
    output_type=_SIGNALREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIGNAL)

DESCRIPTOR.services_by_name['Signal'] = _SIGNAL

# @@protoc_insertion_point(module_scope)
