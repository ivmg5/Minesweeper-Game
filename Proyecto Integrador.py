#Diego Ivan Morales Gallardo
#Importo os porque será necesario para que la función limpia() pueda funcionar
import os

def main():
  #Creo los tres tableros: el que va a estar cambiando según como avance el juego, un tablero de cómo se tendría que ver cuando el usuario gane y así poder compararlo y saber si ya ganó y el que tiene los datos escondidos
  
  tablero_escondido = [[' ',' ',' ',' ',' ',' ','1','X','2','1',' ',' ','1','X','2','X','X','1','1','2','2','1','1','1','2','X','3','X','4','2','1'],[' ',' ',' ',' ',' ',' ','2','4','X','2',' ',' ','2','2','4','4','4','3','2','X','X','2','2','X','2','1','4','X','X','X','1'],[' ',' ',' ',' ','1','1','2','X','X','2',' ',' ','1','X','3','X','X','3','X','3','2','2','X','2','1',' ','3','X','5','2','1'],['1','1',' ',' ','1','X','3','3','3','1',' ',' ','1','2','X','4','X','4','2','2',' ','2','2','2',' ',' ','2','X','2',' ',' '],['X','1',' ',' ','2','3','4','X','1','1','1','1',' ','1','1','2','1','2','X','1',' ','2','X','2',' ',' ','1','1','1',' ',' '],['2','2',' ',' ','1','X','X','2','1','1','X','2','1','1',' ',' ',' ','2','2','2',' ','3','X','3','1','1','2','1','2','1','1'],['X','2','1',' ','2','3','3','1',' ','1','2','3','X','2','1','1',' ','1','X','1',' ','2','X','3','2','X','2','X','3','X','2'],['2','X','1',' ','1','X','1',' ','1','1','2','X','2','3','X','2',' ','1','1','1',' ','1','2','X','2','2','4','4','5','X','3'],['2','2','2','1','2','1','2','1','2','X','2','1','1','2','X','3','1','1',' ',' ',' ',' ','1','1','1','1','X','X','X','4','X'],['X','1','1','X','1',' ','2','X','3','1','1',' ',' ','1','2','3','X','1',' ','1','1','1',' ',' ',' ','1','2','3','2','4','X'],['1','1','1','2','2','1','2','X','3','1',' ',' ','1','1','2','X','3','2','1','1','X','1','1','2','3','2','1',' ',' ','3','X'],['1','1','1','3','X','2','1','2','X','1',' ',' ','1','X','2','2','3','X','3','3','2','1','1','X','X','X','1',' ',' ','2','X'],['X','2','2','X','X','4','1','1','1','1',' ','1','2','3','2','3','X','5','X','X','2',' ','1','2','4','4','3','1',' ','1','1'],['1','2','X','4','X','X','2',' ','1','1','1','2','X','3','X','3','X','4','X','X','2',' ','1','1','2','X','X','2','2','1','1'],[' ','1','1','2','4','X','4','1','1','X','2','3','X','3','1','2','1','2','2','3','2','2','2','X','3','3','4','X','4','X','1'],[' ',' ',' ',' ','2','X','X','1','1','1','2','X','2','1',' ',' ',' ',' ',' ','1','X','2','X','3','X','1','2','X','X','2','1']]
  
  tablero_ganar = [[' ',' ',' ',' ',' ',' ','1','_','2','1',' ',' ','1','_','2','_','_','1','1','2','2','1','1','1','2','_','3','_','4','2','1'],[' ',' ',' ',' ',' ',' ','2','4','_','2',' ',' ','2','2','4','4','4','3','2','_','_','2','2','_','2','1','4','_','_','_','1'],[' ',' ',' ',' ','1','1','2','_','_','2',' ',' ','1','_','3','_','_','3','_','3','2','2','_','2','1',' ','3','_','5','2','1'],['1','1',' ',' ','1','_','3','3','3','1',' ',' ','1','2','_','4','_','4','2','2',' ','2','2','2',' ',' ','2','_','2',' ',' '],['_','1',' ',' ','2','3','4','_','1','1','1','1',' ','1','1','2','1','2','_','1',' ','2','_','2',' ',' ','1','1','1',' ',' '],['2','2',' ',' ','1','_','_','2','1','1','_','2','1','1',' ',' ',' ','2','2','2',' ','3','_','3','1','1','2','1','2','1','1'],['_','2','1',' ','2','3','3','1',' ','1','2','3','_','2','1','1',' ','1','_','1',' ','2','_','3','2','_','2','_','3','_','2'],['2','_','1',' ','1','_','1',' ','1','1','2','_','2','3','_','2',' ','1','1','1',' ','1','2','_','2','2','4','4','5','_','3'],['2','2','2','1','2','1','2','1','2','_','2','1','1','2','_','3','1','1',' ',' ',' ',' ','1','1','1','1','_','_','_','4','_'],['_','1','1','_','1',' ','2','_','3','1','1',' ',' ','1','2','3','_','1',' ','1','1','1',' ',' ',' ','1','2','3','2','4','_'],['1','1','1','2','2','1','2','_','3','1',' ',' ','1','1','2','_','3','2','1','1','_','1','1','2','3','2','1',' ',' ','3','_'],['1','1','1','3','_','2','1','2','_','1',' ',' ','1','_','2','2','3','_','3','3','2','1','1','_','_','_','1',' ',' ','2','_'],['_','2','2','_','_','4','1','1','1','1',' ','1','2','3','2','3','_','5','_','_','2',' ','1','2','4','4','3','1',' ','1','1'],['1','2','_','4','_','_','2',' ','1','1','1','2','_','3','_','3','_','4','_','_','2',' ','1','1','2','_','_','2','2','1','1'],[' ','1','1','2','4','_','4','1','1','_','2','3','_','3','1','2','1','2','2','3','2','2','2','_','3','3','4','_','4','_','1'],[' ',' ',' ',' ','2','_','_','1','1','1','2','_','2','1',' ',' ',' ',' ',' ','1','_','2','_','3','_','1','2','_','_','2','1']]

  tablero_vacio =[['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']]
  
  #Mensaje de bienvenida
  
  print('BIENVENIDO A BUSCAMINAS\n')
  
  #Creo una variable que tiene un valor de 0, pero lo voy a cambiar cuando quiera salir del ciclo
  
  var = 1
  
  #Inicio el ciclo del juego, que se va a repetir hasta que el usuario pierda o gane
  
  while var == 1 and (tablero_ganar != tablero_vacio):
    
    #Mando a desplegar el tablero para que el usuario pueda elegir una celda
    
    despliega_tablero(tablero_vacio)
    
    #Pido el número de fila y columna para poder tomar una decisión con base en ello
    
    print('INDICA LA CELDA QUE DESEA REVELAR')
    fila = int(input('FILA: '))
    columna = int(input('COLUMNA: '))
    
    #Mando a llamar a la función para que realize la acción pertinente dependiendo de que casilla o celda eligió el usuario
    
    valor = verifica_valores_y_revela(fila,columna,tablero_vacio,tablero_escondido)

    #Con base en el resultado que me haya devuelto dependiendo de que habia en la celda elegida, tomo la decisión de si seguir o no
    
    if valor == 1:
      var = 1
    else:
      var += 1

  #Condicional para saber si el tablero esperado es igual al tablero actual y así saber si ya ganó el usuario
      
  if tablero_ganar == tablero_vacio:
    limpia()
    despliega_tablero(tablero_vacio)
    print('¡HAS GANADO!')
    
