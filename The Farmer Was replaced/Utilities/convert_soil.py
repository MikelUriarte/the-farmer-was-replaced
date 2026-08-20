# Converts the entire field to tilled soil.
#
# The drone moves through the field and tills each tile
# until it reaches the opposite corner.

limit = True

while limit:

	for i in range(get_world_size()):

		if get_pos_y() == 31 and get_pos_x() == 31:
			limit = False

		harvest()
		till()

		move(North)

	move(East)