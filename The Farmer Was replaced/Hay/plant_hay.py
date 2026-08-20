# ---------------- HAY FARM ----------------
#
# Continuously harvests hay across the field.
# Water is used after harvesting when available.

while True:

	for _ in range(get_world_size()):

		if can_harvest():
			harvest()

			if num_items(Items.Water) > 0:
				use_item(Items.Water)

		move(North)

	move(East)