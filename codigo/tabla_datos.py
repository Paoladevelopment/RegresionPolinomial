import tkinter as tk
from tkinter import ttk
import minimos_cuadrados as mc

#Para la creación de la tabla
def crear_tabla(page_tab, exp, m, xi, yi):

  #Esta columna alberga todas las columnas que tendrá la tabla en el orden: 
  #si es una recta : xi, yi, x^(grado), x^(grado)yi
  col=["xi", "yi"]
  for i in range(2, exp+1):
    col.append("xi^"+str(i))
  for i in range(1,m+1):
    col.append("xi^"+str(i)+"yi")

  #De esta manera se crea una tabla:
  table= ttk.Treeview(page_tab, columns=(col), show='headings',selectmode='no')
  my_tag='gray' #para darle un indicador a cada fila

  #configurar columnas, para establecer el tamaño de cada una, donde uno quiere que el dato esté si centrado, al inicio, etc.
  for i in range(0,len(col)+1):
    table.column("#"+str(i), anchor="w", stretch="no", width=120)

  #Nombrar cada columna
  for i in range(0,len(col)): 
    table.heading("#"+str(i+1), text=col[i])

  #Cuando se establece un tag a una fila, es para darle estilos personalizados. Acá personalizo para dar efecto de los colores de las filas intercalados entre blanco y gris
  table.tag_configure('gray', background='lightgray')
  table.tag_configure('normal', background='white')

  table.place(x=100, y=150, width=500, height=300)

  #Scrollbars
  scrollbarx= ttk.Scrollbar(page_tab, orient="horizontal")
  scrollbary= ttk.Scrollbar(page_tab, orient="vertical")
  table.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  scrollbary.configure(command=table.yview)
  scrollbarx.configure(command=table.xview)
  scrollbary.place(x=82, y=150, height=300)
  scrollbarx.place(x=100, y=450, width=500)
  

  #Llenar datos
  datos= [xi, yi]
  
  #Llenar los matriz de datos, con los valores de datos que se esté tratando, por ejemplo una columna que tiene el valor de: x^2
  for j in range(1, exp):
    datos.append(mc.operar_lista_xi(xi, j+1))


  for j in range(0, m):
    datos.append(mc.operar_lista_xiyi(xi, yi, j+1))


  values=[]
  for i in range(0, len(datos[0])):
    if(my_tag== 'gray'):
      my_tag= 'normal'
    else: my_tag= 'gray'
    for j in range(0, len(datos)):
      values.append(datos[j][i])
    table.insert("","end", values=(values) ,tags=my_tag)
    values=[]
  
  #Los datos de la fila con la suma total de cada columna
  suma_total= [round(mc.sumatoria_xi_elevada(xi, len(xi), 1), 8),
               round(mc.sumatoria_xi_elevada(yi,len(yi),1), 8)]
  for j in range(1, exp):
    suma_total.append(round(mc.sumatoria_xi_elevada(xi,len(xi), j+1), 8))


  for j in range(0, m):
    suma_total.append(round(mc.sumatoria_xi_por_yi(xi, yi,len(xi), j+1), 8))
  table.insert("","end", values=(suma_total) ,tags=my_tag)
      
 
