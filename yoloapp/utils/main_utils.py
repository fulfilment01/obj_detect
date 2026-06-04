import base64

def encodeImagetoBase(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read)