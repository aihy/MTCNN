from crop_face import cc
import os
import progressbar

num = 0
with progressbar.ProgressBar(max_value=91206) as bar:
    for root,dirs,files in os.walk("/home/zihao_wang/data5/deception/deception_frame/"):
        for name in files:
            i=os.path.join(root,name)
            o=i.replace("deception_frame","deception_face")
            cc(i,o)
            bar.update(num)
            num += 1