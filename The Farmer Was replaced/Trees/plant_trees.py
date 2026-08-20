# ---------------- TREE AND BUSH FARM ----------------
#
# Plants trees in a checkerboard pattern and fills the
# remaining tiles with bushes.

while True:

	for _ in range(get_world_size()):

		# Water the current tile.
		use_item(Items.Water)

		# Plant trees on alternating diagonal positions.
		if get_pos_y() % 2 == 0 and get_pos_x() % 2 == 0:
			harvest()
			plant(Entities.Tree)

		elif get_pos_y() % 2 == 1 and get_pos_x() % 2 == 1:
			harvest()
			plant(Entities.Tree)

		# Fill the remaining positions with bushes.
		else:
			harvest()
			plant(Entities.Bush)

		move(North)

	move(East)