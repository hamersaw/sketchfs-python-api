# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class SketchCreateResponse(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSketchCreateResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SketchCreateResponse()
        x.Init(buf, n + offset)
        return x

    # SketchCreateResponse
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def SketchCreateResponseStart(builder): builder.StartObject(0)
def SketchCreateResponseEnd(builder): return builder.EndObject()