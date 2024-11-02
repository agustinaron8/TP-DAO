from tkinter import *
from tkinter.ttk import *
from Entidades.Prestamo import Prestamo
from tkinter import messagebox as MessageBox
from Entidades.Libro import Libro
from Entidades.Prestamo import Prestamo
from Datos.Datos import BaseDeDatos


class VentanaABMPrestamo:
    
    def __init__(self, principal):

        
        # Asignacion de la ventana principal
        self.principal = principal
        
        # Creación de la ventana
        self.ventana = Tk()
        
        # Configuración de la ventana
        self.ventana.title("Registrar Prestamo")
        self.ventana.geometry("400x200")
        
        # Creación de las etiquetas
        Label(self.ventana, text="Codigo Libro: ").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Codigo Socio: ").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Fecha Prestamo: ").grid(column=0, row=2, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Fecha Devolución Pactada: ").grid(column=0, row=3, padx=10, pady=10, sticky="e")


        # Creación de los cuadros de texto
        self.txt_CodLib = Entry(self.ventana, width=30)
        self.txt_CodSoc = Entry(self.ventana, width=30)
        self.txt_FecPrest = Entry(self.ventana, width=30)
        self.txt_FecDevoPact = Entry(self.ventana, width=30)
        self.txt_FecDevo = Entry(self.ventana, width=30)

        # Ubicación de los cuadros de texto en la ventana        
        self.txt_CodLib.grid(column=1, row=0, sticky="w")
        self.txt_CodSoc.grid(column=1, row=1, sticky="w")
        self.txt_FecPrest.grid(column=1, row=2, sticky="w")
        self.txt_FecDevoPact.grid(column=1, row=3, sticky="w")


        # Creación y ubicación de los botones        
        botonera = Frame(self.ventana)
        botonera.grid(column=1, row=4, sticky="w")
        
        btn_aceptar = Button(botonera, text="Aceptar")
        btn_aceptar.pack(side="left")
        
        btn_cancelar = Button(botonera, text="Cancelar")
        btn_cancelar.pack(side="left")
        
        # Conexión del evento click del
        # botón aceptar con la función manejadora
        btn_aceptar["command"] = self.aceptar
        
        # Conexión del evento click del boton cancelar
        btn_cancelar["command"] = self.ventana.destroy
        
    def aceptar(self):
        
        CodLibro = self.txt_CodLib.get()
        CodSocio = self.txt_CodSoc.get()
        FechaPrestamo = self.txt_FecPrest.get()
        FechaDevolucionPactada = self.txt_FecDevoPact.get()
        
        if self.validar(CodLibro, CodSocio, FechaPrestamo, FechaDevolucionPactada):
            nuevoPrestamo = Prestamo(CodLibro, CodSocio,FechaPrestamo, FechaDevolucionPactada)
            self.principal.prestamoDB.insertar_prestamo(nuevoPrestamo)
            self.principal.refrescar()
            MessageBox.showinfo("Exito", "El prestamo se ha registrado correctamente.")
            self.ventana.destroy()


    def validar(self, CodLibro, CodSocio, FechaPrestamo, FechaDevolucionPactada):
        esvalido = True
        basedatos = Database()
        if CodLibro =="" or CodSocio=="" or FechaPrestamo=="" or FechaDevolucionPactada =="":
            MessageBox.showwarning("Error", "Debe completar todos los campos.")
            esvalido = False
            return esvalido
        
        prest = PrestamoDB(basedatos)
        listprest = prest.listar_prestamos()

        # Validar codigo que sean números

        if CodLibro.isdigit():
            CodLibro = int(CodLibro)
            for cod in listprest:
                if cod.libro == CodLibro:
                    MessageBox.showerror("Error", "El codigo libro ya existe.")
                    esvalido = False
                    return esvalido
        else:
            MessageBox.showerror("Error", "El codigo libro no tiene el formato correcto.")
            esvalido = False
            return esvalido
        if CodSocio.isdigit():
            CodSocio = int(CodSocio)
            libprest = 0 
            for i in listprest:
                if CodSocio == i.socio:
                    libprest += 1
                
            if libprest >= 3:
                MessageBox.showerror("Error", "El codigo socio tiene 3 o más libros registrados")
                esvalido = False
                return esvalido
            
        else:    
            MessageBox.showerror("Error", "El codigo socio no tiene el formato correcto.")
            esvalido = False
            return esvalido
        


        return esvalido
                
        
    def mostrar(self):
        self.ventana.mainloop()