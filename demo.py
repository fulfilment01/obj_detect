from yoloapp.utils.main_utils import encodeImagetoBase, decodeImage

encode_img = encodeImagetoBase("data/55_png.rf.9ec5953ef4e1970bf146139bfc53d35a.jpg")

decodeImage(encode_img, "decoded_image.jpg")