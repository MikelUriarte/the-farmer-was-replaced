# ---------------- MULTI-DRONE CARROT FARM ----------------
#
# Uses multiple drones to continuously harvest and replant
# carrots, with each drone working on a different row.

def farm_carrots():
	while True:

		def row():
			for _ in range(get_world_size()):
				harvest()
				plant(Entities.Carrot)
				move(East)

			harvest()
			plant(Entities.Carrot)

		# Spawn a drone for each row.
		for _ in range(get_world_size()):
			if not spawn_drone(row):
				row()

			move(North)


farm_carrots()