import grpc

import calc_pb2
import calc_pb2_grpc

channel = grpc.insecure_channel("localhost:2000")

stub = calc_pb2_grpc.CalculatorStub(channel)
initial = calc_pb2.Number(value=0)

session = stub.Create(initial)
print('Session is ' + session.token)

stub.Add(calc_pb2.SessionOperation(token=session.token, value=5))
stub.Subtract(calc_pb2.SessionOperation(token=session.token, value=3))
stub.Multiply(calc_pb2.SessionOperation(token=session.token, value=10))
stub.Divide(calc_pb2.SessionOperation(token=session.token, value=2))

answer = stub.Answer(calc_pb2.SessionOperation(token=session.token, value=0))
print('Answer is ' + str(answer.value))

