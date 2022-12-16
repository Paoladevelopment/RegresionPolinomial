import tkinter as tk
from PIL import ImageTk, Image
import basic_tab as bt

#Creación de la ventana principal
root= tk.Tk()

#Nombre de nuestra aplicación
root.title("Mínimos cuadrados")
#Dimensiones de la ventana
root.geometry("900x700+500+150")
#para impedir redimensionar la ventana
root.resizable(0,0)
#Widget principal, el frame contiene otros widgets
main_frame= tk.Frame(root, bg='#feebdd')
main_frame.pack(fill=tk.BOTH, expand=True)
#Imagen de fondo
imagen= ImageTk.PhotoImage(Image.open('img/fondo_app.jpg'))
labelImagenFondo= tk.Label(main_frame, image=imagen, border=0).place(x=0, y=50)

#Titulo ventana
titulo= tk.Label(main_frame, text= "Mínimos cuadrados", font=('Cooper Black', 28), bg='#feebdd', fg='#000000').place(x= 290, y=0)

#Botón para nuestra nueva ventana (Donde se albergará la aplicación)

#Btn versión básica
def cambiar_pag():
  bt.nueva_ventana(main_frame)

semiround_basic= ImageTk.PhotoImage(file= 'img/boton_basico.png')
boton_basico= tk.Button(main_frame, image=semiround_basic, border=0, bg='#feebdd', activebackground='#feebdd', cursor="hand2 #ffffff", command=cambiar_pag).place(x=240,y=270)

#Btn salir
semiround_salir= ImageTk.PhotoImage(file= 'img/boton_salir.png')
boton_pro= tk.Button(main_frame, image=semiround_salir, border=0, bg='#feebdd', activebackground='#feebdd', cursor="hand2 #ffffff", command=root.destroy).place(x=240,y=380)


root.mainloop()