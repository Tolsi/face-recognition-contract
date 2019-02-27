import io
import base64
import sys

from PIL import Image

if sys.argv < 1:
    print("Pass a path to the image")
    sys.exit(1)

im = Image.open(sys.argv[1])
im.thumbnail([350, 350])
bytes = io.BytesIO()
im.save(bytes, format='JPEG', subsampling=2, quality=0)
bytes.seek(0)
data = bytes.read()

x_enc = base64.b64encode(data)
print(len(data))
print(len(x_enc))
print(x_enc)