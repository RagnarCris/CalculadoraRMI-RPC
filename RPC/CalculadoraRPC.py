import grpc

import calc_pb2
import calc_pb2_grpc

import uuid
from concurrent.futures import ThreadPoolExecutor

import time


class CalculatorServicer(calc_pb2_grpc.CalculatorServicer):

    def Create(self, request, context):
        serial = str(uuid.uuid4())
        calc_db[serial] = request.value

        response = calc_pb2.SessionOperation()
        response.token = serial
        response.value = calc_db[serial]

        return response

    def Answer(self, request, context):
        serial = request.token

        response = calc_pb2.Number()
        response.value = calc_db[serial]

        calc_db[serial] = None

        return response

    def Add(self, request, context):
        value = request.value
        serial = request.token

        calc_db[serial] = calc_db[serial] + value        

        response = calc_pb2.Number()
        response.value = calc_db[serial]
        return response

    def Subtract(self, request, context):
        value = request.value
        serial = request.token

        calc_db[serial] = calc_db[serial] - value        

        response = calc_pb2.Number()
        response.value = calc_db[serial]
        return response

    def Multiply(self, request, context):
        value = request.value
        serial = request.token

        calc_db[serial] = calc_db[serial] * value        

        response = calc_pb2.Number()
        response.value = calc_db[serial]
        return response

    def Divide(self, request, context):
        value = request.value
        serial = request.token

        calc_db[serial] = calc_db[serial] / value        

        response = calc_pb2.Number()
        response.value = calc_db[serial]
        return response


calc_db = {}
server = grpc.server(ThreadPoolExecutor(max_workers=10))
calc_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print('Starting server. Listening on port 2000.')
server.add_insecure_port('[::]:2000')
server.start()

try:
    while True:
        time.sleep(10000)
except KeyboardInterrupt:
    server.stop(0)

