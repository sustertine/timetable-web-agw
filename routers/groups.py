import json

import grpc
from fastapi import APIRouter
import sys
import os

from routers.group_dtos import GroupCreateDto

sys.path.insert(0, os.path.abspath('generated'))

from generated import group_pb2_grpc, group_pb2

groups_router = APIRouter(
    prefix="/api/groups",
    tags=["groups"],
)


@groups_router.get("/{id}")
async def find_by_id(id: str):  # default id = 66154d94c6436b3d17102551
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = group_pb2_grpc.GroupGrpcServiceStub(channel)
        request = group_pb2.GroupIdProto(id=id)
        try:
            response = stub.FindById(request)
            return from_proto(response)
        except Exception as e:
            print(e)
            return {"error": str(e)}


@groups_router.get("/")
async def find_all():
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = group_pb2_grpc.GroupGrpcServiceStub(channel)
        request = group_pb2.EmptyProto()
        try:
            response = stub.FindAll(request)
            return [from_proto(group) for group in response.groups]
        except Exception as e:
            print(e)
            return {"error": str(e)}


@groups_router.post("/")
async def create_group(group: GroupCreateDto):
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = group_pb2_grpc.GroupGrpcServiceStub(channel)
        request = group_pb2.CreateGroupProto(
            name=group.name,
            userIds=group.userIds,
            adminId=group.adminId,
            timetableId=group.timetableId,
        )
        try:
            response = stub.Create(request)
            return from_proto(response)
        except Exception as e:
            print(e)
            return {"error": str(e)}

@groups_router.put("/{id}")
async def update_group(id: str, group: GroupCreateDto):
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = group_pb2_grpc.GroupGrpcServiceStub(channel)
        request = group_pb2.GroupProto(
            id=id,
            name=group.name,
            userIds=group.userIds,
            adminId=group.adminId,
            timetableId=group.timetableId,
        )
        try:
            response = stub.Update(request)
            return from_proto(response)
        except Exception as e:
            print(e)
            return {"error": str(e)}


@groups_router.delete("/{id}")
async def delete_group(id: str):
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = group_pb2_grpc.GroupGrpcServiceStub(channel)
        request = group_pb2.GroupIdProto(id=id)
        try:
            response = stub.Delete(request)
            return {}
        except Exception as e:
            print(e)
            return {"error": str(e)}

def from_proto(proto):
    return {
        'id': proto.id,
        'name': proto.name,
        'adminId': proto.adminId,
        'timetableId': proto.timetableId,
    }