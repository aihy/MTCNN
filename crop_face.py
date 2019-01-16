from PIL import Image
from src.detector import detect_faces
from utils.visualization_utils import show_bboxes
import os


def cc(imgin, imgout):
    if os.path.exists(imgout):
        return
    d = os.path.split(imgout)[0]
    if not os.path.exists(d):
        os.makedirs(d)
    if imgin[-3:] != "jpg":
        return
    img = Image.open(imgin)
    try:
        bounding_boxes, _ = detect_faces(img)
        if bounding_boxes.shape[0] == 1:
            bb = bounding_boxes.squeeze()
        else:
            bb = bounding_boxes.squeeze()[0]
    except:
        img.save(imgout)
        return
    img = img.crop((tuple(bb)[:-1]))
    img.save(imgout)
    return
