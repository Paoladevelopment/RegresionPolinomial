import numpy as np
import numpy.linalg as lin 
matriz_mc= []
lst_term_independientes=[]
xi_ult_elevado= 0

#Función que se encarga de llenar la matriz de los coeficientes dado el grado de polinomio y los términos independientes, con sus valores iniciales. Como se está usando la técnica de mínimos cuadrados, la matriz de coeficientes es la sumatoria desde 0 hasta n= numero de los datos, siguiendo la siguiente formula:  
def ingresar_m(m):
  global matriz_mc
  global lst_term_independientes
  global xi_ult_elevado
  for i in range(0, m+1):
    columns= []
    r= i
    for j in range(0, m+1):
      columns.append(r)
      r+=1
    matriz_mc.append(columns)
  
  for i in range(0, m+1):
    lst_term_independientes.append(i)
  xi_ult_elevado= matriz_mc[m][m]
  print(matriz_mc)
  print(lst_term_independientes)

#Calcula la sumatoria de cada termino de nuestra matriz como lo indica la formula según sea el grado del polinomio. 
def calcular_mat_sumxi(xi, n):
  global matriz_mc 
  for i in range(0, len(matriz_mc)):
    for j in range(0, len(matriz_mc[0])):
      matriz_mc[i][j]= sumatoria_xi_elevada(xi, n, matriz_mc[i][j])

#Calcula la sumatoria de cada termino de nuestra lista como lo indica la formula según sea el grado del polinomio, así obteniendo los términos independientes. 
def calcular_mat_xiporyi(xi,yi,n):
  global lst_term_independientes
  for i in range(0, len(lst_term_independientes)):
    lst_term_independientes[i]= sumatoria_xi_por_yi(xi,yi,n, lst_term_independientes[i])


#sumatoria i=0 hasta n de xi^exponente
def sumatoria_xi_elevada(xi, n, exponente):
  suma=0
  for i in range(0, n):
    suma+= pow(xi[i], exponente)
  return suma

#sumatoria i=0 hasta n de xi^exponente*yi
def sumatoria_xi_por_yi(xi, yi, n, exponente):
  suma=0
  for i in range(0, n):
    suma+= pow(xi[i], exponente)*yi[i]
  return suma

#Convertir en arreglos de numpy nuestra matriz de coeficientes y de términos independientes y resolver el sistema de ecuaciones lineales
def resolver_sistema():
  A= np.array(matriz_mc)
  B= np.array(lst_term_independientes)
  print(A)
  print(B)
  solucion= lin.solve(A,B)
  print(solucion)
  return solucion

#obtener ultimo elemento elevado.
def ultimo_indice_elevado():
    return xi_ult_elevado


def operar_lista_xi(xi,exponente):
  xi_nueva=[]
  for i in range(0, len(xi)):
    xi_nueva.append(round(pow(xi[i], exponente), 6))
  return xi_nueva

def operar_lista_xiyi(xi,yi, exponente):
  xi_nueva=[]
  for i in range(0, len(xi)):
    xi_nueva.append(round(pow(xi[i], exponente)*yi[i], 6))
  return xi_nueva

def valores_default():
  global matriz_mc
  global lst_term_independientes
  matriz_mc= []
  lst_term_independientes=[]