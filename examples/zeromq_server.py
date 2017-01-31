import zmq
from jsonrpcserver import methods
from jsonrpcserver.response import NotificationResponse

socket = zmq.Context().socket(zmq.REP)

@methods.add
def ping():
    return 'pong'

if __name__ == '__main__':
    socket.bind('tcp://*:5000')
    while True:
        request = socket.recv().decode()
        response = methods.dispatch(request)
        if not isinstance(response, NotificationResponse):
            socket.send_string(str(response))
