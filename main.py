#25/26th August 2021

#Each voxel is a differnt block
#The for loops generate the world

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
punch_sound = Audio('assests/punch.mp3',loop = False, autoplay = False)
block = 1

def update():
    global block
    if held_keys['1']: block = 1
    if held_keys['2']: block = 2
    if held_keys['3']: block = 3


class Voxel1(Button):
    def __init__(self, position = (0,0,0),):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.green
        )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block == 1:
                    voxel11 = Voxel1(position = self.position + mouse.normal,)
                if block == 2:
                    voxel22 = Voxel2(position = self.position + mouse.normal,)
                if block == 3:
                    Voxel3(position = self.position + mouse.normal,)


            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)


class Voxel2(Button):
    def __init__(self, position = (0,-2,0),):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.light_gray
        )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block == 1:
                    voxel11 = Voxel1(position = self.position + mouse.normal,)
                if block == 2:
                    voxel22 = Voxel2(position = self.position + mouse.normal,)
                if block == 3:
                    Voxel3(position = self.position + mouse.normal,)

            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)


class Voxel3(Button):
    def __init__(self, position = (0,-1,0),):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.rgb(153, 102, 51)
        )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block == 1:
                    voxel11 = Voxel1(position = self.position + mouse.normal,)
                if block == 2:
                    voxel22 = Voxel2(position = self.position + mouse.normal,)
                if block == 3:
                    voxel33 = Voxel3(position = self.position + mouse.normal,)

                

            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            color = color.cyan,
            scale = 150,
            double_sided = True
        )


for z in range(20):
    for x in range(20):
        voxel22 = Voxel2(position = (x,-2,z))


for z in range(20):
    for x in range(20):
        voxel22 = Voxel2(position = (x,-1,z))

for z in range(20):
    for x in range(20):
        voxel33 = Voxel3(position = (x,0,z))

for z in range(20):
    for x in range(20):
        voxel11 = Voxel1(position = (x,1,z))

player = FirstPersonController()
sky = Sky()

app.run()
