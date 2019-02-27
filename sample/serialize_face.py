import face_recognition
import msgpack
import msgpack_numpy as m
import numpy as np
import base64
import sys

if sys.argv < 1:
    print("Pass a path to the image with a face")
    sys.exit(1)
data = face_recognition.load_image_file(sys.argv[1])
faces = face_recognition.face_encodings(data)
if len(faces) == 0:
    print("Faces not detected")
    sys.exit(1)
elif len(faces) > 1:
    print("Too much faces detected")
    sys.exit(1)
else:
    data = faces[0].astype(np.float16)
    data = msgpack.packb(data, default=m.encode)
    x_enc = base64.b64encode(data)
    print(x_enc)