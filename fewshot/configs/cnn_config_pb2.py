# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fewshot/configs/cnn_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fewshot/configs/cnn_config.proto',
  package='fewshot.configs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n fewshot/configs/cnn_config.proto\x12\x0f\x66\x65wshot.configs\"\xa1\x01\n\tCNNConfig\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x13\n\x0bnum_channel\x18\x03 \x01(\x05\x12\x13\n\x0bnum_filters\x18\x04 \x03(\x05\x12\x0f\n\x07strides\x18\x05 \x03(\x05\x12\x0f\n\x07pool_fn\x18\x06 \x03(\t\x12\x14\n\x0cpool_strides\x18\x07 \x03(\x05\x12\x13\n\x0b\x63onv_act_fn\x18\x08 \x03(\t')
)




_CNNCONFIG = _descriptor.Descriptor(
  name='CNNConfig',
  full_name='fewshot.configs.CNNConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='fewshot.configs.CNNConfig.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='fewshot.configs.CNNConfig.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_channel', full_name='fewshot.configs.CNNConfig.num_channel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_filters', full_name='fewshot.configs.CNNConfig.num_filters', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strides', full_name='fewshot.configs.CNNConfig.strides', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pool_fn', full_name='fewshot.configs.CNNConfig.pool_fn', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pool_strides', full_name='fewshot.configs.CNNConfig.pool_strides', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conv_act_fn', full_name='fewshot.configs.CNNConfig.conv_act_fn', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=215,
)

DESCRIPTOR.message_types_by_name['CNNConfig'] = _CNNCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CNNConfig = _reflection.GeneratedProtocolMessageType('CNNConfig', (_message.Message,), dict(
  DESCRIPTOR = _CNNCONFIG,
  __module__ = 'fewshot.configs.cnn_config_pb2'
  # @@protoc_insertion_point(class_scope:fewshot.configs.CNNConfig)
  ))
_sym_db.RegisterMessage(CNNConfig)


# @@protoc_insertion_point(module_scope)
