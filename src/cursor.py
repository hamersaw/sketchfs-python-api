#!/bin/python3
import flatbuffers
import zmq

import random
import time

import sketchfs_flatbuffers
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.DhtListRequest import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.DhtListResponse import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.MessageType import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.Node import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.SketchShowRequest import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.SketchShowResponse import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.QueryRequest import *
from sketchfs_flatbuffers.com.bushpath.sketchfs.flatbuffers.QueryResponse import *

# define sketch record cursor
class Cursor:
    def __init__(self, hostname, port, sketch_id):
        self.hostname = hostname
        self.port = port
        self.sketch_id = sketch_id

        # create DhtListRequest
        builder = flatbuffers.Builder(1)
        DhtListRequestStart(builder)
        root_index = DhtListRequestEnd(builder)
        builder.Finish(root_index)

        # send DhtListRequest
        response = send(MessageType.DhtList, builder.Output(), hostname, port)
        
        # parse DhtListResponse
        dht_list_response = DhtListResponse.GetRootAsDhtListResponse(response, 0)
        nodes = []
        for i in range(0, dht_list_response.NodesLength()):
            nodes.append(dht_list_response.Nodes(i))

        # initialize node variables
        self.nodes = nodes
        self.nodeIndex = 0

        # create SketchShowRequest
        ss_builder = flatbuffers.Builder(1)
        sketch_id_index = ss_builder.CreateString(sketch_id)
        SketchShowRequestStart(ss_builder)
        SketchShowRequestAddId(ss_builder, sketch_id_index)
        ss_root_index = SketchShowRequestEnd(ss_builder)
        ss_builder.Finish(ss_root_index)

        # send SketchShowRequest
        ss_response = send(MessageType.SketchShow, ss_builder.Output(),
            nodes[0].Hostname().decode('utf-8'), nodes[0].DataPort())
        
        # parse SketchShowResponse
        sketch_show_response = \
            SketchShowResponse.GetRootAsSketchShowResponse(ss_response, 0)

        # intialize bins
        bins = []
        sketch = sketch_show_response.Sketch()
        for i in range(0, sketch.FeaturesLength()):
            feature = sketch.Features(i)

            binBoundaries = []
            for j in range(0, feature.ValuesLength()):
                binBoundaries.append(feature.Values(j))

            bins.append(binBoundaries)

        self.bins = bins

        # initialize ranges
        bin_ranges = []
        for i in range(0, len(bins)):
            #print('bin:' + str(i))
            bin_range_values = []
            for j in range(0, len(bins[i]) - 1):
                bin_range_values.append(bins[i][j+1] - bins[i][j])
                #print('\trange:' + str(bin_range_values[j]))

            bin_ranges.append(bin_range_values)

        self.bin_ranges = bin_ranges

        # initialize record variables
        self.records = []
        self.recordIndex = 0
        self.recordCount = len(self.records)

    # returns next record (None if no records remaining)
    def next(self):
        # if we've returned all the records from the current node
        while self.recordIndex >= self.recordCount:
            # if there are no more nodes
            if self.nodeIndex >= len(self.nodes):
                return None

            node = self.nodes[self.nodeIndex]
            self.nodeIndex += 1

            # create QueryRequest 
            builder = flatbuffers.Builder(1)
            sketch_id_index = builder.CreateString(self.sketch_id)
            QueryRequestStart(builder)
            QueryRequestAddSketchId(builder, sketch_id_index)
            root_index = QueryRequestEnd(builder)
            builder.Finish(root_index)

            # send QueryRequest
            response = send(MessageType.Query, builder.Output(),
                node.Hostname().decode('utf-8'), node.DataPort())

            # parse QueryResponse
            query_response = QueryResponse.GetRootAsQueryResponse(response, 0)

            # generate synthetic records
            records = []
            start = time.time()
            for i in range(0, query_response.BinEntriesLength()):
                bin_entry = query_response.BinEntries(i)
                # generate random records based on bin entries
                for j in range(0, bin_entry.RecordCount()):
                    record = []
                    for k in range(0, bin_entry.BinsLength()):
                        item_range = self.bin_ranges[k][bin_entry.Bins(k)]
                        value = self.bins[k][bin_entry.Bins(k)] + (random.random() * item_range)
                        record.append(value)

                    records.append(record)

                    #if len(records) % 1000 == 0:
                        #print('generated ' + str(len(records)) + ' records in ' + str(time.time() - start) + ' seconds')

            # reset record information
            self.records = records
            self.recordIndex = 0
            self.recordCount = len(self.records)

        # return record
        self.recordIndex += 1
        return self.records[self.recordIndex - 1]

def send(message_type, request, hostname, port):
    context = zmq.Context()

    # connect to server
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://' + hostname + ':' + str(port))

    # send request
    socket.send(message_type.to_bytes(2, byteorder='little'), zmq.SNDMORE)
    socket.send(request)

    # recv response
    response = socket.recv()
    response = socket.recv()
    return response

if __name__ == '__main__':
    # create cursor
    cursor = Cursor('127.0.0.1', 5450, 'yearPredictionMSD')

    # iterate over data items
    while True:
        record = cursor.next()
        if record == None:
            break

        #print(','.join(record))
