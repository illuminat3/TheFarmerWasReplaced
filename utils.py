def block_to_be_planted(carrot_count, wheat_count, wood_count, max_carrots, max_wheat, max_wood):
	if carrot_count < max_carrots:
		return Entities.Carrot
	elif wheat_count < max_wheat:
		return Entities.Grass
	elif wood_count < max_wood:
		return Entities.Bush
	else:
		return None
	
def plant_entity(entity, carrot_count, wheat_count, wood_count):
	if entity == Entities.Carrot:
		if get_ground_type() == Grounds.Grassland:
			till()
		carrot_count += 1
	elif entity == Entities.Grass:
		if get_ground_type() == Grounds.Soil:
			till()
		wheat_count += 1
	elif entity == Entities.Bush:
		if get_ground_type() == Grounds.Soil:
			till()
		wood_count += 1

	plant(entity)

	return carrot_count, wheat_count, wood_count

def harvest_entity(carrot_count, wheat_count, wood_count):
	entity = get_entity_type()
	if entity == Entities.Carrot:
		carrot_count -= 1
	elif entity == Entities.Grass:
		wheat_count -= 1
	elif entity == Entities.Bush:
		wood_count -= 1

	harvest()
	return carrot_count, wheat_count, wood_count

def optimal_split(w):
	T = w * w
	c = T // 11
	wheat = 5 * c
	wood = 5 * c
	used = 11 * c
	r = T - used

	extra = r // 11
	if extra:
		c += extra
		wheat += 5 * extra
		wood += 5 * extra
		r -= 11 * extra

	if r >= 9:
		c += 1
		wheat += 4
		wood += 4
		r -= 9

	if r > 0:
		add_w = r // 2
		add_d = r - add_w
		wheat += add_w
		wood += add_d

	return c, wheat, wood
