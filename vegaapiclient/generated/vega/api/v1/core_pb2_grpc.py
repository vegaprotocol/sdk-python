# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ...api.v1 import core_pb2 as vega_dot_api_dot_v1_dot_core__pb2


class CoreServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubmitTransaction = channel.unary_unary(
                '/vega.api.v1.CoreService/SubmitTransaction',
                request_serializer=vega_dot_api_dot_v1_dot_core__pb2.SubmitTransactionRequest.SerializeToString,
                response_deserializer=vega_dot_api_dot_v1_dot_core__pb2.SubmitTransactionResponse.FromString,
                )
        self.PropagateChainEvent = channel.unary_unary(
                '/vega.api.v1.CoreService/PropagateChainEvent',
                request_serializer=vega_dot_api_dot_v1_dot_core__pb2.PropagateChainEventRequest.SerializeToString,
                response_deserializer=vega_dot_api_dot_v1_dot_core__pb2.PropagateChainEventResponse.FromString,
                )
        self.Statistics = channel.unary_unary(
                '/vega.api.v1.CoreService/Statistics',
                request_serializer=vega_dot_api_dot_v1_dot_core__pb2.StatisticsRequest.SerializeToString,
                response_deserializer=vega_dot_api_dot_v1_dot_core__pb2.StatisticsResponse.FromString,
                )
        self.LastBlockHeight = channel.unary_unary(
                '/vega.api.v1.CoreService/LastBlockHeight',
                request_serializer=vega_dot_api_dot_v1_dot_core__pb2.LastBlockHeightRequest.SerializeToString,
                response_deserializer=vega_dot_api_dot_v1_dot_core__pb2.LastBlockHeightResponse.FromString,
                )
        self.GetVegaTime = channel.unary_unary(
                '/vega.api.v1.CoreService/GetVegaTime',
                request_serializer=vega_dot_api_dot_v1_dot_core__pb2.GetVegaTimeRequest.SerializeToString,
                response_deserializer=vega_dot_api_dot_v1_dot_core__pb2.GetVegaTimeResponse.FromString,
                )
        self.ObserveEventBus = channel.stream_stream(
                '/vega.api.v1.CoreService/ObserveEventBus',
                request_serializer=vega_dot_api_dot_v1_dot_core__pb2.ObserveEventBusRequest.SerializeToString,
                response_deserializer=vega_dot_api_dot_v1_dot_core__pb2.ObserveEventBusResponse.FromString,
                )


class CoreServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubmitTransaction(self, request, context):
        """Submit a signed transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateChainEvent(self, request, context):
        """Propagate a chain event
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Statistics(self, request, context):
        """Get Statistics on Vega
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastBlockHeight(self, request, context):
        """Get the height of the last tendermint block
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVegaTime(self, request, context):
        """Get Time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObserveEventBus(self, request_iterator, context):
        """Subscribe to a stream of events from the core
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubmitTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitTransaction,
                    request_deserializer=vega_dot_api_dot_v1_dot_core__pb2.SubmitTransactionRequest.FromString,
                    response_serializer=vega_dot_api_dot_v1_dot_core__pb2.SubmitTransactionResponse.SerializeToString,
            ),
            'PropagateChainEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateChainEvent,
                    request_deserializer=vega_dot_api_dot_v1_dot_core__pb2.PropagateChainEventRequest.FromString,
                    response_serializer=vega_dot_api_dot_v1_dot_core__pb2.PropagateChainEventResponse.SerializeToString,
            ),
            'Statistics': grpc.unary_unary_rpc_method_handler(
                    servicer.Statistics,
                    request_deserializer=vega_dot_api_dot_v1_dot_core__pb2.StatisticsRequest.FromString,
                    response_serializer=vega_dot_api_dot_v1_dot_core__pb2.StatisticsResponse.SerializeToString,
            ),
            'LastBlockHeight': grpc.unary_unary_rpc_method_handler(
                    servicer.LastBlockHeight,
                    request_deserializer=vega_dot_api_dot_v1_dot_core__pb2.LastBlockHeightRequest.FromString,
                    response_serializer=vega_dot_api_dot_v1_dot_core__pb2.LastBlockHeightResponse.SerializeToString,
            ),
            'GetVegaTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVegaTime,
                    request_deserializer=vega_dot_api_dot_v1_dot_core__pb2.GetVegaTimeRequest.FromString,
                    response_serializer=vega_dot_api_dot_v1_dot_core__pb2.GetVegaTimeResponse.SerializeToString,
            ),
            'ObserveEventBus': grpc.stream_stream_rpc_method_handler(
                    servicer.ObserveEventBus,
                    request_deserializer=vega_dot_api_dot_v1_dot_core__pb2.ObserveEventBusRequest.FromString,
                    response_serializer=vega_dot_api_dot_v1_dot_core__pb2.ObserveEventBusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vega.api.v1.CoreService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CoreService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubmitTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.api.v1.CoreService/SubmitTransaction',
            vega_dot_api_dot_v1_dot_core__pb2.SubmitTransactionRequest.SerializeToString,
            vega_dot_api_dot_v1_dot_core__pb2.SubmitTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateChainEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.api.v1.CoreService/PropagateChainEvent',
            vega_dot_api_dot_v1_dot_core__pb2.PropagateChainEventRequest.SerializeToString,
            vega_dot_api_dot_v1_dot_core__pb2.PropagateChainEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Statistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.api.v1.CoreService/Statistics',
            vega_dot_api_dot_v1_dot_core__pb2.StatisticsRequest.SerializeToString,
            vega_dot_api_dot_v1_dot_core__pb2.StatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastBlockHeight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.api.v1.CoreService/LastBlockHeight',
            vega_dot_api_dot_v1_dot_core__pb2.LastBlockHeightRequest.SerializeToString,
            vega_dot_api_dot_v1_dot_core__pb2.LastBlockHeightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVegaTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.api.v1.CoreService/GetVegaTime',
            vega_dot_api_dot_v1_dot_core__pb2.GetVegaTimeRequest.SerializeToString,
            vega_dot_api_dot_v1_dot_core__pb2.GetVegaTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ObserveEventBus(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vega.api.v1.CoreService/ObserveEventBus',
            vega_dot_api_dot_v1_dot_core__pb2.ObserveEventBusRequest.SerializeToString,
            vega_dot_api_dot_v1_dot_core__pb2.ObserveEventBusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)