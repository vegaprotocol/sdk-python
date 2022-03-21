# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/commands/v1/transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...commands.v1 import commands_pb2 as vega_dot_commands_dot_v1_dot_commands__pb2
from ...commands.v1 import validator_commands_pb2 as vega_dot_commands_dot_v1_dot_validator__commands__pb2
from ...commands.v1 import oracles_pb2 as vega_dot_commands_dot_v1_dot_oracles__pb2
from ...commands.v1 import signature_pb2 as vega_dot_commands_dot_v1_dot_signature__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vega/commands/v1/transaction.proto',
  package='vega.commands.v1',
  syntax='proto3',
  serialized_options=_b('Z,code.vegaprotocol.io/protos/vega/commands/v1'),
  serialized_pb=_b('\n\"vega/commands/v1/transaction.proto\x12\x10vega.commands.v1\x1a\x1fvega/commands/v1/commands.proto\x1a)vega/commands/v1/validator_commands.proto\x1a\x1evega/commands/v1/oracles.proto\x1a vega/commands/v1/signature.proto\"\xec\x0f\n\tInputData\x12\x14\n\x05nonce\x18\x01 \x01(\x04R\x05nonce\x12!\n\x0c\x62lock_height\x18\x02 \x01(\x04R\x0b\x62lockHeight\x12O\n\x10order_submission\x18\xe9\x07 \x01(\x0b\x32!.vega.commands.v1.OrderSubmissionH\x00R\x0forderSubmission\x12U\n\x12order_cancellation\x18\xea\x07 \x01(\x0b\x32#.vega.commands.v1.OrderCancellationH\x00R\x11orderCancellation\x12L\n\x0forder_amendment\x18\xeb\x07 \x01(\x0b\x32 .vega.commands.v1.OrderAmendmentH\x00R\x0eorderAmendment\x12X\n\x13withdraw_submission\x18\xec\x07 \x01(\x0b\x32$.vega.commands.v1.WithdrawSubmissionH\x00R\x12withdrawSubmission\x12X\n\x13proposal_submission\x18\xed\x07 \x01(\x0b\x32$.vega.commands.v1.ProposalSubmissionH\x00R\x12proposalSubmission\x12L\n\x0fvote_submission\x18\xee\x07 \x01(\x0b\x32 .vega.commands.v1.VoteSubmissionH\x00R\x0evoteSubmission\x12w\n\x1eliquidity_provision_submission\x18\xef\x07 \x01(\x0b\x32..vega.commands.v1.LiquidityProvisionSubmissionH\x00R\x1cliquidityProvisionSubmission\x12X\n\x13\x64\x65legate_submission\x18\xf0\x07 \x01(\x0b\x32$.vega.commands.v1.DelegateSubmissionH\x00R\x12\x64\x65legateSubmission\x12^\n\x15undelegate_submission\x18\xf1\x07 \x01(\x0b\x32&.vega.commands.v1.UndelegateSubmissionH\x00R\x14undelegateSubmission\x12}\n liquidity_provision_cancellation\x18\xf2\x07 \x01(\x0b\x32\x30.vega.commands.v1.LiquidityProvisionCancellationH\x00R\x1eliquidityProvisionCancellation\x12t\n\x1dliquidity_provision_amendment\x18\xf3\x07 \x01(\x0b\x32-.vega.commands.v1.LiquidityProvisionAmendmentH\x00R\x1bliquidityProvisionAmendment\x12\x39\n\x08transfer\x18\xf4\x07 \x01(\x0b\x32\x1a.vega.commands.v1.TransferH\x00R\x08transfer\x12L\n\x0f\x63\x61ncel_transfer\x18\xf5\x07 \x01(\x0b\x32 .vega.commands.v1.CancelTransferH\x00R\x0e\x63\x61ncelTransfer\x12\x46\n\rannounce_node\x18\xf6\x07 \x01(\x0b\x32\x1e.vega.commands.v1.AnnounceNodeH\x00R\x0c\x61nnounceNode\x12:\n\tnode_vote\x18\xd2\x0f \x01(\x0b\x32\x1a.vega.commands.v1.NodeVoteH\x00R\x08nodeVote\x12I\n\x0enode_signature\x18\xd3\x0f \x01(\x0b\x32\x1f.vega.commands.v1.NodeSignatureH\x00R\rnodeSignature\x12@\n\x0b\x63hain_event\x18\xd4\x0f \x01(\x0b\x32\x1c.vega.commands.v1.ChainEventH\x00R\nchainEvent\x12\\\n\x15key_rotate_submission\x18\xd5\x0f \x01(\x0b\x32%.vega.commands.v1.KeyRotateSubmissionH\x00R\x13keyRotateSubmission\x12\x62\n\x17state_variable_proposal\x18\xd6\x0f \x01(\x0b\x32\'.vega.commands.v1.StateVariableProposalH\x00R\x15stateVariableProposal\x12X\n\x13validator_heartbeat\x18\xd7\x0f \x01(\x0b\x32$.vega.commands.v1.ValidatorHeartbeatH\x00R\x12validatorHeartbeat\x12_\n\x16oracle_data_submission\x18\xb9\x17 \x01(\x0b\x32&.vega.commands.v1.OracleDataSubmissionH\x00R\x14oracleDataSubmission\x12\x64\n\x1brestore_snapshot_submission\x18\xa1\x1f \x01(\x0b\x32!.vega.commands.v1.RestoreSnapshotH\x00R\x19restoreSnapshotSubmissionB\t\n\x07\x63ommand\"\xc3\x01\n\x0bTransaction\x12\x1d\n\ninput_data\x18\x01 \x01(\x0cR\tinputData\x12\x39\n\tsignature\x18\x02 \x01(\x0b\x32\x1b.vega.commands.v1.SignatureR\tsignature\x12\x1b\n\x07\x61\x64\x64ress\x18\xe9\x07 \x01(\tH\x00R\x07\x61\x64\x64ress\x12\x1a\n\x07pub_key\x18\xea\x07 \x01(\tH\x00R\x06pubKey\x12\x19\n\x07version\x18\xd0\x0f \x01(\rR\x07versionB\x06\n\x04\x66romB.Z,code.vegaprotocol.io/protos/vega/commands/v1b\x06proto3')
  ,
  dependencies=[vega_dot_commands_dot_v1_dot_commands__pb2.DESCRIPTOR,vega_dot_commands_dot_v1_dot_validator__commands__pb2.DESCRIPTOR,vega_dot_commands_dot_v1_dot_oracles__pb2.DESCRIPTOR,vega_dot_commands_dot_v1_dot_signature__pb2.DESCRIPTOR,])




