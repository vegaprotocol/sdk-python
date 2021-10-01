# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ...coreapi.v1 import coreapi_pb2 as vega_dot_coreapi_dot_v1_dot_coreapi__pb2


class CoreApiServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAccounts = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListAccounts',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAccountsRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAccountsResponse.FromString,
                )
        self.ListAssets = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListAssets',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAssetsRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAssetsResponse.FromString,
                )
        self.ListNetworkParameters = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListNetworkParameters',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListNetworkParametersRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListNetworkParametersResponse.FromString,
                )
        self.ListParties = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListParties',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesResponse.FromString,
                )
        self.ListValidators = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListValidators',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListValidatorsRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListValidatorsResponse.FromString,
                )
        self.ListMarkets = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListMarkets',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsResponse.FromString,
                )
        self.ListProposals = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListProposals',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListProposalsRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListProposalsResponse.FromString,
                )
        self.ListMarketsData = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListMarketsData',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsDataRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsDataResponse.FromString,
                )
        self.ListVotes = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListVotes',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListVotesRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListVotesResponse.FromString,
                )
        self.ListPartiesStake = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListPartiesStake',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesStakeRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesStakeResponse.FromString,
                )
        self.ListDelegations = channel.unary_unary(
                '/vega.coreapi.v1.CoreApiService/ListDelegations',
                request_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListDelegationsRequest.SerializeToString,
                response_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListDelegationsResponse.FromString,
                )


class CoreApiServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListAccounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAssets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNetworkParameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListParties(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListValidators(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMarkets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProposals(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMarketsData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVotes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPartiesStake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDelegations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoreApiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccounts,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAccountsRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAccountsResponse.SerializeToString,
            ),
            'ListAssets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAssets,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAssetsRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAssetsResponse.SerializeToString,
            ),
            'ListNetworkParameters': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNetworkParameters,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListNetworkParametersRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListNetworkParametersResponse.SerializeToString,
            ),
            'ListParties': grpc.unary_unary_rpc_method_handler(
                    servicer.ListParties,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesResponse.SerializeToString,
            ),
            'ListValidators': grpc.unary_unary_rpc_method_handler(
                    servicer.ListValidators,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListValidatorsRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListValidatorsResponse.SerializeToString,
            ),
            'ListMarkets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMarkets,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsResponse.SerializeToString,
            ),
            'ListProposals': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProposals,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListProposalsRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListProposalsResponse.SerializeToString,
            ),
            'ListMarketsData': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMarketsData,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsDataRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsDataResponse.SerializeToString,
            ),
            'ListVotes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListVotes,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListVotesRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListVotesResponse.SerializeToString,
            ),
            'ListPartiesStake': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPartiesStake,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesStakeRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesStakeResponse.SerializeToString,
            ),
            'ListDelegations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDelegations,
                    request_deserializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListDelegationsRequest.FromString,
                    response_serializer=vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListDelegationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vega.coreapi.v1.CoreApiService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CoreApiService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListAccounts',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAccountsRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAssets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListAssets',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAssetsRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListAssetsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNetworkParameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListNetworkParameters',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListNetworkParametersRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListNetworkParametersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListParties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListParties',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListValidators(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListValidators',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListValidatorsRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListValidatorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMarkets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListMarkets',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProposals(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListProposals',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListProposalsRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListProposalsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMarketsData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListMarketsData',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsDataRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListMarketsDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListVotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListVotes',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListVotesRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListVotesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPartiesStake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListPartiesStake',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesStakeRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListPartiesStakeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDelegations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vega.coreapi.v1.CoreApiService/ListDelegations',
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListDelegationsRequest.SerializeToString,
            vega_dot_coreapi_dot_v1_dot_coreapi__pb2.ListDelegationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
