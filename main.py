from PIL import Image ,ImageDraw
import glob

frames = []
imgs = glob.glob("*.jpg")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save('jpg_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=600, Loop=0)
