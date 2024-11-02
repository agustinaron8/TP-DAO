from tkinter import *
from tkinter.ttk import *
from Entidades.Libro import Libro
from tkinter import messagebox as MessageBox

class VentanaABMLibro:
    
    def __init__(self, principal, modo):

        # Asignacion de la ventana principal
        self.principal = principal
        self.modo = modo
        
        # Creación de la ventana
        self.ventana = Tk()
        
        # Configuración de la ventana
        if modo == 1:
            self.ventana.title("Registrar libro")
        elif modo == 2:
            self.ventana.title("Modificar libro")
        elif modo == 3:
            self.ventana.title("Eliminar libro")
            
        self.ventana.geometry("400x200")
        
        # Creación de las etiquetas
        Label(self.ventana, text="Código: ").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Título: ").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Precio de reposición: $").grid(column=0, row=2, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Estado: ").grid(column=0, row=3, padx=10, pady=10, sticky="e")
        
        # Creación de los cuadros de texto
        self.txt_codigo = Entry(self.ventana, width=30)
        self.txt_titulo = Entry(self.ventana, width=30)
        self.txt_precio = Entry(self.ventana, width=30)
        self.txt_estado = Entry(self.ventana, width=30)
        
        if modo != 1:
            self.txt_codigo.insert(0, self.principal.libro_seleccionado.codigo)
            self.txt_titulo.insert(0, self.principal.libro_seleccionado.titulo)
            self.txt_precio.insert(0, self.principal.libro_seleccionado.precio_reposicion)
            self.txt_estado.insert(0, self.principal.libro_seleccionado.estado)
        
        if modo == 3:
            self.txt_codigo.config(state="disabled")
            self.txt_titulo.config(state="disabled")
            self.txt_precio.config(state="disabled")
            self.txt_estado.config(state="disabled")

        # Ubicación de los cuadros de texto en la ventana        
        self.txt_codigo.grid(column=1, row=0, sticky="w")
        self.txt_titulo.grid(column=1, row=1, sticky="w")
        self.txt_precio.grid(column=1, row=2, sticky="w")
        self.txt_estado.grid(column=1, row=3, sticky="w")

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
        
        codigo = self.txt_codigo.get()
        titulo = self.txt_titulo.get()
        precio = self.txt_precio.get()
        estado = self.txt_estado.get()
        
        if self.modo == 3:
            if MessageBox.askyesno(message="¿Está seguro que desea dar de baja el libro?"):
                self.principal.libroDB.eliminar_libro(self.principal.libro_seleccionado.codigo)
                self.principal.refrescar()
                MessageBox.showinfo("Baja", "El libro se ha ha dado de baja.")
                self.ventana.destroy()
        
        elif self.validar(codigo, titulo, precio, estado):
            if self.modo == 1:
                nuevoLibro = Libro(codigo, titulo, precio, estado)
                self.principal.libroDB.insertar_libro(nuevoLibro)
                self.principal.refrescar()
                MessageBox.showinfo("Registro", "El libro se ha registrado.")
                self.ventana.destroy()
            if self.modo == 2:
                if MessageBox.askyesno(message="¿Está seguro que desea modificar el libro?"):
                    libroModificado = Libro(codigo, titulo, precio, estado)
                    self.principal.libroDB.actualizar_libro(libroModificado)
                    self.principal.refrescar()
                    MessageBox.showinfo("Modificación", "El libro se ha modificado.")
                    self.ventana.destroy()
    
    def validar(self, cod, tit, precio, est):
        esvalido = True
        if cod=="" or tit=="" or precio=="" or est=="":
            MessageBox.showwarning("Error", "Debe completar todos los campos.")
            esvalido = False
            return esvalido
        
        # Validar codigo que sean números
        if not cod.isdigit():
            MessageBox.showerror("Error", "El código debe ser un número.")
            esvalido = False
            return esvalido
        
        # Validar que no haya un libro con el mismo código
        for libro in self.principal.libros:
            if (libro.codigo == int(cod) and self.modo == 1) or (libro.codigo == int(cod) and libro.codigo != self.principal.libro_seleccionado.codigo and self.modo == 2):
                MessageBox.showerror("Error", "Ya existe un libro con el mismo código.")
                esvalido = False
                return esvalido
        

        # Validar que el precio sea un digito
        if not precio.isdigit():
            MessageBox.showerror("Error", "El precio debe ser un número sin coma o debe ser mayor a 0.")
            esvalido = False
            return esvalido

        return esvalido
                
    def mostrar(self):
        self.ventana.mainloop()