_INPUTDATA = _descriptor.Descriptor(
  name='InputData',
  full_name='vega.commands.v1.InputData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='vega.commands.v1.InputData.nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nonce', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='vega.commands.v1.InputData.block_height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='blockHeight', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_submission', full_name='vega.commands.v1.InputData.order_submission', index=2,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='orderSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_cancellation', full_name='vega.commands.v1.InputData.order_cancellation', index=3,
      number=1002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='orderCancellation', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_amendment', full_name='vega.commands.v1.InputData.order_amendment', index=4,
      number=1003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='orderAmendment', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdraw_submission', full_name='vega.commands.v1.InputData.withdraw_submission', index=5,
      number=1004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='withdrawSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposal_submission', full_name='vega.commands.v1.InputData.proposal_submission', index=6,
      number=1005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='proposalSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote_submission', full_name='vega.commands.v1.InputData.vote_submission', index=7,
      number=1006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='voteSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liquidity_provision_submission', full_name='vega.commands.v1.InputData.liquidity_provision_submission', index=8,
      number=1007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='liquidityProvisionSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegate_submission', full_name='vega.commands.v1.InputData.delegate_submission', index=9,
      number=1008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delegateSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='undelegate_submission', full_name='vega.commands.v1.InputData.undelegate_submission', index=10,
      number=1009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='undelegateSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liquidity_provision_cancellation', full_name='vega.commands.v1.InputData.liquidity_provision_cancellation', index=11,
      number=1010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='liquidityProvisionCancellation', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liquidity_provision_amendment', full_name='vega.commands.v1.InputData.liquidity_provision_amendment', index=12,
      number=1011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='liquidityProvisionAmendment', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer', full_name='vega.commands.v1.InputData.transfer', index=13,
      number=1012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transfer', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancel_transfer', full_name='vega.commands.v1.InputData.cancel_transfer', index=14,
      number=1013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cancelTransfer', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='announce_node', full_name='vega.commands.v1.InputData.announce_node', index=15,
      number=1014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='announceNode', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_vote', full_name='vega.commands.v1.InputData.node_vote', index=16,
      number=2002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeVote', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_signature', full_name='vega.commands.v1.InputData.node_signature', index=17,
      number=2003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeSignature', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_event', full_name='vega.commands.v1.InputData.chain_event', index=18,
      number=2004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chainEvent', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_rotate_submission', full_name='vega.commands.v1.InputData.key_rotate_submission', index=19,
      number=2005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keyRotateSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_variable_proposal', full_name='vega.commands.v1.InputData.state_variable_proposal', index=20,
      number=2006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stateVariableProposal', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_heartbeat', full_name='vega.commands.v1.InputData.validator_heartbeat', index=21,
      number=2007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validatorHeartbeat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oracle_data_submission', full_name='vega.commands.v1.InputData.oracle_data_submission', index=22,
      number=3001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='oracleDataSubmission', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restore_snapshot_submission', full_name='vega.commands.v1.InputData.restore_snapshot_submission', index=23,
      number=4001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='restoreSnapshotSubmission', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='command', full_name='vega.commands.v1.InputData.command',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=199,
  serialized_end=2227,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='vega.commands.v1.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_data', full_name='vega.commands.v1.Transaction.input_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='inputData', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='vega.commands.v1.Transaction.signature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signature', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='vega.commands.v1.Transaction.address', index=2,
      number=1001, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='vega.commands.v1.Transaction.pub_key', index=3,
      number=1002, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pubKey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='vega.commands.v1.Transaction.version', index=4,
      number=2000, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='from', full_name='vega.commands.v1.Transaction.from',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=2230,
  serialized_end=2425,
)

