import numpy as np
import time
import struct

startTime = time.time()
shape = (1000 , 1000)
randomArray = np.random.randint(low = 0 , high = 9999 , size = shape , dtype = 'int32')
print(randomArray)
creationTime = time.time() - startTime
print(f'Creation Time\t: {creationTime}')


shapeBytes = struct.pack('ii' , *shape)
dataType = randomArray.dtype
dataTypeBytes = dataType.name.encode('utf-8')


bytedArray = randomArray.tobytes()
byteObject = shapeBytes + dataTypeBytes + bytedArray

with open('ByteArray.bin' , 'wb') as file :
    file.write(byteObject)
