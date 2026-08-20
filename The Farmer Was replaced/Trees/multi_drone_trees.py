def for_all():
	while True:
		def row():
			for _ in range(get_world_size()):
				harvest()
				use_item(Items.Water)
				if(get_pos_y() % 2 ==0 and get_pos_x() % 2 ==0):
					harvest()
					plant(Entities.Tree)
				elif(get_pos_y() % 2 ==1 and get_pos_x() % 2 ==1):
					harvest()
					plant(Entities.Tree)
				else:
					harvest()
					plant(Entities.Bush)
				move(East)
	
		for _ in range(get_world_size()):
			if not spawn_drone(row):
				row()
			move(North)

for_all()