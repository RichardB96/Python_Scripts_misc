def VerticesSort(vlist):

	vertexlist=[]
	vertexlist.append(vlist[0])

	for vertexpair in vlist[1:]:
		placed = 0 #0 if the vertex pair has not been placed, 1 if it has, to avoid placing the same vertices multiple times where one vertex is novel
		duplicate = False
		for y in vertexlist:
			if vertexpair[0] in y:
				if vertexpair[1] not in y:
					y.append(vertexpair[1])
					placed = 1
				else:
					duplicate = True
			elif vertexpair[1] in y:
				if vertexpair[0] not in y:
					y.append(vertexpair[0])
					placed = 1
				else:
					duplicate = True
			
			else:
				placed = 0
		if placed == 0 :
			if duplicate == False : 
				vertexlist.append(vertexpair)

	return(vertexlist)