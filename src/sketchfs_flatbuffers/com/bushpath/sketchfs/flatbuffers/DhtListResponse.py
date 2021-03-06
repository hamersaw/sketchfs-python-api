# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class DhtListResponse(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDhtListResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DhtListResponse()
        x.Init(buf, n + offset)
        return x

    # DhtListResponse
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DhtListResponse
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

    # DhtListResponse
    def NodesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def DhtListResponseStart(builder): builder.StartObject(1)
def DhtListResponseAddNodes(builder, nodes): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodes), 0)
def DhtListResponseStartNodesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DhtListResponseEnd(builder): return builder.EndObject()
