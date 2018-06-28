#!/bin/python3
import flatbuffers
import zmq

import sketchfs_flatbuffers

# define sketch record cursor
class Cursor:
    def __init__(self, hostname, port, sketch_id):
        self.hostname = hostname
        self.port = port
        self.sketch_id = sketch_id

        # send DhtListRequest
        builder = flatbuffers.Builder(1)

    # returns next record (None if no records remaining)
    def next(self):
        return None;

def send(message_type, request, hostname, port):
    context = zmq.Context()

    # connect to server
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://' + hostname + ':' + port)

    # send request
    socket.send(message_type.to_bytes(2), zmq.SNDMORE)
    socket.send(request)

    # recv response
    response = socket.recv()
    response = socket.recv()
    #socket.send(message_type,

if __name__ == '__main__':
    # create cursor
    cursor = Cursor('127.0.0.1', 5450, 'yearPredictionMSD')

    # iterate over data items
    while True:
        record = cursor.next()
        if record == None:
            break

        print(record)
