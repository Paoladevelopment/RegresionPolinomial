import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np 
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import minimos_cuadrados as mc
import tabla_datos as td

#se declaran acá porque necesito usarlas como varaibles globales
sol=[]
xi=[]
yi=[]

#Esta función te devuelve a la página inical
def devolver_pag_principal(page_actual):
  page_actual.pack_forget()

#Acá se encuentra todo el código de la página que genera el polinomio y la gráfica
def nueva_ventana(main_frame):
  global upload
  global upload1
  #Nueva página
  page_tab= tk.Frame(main_frame)
  page_tab.pack(fill=tk.BOTH, expand=True)
  page_tab.config(bg='#F4E39D')

  #Label cargar datos
  label_datos= tk.Label(page_tab, text="Cargar\nDatos:", font=('Jokerman', 30), bg='#f4e39d')
  label_datos.place(x= 160, y=5)

  #imagen selección archivo
  imagen_withoutresize= (Image.open('folder.png'))
  resized_image= imagen_withoutresize.resize((80, 80))
  upload= ImageTk.PhotoImage(resized_image)

  #Función para cargar el archivo
  def abrir_archivo():
    global archivo
    archivo= filedialog.askopenfilename(title="Elige un documento", initialdir="C:/Documents/")

  #Función que calcula el polinomio dado un grado introducido por el usuario por medio de la técnica de mínimos cuadrados
  def calcular_mc():
    global sol
    global xi
    global yi

    try:

      with open(archivo, "r") as File:
        file_content= File.readlines()
      File.close()

      lista_datos= []
      xi= []
      yi=[]
      #Crea una lista de datos con el contenido del archivo de texto,  ejemplo: (1,6 \n 2.3,5) donde el dato antes de la coma representa
      #el valor de x y después de la coma el de y. Entonces nuestra lista de datos sería ["1,6", "\n", "2.3,5"], es por eso que el dato \n tiene que reemplazarse
      #por comillas vacias. Realizado esto se puede añadir a la lista de datos
      for dato in file_content:
        dato= dato.replace("\n", "")
        lista_datos.append(dato)
      
      #Acá se recorre la lista de datos, usando substrings se van llenando xi e yi, recordemos que nuestros datos se almacenan: "x,y", para poder hacer el substring adecuado y poder guardar el valor de x en xi y el de y en yi, se debe saber el indice donde se encuentra la coma y obtener el dato de x [0:indice] y el de y [indice+1:]

      for i in range(0, len(lista_datos)):
        indice= int(lista_datos[i].index(","))
        xi.append(float(lista_datos[i][0:indice]))
        yi.append(float(lista_datos[i][indice+1:]))

      
      if grado_polinomio.get()== "":
        top= tk.Toplevel()
        top.geometry('+800+300')
        Label_error= tk.Label(top, text="Debes ingresar el grado de\nun polinomio")
        Label_error.pack()
      else:
        #se ingresa el grado del polinomio
        mc.ingresar_m(int(grado_polinomio.get()))
        #se calculan las matrices de los coeficientes y de los valores independientes.
        mc.calcular_mat_sumxi(xi, len(xi))
        mc.calcular_mat_xiporyi(xi, yi, len(xi))
        #se soluciona el sistema de ecuaciones
        sol= mc.resolver_sistema()

        #Crear y visualizar la tabla con los datos
        td.crear_tabla(page_tab, mc.ultimo_indice_elevado(),int(grado_polinomio.get()),xi,yi)
        
        #Mostrar el polinomio, nuestra la variable solución contiene en una lista los valores de nuestras incógnitas, entonces se recorre y se va añadiendo al string_sol
        string_sol= "Polinomio "
        grado_pol=0
        for i in range(0, len(sol)):
          if grado_pol==0:
            string_sol+=str(round(sol[i], 6)) + " + "
          elif grado_pol < int(grado_polinomio.get()):
            string_sol+=str(round(sol[i], 6))+"x^"+str(grado_pol) +" + "
          else:
            string_sol+=str(round(sol[i], 6))+"x^"+str(grado_pol)
          grado_pol+=1
        
        #Visualizar en nuestra ventana la solución, usando un entry para poder usar scrollbar
        thesoltext= tk.StringVar(value=string_sol)
        label_polinomio= tk.Entry(page_tab, textvariable=thesoltext, font=('Modern', 20), bg='#d5baa5', state='readonly')
        label_polinomio.place(x=100, y=500, width=400)
        scrollx= ttk.Scrollbar(page_tab, orient='horizontal', command=label_polinomio.xview)
        scrollx.place(x=100, y=530, width=100)
        label_polinomio.config(xscrollcommand=scrollx.set)

        #se reinician los valores a default las matrices que se manejan en el codigo de minimos cuadrados
        mc.valores_default()
    except:
      top= tk.Toplevel()
      top.geometry('+800+300')
      Label_error= tk.Label(top, text="Debes cargar\nun archivo")
      Label_error.pack()
      
    
  #Boton para abrir el archivo
  boton_upload= tk.Button(page_tab, border=0, bg='#f4e39d', activebackground='#f4e39d', cursor="hand2 #ffffff", image=upload, command=abrir_archivo)
  boton_upload.place(x=360,y=30)

  #Boton para generar la tabla y mostrar el polinomio generado
  boton_calcular= tk.Button(page_tab, text="Calcular\nPolinomio", font=('Helvetica', 10, 'bold'), cursor="hand2 #ffffff", command=calcular_mc)
  boton_calcular.place(x= 660, y=45)

  #entrada del grado del polinomio
  Label_ingresar_datos= tk.Label(page_tab, text="Grado polinomio", font=('Arial black', 10), bg='#f4e39d')
  Label_ingresar_datos.place(x=500, y= 40)
  grado_polinomio= tk.Entry(page_tab)
  grado_polinomio.place(x=500, y=70)

  #Boton para obtener gráfica
  def graficar():
    if sol== []:
      top= tk.Toplevel()
      top.geometry('+800+300')
      Label_error= tk.Label(top, text="Debes calcular\nel polinomio primero")
      Label_error.pack()
    else:
      #De esta manera se genera un polinomio usando numpy
      polinomio= Polynomial(coef=sol)
      x= np.linspace(start=0, stop=30, num=30)
      #para representar puntos
      plt.scatter(xi,yi)
      #para el gráfico de una función
      plt.plot(x, polinomio(x))
      plt.show()
      
  #Boton para generar la gráfica
  boton_grafica= tk.Button(page_tab, text="Graficar", font=('Helvetica', 10, 'bold'), cursor="hand2 #ffffff", command=graficar)
  boton_grafica.place(x= 750, y=55)

  #Boton para devolverse
  imagen_withoutresize= (Image.open('flecha_atras.png'))
  resized_image= imagen_withoutresize.resize((80, 80))
  upload1= ImageTk.PhotoImage(resized_image)
  btn= tk.Button(page_tab, image=upload1,bg='#f4e39d', activebackground='#f4e39d', cursor='hand2 #ffffff',border=0, command= lambda: devolver_pag_principal(page_tab))
  btn.place(x=780, y=590)


