grassland_entities = [Entities.Grass, Entities.Tree]
soil_entities = [Entities.Carrot, Entities.Pumpkin]

def plant_entity(entity):
	if entity in grassland_entities:
		desired_ground_type = Grounds.Grassland
	elif entity in soil_entities:
		desired_ground_type = Grounds.Soil

	set_ground_type(desired_ground_type)
	
	plant(entity)

	if entity == Entities.Tree:
		use_item(Items.Water)

def set_ground_type(desired_ground_type):
	ground_type = get_ground_type()
	if ground_type != desired_ground_type:
		till()



def setup(grid_layout):
	go_to_starting_position()
	for x in grid_layout:
		for y in x:
			if get_entity_type() != y:
				plant_entity(y)
			if can_harvest():
				harvest()
				plant_entity(y)
			move(North)
		move(East)


def go_to_starting_position():
	x = get_pos_x()
	y = get_pos_y()

	while x > 0:
		move(West)
		x = get_pos_x()
		
	while y > 0:
		move(South)
		y = get_pos_y()