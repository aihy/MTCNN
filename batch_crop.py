from crop_face import cc
import os
import progressbar

num = 0
with progressbar.ProgressBar(max_value=33954) as bar:
    for root,dirs,files in os.walk("/home/zihao_wang/data5/demo/first-impression-v2/data/val-images"):
        for name in files:
            i=os.path.join(root,name)
            o=i.replace("val-images","val-images-face")
            cc(i,o)
            bar.update(num)
            num += 1
