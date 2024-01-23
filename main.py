
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene ,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.blue,
        )

class Inventory(Entity):
    def __init__(self, width=5, height=5, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            texture = 'white_cube',
            texture_scale = (width, height),
            scale = (width*.1, height*.1),
            origin = (-.5,.5),
            position = (-.3,.4),
            color = color.color(0, 0, .1, .9),
            )

        self.width = width
        self.height = height

        for key, value in kwargs.items():
            setattr(self, key, value)

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

def player_fly():
    fly_speed = 15
    if held_keys['space']:
        player.y += fly_speed * time.dt
    if held_keys['control']:
        player.y -= fly_speed * time.dt

def open_inventory():
    inventory = Inventory()    

def update():
    player_fly()
    if held_keys['e']:
        open_inventory()


player = FirstPersonController()
player.speed = 10
player.gravity = 0

for z in range(15):
    for x in range(15):
        for y in range(2):
            voxel = Voxel(position=(z,y,x))

      

app.run()