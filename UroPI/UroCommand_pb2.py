# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UroCommand.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10UroCommand.proto\"\xb4\x01\n\x07\x43ommand\x12\x14\n\x07\x63ommand\x18\x01 \x01(\tH\x01\x88\x01\x01\x12\x19\n\x06\x63lient\x18\x02 \x01(\x0b\x32\x07.ClientH\x00\x12\x17\n\x05music\x18\x03 \x01(\x0b\x32\x06.MusicH\x00\x12\x17\n\x05light\x18\x04 \x01(\x0b\x32\x06.LightH\x00\x12\x13\n\x03uro\x18\x05 \x01(\x0b\x32\x04.UroH\x00\x12\x1e\n\x07network\x18\x06 \x01(\x0b\x32\x0b.NetworkCreH\x00\x42\x05\n\x03msgB\n\n\x08_command\"B\n\x06\x43lient\x12\x12\n\x05token\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04imei\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_tokenB\x07\n\x05_imei\"=\n\x05Music\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_idB\x08\n\x06_title\"y\n\x05Light\x12\x12\n\x05state\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x10\n\x03red\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05green\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x11\n\x04\x62lue\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x08\n\x06_stateB\x06\n\x04_redB\x08\n\x06_greenB\x07\n\x05_blue\"#\n\x03Uro\x12\x12\n\x05model\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_model\"B\n\nNetworkCre\x12\x11\n\x04ssid\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03psw\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_ssidB\x06\n\x04_pswb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UroCommand_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMAND._serialized_start=21
  _COMMAND._serialized_end=201
  _CLIENT._serialized_start=203
  _CLIENT._serialized_end=269
  _MUSIC._serialized_start=271
  _MUSIC._serialized_end=332
  _LIGHT._serialized_start=334
  _LIGHT._serialized_end=455
  _URO._serialized_start=457
  _URO._serialized_end=492
  _NETWORKCRE._serialized_start=494
  _NETWORKCRE._serialized_end=560
# @@protoc_insertion_point(module_scope)
