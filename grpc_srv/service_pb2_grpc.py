# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

# Using try except to make sure this script could be called independently or through flask app (from different dir)
try:
    import service_pb2 as service__pb2
except:
    import grpc_srv.service_pb2 as service__pb2


class CalStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add_matrix = channel.unary_unary(
            '/Cal/add_matrix',
            request_serializer=service__pb2.request_msg.SerializeToString,
            response_deserializer=service__pb2.response_msg.FromString,
        )
        self.mul_matrix = channel.unary_unary(
            '/Cal/mul_matrix',
            request_serializer=service__pb2.request_msg.SerializeToString,
            response_deserializer=service__pb2.response_msg.FromString,
        )


class CalServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add_matrix(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mul_matrix(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'add_matrix':
        grpc.unary_unary_rpc_method_handler(
            servicer.add_matrix,
            request_deserializer=service__pb2.request_msg.FromString,
            response_serializer=service__pb2.response_msg.SerializeToString,
        ),
        'mul_matrix':
        grpc.unary_unary_rpc_method_handler(
            servicer.mul_matrix,
            request_deserializer=service__pb2.request_msg.FromString,
            response_serializer=service__pb2.response_msg.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Cal', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class Cal(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add_matrix(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/Cal/add_matrix',
            service__pb2.request_msg.SerializeToString,
            service__pb2.response_msg.FromString, options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)

    @staticmethod
    def mul_matrix(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/Cal/mul_matrix',
            service__pb2.request_msg.SerializeToString,
            service__pb2.response_msg.FromString, options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout,
            metadata)
