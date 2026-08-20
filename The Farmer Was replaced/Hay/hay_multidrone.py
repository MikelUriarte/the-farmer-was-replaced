def farm_hay():
	while True:

		def row():
			for _ in range(get_world_size() - 1):
				harvest()
				move(East)

			harvest()

		# Spawn a drone for each row.
		for _ in range(get_world_size()):
			if not spawn_drone(row):
				row()

			move(North)


farm_hay()