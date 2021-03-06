# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dsws.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dsws.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndsws.proto\x1a\x1bgoogle/protobuf/empty.proto\"&\n\rLocationClass\x12\x15\n\rLocationClass\x18\x01 \x01(\t\" \n\x0cLocationName\x12\x10\n\x08Location\x18\x01 \x01(\t\".\n\x08Location\x12\x10\n\x08Location\x18\x01 \x01(\t\x12\x10\n\x08MeasType\x18\x02 \x01(\t\"F\n\rLocationEvent\x12\x10\n\x08Location\x18\x01 \x01(\t\x12\x10\n\x08MeasType\x18\x02 \x01(\t\x12\x11\n\tMeasValue\x18\x03 \x01(\t\"B\n\x0bSensorEvent\x12\x0e\n\x06Sensor\x18\x01 \x01(\t\x12\x10\n\x08MeasType\x18\x02 \x01(\t\x12\x11\n\tMeasValue\x18\x03 \x01(\t\"P\n\x05\x45vent\x12\x10\n\x08\x44\x61teTime\x18\x01 \x01(\t\x12\x10\n\x08Location\x18\x02 \x01(\t\x12\x10\n\x08MeasType\x18\x03 \x01(\t\x12\x11\n\tMeasValue\x18\x04 \x01(\t\"\x1c\n\x08SensorId\x12\x10\n\x08SensorId\x18\x01 \x01(\t\"2\n\x0cSensorConfig\x12\x10\n\x08SensorId\x18\x01 \x01(\t\x12\x10\n\x08Location\x18\x02 \x01(\t\"B\n\nSensorInfo\x12\x10\n\x08SensorId\x18\x01 \x01(\t\x12\x10\n\x08Location\x18\x02 \x01(\t\x12\x10\n\x08LastSeen\x18\x03 \x01(\t2\x8d\x08\n\x0b\x45ventServer\x12=\n\x13NotifyLocationEvent\x12\x0e.LocationEvent\x1a\x16.google.protobuf.Empty\x12\x39\n\x11NotifySensorEvent\x12\x0c.SensorEvent\x1a\x16.google.protobuf.Empty\x12\x33\n\x0fGetLatestEvents\x12\x16.google.protobuf.Empty\x1a\x06.Event0\x01\x12\x34\n\x10GetMinimumEvents\x12\x16.google.protobuf.Empty\x1a\x06.Event0\x01\x12\x34\n\x10GetMaximumEvents\x12\x16.google.protobuf.Empty\x1a\x06.Event0\x01\x12\x34\n\x10GetUnknownEvents\x12\x16.google.protobuf.Empty\x1a\x06.Event0\x01\x12\x44\n\x12\x43learUnknownEvents\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12:\n\x0fGetAllLocations\x12\x16.google.protobuf.Empty\x1a\r.LocationName0\x01\x12\x33\n\x0cGetLocations\x12\x16.google.protobuf.Empty\x1a\t.Location0\x01\x12(\n\x11GetLocationEvents\x12\t.Location\x1a\x06.Event0\x01\x12\x32\n\x16GetLocationClassEvents\x12\x0e.LocationClass\x1a\x06.Event0\x01\x12\x34\n\x10GetSummaryEvents\x12\x16.google.protobuf.Empty\x1a\x06.Event0\x01\x12\x30\n\x0cGetAllEvents\x12\x16.google.protobuf.Empty\x1a\x06.Event0\x01\x12\x31\n\x0c\x44\x65leteSensor\x12\t.SensorId\x1a\x16.google.protobuf.Empty\x12\x35\n\x0c\x43onfigSensor\x12\r.SensorConfig\x1a\x16.google.protobuf.Empty\x12G\n\x15\x44\x65leteClimeMetSensors\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\x45\n\x13\x44\x65leteUnseenSensors\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\x36\n\rGetSensorInfo\x12\x16.google.protobuf.Empty\x1a\x0b.SensorInfo0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_LOCATIONCLASS = _descriptor.Descriptor(
  name='LocationClass',
  full_name='LocationClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='LocationClass', full_name='LocationClass.LocationClass', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=43,
  serialized_end=81,
)


_LOCATIONNAME = _descriptor.Descriptor(
  name='LocationName',
  full_name='LocationName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Location', full_name='LocationName.Location', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=83,
  serialized_end=115,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Location', full_name='Location.Location', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasType', full_name='Location.MeasType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=117,
  serialized_end=163,
)


_LOCATIONEVENT = _descriptor.Descriptor(
  name='LocationEvent',
  full_name='LocationEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Location', full_name='LocationEvent.Location', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasType', full_name='LocationEvent.MeasType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasValue', full_name='LocationEvent.MeasValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=165,
  serialized_end=235,
)


_SENSOREVENT = _descriptor.Descriptor(
  name='SensorEvent',
  full_name='SensorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Sensor', full_name='SensorEvent.Sensor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasType', full_name='SensorEvent.MeasType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasValue', full_name='SensorEvent.MeasValue', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=237,
  serialized_end=303,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DateTime', full_name='Event.DateTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Location', full_name='Event.Location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasType', full_name='Event.MeasType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MeasValue', full_name='Event.MeasValue', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=305,
  serialized_end=385,
)


