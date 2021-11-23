from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import json
import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "../build/service/")
print(BUILD_DIR)
# sys.exit(0)
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
import fib_pb2
import fib_pb2_grpc

# from models import Fibonacci
# Create your views here.
DATA = {"history":[]}
class FibCalView(APIView):
    # fib = Fibonacci()
    def get(self, request):
        permission_classes = (permissions.AllowAny,)
        print("request is ", request)
        return Response(data=DATA, status=200)
    def post(self, request):
        print("request is ", request.data)
        data = request.data.get('data')
        # Now data is a string 
        print("data is ", data)
        order = int(data.split(':')[-1].replace('}', ""))
        DATA["history"].append(order)
        print(order)
        host = f"0.0.0.0:8080"
        print("host is ", host)
        with grpc.insecure_channel(host) as channel:
            stub = fib_pb2_grpc.FibCalculatorStub(channel)

            request = fib_pb2.FibRequest()
            request.order = order
            print("request is ", request)
            response = stub.Compute(request)
            print("response received at django ",type(response))
        return Response(data={ f'Fib number of order {order} ': response.value }, status = 200)