def crea_lista():
  '''Crea la lista de números que se usa para mostrar el número de columnas y la devuelve. Esta función la uso dentro de la función despliega_tablero()'''
  lista = []
  for i in range(1,32):
    lista.append(i)
  return lista


def despliega_tablero(tablero):
  '''Despliega el tablero junto con el número de filas y columnas'''
  lista = crea_lista()
  print('   ',end='')
  for elemento in lista:
    print(str(elemento).center(3), end='')
  cont = 1
  for renglon in tablero:
    print("\n")
    print(str(cont).center(2)+ ' ', end="")
    cont += 1
    print("|", end="")
    for elemento in renglon:
      print(f'{elemento}'.center(2), end='')
      print("|", end="")
  print("\n")


def verifica_valores_y_revela(fila,columna,tablero_vacio,tablero_escondido):
    '''Verifica que la fila y la columna sean valores válidos (que estén dentro del rango de celdas) y que no se repitan. Asimismo, revela en el tablero la celda. La función devuelve un 2 en caso de error o bomba y 1 cuando no lo es.'''
    if (1 <= fila <= 16) and (1 <= columna <= 31):
      posicion = tablero_escondido[fila-1][columna-1]
      actual = tablero_vacio[fila-1][columna-1]
      #El siguiente if se activa cuando el valor no ha sido elegido anteriormente
      if actual == '_':
        #El siguiente if se activa cuando la celda elegida por el usuario no corresponde a una bomba
        if posicion != "X":
            #Todos los los ifs y elifs siguientes se van a activar cuando el usuario elija una celda que esté en blanco
            if (1 <= columna <= 6 and 1 <= fila <= 2) or (fila == 3 and 1 <= columna <= 4) or (4 <= fila <= 6 and 3 <= columna <= 4) or (7 <= fila <= 8 and columna == 4):
              tablero_vacio[0][0] = tablero_escondido[0][0]
              tablero_vacio[0][1] = tablero_escondido[0][1]
              tablero_vacio[0][2] = tablero_escondido[0][2]
              tablero_vacio[0][3] = tablero_escondido[0][3]
              tablero_vacio[0][4] = tablero_escondido[0][4]
              tablero_vacio[0][5] = tablero_escondido[0][5]
              tablero_vacio[0][6] = tablero_escondido[0][6]
              tablero_vacio[1][0] = tablero_escondido[1][0]
              tablero_vacio[1][1] = tablero_escondido[1][1]
              tablero_vacio[1][2] = tablero_escondido[1][2]
              tablero_vacio[1][3] = tablero_escondido[1][3]
              tablero_vacio[1][4] = tablero_escondido[1][4]
              tablero_vacio[1][5] = tablero_escondido[1][5]
              tablero_vacio[1][6] = tablero_escondido[1][6]
              tablero_vacio[2][0] = tablero_escondido[2][0]
              tablero_vacio[2][1] = tablero_escondido[2][1]
              tablero_vacio[2][2] = tablero_escondido[2][2]
              tablero_vacio[2][3] = tablero_escondido[2][3]
              tablero_vacio[2][4] = tablero_escondido[2][4]
              tablero_vacio[2][5] = tablero_escondido[2][5]
              tablero_vacio[2][6] = tablero_escondido[2][6]
              tablero_vacio[3][0] = tablero_escondido[3][0]
              tablero_vacio[3][1] = tablero_escondido[3][1]
              tablero_vacio[3][2] = tablero_escondido[3][2]
              tablero_vacio[3][3] = tablero_escondido[3][3]
              tablero_vacio[3][4] = tablero_escondido[3][4]
              tablero_vacio[4][1] = tablero_escondido[4][1]
              tablero_vacio[4][2] = tablero_escondido[4][2]
              tablero_vacio[4][3] = tablero_escondido[4][3]
              tablero_vacio[4][4] = tablero_escondido[4][4]
              tablero_vacio[5][1] = tablero_escondido[5][1]
              tablero_vacio[5][2] = tablero_escondido[5][2]
              tablero_vacio[5][3] = tablero_escondido[5][3]
              tablero_vacio[5][4] = tablero_escondido[5][4]
              tablero_vacio[6][1] = tablero_escondido[6][1]
              tablero_vacio[6][2] = tablero_escondido[6][2]
              tablero_vacio[6][3] = tablero_escondido[6][3]
              tablero_vacio[6][4] = tablero_escondido[6][4]
              tablero_vacio[7][2] = tablero_escondido[7][2]
              tablero_vacio[7][3] = tablero_escondido[7][3]
              tablero_vacio[7][4] = tablero_escondido[7][4]
              tablero_vacio[8][2] = tablero_escondido[8][2]
              tablero_vacio[8][3] = tablero_escondido[8][3]
              tablero_vacio[8][4] = tablero_escondido[8][4]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif  fila == 10 and columna == 6:
              tablero_vacio[8][4] = tablero_escondido[8][4]
              tablero_vacio[8][5] = tablero_escondido[8][5]
              tablero_vacio[8][6] = tablero_escondido[8][6]
              tablero_vacio[9][4] = tablero_escondido[9][4]
              tablero_vacio[9][5] = tablero_escondido[9][5]
              tablero_vacio[9][6] = tablero_escondido[9][6]
              tablero_vacio[10][4] = tablero_escondido[10][4]
              tablero_vacio[10][5] = tablero_escondido[10][5]
              tablero_vacio[10][6] = tablero_escondido[10][6]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (fila == 8 and columna == 8) or (fila == 7 and columna == 9):
              tablero_vacio[5][7] = tablero_escondido[5][7]
              tablero_vacio[5][8] = tablero_escondido[5][8]
              tablero_vacio[5][9] = tablero_escondido[5][9]
              tablero_vacio[6][6] = tablero_escondido[6][6]
              tablero_vacio[6][7] = tablero_escondido[6][7]
              tablero_vacio[6][8] = tablero_escondido[6][8]
              tablero_vacio[6][9] = tablero_escondido[6][9]
              tablero_vacio[7][6] = tablero_escondido[7][6]
              tablero_vacio[7][7] = tablero_escondido[7][7]
              tablero_vacio[7][8] = tablero_escondido[7][8]
              tablero_vacio[7][9] = tablero_escondido[7][9]
              tablero_vacio[8][6] = tablero_escondido[8][6]
              tablero_vacio[8][7] = tablero_escondido[8][7]
              tablero_vacio[8][8] = tablero_escondido[8][8]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif fila == 14 and columna == 8:
              tablero_vacio[12][6] = tablero_escondido[12][6]
              tablero_vacio[12][7] = tablero_escondido[12][7]
              tablero_vacio[12][8] = tablero_escondido[12][8]
              tablero_vacio[13][6] = tablero_escondido[13][6]
              tablero_vacio[13][7] = tablero_escondido[13][7]
              tablero_vacio[13][8] = tablero_escondido[13][8]
              tablero_vacio[14][6] = tablero_escondido[14][6]
              tablero_vacio[14][7] = tablero_escondido[14][7]
              tablero_vacio[14][8] = tablero_escondido[14][8]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (1 <= fila <= 4 and 11 <= columna <= 12) or (fila == 5 and columna == 13):
              tablero_vacio[0][9] = tablero_escondido[0][9]
              tablero_vacio[0][10] = tablero_escondido[0][10]
              tablero_vacio[0][11] = tablero_escondido[0][11]
              tablero_vacio[0][12] = tablero_escondido[0][12]
              tablero_vacio[1][9] = tablero_escondido[1][9]
              tablero_vacio[1][10] = tablero_escondido[1][10]
              tablero_vacio[1][11] = tablero_escondido[1][11]
              tablero_vacio[1][12] = tablero_escondido[1][12]
              tablero_vacio[2][9] = tablero_escondido[2][9]
              tablero_vacio[2][10] = tablero_escondido[2][10]
              tablero_vacio[2][11] = tablero_escondido[2][11]
              tablero_vacio[2][12] = tablero_escondido[2][12]
              tablero_vacio[3][9] = tablero_escondido[3][9]
              tablero_vacio[3][10] = tablero_escondido[3][10]
              tablero_vacio[3][11] = tablero_escondido[3][11]
              tablero_vacio[3][12] = tablero_escondido[3][12]
              tablero_vacio[3][13] = tablero_escondido[3][13]
              tablero_vacio[4][9] = tablero_escondido[4][9]
              tablero_vacio[4][10] = tablero_escondido[4][10]
              tablero_vacio[4][11] = tablero_escondido[4][11]
              tablero_vacio[4][12] = tablero_escondido[4][12]
              tablero_vacio[4][13] = tablero_escondido[4][13]
              tablero_vacio[5][11] = tablero_escondido[5][11]
              tablero_vacio[5][12] = tablero_escondido[5][12]
              tablero_vacio[5][13] = tablero_escondido[5][13]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (fila == 10 and 12 <= columna <= 13) or (11 <= fila <= 12 and 11 <= columna <= 12) or (fila == 13 and columna == 11):
              tablero_vacio[8][10] = tablero_escondido[8][10]
              tablero_vacio[8][11] = tablero_escondido[8][11]
              tablero_vacio[8][12] = tablero_escondido[8][12]
              tablero_vacio[8][13] = tablero_escondido[8][13]
              tablero_vacio[9][9] = tablero_escondido[9][9]
              tablero_vacio[9][10] = tablero_escondido[9][10]
              tablero_vacio[9][11] = tablero_escondido[9][11]
              tablero_vacio[9][12] = tablero_escondido[9][12]
              tablero_vacio[9][13] = tablero_escondido[9][13]
              tablero_vacio[10][9] = tablero_escondido[10][9]
              tablero_vacio[10][10] = tablero_escondido[10][10]
              tablero_vacio[10][11] = tablero_escondido[10][11]
              tablero_vacio[10][12] = tablero_escondido[10][12]
              tablero_vacio[10][13] = tablero_escondido[10][13]
              tablero_vacio[11][9] = tablero_escondido[11][9]
              tablero_vacio[11][10] = tablero_escondido[11][10]
              tablero_vacio[11][11] = tablero_escondido[11][11]
              tablero_vacio[11][12] = tablero_escondido[11][12]
              tablero_vacio[12][9] = tablero_escondido[12][9]
              tablero_vacio[12][10] = tablero_escondido[12][10]
              tablero_vacio[12][11] = tablero_escondido[12][11]
              tablero_vacio[12][12] = tablero_escondido[12][12]
              tablero_vacio[13][9] = tablero_escondido[13][9]
              tablero_vacio[13][10] = tablero_escondido[13][10]
              tablero_vacio[13][11] = tablero_escondido[13][11]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (fila == 6 and 15 <= columna <= 17) or (7 <= fila <= 8 and columna == 17):
              tablero_vacio[4][13] = tablero_escondido[4][13]
              tablero_vacio[4][14] = tablero_escondido[4][14]
              tablero_vacio[4][15] = tablero_escondido[4][15]
              tablero_vacio[4][16] = tablero_escondido[4][16]
              tablero_vacio[4][17] = tablero_escondido[4][17]
              tablero_vacio[5][13] = tablero_escondido[5][13]
              tablero_vacio[5][14] = tablero_escondido[5][14]
              tablero_vacio[5][15] = tablero_escondido[5][15]
              tablero_vacio[5][16] = tablero_escondido[5][16]
              tablero_vacio[5][17] = tablero_escondido[5][17]
              tablero_vacio[6][13] = tablero_escondido[6][13]
              tablero_vacio[6][14] = tablero_escondido[6][14]
              tablero_vacio[6][15] = tablero_escondido[6][15]
              tablero_vacio[6][16] = tablero_escondido[6][16]
              tablero_vacio[6][17] = tablero_escondido[6][17]
              tablero_vacio[7][15] = tablero_escondido[7][15]
              tablero_vacio[7][16] = tablero_escondido[7][16]
              tablero_vacio[7][17] = tablero_escondido[7][17]
              tablero_vacio[8][15] = tablero_escondido[8][15]
              tablero_vacio[8][16] = tablero_escondido[8][16]
              tablero_vacio[8][17] = tablero_escondido[8][17]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif fila == 16 and 15 <= columna <= 19:
              tablero_vacio[14][13] = tablero_escondido[14][13]
              tablero_vacio[14][14] = tablero_escondido[14][14]
              tablero_vacio[14][15] = tablero_escondido[14][15]
              tablero_vacio[14][16] = tablero_escondido[14][16]
              tablero_vacio[14][17] = tablero_escondido[14][17]
              tablero_vacio[14][18] = tablero_escondido[14][18]
              tablero_vacio[14][19] = tablero_escondido[14][19]
              tablero_vacio[15][13] = tablero_escondido[15][13]
              tablero_vacio[15][14] = tablero_escondido[15][14]
              tablero_vacio[15][15] = tablero_escondido[15][15]
              tablero_vacio[15][16] = tablero_escondido[15][16]
              tablero_vacio[15][17] = tablero_escondido[15][17]
              tablero_vacio[15][18] = tablero_escondido[15][18]
              tablero_vacio[15][19] = tablero_escondido[15][19]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (4 <= fila <= 8 and columna == 21) or (fila == 9 and 19 <= columna <= 22) or (fila == 10 and columna == 19) or (fila == 10 and 23 <= columna <= 25):
              tablero_vacio[2][19] = tablero_escondido[2][19]
              tablero_vacio[2][20] = tablero_escondido[2][20]
              tablero_vacio[2][21] = tablero_escondido[2][21]
              tablero_vacio[3][19] = tablero_escondido[3][19]
              tablero_vacio[3][20] = tablero_escondido[3][20]
              tablero_vacio[3][21] = tablero_escondido[3][21]
              tablero_vacio[4][19] = tablero_escondido[4][19]
              tablero_vacio[4][20] = tablero_escondido[4][20]
              tablero_vacio[4][21] = tablero_escondido[4][21]
              tablero_vacio[5][19] = tablero_escondido[5][19]
              tablero_vacio[5][20] = tablero_escondido[5][20]
              tablero_vacio[5][21] = tablero_escondido[5][21]
              tablero_vacio[6][19] = tablero_escondido[6][19]
              tablero_vacio[6][20] = tablero_escondido[6][20]
              tablero_vacio[6][21] = tablero_escondido[6][21]
              tablero_vacio[7][17] = tablero_escondido[7][17]
              tablero_vacio[7][18] = tablero_escondido[7][18]
              tablero_vacio[7][19] = tablero_escondido[7][19]
              tablero_vacio[7][20] = tablero_escondido[7][20]
              tablero_vacio[7][21] = tablero_escondido[7][21]
              tablero_vacio[7][22] = tablero_escondido[7][22]
              tablero_vacio[8][17] = tablero_escondido[8][17]
              tablero_vacio[8][18] = tablero_escondido[8][18]
              tablero_vacio[8][19] = tablero_escondido[8][19]
              tablero_vacio[8][20] = tablero_escondido[8][20]
              tablero_vacio[8][21] = tablero_escondido[8][21]
              tablero_vacio[8][22] = tablero_escondido[8][22]
              tablero_vacio[8][23] = tablero_escondido[8][23]
              tablero_vacio[8][24] = tablero_escondido[8][24]
              tablero_vacio[8][25] = tablero_escondido[8][25]
              tablero_vacio[9][17] = tablero_escondido[9][17]
              tablero_vacio[9][18] = tablero_escondido[9][18]
              tablero_vacio[9][19] = tablero_escondido[9][19]
              tablero_vacio[9][20] = tablero_escondido[9][20]
              tablero_vacio[9][21] = tablero_escondido[9][21]
              tablero_vacio[9][22] = tablero_escondido[9][22]
              tablero_vacio[9][23] = tablero_escondido[9][23]
              tablero_vacio[9][24] = tablero_escondido[9][24]
              tablero_vacio[9][25] = tablero_escondido[9][25]
              tablero_vacio[10][17] = tablero_escondido[10][17]
              tablero_vacio[10][18] = tablero_escondido[10][18]
              tablero_vacio[10][19] = tablero_escondido[10][19]
              tablero_vacio[10][21] = tablero_escondido[10][21]
              tablero_vacio[10][22] = tablero_escondido[10][22]
              tablero_vacio[10][23] = tablero_escondido[10][23]
              tablero_vacio[10][24] = tablero_escondido[10][24]
              tablero_vacio[10][25] = tablero_escondido[10][25]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif 13 <= fila <= 14 and columna == 22:
              tablero_vacio[11][20] = tablero_escondido[11][20]
              tablero_vacio[11][21] = tablero_escondido[11][21]
              tablero_vacio[11][22] = tablero_escondido[11][22]
              tablero_vacio[12][20] = tablero_escondido[12][20]
              tablero_vacio[12][21] = tablero_escondido[12][21]
              tablero_vacio[12][22] = tablero_escondido[12][22]
              tablero_vacio[13][20] = tablero_escondido[13][20]
              tablero_vacio[13][21] = tablero_escondido[13][21]
              tablero_vacio[13][22] = tablero_escondido[13][22]
              tablero_vacio[14][20] = tablero_escondido[14][20]
              tablero_vacio[14][21] = tablero_escondido[14][21]
              tablero_vacio[14][22] = tablero_escondido[14][22]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (4 <= fila <= 5 and 25 <= columna <= 26) or (fila == 3 and columna == 26):
              tablero_vacio[1][24] = tablero_escondido[1][24]
              tablero_vacio[1][25] = tablero_escondido[1][25]
              tablero_vacio[1][26] = tablero_escondido[1][26]
              tablero_vacio[2][23] = tablero_escondido[2][23]
              tablero_vacio[2][24] = tablero_escondido[2][24]
              tablero_vacio[2][25] = tablero_escondido[2][25]
              tablero_vacio[2][26] = tablero_escondido[2][26]
              tablero_vacio[3][23] = tablero_escondido[3][23]
              tablero_vacio[3][24] = tablero_escondido[3][24]
              tablero_vacio[3][25] = tablero_escondido[3][25]
              tablero_vacio[3][26] = tablero_escondido[3][26]
              tablero_vacio[4][23] = tablero_escondido[4][23]
              tablero_vacio[4][24] = tablero_escondido[4][24]
              tablero_vacio[4][25] = tablero_escondido[4][25]
              tablero_vacio[4][26] = tablero_escondido[4][26]
              tablero_vacio[5][23] = tablero_escondido[5][23]
              tablero_vacio[5][24] = tablero_escondido[5][24]
              tablero_vacio[5][25] = tablero_escondido[5][25]
              tablero_vacio[5][26] = tablero_escondido[5][26]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (11 <= fila <= 12 and 28 <= columna <= 29) or (fila == 13 and columna == 29):
              tablero_vacio[9][26] = tablero_escondido[9][26]
              tablero_vacio[9][27] = tablero_escondido[9][27]
              tablero_vacio[9][28] = tablero_escondido[9][28]
              tablero_vacio[9][29] = tablero_escondido[9][29]
              tablero_vacio[10][26] = tablero_escondido[10][26]
              tablero_vacio[10][27] = tablero_escondido[10][27]
              tablero_vacio[10][28] = tablero_escondido[10][28]
              tablero_vacio[10][29] = tablero_escondido[10][29]
              tablero_vacio[11][26] = tablero_escondido[11][26]
              tablero_vacio[11][27] = tablero_escondido[11][27]
              tablero_vacio[11][28] = tablero_escondido[11][28]
              tablero_vacio[11][29] = tablero_escondido[11][29]
              tablero_vacio[12][26] = tablero_escondido[12][26]
              tablero_vacio[12][27] = tablero_escondido[12][27]
              tablero_vacio[12][28] = tablero_escondido[12][28]
              tablero_vacio[12][29] = tablero_escondido[12][29]
              tablero_vacio[13][27] = tablero_escondido[13][27]
              tablero_vacio[13][28] = tablero_escondido[13][28]
              tablero_vacio[13][29] = tablero_escondido[13][29]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif 4 <= fila <= 5 and 30 <= columna <= 31:
              tablero_vacio[2][28] = tablero_escondido[2][28]
              tablero_vacio[2][29] = tablero_escondido[2][29]
              tablero_vacio[2][30] = tablero_escondido[2][30]
              tablero_vacio[3][28] = tablero_escondido[3][28]
              tablero_vacio[3][29] = tablero_escondido[3][29]
              tablero_vacio[3][30] = tablero_escondido[3][30]
              tablero_vacio[4][28] = tablero_escondido[4][28]
              tablero_vacio[4][29] = tablero_escondido[4][29]
              tablero_vacio[4][30] = tablero_escondido[4][30]
              tablero_vacio[5][28] = tablero_escondido[5][28]
              tablero_vacio[5][29] = tablero_escondido[5][29]
              tablero_vacio[5][30] = tablero_escondido[5][30]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            elif (fila == 15 and columna == 1) or (fila == 16 and 1 <= columna <= 4):
              tablero_vacio[13][0] = tablero_escondido[13][0]
              tablero_vacio[13][1] = tablero_escondido[13][1]
              tablero_vacio[14][0] = tablero_escondido[14][0]
              tablero_vacio[14][1] = tablero_escondido[14][1]
              tablero_vacio[14][2] = tablero_escondido[14][2]
              tablero_vacio[14][3] = tablero_escondido[14][3]
              tablero_vacio[14][4] = tablero_escondido[14][4]
              tablero_vacio[15][0] = tablero_escondido[15][0]
              tablero_vacio[15][1] = tablero_escondido[15][1]
              tablero_vacio[15][2] = tablero_escondido[15][2]
              tablero_vacio[15][3] = tablero_escondido[15][3]
              tablero_vacio[15][4] = tablero_escondido[15][4]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
            else:
              #El siguiente else se activa cuando la celda elegida es un número porque ya descartamos que no es una bomba y si no se activo en los elif anteriores, sólo queda que sea un número
              tablero_vacio[fila-1][columna-1] = tablero_escondido[fila-1][columna-1]
              despliega_tablero(tablero_vacio)
              limpia()
              return 1
        else:
          #El siguiente else se activa cuando la celda elegida pertenece a una bomba
          tablero_vacio[fila-1][columna-1] = tablero_escondido[fila-1][columna-1]
          limpia()
          print('HAS PERDIDO\n')
          despliega_tablero(tablero_vacio)
          return 2
      else:
        limpia()
        print('\nVALORES REPETIDOS')
        return 1
    else:
      limpia()
      print('\nVALORES FUERA DE RANGO')
      return 1



def limpia():
  '''Función que limpia a pantalla sin importar el sistema operativo de la máquina donde esté corriendo'''
  if os.name == 'nt':
    os.system('cls') #Windows
  else: #'posix'
    os.system('clear') #Mac/Linux

#Ejecuto la función main
main()