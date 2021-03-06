# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class GossipDhtRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGossipDhtRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GossipDhtRequest()
        x.Init(buf, n + offset)
        return x

    # GossipDhtRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GossipDhtRequest
    def Nodes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Node import Node
            obj = Node()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GossipDhtRequest
    def NodesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def GossipDhtRequestStart(builder): builder.StartObject(1)
def GossipDhtRequestAddNodes(builder, nodes): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodes), 0)
def GossipDhtRequestStartNodesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GossipDhtRequestEnd(builder): return builder.EndObject()
