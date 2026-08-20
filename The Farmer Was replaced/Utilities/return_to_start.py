# ---------------- RETURN TO START ----------------
#
# Moves the drone back to the starting position (0, 0).

while True:

	pos_x = get_pos_x()
	pos_y = get_pos_y()

	if pos_x != 0:
		move(West)

	elif pos_y != 0:
		move(South)

	if pos_x == 0 and pos_y == 0:
		break