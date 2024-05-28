
from parseador import parse_input
import heapq

# Funcion para verificar si una posicion en DFS ya ha sido visitada
def visitado(pos, visitados):
    return pos in visitados

# Algoritmo DFS 
def DFS(pos, grid, visitados_dfs, camino):
    numFil = len(grid)
    numCol = len(grid[0])
    pos_x, pos_y = pos
    camino.append(pos)
    print(f"visitando posicion {pos}")
    
    # Condiciones para saber si estamos en una posicion correcta y dicha posicion no ha sido visitada. 
    if pos_x < 0 or pos_y < 0 or pos_x >= numFil or pos_y >= numCol or visitado(pos, visitados_dfs):
        camino.pop() # Si la posicion no cumple la saca de la lista del camino recorrido
        return None

    if grid[pos_x][pos_y] == 0: # Caso base. Destino encontrado. 
        return camino

    visitados_dfs.append(pos) # Marcamos la posicion actual como visitada.
    valor = grid[pos_x][pos_y]

    if DFS((pos_x, pos_y - valor), grid, visitados_dfs, camino): # Verificamos hacia arriba.
        return camino
    if DFS((pos_x, pos_y + valor), grid, visitados_dfs, camino): # Verificamos hacia abajo
        return camino
    if DFS((pos_x + valor, pos_y), grid, visitados_dfs, camino): # Verificamos hacia la derecha.
        return camino
    if DFS((pos_x - valor, pos_y), grid, visitados_dfs, camino): # Verificamos hacia la izquierda
        return camino

    camino.pop()
    return None # No encuentra camino.

# Algoritmo UCS. Logica similar DFS 
def UCS(grid, start):
    numFil = len(grid)
    numCol = len(grid[0])
    visitados_ucs = set() # Conjunto de pos visitadas.
    pq = [(0, start, [])]  # (costo, posicion, camino).
    heapq.heapify(pq)

    while pq:
        costo, (pos_x, pos_y), camino = heapq.heappop(pq)
        if (pos_x, pos_y) in visitados_ucs:
            continue
        camino = camino + [(pos_x, pos_y)]
        print(f"Visitando nodo: {(pos_x, pos_y)} con costo: {costo}")

        if grid[pos_x][pos_y] == 0:
            print(f"Destino encontrado con costo: {costo}")
            return costo, camino

        visitados_ucs.add((pos_x, pos_y))
        valor = grid[pos_x][pos_y]

        for dx, dy in [(-valor, 0), (valor, 0), (0, -valor), (0, valor)]:
            new_x, new_y = pos_x + dx, pos_y + dy
            if 0 <= new_x < numFil and 0 <= new_y < numCol and (new_x, new_y) not in visitados_ucs:
                heapq.heappush(pq, (costo + 1, (new_x, new_y), camino))

    print("Destino no encontrado")
    return None

def main(filename):
    try: 
        laberintos = parse_input(filename)
        for laberinto in laberintos:
            m, n, start_x, start_y, end_x, end_y, grid = laberinto
            start = (start_x, start_y)
            destino = (end_x, end_y)

            print(m, n, start, destino)
            # print(grid[3][1])
            
            # Resolvemos con metodo DFS
            camino = []
            visitados_dfs = []
            resultado_dfs = DFS(start, grid, visitados_dfs, camino) 
            print("DFS Resultado:", resultado_dfs)

            # Resolvemos con metodo de costo uniforme
            resultado_ucs = UCS(grid, start)
            print("UCS Resultado:", resultado_ucs)

    except FileNotFoundError:
        print(f"Error: el archivo '{filename}' no se encuentra")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    main(args.filename)
