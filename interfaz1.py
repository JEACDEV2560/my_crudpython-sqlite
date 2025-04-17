import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from my_conex import *
from clientes import *

class FormularioUsuarios:
    global base 
    base = None

    global textBoxId
    textBoxId= None

    global textBoxNombres
    textBoxNombres = None
    
    global textBoxApellidos
    textBoxApellidos = None

    global textBoxEdad
    textBoxEdad = None

    
    
    global combo
    combo = None

    global  groupBox
    groupBox = None

    global tree
    tree = None
    

def Formulario():
        global textBoxId
        global textBoxNombres
        global textBoxApellidos
        global combo
        global textBoxEdad
        global base 
        global groupBox
        global tree

        try:
              

            base = Tk()
            base.geometry("1450x300")
            base.title("CRUD python + sqlite")
            
            groupBox = LabelFrame(base,text="Datos del Usuario", padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            LabelId = Label (groupBox,text="Id",width=13, font=('arial',12)).grid(row=0,column=0)
            textBoxId=Entry(groupBox)
            textBoxId.grid(row=0,column=1)

            LabelNombres  = Label (groupBox,text="Nombres",width=13, font=('arial',12)).grid(row=1,column=0)
            textBoxNombres=Entry(groupBox)
            textBoxNombres.grid(row=1,column=1)

            LabelApellidos = Label (groupBox,text="Apellidos",width=13, font=('arial',12)).grid(row=2,column=0)
            textBoxApellidos=Entry(groupBox)
            textBoxApellidos.grid(row=2,column=1)

            LabelSexo = Label (groupBox,text="Sexo",width=13, font=('arial',12)).grid(row=3,column=0)
            seleccionSexo= tk.StringVar()
            combo= ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=seleccionSexo)
            combo.grid(row=3,column=1)
            seleccionSexo.set("Masculino,Femenino")

        
            LabelEdad = Label (groupBox,text="Edad",width=13, font=('arial',12)).grid(row=4,column=0)
            textBoxEdad=Entry(groupBox)
            textBoxEdad.grid(row=4,column=1)

            Button(groupBox,text="Guardar", width=10).grid(row=5,column=1)
            Button(groupBox,text="Modificar", width=10).grid(row=5,column=2)
            Button(groupBox,text="Eliminar", width=10).grid(row=5,column=3)

            groupBox= LabelFrame(base,text="Lista de Usuario", padx=5, pady=5)
            groupBox.grid(row=0,column=1,padx=5,pady=5)

            tree=  ttk.Treeview(groupBox,columns=("Id","Nombres", "Apellidos","Sexo","Edad"),show="headings",height=5,)
            tree.column("#1", anchor="center")
            tree.heading("#1", text="Id")
            tree.column("#2", anchor="center")
            tree.heading("#2", text="Nombres")
            tree.column("#3", anchor="center")
            tree.heading("#3", text="Apellidos")
            tree.column("#4", anchor="center")
            tree.heading("#4", text="Sexo")  # Added heading for Sexo
            tree.column("#5", anchor="center")
            tree.heading("#5", text="Edad")  # Added heading for Edad

            vsb= ttk.Scrollbar(groupBox,orient="vertical",command=tree.yview)
            tree.configure(yscrollcommand=vsb.set) 
            tree.pack(side="left",fill="both", expand=True)
            vsb.pack(side="right", fill="y")

            base.mainloop()

        except ValueError as error:
             print("Error al mostrar la interfaz: ",error)
       
       #Aqui llenamos la tabla de Base de datos 

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)
        #Llamamos a la funcion Formulario
       
       
       
       
       
        
Formulario()
        
        