_SENSORID = _descriptor.Descriptor(
  name='SensorId',
  full_name='SensorId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SensorId', full_name='SensorId.SensorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=387,
  serialized_end=415,
)


_SENSORCONFIG = _descriptor.Descriptor(
  name='SensorConfig',
  full_name='SensorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SensorId', full_name='SensorConfig.SensorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Location', full_name='SensorConfig.Location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=417,
  serialized_end=467,
)


_SENSORINFO = _descriptor.Descriptor(
  name='SensorInfo',
  full_name='SensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SensorId', full_name='SensorInfo.SensorId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Location', full_name='SensorInfo.Location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LastSeen', full_name='SensorInfo.LastSeen', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=469,
  serialized_end=535,
)

DESCRIPTOR.message_types_by_name['LocationClass'] = _LOCATIONCLASS
DESCRIPTOR.message_types_by_name['LocationName'] = _LOCATIONNAME
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['LocationEvent'] = _LOCATIONEVENT
DESCRIPTOR.message_types_by_name['SensorEvent'] = _SENSOREVENT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['SensorId'] = _SENSORID
DESCRIPTOR.message_types_by_name['SensorConfig'] = _SENSORCONFIG
DESCRIPTOR.message_types_by_name['SensorInfo'] = _SENSORINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationClass = _reflection.GeneratedProtocolMessageType('LocationClass', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONCLASS,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:LocationClass)
  })
_sym_db.RegisterMessage(LocationClass)

LocationName = _reflection.GeneratedProtocolMessageType('LocationName', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONNAME,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:LocationName)
  })
_sym_db.RegisterMessage(LocationName)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

LocationEvent = _reflection.GeneratedProtocolMessageType('LocationEvent', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONEVENT,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:LocationEvent)
  })
_sym_db.RegisterMessage(LocationEvent)

SensorEvent = _reflection.GeneratedProtocolMessageType('SensorEvent', (_message.Message,), {
  'DESCRIPTOR' : _SENSOREVENT,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:SensorEvent)
  })
_sym_db.RegisterMessage(SensorEvent)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:Event)
  })
_sym_db.RegisterMessage(Event)

SensorId = _reflection.GeneratedProtocolMessageType('SensorId', (_message.Message,), {
  'DESCRIPTOR' : _SENSORID,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:SensorId)
  })
_sym_db.RegisterMessage(SensorId)

SensorConfig = _reflection.GeneratedProtocolMessageType('SensorConfig', (_message.Message,), {
  'DESCRIPTOR' : _SENSORCONFIG,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:SensorConfig)
  })
_sym_db.RegisterMessage(SensorConfig)

SensorInfo = _reflection.GeneratedProtocolMessageType('SensorInfo', (_message.Message,), {
  'DESCRIPTOR' : _SENSORINFO,
  '__module__' : 'dsws_pb2'
  # @@protoc_insertion_point(class_scope:SensorInfo)
  })
_sym_db.RegisterMessage(SensorInfo)



_EVENTSERVER = _descriptor.ServiceDescriptor(
  name='EventServer',
  full_name='EventServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=538,
  serialized_end=1575,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyLocationEvent',
    full_name='EventServer.NotifyLocationEvent',
    index=0,
    containing_service=None,
    input_type=_LOCATIONEVENT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NotifySensorEvent',
    full_name='EventServer.NotifySensorEvent',
    index=1,
    containing_service=None,
    input_type=_SENSOREVENT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLatestEvents',
    full_name='EventServer.GetLatestEvents',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMinimumEvents',
    full_name='EventServer.GetMinimumEvents',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMaximumEvents',
    full_name='EventServer.GetMaximumEvents',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUnknownEvents',
    full_name='EventServer.GetUnknownEvents',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClearUnknownEvents',
    full_name='EventServer.ClearUnknownEvents',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllLocations',
    full_name='EventServer.GetAllLocations',
    index=7,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LOCATIONNAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocations',
    full_name='EventServer.GetLocations',
    index=8,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocationEvents',
    full_name='EventServer.GetLocationEvents',
    index=9,
    containing_service=None,
    input_type=_LOCATION,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocationClassEvents',
    full_name='EventServer.GetLocationClassEvents',
    index=10,
    containing_service=None,
    input_type=_LOCATIONCLASS,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSummaryEvents',
    full_name='EventServer.GetSummaryEvents',
    index=11,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllEvents',
    full_name='EventServer.GetAllEvents',
    index=12,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSensor',
    full_name='EventServer.DeleteSensor',
    index=13,
    containing_service=None,
    input_type=_SENSORID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConfigSensor',
    full_name='EventServer.ConfigSensor',
    index=14,
    containing_service=None,
    input_type=_SENSORCONFIG,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteClimeMetSensors',
    full_name='EventServer.DeleteClimeMetSensors',
    index=15,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUnseenSensors',
    full_name='EventServer.DeleteUnseenSensors',
    index=16,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSensorInfo',
    full_name='EventServer.GetSensorInfo',
    index=17,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SENSORINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSERVER)

DESCRIPTOR.services_by_name['EventServer'] = _EVENTSERVER

# @@protoc_insertion_point(module_scope)
