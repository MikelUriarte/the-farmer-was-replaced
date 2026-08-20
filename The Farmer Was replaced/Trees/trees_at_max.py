# ---------------- MAXIMUM TREE FARM ----------------
#
# Plants trees on every tile of the field.
# Trees are harvested and replanted whenever they are ready,
# while keeping the field watered.

while True:

	for _ in range(get_world_size()):

		plant(Entities.Tree)

		if can_harvest():
			harvest()
			plant(Entities.Tree)
			use_item(Items.Water)

		move(North)

	move(East)