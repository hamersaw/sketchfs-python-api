# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class QueryRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsQueryRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = QueryRequest()
        x.Init(buf, n + offset)
        return x

    # QueryRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # QueryRequest
    def SketchId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def QueryRequestStart(builder): builder.StartObject(1)
def QueryRequestAddSketchId(builder, sketchId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sketchId), 0)
def QueryRequestEnd(builder): return builder.EndObject()
