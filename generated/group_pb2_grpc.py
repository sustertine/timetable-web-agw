# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import group_pb2 as group__pb2


class GroupGrpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindAll = channel.unary_unary(
                '/GroupGrpcService/FindAll',
                request_serializer=group__pb2.EmptyProto.SerializeToString,
                response_deserializer=group__pb2.GroupListProto.FromString,
                )
        self.FindById = channel.unary_unary(
                '/GroupGrpcService/FindById',
                request_serializer=group__pb2.GroupIdProto.SerializeToString,
                response_deserializer=group__pb2.GroupProto.FromString,
                )
        self.Create = channel.unary_unary(
                '/GroupGrpcService/Create',
                request_serializer=group__pb2.CreateGroupProto.SerializeToString,
                response_deserializer=group__pb2.GroupProto.FromString,
                )
        self.Delete = channel.unary_unary(
                '/GroupGrpcService/Delete',
                request_serializer=group__pb2.GroupIdProto.SerializeToString,
                response_deserializer=group__pb2.EmptyProto.FromString,
                )
        self.Update = channel.unary_unary(
                '/GroupGrpcService/Update',
                request_serializer=group__pb2.GroupProto.SerializeToString,
                response_deserializer=group__pb2.GroupProto.FromString,
                )


class GroupGrpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GroupGrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindAll': grpc.unary_unary_rpc_method_handler(
                    servicer.FindAll,
                    request_deserializer=group__pb2.EmptyProto.FromString,
                    response_serializer=group__pb2.GroupListProto.SerializeToString,
            ),
            'FindById': grpc.unary_unary_rpc_method_handler(
                    servicer.FindById,
                    request_deserializer=group__pb2.GroupIdProto.FromString,
                    response_serializer=group__pb2.GroupProto.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=group__pb2.CreateGroupProto.FromString,
                    response_serializer=group__pb2.GroupProto.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=group__pb2.GroupIdProto.FromString,
                    response_serializer=group__pb2.EmptyProto.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=group__pb2.GroupProto.FromString,
                    response_serializer=group__pb2.GroupProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GroupGrpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GroupGrpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GroupGrpcService/FindAll',
            group__pb2.EmptyProto.SerializeToString,
            group__pb2.GroupListProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GroupGrpcService/FindById',
            group__pb2.GroupIdProto.SerializeToString,
            group__pb2.GroupProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GroupGrpcService/Create',
            group__pb2.CreateGroupProto.SerializeToString,
            group__pb2.GroupProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GroupGrpcService/Delete',
            group__pb2.GroupIdProto.SerializeToString,
            group__pb2.EmptyProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GroupGrpcService/Update',
            group__pb2.GroupProto.SerializeToString,
            group__pb2.GroupProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
