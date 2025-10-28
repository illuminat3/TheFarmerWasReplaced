from utils import *

max_carrots, max_wheat, max_wood = optimal_split(get_world_size())
carrot_count, wheat_count, wood_count = 0, 0, 0
clear()
for x in range(get_world_size()):
	for y in range(get_world_size()):
		entity = block_to_be_planted(carrot_count, wheat_count, wood_count, max_carrots, max_wheat, max_wood)
		if entity != None:
			carrot_count, wheat_count, wood_count = plant_entity(entity, carrot_count, wheat_count, wood_count)
		move(North)
	move(East)
	
while True:
	for i in range(get_world_size()):
		if can_harvest():
			carrot_count, wheat_count, wood_count = harvest_entity(carrot_count, wheat_count, wood_count)
			entity = block_to_be_planted(carrot_count, wheat_count, wood_count, max_carrots, max_wheat, max_wood)
			if entity != None:
				carrot_count, wheat_count, wood_count = plant_entity(entity, carrot_count, wheat_count, wood_count)
			move(North)
		else:
			move(North)
			
	move(East)
	