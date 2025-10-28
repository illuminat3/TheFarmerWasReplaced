from farmables import *

farm_items = [pumpkin, carrot, grass, tree]

def get_optimal_layout(world_size):
	total_size = world_size * world_size

	optimal_entity_counts = {}

	for farmable in farm_items:
		item_cost = farmable["cost"]
		for base_item in item_cost:
			parent_entity = get_entity_from_item(base_item)
			amount = item_cost[base_item]/parent_entity["value"]
			key = parent_entity["entity"]
			if key in optimal_entity_counts:
				optimal_entity_counts[key] += amount
			else:
				optimal_entity_counts[key] = amount

	for farmable in farm_items:
		entity = farmable["entity"]
		if entity not in optimal_entity_counts:
			optimal_entity_counts[entity] = 1
		else:
			optimal_entity_counts[entity] += 1

	print(dict(optimal_entity_counts))

def get_entity_from_item(item):
	for farmable in farm_items:
		if farmable["item"] == item:
			return farmable

get_optimal_layout(8)