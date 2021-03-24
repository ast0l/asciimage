from PIL import Image as PilImg
from PIL import ImageDraw as PilDraw
from PIL import ImageFont as PilFont

from image.Image import Image
from random import randint

import time


class Transform(Image):
    def __init__(self, image_path: str):
        super().__init__()
        self.image = image_path
        self.__ascii_list = '@*/.,%$()&+-^_:<>=;!?'

    def to_greyscale(self, image_name: str, path: str = 'img/greyscale') -> None:
        """
        convert and save RGB image to greyscale
        :param path:
        :param image_name:
        :return:
        """
        img_name = self._get_info()['name']
        img_load = PilImg.open(img_name)
        img_greyscale = img_load.convert('L')
        img_greyscale.save(f'{path}/{image_name}.png')

    def to_ascii(self, image_name: str = 'new', path: str = 'img/ascii') -> None:
        """
        create and save new image in ascii art
        :return:
        """
        # get image size
        size = self._get_info()[1]
        # create empty dict to stock pixel value later
        pixel_color: dict = {}

        # create new image and save it
        new_img = PilImg.new(mode='L', size=size)
        new_img.save(f'{path}/{image_name}.png')
        new_img.close()

        # get all shade of gray from the original image
        pixel = self.image.getpixel((0, 0))
        print(pixel)

        # check the color for each pixel
        for y in range(0, size[1]):
            for x in range(0, size[0]):
                coordinate: tuple = (x, y)
                pixel = self.image.getpixel(xy=coordinate)

                # stock pixel in the color list and assign ascii to it
                if pixel not in pixel_color and pixel != 0:
                    pixel_color[pixel] = self.__ascii_list[randint(0, len(self.__ascii_list) - 1)]

                print(f'({x}, {y}) -> {pixel}')
        print('CHAR ATTRIBUTION END')
        time.sleep(3)

        # check the pixel color to add the correct character
        new_img = PilImg.open(f'{path}/{image_name}.png')
        set_font_size = PilFont.truetype('arial.ttf', 1)
        add_ascii = PilDraw.Draw(new_img)

        for y in range(0, size[1]):
            for x in range(0, size[0]):
                coordinate: tuple = (x, y)
                pixel = self.image.getpixel(xy=coordinate)

                # add character
                add_ascii.text(coordinate, pixel_color[pixel], 1000, font=set_font_size)

                print(f'{coordinate} -> {pixel}')
        new_img.save('img/new.png')
        new_img.close()
