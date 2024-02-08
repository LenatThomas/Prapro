import struct
import numpy as np

with open('ByteArray.bin' , 'rb') as file:
    byteObject = file.read()

shapeByte = byteObject[:8]
dataTypeBytes = byteObject[8:13]
shape = struct.unpack('ii' , shapeByte)
dataType = np.dtype(dataTypeBytes.decode('utf-8'))
byteArray = byteObject[13:]

randomArray = np.frombuffer(byteArray , dtype = dataType).reshape(shape)
print(randomArray)