from pattern_utils import *
from pattern_grid import *

setup(grid)

while True:
	for x in grid:
		for y in x:
			if can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
				harvest()
			
			plant_entity(y)
			move(North)

		move(East)