from .generated.data_node.api.v1 import trading_data_grpc
from .grpcclient import GRPCClient


class VegaTradingDataClient(GRPCClient):
    """
    The Vega Core State Client talks to a back-end node.
    """

    def __init__(self, url: str, channel=None) -> None:
        super().__init__(url, channel=channel)
        self._corestate = trading_data_grpc.TradingDataServiceStub(self.channel)

    def __getattr__(self, funcname):
        return getattr(self._corestate, funcname)
