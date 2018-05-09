# Search methods

import search

rutas = []
rutas.append(search.GPSProblem('A', 'B', search.romania))
rutas.append(search.GPSProblem('S', 'M', search.romania))
rutas.append(search.GPSProblem('B', 'L', search.romania))
rutas.append(search.GPSProblem('V', 'L', search.romania))
rutas.append(search.GPSProblem('L', 'R', search.romania))
rutas.append(search.GPSProblem('F', 'C', search.romania))

for ruta in rutas:
    print "Metodo primero en anchura: "
    print search.breadth_first_graph_search(ruta).path()
    print ""

    print "Metodo primero en profundidad: "
    print search.depth_first_graph_search(ruta).path()
    print ""

    print "Metodo de Ramificacion y Acotacion: "
    print search.busqueda_ramificacion_acotada(ruta).path()
    print ""

    print "Metodo de Ramificacion y Acotacion Substimada: "
    print search.busqueda_ramificacion_acotada_subestimada(ruta).path()
    print ""

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
