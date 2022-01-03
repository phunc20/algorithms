import os
import struct
import sys

#if sys.version < "3":
#    print "These scripts are written for Python3. Please run by Python3."
#    sys.exit(1)

#try:
#    import numpy as np
#    from PIL import Image
#except ModuleNotFoundError as e:
#    print "Please pip install numpy, pillow"
#    sys.exit(1)

import numpy as np
from PIL import Image

from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ImageOps import exif_transpose

INV_TAGS = {info: id_ for id_, info in TAGS.items()}
def pil_loader(path):
    with open(path, "rb") as f:
        image = Image.open(f)
        exif_data = None
        try:
            exif_data = image._getexif()
        except:
            pass
        if exif_data:
            orientation = exif_data.get(INV_TAGS["Orientation"])
            if orientation:
                image = exif_transpose(image)
        # If RGB images are uniformly desired,
        # instead of inhomogeneous RGBA, gray-scale images,
        # then uncomment the next line
        image = image.convert("RGB")
        return image

class SeamError(Exception):
    pass

class Bild:
    def __init__(self, path_image):
        image = pil_loader(path_image)
        self.width, self.height = image.size
        self.array = np.asarray(image)

    def color_seam(self, seam, color=(255,0,0)):
        """Takes a seam (a list of coordinates) and colors it all one
        color."""
        # Implementation 01: simple for loop
        for i, j in seam:
            self[i, j] = color
        # Implementation 02: np.put()

    def remove_seam(self, seam):
        """Takes a seam (a list of coordinates with exactly one pair of
        coordinates per row). Removes pixel at each of those coordinates,
        and slides left all the pixels to its right. Decreases the width
        by 1."""
        mask = np.ones_like(self.array, dtype=np.bool)
        for i, j in seam:
            mask[i, j] = False
        self.array = self.array[mask].reshape((self.height, self.width-1, 3))
        self.width -= 1

    def image(self):
        """Returns a PIL Image that is represented by self.array"""
        return Image.fromarray(self.array)

    def save(self,*args,**keyw):
        self.image().save(*args,**keyw)

    def ppm(self):
        """Returns self in (binary) ppm form."""
        return 'P6 %d %d 255\n' % (self.width, self.height) + \
            ''.join ([struct.pack('BBB', *self[i,j])
                      for j in range(self.height) for i in range(self.width)])
    def save_ppm(self, filename):
        """Saves self as a .ppm"""
        f = open(filename, 'wb')
        f.write(self.ppm())
        f.close()

    def show(self,title='image',temp='_temp_.ppm'):
        """Displays self in a pop-up window using Tkinter,
        and waits till the user either clicks on or closes the window.
        Saves the image as a temporary ppm file (specified by temp)."""
        import Tkinter
        if Tkinter._default_root:
            root=Tkinter.Toplevel()
        else:
            root=Tkinter.Tk()
        self.save_ppm(temp)
        image = Tkinter.PhotoImage(master=root, file=temp)
        root.title('%dx%d image' % (self.width, self.height))
        label = Tkinter.Label(root, image=image)
        label.pack()
        label.bind('<Button>', lambda e: root.destroy())
        root.mainloop()
        os.remove(temp)

    def energy(self, i, j):
        """Given coordinates (i,j), returns an energy, or cost associated
        with removing that pixel."""
        if i==0 or j==0 or i==self.height-1 or j==self.width-1:
            return np.inf
        else: # I think this is equivalent to the Sobel gradient magnitude.
            return self.distance(self[i-1,j], self[i+1,j]) +\
                   self.distance(self[i,j-1], self[i,j+1]) +\
                   self.distance(self[i-1,j-1], self[i+1,j+1]) +\
                   self.distance(self[i+1,j-1], self[i-1,j+1])

    def distance(self, pixelA, pixelB):
        """A distance metric between two pixels, based on their colors."""
        return np.sum(np.abs(pixelA - pixelB))
