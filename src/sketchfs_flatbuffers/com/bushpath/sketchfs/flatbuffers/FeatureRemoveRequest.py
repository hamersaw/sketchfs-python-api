# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class FeatureRemoveRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFeatureRemoveRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FeatureRemoveRequest()
        x.Init(buf, n + offset)
        return x

    # FeatureRemoveRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FeatureRemoveRequest
    def SketchId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # FeatureRemoveRequest
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def FeatureRemoveRequestStart(builder): builder.StartObject(2)
def FeatureRemoveRequestAddSketchId(builder, sketchId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sketchId), 0)
def FeatureRemoveRequestAddName(builder, name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def FeatureRemoveRequestEnd(builder): return builder.EndObject()
