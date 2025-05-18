from collections import deque

def resolver_laberinto(laberinto):
   
    if not laberinto or not laberinto[0]:
        return None
    
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    inicio = (0, 0)
   
    final = (filas - 1, columnas - 1)
    
    if laberinto[inicio[0]][inicio[1]] == 0 or laberinto[final[0]][final[1]] == 0:
        return None
    
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    cola = deque()
    cola.append(inicio)
    
    procedencia = {}
    procedencia[inicio] = None
    
    encontrado = False
    while cola:
        actual = cola.popleft()
        
        if actual == final:
            encontrado = True
            break
        
        
        for movimiento in movimientos:
            nueva_fila = actual[0] + movimiento[0]
            nueva_col = actual[1] + movimiento[1]
            
            
            if (0 <= nueva_fila < filas and 0 <= nueva_col < columnas and 
                laberinto[nueva_fila][nueva_col] == 1 and (nueva_fila, nueva_col) not in procedencia):
                procedencia[(nueva_fila, nueva_col)] = actual
                cola.append((nueva_fila, nueva_col))
    
    
    if not encontrado:
        return None
    
    
    camino = []
    actual = final
    while actual != inicio:
        camino.append(actual)
        actual = procedencia[actual]
    camino.append(inicio)
    camino.reverse()  
    
   
    solucion = [[0 for _ in range(columnas)] for _ in range(filas)]
    for fila, col in camino:
        solucion[fila][col] = 'S'
    
    return solucion

def mostrar_laberinto(laberinto, solucion=None):
    for i in range(len(laberinto)):
        fila_mostrar = []
        for j in range(len(laberinto[0])):
            if solucion and solucion[i][j] == 'S':
                fila_mostrar.append('S')
            elif laberinto[i][j] == 1:
                fila_mostrar.append('.')
            else:
                fila_mostrar.append('#')
        print(' '.join(fila_mostrar))
    print()

if __name__ == '__main__':
    
    laberinto_simple = [
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    
    laberinto_facil = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1]
    ]

    laberinto_medio = [
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1]
    ]   
    
    laberinto_dificil = [
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    
    
    for lab in [laberinto_simple, laberinto_facil, laberinto_medio, laberinto_dificil]:
        print("Laberinto original:")
        mostrar_laberinto(lab)
        
        sol = resolver_laberinto(lab)
        if sol:
            print("Solución encontrada:")
            mostrar_laberinto(lab, sol)
        else:
            print("No hay solución para este laberinto")
        print("-" * 40)
