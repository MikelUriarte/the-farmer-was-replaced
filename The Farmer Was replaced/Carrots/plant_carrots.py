# ---------------- CARROT FARM ----------------
#
# Continuously plants and harvests carrots across the field.
# Water is used after harvesting.

while True:

	for _ in range(get_world_size()):

		plant(Entities.Carrot)

		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			use_item(Items.Water)

		move(North)

	move(East)