_INPUTDATA.fields_by_name['order_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._ORDERSUBMISSION
_INPUTDATA.fields_by_name['order_cancellation'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._ORDERCANCELLATION
_INPUTDATA.fields_by_name['order_amendment'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._ORDERAMENDMENT
_INPUTDATA.fields_by_name['withdraw_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._WITHDRAWSUBMISSION
_INPUTDATA.fields_by_name['proposal_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._PROPOSALSUBMISSION
_INPUTDATA.fields_by_name['vote_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._VOTESUBMISSION
_INPUTDATA.fields_by_name['liquidity_provision_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._LIQUIDITYPROVISIONSUBMISSION
_INPUTDATA.fields_by_name['delegate_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._DELEGATESUBMISSION
_INPUTDATA.fields_by_name['undelegate_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._UNDELEGATESUBMISSION
_INPUTDATA.fields_by_name['liquidity_provision_cancellation'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._LIQUIDITYPROVISIONCANCELLATION
_INPUTDATA.fields_by_name['liquidity_provision_amendment'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._LIQUIDITYPROVISIONAMENDMENT
_INPUTDATA.fields_by_name['transfer'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._TRANSFER
_INPUTDATA.fields_by_name['cancel_transfer'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._CANCELTRANSFER
_INPUTDATA.fields_by_name['announce_node'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._ANNOUNCENODE
_INPUTDATA.fields_by_name['node_vote'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._NODEVOTE
_INPUTDATA.fields_by_name['node_signature'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._NODESIGNATURE
_INPUTDATA.fields_by_name['chain_event'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._CHAINEVENT
_INPUTDATA.fields_by_name['key_rotate_submission'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._KEYROTATESUBMISSION
_INPUTDATA.fields_by_name['state_variable_proposal'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._STATEVARIABLEPROPOSAL
_INPUTDATA.fields_by_name['validator_heartbeat'].message_type = vega_dot_commands_dot_v1_dot_validator__commands__pb2._VALIDATORHEARTBEAT
_INPUTDATA.fields_by_name['oracle_data_submission'].message_type = vega_dot_commands_dot_v1_dot_oracles__pb2._ORACLEDATASUBMISSION
_INPUTDATA.fields_by_name['restore_snapshot_submission'].message_type = vega_dot_commands_dot_v1_dot_commands__pb2._RESTORESNAPSHOT
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['order_submission'])
_INPUTDATA.fields_by_name['order_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['order_cancellation'])
_INPUTDATA.fields_by_name['order_cancellation'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['order_amendment'])
_INPUTDATA.fields_by_name['order_amendment'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['withdraw_submission'])
_INPUTDATA.fields_by_name['withdraw_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['proposal_submission'])
_INPUTDATA.fields_by_name['proposal_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['vote_submission'])
_INPUTDATA.fields_by_name['vote_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['liquidity_provision_submission'])
_INPUTDATA.fields_by_name['liquidity_provision_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['delegate_submission'])
_INPUTDATA.fields_by_name['delegate_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['undelegate_submission'])
_INPUTDATA.fields_by_name['undelegate_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['liquidity_provision_cancellation'])
_INPUTDATA.fields_by_name['liquidity_provision_cancellation'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['liquidity_provision_amendment'])
_INPUTDATA.fields_by_name['liquidity_provision_amendment'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['transfer'])
_INPUTDATA.fields_by_name['transfer'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['cancel_transfer'])
_INPUTDATA.fields_by_name['cancel_transfer'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['announce_node'])
_INPUTDATA.fields_by_name['announce_node'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['node_vote'])
_INPUTDATA.fields_by_name['node_vote'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['node_signature'])
_INPUTDATA.fields_by_name['node_signature'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['chain_event'])
_INPUTDATA.fields_by_name['chain_event'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['key_rotate_submission'])
_INPUTDATA.fields_by_name['key_rotate_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['state_variable_proposal'])
_INPUTDATA.fields_by_name['state_variable_proposal'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['validator_heartbeat'])
_INPUTDATA.fields_by_name['validator_heartbeat'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['oracle_data_submission'])
_INPUTDATA.fields_by_name['oracle_data_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_INPUTDATA.oneofs_by_name['command'].fields.append(
  _INPUTDATA.fields_by_name['restore_snapshot_submission'])
_INPUTDATA.fields_by_name['restore_snapshot_submission'].containing_oneof = _INPUTDATA.oneofs_by_name['command']
_TRANSACTION.fields_by_name['signature'].message_type = vega_dot_commands_dot_v1_dot_signature__pb2._SIGNATURE
_TRANSACTION.oneofs_by_name['from'].fields.append(
  _TRANSACTION.fields_by_name['address'])
_TRANSACTION.fields_by_name['address'].containing_oneof = _TRANSACTION.oneofs_by_name['from']
_TRANSACTION.oneofs_by_name['from'].fields.append(
  _TRANSACTION.fields_by_name['pub_key'])
_TRANSACTION.fields_by_name['pub_key'].containing_oneof = _TRANSACTION.oneofs_by_name['from']
DESCRIPTOR.message_types_by_name['InputData'] = _INPUTDATA
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputData = _reflection.GeneratedProtocolMessageType('InputData', (_message.Message,), dict(
  DESCRIPTOR = _INPUTDATA,
  __module__ = 'vega.commands.v1.transaction_pb2'
  # @@protoc_insertion_point(class_scope:vega.commands.v1.InputData)
  ))
_sym_db.RegisterMessage(InputData)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'vega.commands.v1.transaction_pb2'
  # @@protoc_insertion_point(class_scope:vega.commands.v1.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
