
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.blue,
        )

for z in range(15):
    for x in range(15):
        for y in range(2):
            voxel = Voxel(position=(z,y,x))


def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)


def update():
    fly_speed = 15
    if held_keys['space']:
        player.y += fly_speed * time.dt
    if held_keys['control']:
        player.y -= fly_speed * time.dt


player = FirstPersonController()
player.speed = 10
player.gravity = 0

app.run()