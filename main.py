# 25/26th August 2021
# Latest change : 25/11/22

# Each voxel is a different block
# The loops generate the world

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
window.borderless = False 
window.exit_button.visible = False
punch_sound = Audio('assests/punch.mp3',loop = False, autoplay = False) # Download the latest release for the punch sound.
block = 1


pause_handler = Entity(ignore_paused=True)
pause_text = Text('You paused the game :D', origin=(0,0), scale=5, enabled=False)

def pause_handler_input(key):
    if key == 'escape':
        application.paused = not application.paused # Pause/unpause the game.
        player.enabled = not player.enabled
        pause_text.enabled = application.paused     # Also toggle "PAUSED" graphic.


pause_handler.input = pause_handler_input


def update():
    global block
    if held_keys['1']: block = 1
    if held_keys['2']: block = 2
    if held_keys['3']: block = 3
    if held_keys['4']: block = 4


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

class Voxel4(Button):
    def __init__(self, position = (0,-1,0),):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.rgb(108, 89, 247)
        )

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
                if block == 3:
                    voxel44 = Voxel4(position = self.position + mouse.normal,)

                

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
