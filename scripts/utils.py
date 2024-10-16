import os
import pygame


BASE_IMG_PATH = 'data/images/'

def load_image(path) -> None:
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path) -> None:
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)): # os might not work on Linux(won't sort alphabethicaly), use sorted!
        images.append(load_image(path + '/' + img_name))
    return images


class Animation:
    def __init__(self, images, img_dur=5, loop=True) -> None:
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0
  

    def copy(self) -> None:
        return Animation(self.images, self.img_duration, self.loop)
    
    
    def update(self) -> None:
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
            
            
    def img(self) -> None:
        return self.images[int(self.frame / self.img_duration)] # Used for indexing, which image to show