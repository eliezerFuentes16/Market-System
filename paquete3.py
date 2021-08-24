from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import calendar
import locale
import time
import sys
import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import getpass
import tempfile
import os
from reportlab.lib.pagesizes import letter
logo=''


directorio=os.getcwd()

fecha=time.strftime("%d/%m/%y")
raiz=Tk()
raiz.geometry('1100x750')
raiz.state('zoomed')
raiz.title('SysMark')
raiz.configure(bg='#b6bdff')#lavender
raiz.iconbitmap(logo)

raiz.grid_rowconfigure(0, weight=1)
raiz.grid_columnconfigure(0, weight=1)

#tasa_del_dolar

tasa_del_dolar=DoubleVar()
true=1
false=0
tasa_del_dolar_nueva=DoubleVar()





#variables_venta


total_venta_B=DoubleVar()
total_venta_D=DoubleVar()

Buscar_venta_VEN=StringVar()



#total_filtro_venta
sub_total_iva_B_rp=DoubleVar()
sub_total_iva_D_rp=DoubleVar()

total_iva_B_rp=DoubleVar()
total_iva_D_rp=DoubleVar()

total_B_rp=DoubleVar()
total_D_rp=DoubleVar()


sub_total_B_rp=DoubleVar()
sub_total_D_rp=DoubleVar()

iva_B_rp=DoubleVar()
iva_D_rp=DoubleVar()

suma_total_B_rp=DoubleVar()
suma_total_D_rp=DoubleVar()
#-------------

tiempo=StringVar()

IVA=IntVar()
IVA.set(16)
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
continua=IntVar()

identificador_C=StringVar()
nombre_de_C=StringVar()
precio_total_D_C=DoubleVar()
precio_total_B_C=DoubleVar()

producto1_C=StringVar()
cantidad1_C=DoubleVar()

total_original_D_C=DoubleVar()
total_original_B_C=DoubleVar()
total=DoubleVar()
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
total_compra_bolivares_V=DoubleVar()
total_compra_dolares_V=DoubleVar()
tasa_del_dolar_V=DoubleVar()
cedula_cliente_V=StringVar()
Nombre_cliente_V=StringVar()
Apellido_cliente_V=StringVar()

oferta_V=StringVar()
cantidad_oferta_V=DoubleVar()

cedula_cliente_V2=StringVar()
Nombre_cliente_V2=StringVar()
Apellido_cliente_V2=StringVar()

identificador_de_venta2=IntVar()
identificador_de_deuda2=IntVar()
identificador_de_deuda=IntVar()
identificador_de_deuda3=IntVar()
identificador_de_venta3=IntVar()
enlace=0


Buscar_combo2=StringVar()

producto_ingresar_V=StringVar()
identificador_ingresar_V=StringVar()
precio_ingresar_D_V=DoubleVar()
precio_ingresar_B_V=DoubleVar()
cantidad_ingresar_V=DoubleVar()
exento_ingresar_V=BooleanVar()
unidad_ingresar_V=StringVar()
total_D=DoubleVar()
total_B=DoubleVar()
precio_ingresar_D_sin_iva_V=DoubleVar()
precio_ingresar_B_sin_iva_V=DoubleVar()
porcentaje_de_gacnancia_V=DoubleVar()



identificador_ingresar_B=StringVar()		
producto_ingresar_B=StringVar()
exento_ingresar_B=BooleanVar()
porcentaje_de_gacnancia_B=DoubleVar()
precio_ingresar_D_sin_iva_B=DoubleVar()
precio_ingresar_B_sin_iva_B=DoubleVar()
precio_original_D_B=DoubleVar()
precio_original_B_B=DoubleVar()
unidad_ingresar_B=StringVar()
precio_ingresar_D_B=DoubleVar()
precio_ingresar_B_B=DoubleVar()
cantidad_ingresar_B=DoubleVar()










total_venta_sin_iva_B=DoubleVar()
total_venta_sin_iva_D=DoubleVar()

total_iva_B=DoubleVar()
total_iva_D=DoubleVar()

precio_original_D_V=DoubleVar()
precio_original_B_V=DoubleVar()

producto_busca=StringVar()
cantidad_busca=DoubleVar()
combo_busca=StringVar()
cantidad2_busca=DoubleVar()

continua_V=StringVar()

identificador_de_combo=StringVar()

editar_producto_V=StringVar()
editar_cantidad_producto_V=DoubleVar()

enlace2=0
enlace3=0
#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
identificador_P=StringVar()
producto_P=StringVar()
precio_inicial_dolares_P=DoubleVar()
precio_inicial_bolivares_P=DoubleVar()
cantidad_P=DoubleVar()
unidad_p=StringVar()
exento_P=BooleanVar()
porcentaje_P=DoubleVar()
precio_final_B_P=DoubleVar()
precio_final_D_P=DoubleVar()
precio_final_D_P_iva=DoubleVar()
precio_final_B_P_iva=DoubleVar()
Buscar_producto_P=StringVar()
exento=BooleanVar()
a=''
ver_producto_con_oferta_P=BooleanVar()






agregar_departamento_depar=StringVar()

necesario_depar=StringVar()
#PPPPPPPPPPPPPPPPPPPPPPPPPPP
proveedor_pro=StringVar()
rif_pro=StringVar()
telefono_pro=StringVar()
direccion_pro=StringVar()



###################################3
proveedores_com=StringVar()
rif_com=StringVar()
producto_com=StringVar()
cantidad_com=DoubleVar()
precio_B_com=DoubleVar()
precio_D_com=DoubleVar()

buscar_proveedores_en_com=StringVar()
buscar_productos_en_com=StringVar()

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

cambur=''

identificador_=StringVar()
cantidad_=DoubleVar()
precio=DoubleVar()
producto=StringVar()

precio_oferta=DoubleVar()
producto_oferta=StringVar()
cantidad_oferta=DoubleVar()
total_oferta=DoubleVar()
identificador_oferta=StringVar()
producto_dos=StringVar()
cantidad_dos=DoubleVar()
Total=DoubleVar()
total_dos=DoubleVar()
dolares=DoubleVar()
dolares_dos=DoubleVar()
dolares_tres=DoubleVar()
dolares.set('')
total_D_oferta=DoubleVar()
total_B_oferta=DoubleVar()
precio_original_D_O=DoubleVar()
precio_original_B_O=DoubleVar()
#_---------------------VARIABLES OFERTAS----------------
identificador1=StringVar()
producto1=StringVar()
precio1=DoubleVar()
cantidad1=DoubleVar()
precio1.set('')

identificador2=StringVar()
producto2=StringVar()
precio2=DoubleVar()
cantidad2=StringVar()
precio2.set('')
precio.set('')
cantidad_.set('')
#CCCCCCCCCCCCCCCTTTTTTTTTTTTTTTTTNNNNNNNNNNNNN
continua2=StringVar()
continua_CTN=DoubleVar()

nombre_cliente_CTN=StringVar()
apellido_cliente_CTN=StringVar()
cedula_cliente_CTN=StringVar()
direccion_cliente_CTN=StringVar()
telefono_cliente_CTN=StringVar()
cedula_cliente_CTN.set('')
iden=DoubleVar()
iden.set(1)
#CCCCCCCCCCCCCCTTTTTTTTTTTTTTTTTTTNNNNNNNNNNNNNNNN


total_productos_ven_B=DoubleVar()
total_productos_ven_D=DoubleVar()
sub_total_productos_ven_B=DoubleVar()
sub_total_productos_ven_D=DoubleVar()
iva_productos_ven_D=DoubleVar()
iva_productos_ven_B=DoubleVar()
cantidad_productos_ven=DoubleVar()

Forma_de_pago=StringVar()


continua_compra=0
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
variable_clave=StringVar()
licencia_programa=StringVar()
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
nombre_cajero=StringVar()

def conectar_todo(event):
	pass


def conectar_Ofertas():#listo
	
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		try:
		
			micursor.execute('''
				CREATE TABLE OFERTAS (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				CODIGO_PRODUCTO VARCHAR(50),
				PRODUCTO_OFERTA VARCHAR(100),
				UNIDAD_OFERTA VARCHAR(10),
				DESCUENTO DECIMAL,
				TOTAL_OFERTA_D DECIMAL,
				TOTAL_OFERTA_B DECIMAL,
				DEPARTAMENTO VARCHAR(50),
				DURACION INTEGER,
				FECHA_OFERTA DATE,
				BOOLEANO BOOLEAN)

				''')
			messagebox.showinfo('BBDD','BBDD Ofertas creada con éxito')
		except:
			messagebox.showwarning('BBDD','La BBDD Ofertas ya éxiste')


def conectar_ofertas_por_departamentos():#listo
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	

	try:
		micursor.execute('''
			CREATE TABLE OFERTAS_DEPARTAMENTOS(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			DEPARTAMENTO VARCHAR(50),
			DESCUENTO DECIMAL,
			FECHA_INICIAL DATE,
			FECHA_FINAL DATE,
			BOOLEANO BOOLEAN)

		
			''')
		messagebox.showinfo('BBDD','BBDD Ofertas Departamentos creada con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Ofertas Departamentos ya éxiste')
#-----------------------------------------------------
def conectar_Productos():#LISTO
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	conectar_departamentos()

	try:
		micursor.execute('''
			CREATE TABLE PRODUCTOS(
			ID VARCHAR(50) UNIQUE NOT NULL,
			NOMBRE_PRODUCTO VARCHAR(100),
			CANTIDAD_PRODUCTO INTEGER,
			UNIDAD VARCHAR(20),
			EXENTO BOOLEAN,
			PRECIO_D_PRODUCTO DECIMAL,
			PRECIO_B_PRODUCTO INTEGER,
			PORCENTAJE_GANANCIA INTEGER,
			PRECIO_FINAL_D_P DECIMAL,
			PRECIO_FINAL_B_P DECIMAL,
			SUB_TOTAL_D DECIMAL,
			SUB_TOTAL_B DECIMAL,
			AUTO INTEGER PRIMARY KEY AUTOINCREMENT,
			DEPARTAMENTO VARCHAR(50))
			''')
		messagebox.showinfo('BBDD','BBDD Productos creada con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Productos ya éxiste')


def conectar_departamentos():#LISTO
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()

	try:
		micursor.execute('''
			CREATE TABLE DEPARTAMENTOS(
			DEPARTAMENTO VARCHAR(50),
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			TASA DECIMAL)
			''')
		agregar_departamento_por_defecto()
		messagebox.showinfo('BBDD','BBDD Departamentos creada  con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Departamentos ya éxiste')



def agregar_departamento_por_defecto():
			
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos3='Comida'.capitalize(),1000000

	micursor.execute("INSERT INTO DEPARTAMENTOS VALUES(?,NULL,?)",(datos3))
	miconexion.commit()
	
	agregar_departamento_depar.set('')



def conectar_combos():
    
    miconexion=sqlite3.connect('SISTEMA_LUMINA')
    mycursor=miconexion.cursor()
    try:
        
        mycursor.execute('''
        CREATE TABLE COMBOS_C (
        ID_COMBO VARCHAR(50) UNIQUE NOT NULL,
        NOMBRE_COMBO VARCHAR(50),
        TOTAL_BS_COMBO DECIMAL,
        TOTAL_DOLARES_COMBO DECIMAL,
        AUTO INTEGER PRIMARY KEY AUTOINCREMENT)

        ''')
        conectar_PRODUCTOS_COMBO()
        messagebox.showinfo('BBDD','BBDD creada Combos con éxito')
    except:
        messagebox.showwarning('BBDD','La BBDD Combos ya éxiste')


def conectar_PRODUCTOS_COMBO():
    
    miconexion=sqlite3.connect('SISTEMA_LUMINA')
    mycursor=miconexion.cursor()
    try:
        
        mycursor.execute('''
        CREATE TABLE PRODUCTOS_C (
        ID_COMBO VARCHAR(50),
        NOMBRE_PRODUCTO_C VARCHAR(50),
        CANTIDAD_PRODUCTO_C DECIMAL,
        UNIDAD_PRODUCTO_C VARCHAR(20),
        AUTO INTEGER PRIMARY KEY AUTOINCREMENT)

        ''')
        messagebox.showinfo('BBDD','BBDD creada Productos combos con éxito')
    except:
        messagebox.showwarning('BBDD','La BBDD Productos combos ya éxiste')
        	


def conectar_CTN():#LISTO
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	try:
		
		micursor.execute('''
			CREATE TABLE CLIENTES (
			NOMBRE_CLIENTE VARCHAR(50),
			APELLIDO_CLIENTE VARCHAR(50),
			CEDULA_CLIENTE INTEGER UNIQUE NOT NULL,
			DIRECCION_CLIENTE VARCHAR(100),
			TELEFONO_CLIENTE VARCHAR (12),
			FECHA INTEGER,
			AUTO INTEGER PRIMARY KEY AUTOINCREMENT)

			''')
		messagebox.showinfo('BBDD','BBDD creada Clientes con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Clientes ya éxiste')


def conectar_tasa_moneda():#LISTO
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	mycursor=miconexion.cursor()
	try:
        
		mycursor.execute('''
		CREATE TABLE TASA_MONEDA (
		ID_TASA INTEGER PRIMARY KEY AUTOINCREMENT,
		TASA DECIMAL,
		FECHA INTEGER,
		HORA INTEGER,
		BOOLEANO BOOLEAN)
		''')
		agregar_tasa_moneda_por_defecto()
		messagebox.showinfo('BBDD','BBDD creada Tasa con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Tasa ya éxiste')


def conectar_tasa_moneda_compras():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	mycursor=miconexion.cursor()
	try:
        
		mycursor.execute('''
		CREATE TABLE TASA_MONEDA_COMPRAS (
		ID_TASA INTEGER PRIMARY KEY AUTOINCREMENT,
		TASA DECIMAL,
		FECHA INTEGER,
		HORA INTEGER,
		BOOLEANO BOOLEAN,
		PROVEERDOR VARCHAR(100),
		COMPRADO BOOLEAN)
		''')
		agregar_tasa_moneda_por_defecto_compras()
		messagebox.showinfo('BBDD','BBDD creada Tasa con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Tasa ya éxiste')


def conectar_Formas_de_pago():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	mycursor=miconexion.cursor()
	try:
        
		mycursor.execute('''
		CREATE TABLE FORMAS_DE_PAGO (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		FORMAS_DE_PAGO VARCHAR(30))
		''')
		agregar_forma_de_pago_por_defecto()
		
	except:
		pass
		return


def agregar_forma_de_pago_por_defecto():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos=1000000,fecha,tiempo.get(),true,'Nulo',0
	micursor.execute("INSERT INTO FORMAS_DE_PAGO VALUES(NULL,?)",('Punto De Venta', ))
	micursor.execute("INSERT INTO FORMAS_DE_PAGO VALUES(NULL,?)",('Bio Pago', ))
	micursor.execute("INSERT INTO FORMAS_DE_PAGO VALUES(NULL,?)",('Transferencia', ))
	micursor.execute("INSERT INTO FORMAS_DE_PAGO VALUES(NULL,?)",('Pago Movil', ))
	micursor.execute("INSERT INTO FORMAS_DE_PAGO VALUES(NULL,?)",('Divisa', ))

	miconexion.commit()

conectar_Formas_de_pago()

def agregar_tasa_moneda_por_defecto():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos=1000000,fecha,tiempo.get(),true
	micursor.execute("INSERT INTO TASA_MONEDA VALUES(NULL,?,?,?,?)",(datos))
	miconexion.commit()
	
def agregar_tasa_moneda_por_defecto_compras():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos=1000000,fecha,tiempo.get(),true,'Nulo',0
	micursor.execute("INSERT INTO TASA_MONEDA_COMPRAS VALUES(NULL,?,?,?,?,?,?)",(datos))
	miconexion.commit()
	






def conectar_Ventas():#listo
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	
	
	try:
		micursor.execute('''
		CREATE TABLE VENTAS (
		ID_VENTAS INTEGER PRIMARY KEY AUTOINCREMENT,
		CEDULA_CLIENTE INTEGER,
		SUB_TOTAL_V_D DECIMAL,
		SUB_TOTAL_V_B DECIMAL,
		IVA_V_D DECIMAL,
		IVA_V_B DECIMAL,
		TOTAL_V_D DECIMAL,
		TOTAL_V_B DECIMAL,
		FECHA INTEGER,
		HORA INTEGER,
		TASA_DEL_DIA DECIMAL,
		BOOLEANOS BOOLEAN,
		CAJERO VARCHAR(100),
		NUMERO_CAJA INTEGER,
		FORMA_DE_PAGO VARCHAR(30))

		''')
		
		messagebox.showinfo('BBDD','BBDD creada Ventas con exito')
		crear_venta_V()
	except:
		messagebox.showwarning('BBDD','La BBDD Ventas ya existe')

def conectar_productos_de_Venta():#Listo
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	try:
		micursor.execute('''
		CREATE TABLE PRODUCTO_V(
		ID_VENTA INTEGER PRIMARY KEY AUTOINCREMENT,
		IDENTIFICADOR_DE_VENTA INTEGER,
		C_CLIENTE INTEGER,
		CODIGO_PRODUCTO VARCHAR(100),
		PRODUCTO VARCHAR(100),
		CANTIDAD INTEGER,
		EXENTO BOOLEAN,
		UNIDAD VARCHAR(10),
		PRECIO_D DECIMAL,
		PRECIO_B DECIMAL,
		PRECIO_TOTAL_D DECIMAL,
		PRECIO_TOTAL_B DECIMAL,
		PRECIO_TOTAL_D_SIN_IVA DECIMAL,
		PRECIO_TOTAL_B_SIN_IVA DECIMAL,
		PORCENTAJE_DE_PRODCUTO DECIMAL,
		PRECIO_ORIGINAL_D DECIMAL,
		PRECIO_ORIGINAL_B DECIMAL,
		FECHA INTEGER,
		BOOLEANOSS BOOLEAN,
		DEPARTAMENTO VARCHAR(50))
			''')
		messagebox.showinfo('BBDD','BBDD creada Productos ventas con exito')

	except:
		messagebox.showwarning('BBDD','La BBDD Productos ventas ya existe')



def conectar_productos_Deudas():#listo
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	try:
		micursor.execute('''
		CREATE TABLE PRODUCTOS_DEUDAS(
		ID_DEUDAS INTEGER PRIMARY KEY AUTOINCREMENT,
		IDENTIFICADOR_DE_DEUDA INTEGER,
		C_CLIENTE INTEGER,
		CODIGO_PRODUCTO VARCHAR(100),
		PRODUCTO VARCHAR(100),
		CANTIDAD INTEGER,
		EXENTO BOOLEAN,
		UNIDAD VARCHAR(10),
		PRECIO_D DECIMAL,
		PRECIO_B DECIMAL,
		PRECIO_TOTAL_D DECIMAL,
		PRECIO_TOTAL_B DECIMAL,
		PRECIO_TOTAL_D_SIN_IVA DECIMAL,
		PRECIO_TOTAL_B_SIN_IVA DECIMAL,
		PORCENTAJE_DE_PRODCUTO DECIMAL,
		PRECIO_ORIGINAL_D DECIMAL,
		PRECIO_ORIGINAL_B DECIMAL,
		FECHA INTEGER,
		BOOLEANOSS BOOLEAN,
		DEPARTAMENTO VARCHAR(50))
			''')
		messagebox.showinfo('BBDD','BBDD creada Productos Deudas con exito')

	except:
		messagebox.showwarning('BBDD','La BBDD Productos Deudas ya existe')

def conectar_compras_2():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	try:

		micursor.execute('''
		CREATE TABLE COMPRAS (
		ID_COMPRA INTEGER PRIMARY KEY AUTOINCREMENT,
		RIF_PROVEEDOR INTEGER,
		SUB_TOTAL_C_D DECIMAL,
		SUB_TOTAL_C_B DECIMAL,
		IVA_C_D DECIMAL,
		IVA_C_B DECIMAL,
		TOTAL_C_D DECIMAL,
		TOTAL_C_B DECIMAL,
		FECHA INTEGER,
		HORA INTEGER,
		TASA_DEL_DIA DECIMAL,
		BOOLEANOS BOOLEAN,
		ID_PIBOTE VARCHAR(50) UNIQUE NOT NULL)

		''')
		
		messagebox.showinfo('BBDD','BBDD creada Compras con exito')
		crear_compra()
	except:
		messagebox.showwarning('BBDD','La BBDD Compras ya existe')

		
	

def Conectar_compras():#LISTO
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	try:
		micursor.execute('''
		CREATE TABLE PRODUCTOS_COMPRAS(
		ID_COMPRA INTEGER PRIMARY KEY AUTOINCREMENT,
		IDENTIFICADOR_DE_COMPRA INTEGER,
		RIF_PROVEEDOR VARCHAR(30),
		CODIGO_PRODUCTO VARCHAR(100),
		PRODUCTO VARCHAR(100),
		CANTIDAD INTEGER,
		EXENTO BOOLEAN,
		UNIDAD VARCHAR(10),
		PRECIO_TOTAL_D DECIMAL,
		PRECIO_TOTAL_B DECIMAL,
		PORCENTAJE_DE_PRODCUTO DECIMAL,
		FECHA INTEGER,
		BOOLEANOSS BOOLEAN,
		DEPARTAMENTO VARCHAR(50),
		SUB_TOTAL_D DECIMAL,
		SUB_TOTAL_B DECIMAL)
			''')
		messagebox.showinfo('BBDD','BBDD creada Productos Deudas con exito')

	except:
		messagebox.showwarning('BBDD','La BBDD Productos Deudas ya existe')



def Conectar_proveedores():#listo

	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	mycursor=miconexion.cursor()
	try:
        
		mycursor.execute('''
		CREATE TABLE PROVEEDORES (
		AUTO INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_PROVEEDOR VARCHAR(150),
		RIF_PROVEEDOR VARCHAR(50) UNIQUE NOT NULL,
		TELEFONO_PROVEEDOR VARCHAR(20),
		DIRECCION_PROVEEDOR VARCHAR(100))
		''')
		messagebox.showinfo('BBDD','BBDD creada Proveedores con éxito')
	except:
		messagebox.showwarning('BBDD','La BBDD Proveedores ya éxiste')



def conectar_deudas():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	try:
		micursor.execute('''
		CREATE TABLE DEUDAS (
		ID_DEUDAS INTEGER PRIMARY KEY AUTOINCREMENT,
		CEDULA_CLIENTE INTEGER,
		SUB_TOTAL_D_D DECIMAL,
		SUB_TOTAL_D_B DECIMAL,
		IVA_D_D DECIMAL,
		IVA_D_B DECIMAL,
		TOTAL_D_D DECIMAL,
		TOTAL_D_B DECIMAL,
		FECHA INTEGER,
		HORA INTEGER,
		TASA_DEL_DIA DECIMAL,
		BOOLEANOS BOOLEAN,
		NOMBRE_CAJERO VARCHAR(100),
		NUMERO_CAJA INTEGER)

		''')
		
		messagebox.showinfo('BBDD','BBDD creada Deudas con exito')
		crear_deuda()
	except:
		messagebox.showwarning('BBDD','La BBDD Deudas ya existe')




def conectar_usuarios():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	try:
		micursor.execute('''
		CREATE TABLE USUARIOS (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_USUARIO VARCHAR(100),
		NUMERO_CAJA INTEGER,
		FECHA DATE,
		ESTADO BOOLEAN,
		BOOLEANO BOOLEAN)

		''')
		
		miconexion.commit()
		usuario_por_defecto()
	except:
		pass
		return

def usuario_por_defecto():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos='Cajero 1',1,fecha,1,1
	micursor.execute('INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?)',(datos))

	miconexion.commit()


conectar_usuarios()
numero_caja=IntVar()
def ver_cajero():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	micursor.execute('SELECT * FROM USUARIOS WHERE ESTADO=1 AND BOOLEANO=1')
	A=micursor.fetchall()
	for i in A:
		nombre_cajero.set(i[1])
		numero_caja.set(i[2])
	miconexion.commit()
ver_cajero()
print(nombre_cajero.get())


def conectar_licencia():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	try:
		micursor.execute('''
		CREATE TABLE LICENCIA (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		LOCAL VARCHAR(50),
		FECHA_INCIAL DATE,
		FECHA_FINAL DATE,
		BOOLEANO BOOLEAN,
		COSTO DECIMAL,
		USER VARCHAR (100))

		''')
		
		licencia_por_defecto()
	except:
		pass
		return


conectar_licencia()


def licencia_por_defecto():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()

	datos='Defecto','Nulo','Nulo',0,'Nulo'
	micursor.execute("INSERT INTO LICENCIA VALUES(NULL,?,?,?,?,?)",(datos))

	miconexion.commit()






def verificar_fecha_licencia():
	if fecha!='':
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		fecha_actual=fecha.split('/');print(fecha_actual,'fecha_actual')
	
		dia_a=fecha_actual[0]
		mes_a=fecha_actual[1]
		año_a=fecha_actual[2]

		micursor.execute("SELECT * FROM LICENCIA WHERE BOOLEANO=1")
		a=micursor.fetchall()
		for i in a:
			fecha_final=i[3].split('/')

			dia_f=fecha_final[0]
			mes_f=fecha_final[1]
			año_f=fecha_final[2]
			a10=getpass.getuser()
			print(a10,i[6])
			if a10!=i[6]:
				messagebox.showerror('BBDD','Error al abrir programa')
				return

			if dia_f<=dia_a and mes_f<=mes_a and año_f<=año_a:
				micursor.execute("UPDATE LICENCIA SET BOOLEANO=0 WHERE BOOLEANO=1")



		miconexion.commit()
	
		
def maldad_licencia():
	hola=StringVar()
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()

	micursor.execute("SELECT * FROM LICENCIA WHERE BOOLEANO=1")
	x=micursor.fetchall()
	print(x)
	for i in x:
		hola.set(i[0])
	if hola.get()!='':
		
			

		licencia_programa.set('si')
	else:
		licencia_programa.set('no')

	a10=getpass.getuser()
	
	a10=getpass.getuser()
	micursor.execute("SELECT * FROM LICENCIA WHERE BOOLEANO=1")
	x=micursor.fetchall()
	for i in x:
		if a10!=i[6]:
			licencia_programa.set('no')

	miconexion.commit()

	


verificar_fecha_licencia()
maldad_licencia()


def alterar_tabla():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	mycursor=miconexion.cursor()
	mycursor.execute('ALTER TABLE COMPRAS ADD COLUMN id INTEGER')
	miconexion.commit()


def run_query(query,parametro=()):
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	result=micursor.execute(query,parametro)
	miconexion.commit()
	return result



def informacion_sobre_licencia():
	info=Toplevel(raiz)
	info.title('Informacion')
	ancho_ventana = 400
	alto_ventana = 300
	x_ventana = info.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = info.winfo_screenheight() // 2 - alto_ventana // 2
	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
	info.geometry(posicion)
	info.config(bg='#b6bdff')
	info.iconbitmap(logo)
	info.resizable(0,0)


	Label(info,text='Creador: ',bg='#b6bdff',font='Helvetica 12').place(x=20,y=20)
	creador=Text(info,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b6bdff')
	creador.place(x=115,y=20)

	creador.configure(state='normal')
	creador.insert(END, 'Eliezer David Fuentes Moreno')
	creador.configure(state='disabled')


	Label(info,text='Programa: ',bg='#b6bdff',font='Helvetica 12').place(x=20,y=80)
	cedula_id=Text(info,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b6bdff')
	cedula_id.place(x=115,y=80)

	cedula_id.configure(state='normal')
	cedula_id.insert(END, 'SysMark V1.0.0')
	cedula_id.configure(state='disabled')

	Label(info,text='Telefono: ',bg='#b6bdff',font='Helvetica 12').place(x=20,y=140)
	telefono=Text(info,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b6bdff')
	telefono.place(x=115,y=140)

	telefono.configure(state='normal')
	telefono.insert(END, '0416-687-6793')
	telefono.configure(state='disabled')


	Label(info,text='Correo: ',bg='#b6bdff',font='Helvetica 12').place(x=20,y=200)
	telefono=Text(info,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b6bdff')
	telefono.place(x=115,y=200)

	telefono.configure(state='normal')
	telefono.insert(END, 'SysMark807@gmail.com')
	telefono.configure(state='disabled')



def accediendo():
	hija2=Toplevel(raiz)
	hija2.configure(bg='#b6bdff')
	ancho_ventana = 800
	alto_ventana = 530
	x_ventana = hija2.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = hija2.winfo_screenheight() // 2 - alto_ventana // 2
	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
	hija2.geometry(posicion)
	
	hija2.iconbitmap(logo)
	hija2.resizable(0,0)
	hija2.transient(master=raiz)

	botonsito=Button(hija2,cursor='hand2',text='Productos',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_Productos)
	botonsito.place(x=50,y=30)

	botonsito2=Button(hija2,cursor='hand2',text='Ofertas',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_Ofertas)
	botonsito2.place(x=50,y=100)

	botonsito3=Button(hija2,cursor='hand2',text='Combos',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_combos)
	botonsito3.place(x=50,y=170)

	botonsito4=Button(hija2,cursor='hand2',text='Clientes',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_CTN)
	botonsito4.place(x=50,y=240)

	botonsito5=Button(hija2,cursor='hand2',text='Tasa',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_tasa_moneda)
	botonsito5.place(x=50,y=310)

	botonsito5=Button(hija2,cursor='hand2',text='Ventas',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_Ventas)
	botonsito5.place(x=50,y=380)

	botonsito5=Button(hija2,cursor='hand2',text='Proveedores',height=2,width=10,font='Helvetica 12',bg='silver',command=Conectar_proveedores)
	botonsito5.place(x=50,y=450)

	botonsito5=Button(hija2,cursor='hand2',text='Compras',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_compras_2)
	botonsito5.place(x=200,y=30)

	botonsito5=Button(hija2,cursor='hand2',text='Ofertas D.',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_ofertas_por_departamentos)
	botonsito5.place(x=200,y=100)

	botonsito5=Button(hija2,cursor='hand2',text='Deudores',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_deudas)
	botonsito5.place(x=200,y=170)

	botonsito5=Button(hija2,cursor='hand2',text='Productos D',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_productos_Deudas)
	botonsito5.place(x=200,y=240)


	botonsito5=Button(hija2,cursor='hand2',text='Tasa C',height=2,width=10,font='Helvetica 12',bg='silver',command=conectar_tasa_moneda_compras)
	botonsito5.place(x=200,y=310)


	botonsito5=Button(hija2,cursor='hand2',text='Productos V',width=10,height=2,font='Helvetica 12',bg='silver',command=conectar_productos_de_Venta)
	botonsito5.place(x=200,y=380)

	botonsito5=Button(hija2,cursor='hand2',text='Compras P',width=10,height=2,font='Helvetica 12',bg='silver',command=Conectar_compras)
	botonsito5.place(x=200,y=450)





	local=StringVar()

	fecha1=StringVar()
	fecha2=StringVar()

	costo_licencia=DoubleVar()
	costo_licencia.set('')
	clave_licencia1=StringVar()



	def ver_licencias():
		record=lista_licen.get_children()
		for element in record:
			lista_licen.delete(element)


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		micursor.execute("SELECT * FROM LICENCIA")
		A=micursor.fetchall()
		for i in A:


			if i[4]==1:
				s='Si'
			elif i[4]==0:
				s='No'

			lista_licen.insert('',0,text=i[2],values=(i[3],i[5],s))








	#-----------------
	def aceptar_licencia():
		acl=Toplevel(hija2)
		ancho_ventana = 300
		alto_ventana = 425
		x_ventana = acl.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = acl.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		acl.geometry(posicion)
		
		acl.iconbitmap(logo)
		acl.config(bg='#b6bdff')
		acl.resizable(0,0)
		if mes_licen.get()=='Enero':
			me='01'
		elif mes_licen.get()=='Febrero':
			me='02'
		elif mes_licen.get()=='Marzo':
			me='03'
		elif mes_licen.get()=='Abril':
			me='04'
		elif mes_licen.get()=='Mayo':
			me='05'
		elif mes_licen.get()=='Junio':
			me='06'
		elif mes_licen.get()=='Julio':
			me='07'
		elif mes_licen.get()=='Agosto':
			me='08'
		elif mes_licen.get()=='Septiembre':
			me='09'								
		elif mes_licen.get()=='Octubre':				
			me='10'
		elif mes_licen.get()=='Noviembre':
			me='11'
		elif mes_licen.get()=='Diciembre':
			me='12'

		elif mes_licen.get()=='Todos':
			me='00'
		elif mes_licen.get()=='Prueba':
			mes_final2=int(time.strftime("%m"))
			me=str(mes_final2+1)

			if mes_final2<10:
				me='0'+me

			elif mes_final2==12:
				me='01'
			print(me)

		a=int(años_licen.get())
		año=a-2000

		fecha_licencia=str(dia_licen.get())+'/'+me+'/'+str(año)				
		print(fecha_licencia)


		def funcion_clave2():
			clave=Toplevel(acl)
			clave.resizable(0,0)
			clave.configure(bg='#b6bdff')
			clave.iconbitmap(logo)
			ancho_ventana = 400
			alto_ventana = 100
			x_ventana = clave.winfo_screenwidth() // 2 - ancho_ventana // 2
			y_ventana = clave.winfo_screenheight() // 2 - alto_ventana // 2
			posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
			clave.geometry(posicion)
			
			variable_clave.set('')
			clave.transient(master=raiz)

			acceso=Entry(clave,font='Helvetica 12',bd=9,relief='sunken',textvariable=clave_licencia1)
			acceso.place(x=140,y=20,width=180,height=35)
			acceso.configure(show='*');acceso.focus()


			accediendo=Label(clave,font='Helvetica 12',text='Clave de acceso',bg='#b6bdff')
			accediendo.place(x=10,y=20)

			




			def accediendo_a_licencia():
				
				if clave_licencia1.get()=='Leiserpro':
					nueva_licencia()
					return
				else:
					
					messagebox.showerror('BBDD','Clave Incorrecta',parent=clave)

			boton_acceso=Button(clave,cursor='hand2',text='O.K.',bg='silver',font='Helvetica 12',width=5,height=1,bd=4,relief='raised',command=accediendo_a_licencia)
			boton_acceso.place(x=330,y=20)
			clave.grab_set()	

		def nueva_licencia():
			if local.get()!='':
				pass
			else:
				messagebox.showerror('BBDD','Necesita agregar el Local donde esta el programa',parent=hija2)
				return
			try:
				if costo_licencia.get()!='':
					pass
				
					
			except TclError:
				messagebox.showerror('BBDD','Necesita agregar total de costo de la licencia',parent=hija2)
				return





			if mes_licen.get()=='Enero':
				me='01'
			elif mes_licen.get()=='Febrero':
				me='02'
			elif mes_licen.get()=='Marzo':
				me='03'
			elif mes_licen.get()=='Abril':
				me='04'
			elif mes_licen.get()=='Mayo':
				me='05'
			elif mes_licen.get()=='Junio':
				me='06'
			elif mes_licen.get()=='Julio':
				me='07'
			elif mes_licen.get()=='Agosto':
				me='08'
			elif mes_licen.get()=='Septiembre':
				me='09'								
			elif mes_licen.get()=='Octubre':				
				me='10'
			elif mes_licen.get()=='Noviembre':
				me='11'
			elif mes_licen.get()=='Diciembre':
				me='12'
			elif mes_licen.get()=='Todos':
				me='00'
			elif mes_licen.get()=='Prueba':
				mes_final2=int(time.strftime("%m"))
				me=str(mes_final2+1)
				
				if mes_final2<10:
					me='0'+me

				elif mes_final2==12:
					me='01'
				print(me)


			a=int(años_licen.get())
			año=a-2000

			fecha_licencia=str(dia_licen.get())+'/'+me+'/'+str(año)				
			print(fecha_licencia)
			try:
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				a10=getpass.getuser()
				datos=local.get(),fecha,fecha_licencia,1,costo_licencia.get(),a10

				micursor.execute("INSERT INTO LICENCIA VALUES(NULL,?,?,?,?,?,?)",(datos))

				miconexion.commit()
				local.set('')

				fecha1.set('')
				fecha2.set('')

				costo_licencia.set('')
				maldad_licencia()
				ver_licencias()
				acl.destroy()
			except:
				pass
				return


		Label(acl,font='Helvetica 12',text='Local',bg='#b6bdff').place(x=120,y=10)
		Label(acl,font='Helvetica 12',text='Fecha Inicial',bg='#b6bdff').place(x=100,y=100)
		Label(acl,font='Helvetica 12',text='Fecha Final',bg='#b6bdff').place(x=100,y=190)
		Label(acl,font='Helvetica 12',text='Costo',bg='#b6bdff').place(x=120,y=280)

		fecha1.set(fecha)
		fecha2.set(fecha_licencia)
		Entry(acl,font='Helvetica 12',bd=7,width=30,relief='sunken',textvariable=local).place(x=5,y=50,height=41)
		Entry(acl,font='Helvetica 12',bd=7,width=30,relief='sunken',state='readonly',textvariable=fecha1).place(x=5,y=140,height=41)
		Entry(acl,font='Helvetica 12',bd=7,width=30,relief='sunken',state='readonly',textvariable=fecha2).place(x=5,y=230,height=41)
		Entry(acl,font='Helvetica 12',bd=7,width=30,relief='sunken',textvariable=costo_licencia).place(x=5,y=320,height=41)

		Button(acl,font='Helvetica 12',bd=7,width=31,relief='raised',text='Aceptar',cursor='hand2',command=funcion_clave2).place(x=0,y=380)



		acl.grab_set()



	def borrar_licencia():


		try:
			fecha_ini=lista_licen.item(lista_licen.selection())['text']


		except IndexError:
			pass
			return

		Valor=messagebox.askquestion('BBDD','¿Desea borrar esta licencia?',parent=licen)
			
		if Valor=='yes':
			pass
				
		else:
			pass
			return


		fecha_ini=lista_licen.item(lista_licen.selection())['text']
		fecha_fini=lista_licen.item(lista_licen.selection())['values'][0]
		costo_li=lista_licen.item(lista_licen.selection())['values'][1]
		vigen_li=lista_licen.item(lista_licen.selection())['values'][2]
		if vigen_li=='Si':
			vigen_li=1
		else:
			vigen_li=0

		cone=sqlite3.connect('SISTEMA_LUMINA')
		cursor=cone.cursor()
		datos=fecha_ini,fecha_fini,vigen_li,costo_li
		print(datos,'datos')
		cursor.execute('DELETE FROM LICENCIA WHERE FECHA_INCIAL=? AND FECHA_FINAL=? AND BOOLEANO=? AND COSTO=?',(datos))


		cone.commit()
		messagebox.showinfo('BBDD','Licencia Borrarda con exito',parent=licen)
		ver_licencias()
	#---------------------------
	licen=Frame(hija2,bg='#b8d3ff',width=500,height=800)
	licen.place(x=400,y=0)
	
	Label(licen,text='Licencia',font='Helvetica 18',fg='black',bg='#b8d3ff').place(x=150,y=10)

	
	dia_final2=int(time.strftime("%d"))

	dia_licen=ttk.Combobox(licen,font='Helvetica 11', state="readonly", height=10,width=6)
	dia_licen['values']= ('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','Todos')
	dia_licen.current(dia_final2-1)
	dia_licen.pack(side=tk.RIGHT)
		
	dia_licen.place(x=50,y=100)




	mes_final2=int(time.strftime("%m"))

	mes_licen=ttk.Combobox(licen,font='Helvetica 11', state="readonly", height=10,width=10)
	mes_licen['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Prueba','Todos')
	mes_licen.current(mes_final2-1)
	mes_licen.pack(side=tk.RIGHT)
	
	mes_licen.place(x=145,y=100)

	

	año_final2=time.strftime("%y")
	d2=int(año_final2)
	fech2=d2+2051

	años = list(range(2021, fech2))
	a2=len(años)-1
	años_licen=ttk.Combobox(licen,font='Helvetica 11', state="readonly", height=10,width=10,values=años)
	años_licen.current(1)
	años_licen.pack(side=tk.RIGHT)

	años_licen.place(x=270,y=100)


	Button(licen,text='Restaurar',font='Helvetica 12',relief='raised',bd=7,cursor='hand2',command=aceptar_licencia).place(x=0,y=160)
	Button(licen,text='  Borrar ',font='Helvetica 12',relief='raised',bd=7,cursor='hand2',command=borrar_licencia).place(x=100,y=160)




	lista_licen=ttk.Treeview(licen,height=15,style="Treeview",columns=[f"#{n}" for n in range(1, 4)])
	
	lista_licen.place(x=0,y=205)


	barrita=Scrollbar(licen,command=lista_licen.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	barrita.place(x=382,y=228,height=305)
	lista_licen.config(yscrollcommand=barrita.set)
		
	lista_licen.heading('#0',text='Fecha Inicial',anchor=CENTER)
	lista_licen.heading('#1',text='Fecha Final',anchor=CENTER)
	lista_licen.heading('#2',text='Costo',anchor=CENTER)
	lista_licen.heading('#3',text='Vigente',anchor=CENTER)


	lista_licen.column("#0",minwidth=70, width = 100)
	lista_licen.column("#1",minwidth=70, width = 100)
	lista_licen.column("#2",minwidth=70, width = 160)
	lista_licen.column("#3",minwidth=70, width = 40)
	
	
	ver_licencias()
	hija2.grab_set()






def verificar_fecha_ofertas():
	try:
		cone=sqlite3.connect('SISTEMA_LUMINA')
		cursor=cone.cursor()

		fecha_actual=fecha.split('/');print(fecha_actual,'fecha_actual')
		
		dia_a=fecha_actual[0]
		mes_a=fecha_actual[1]
		año_a=fecha_actual[2]


		cursor.execute("SELECT * FROM OFERTAS WHERE BOOLEANO=1")
		A=cursor.fetchall()
		for i in A:
			fecha_tope=i[9].split('/')

			dia_t=fecha_tope[0]
			mes_t=fecha_tope[1]
			año_t=fecha_tope[2]


			if dia_t<=dia_a and mes_t<=mes_a and año_t<=año_a:
				cursor.execute("DELETE FROM OFERTAS WHERE BOOLEANO=1 AND id=?",(i[0], ))
		

		cursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=1")
		B=cursor.fetchall()
		for i in B:
			fecha_tope2=i[4].split('/')

			dia_t2=fecha_tope2[0]
			mes_t2=fecha_tope2[1]
			año_t2=fecha_tope2[2]


			if dia_t2<=dia_a and mes_t2<=mes_a and año_t2<=año_a:
				cursor.execute("DELETE FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=1 AND id=?",(i[0], ))
		

		cone.commit()

	except:
		pass
		return

def grouper2(iterable, n):
	args = [iter(iterable)] * n
	return itertools.zip_longest(*args)

def hacer_pdf(data,nombre):

	dsds=nombre
	fdfd=dsds+'.pdf'
	c = canvas.Canvas(fdfd, pagesize=A4)
	w, h = A4
	max_rows_per_page = 45
	# Margin.
	x_offset = 50
	y_offset = 50
	# Space between rows.
	padding = 15
		    
	xlist = [x + x_offset for x in [0, 250, 400 ,500]]
	ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
		    
	for rows in grouper2(data, max_rows_per_page):
		rows = tuple(filter(bool, rows))
		c.grid(xlist, ylist[:len(rows) + 1])
		for y, row in zip(ylist[:-1], rows):
			for x, cell in zip(xlist, row):
				c.drawString(x + 2, y - padding + 3, str(cell))
				

		c.showPage()

	c.save()


verificar_fecha_ofertas()
#--------------------------------------------------------------------------	

def INVENTARIOS(event):

	hijita=Toplevel(raiz)
	hijita.state('zoomed')
	hijita.geometry('1000x750')
	hijita.title('Inventarios')
	hijita.iconbitmap(logo)

	tab_control=ttk.Notebook(hijita)
	hija=Frame(tab_control)
	pro=Frame(tab_control)
	gana=Frame(tab_control)
	root=Frame(tab_control)
	ventana=Frame(tab_control)
	CTN=Frame(tab_control)
	ven=Frame(tab_control)
	com=Frame(tab_control)
	deu=Frame(tab_control)

	hija.config(bg='#b6bdff')
	gana.config(bg='#b6bdff')

	tab_control.add(hija, text='Productos')
	#tab_control.add(root, text='Ofertas')
	#tab_control.add(ventana, text='Combos')
	tab_control.add(ven, text='Ventas')
	tab_control.add(com, text='Compras')
	
	tab_control.add(deu, text='Deudores')
	tab_control.add(pro, text='Proveedores')
	tab_control.add(CTN, text='Clientes')
	

	
	tab_control.pack(expand=1, fill='both')

#-----------------------
	producto1=StringVar()
	cantidad1=DoubleVar()
	precio1=DoubleVar()
	identificador1=StringVar()
#-----------------------------
	def productos():
		pass
	def Resultado(event):


		try:

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?',(departamento_v.get(), ))			
			A=micursor.fetchall()
			for i in A:
				tasa_v=i[0]

			miconexion.commit()
			print(tasa_v)

			try:
				if precio_inicial_bolivares_P.get()=='':
					precio_inicial_bolivares_P.set(precio_inicial_dolares_P.get()*tasa_v)


			except TclError:
				precio_inicial_bolivares_P.set(precio_inicial_dolares_P.get()*tasa_v)


			try:
				if precio_inicial_dolares_P.get()==0:
					precio_inicial_dolares_P.set(precio_inicial_bolivares_P.get()/tasa_v)

			except TclError:
				precio_inicial_dolares_P.set(precio_inicial_bolivares_P.get()/tasa_v)


			try:
				if porcentaje_P.get()==0:
					porcentaje_P.set(0)

			except TclError:
				porcentaje_P.set(0)


			try:


				if exento_P.get()==0:
					iva=IVA.get()/100+1
					w=porcentaje_P.get()
					totalizando=precio_inicial_bolivares_P.get()*porcentaje_P.get()/100+precio_inicial_bolivares_P.get()
					
					a=format(totalizando).replace(",", "@").replace(".", ",").replace("@", ".")

					d1=totalizando*IVA.get()/100
					
					d=d1+totalizando
					precio_final_B_P.set(d)

					re=precio_final_B_P.get()/iva
					precio_final_B_P_iva.set(re)


					totalizando2=precio_inicial_dolares_P.get()*porcentaje_P.get()/100+precio_inicial_dolares_P.get()
					ba=format(totalizando2).replace(",", "@").replace(".", ",").replace("@", ".")
					s=totalizando2*IVA.get()/100+totalizando2


					precio_final_D_P.set(s)
					
					num=precio_inicial_dolares_P.get()*w/100

					c=precio_final_D_P.get()/iva

					precio_final_D_P_iva.set(c)
					
				else:
					
					totalizando=precio_inicial_bolivares_P.get()*porcentaje_P.get()/100+precio_inicial_bolivares_P.get()
					a=format(totalizando).replace(",", "@").replace(".", ",").replace("@", ".")

					precio_final_B_P.set(totalizando)
					try:
						
						rg=precio_final_B_P.get()/porcentaje_P.get()

						precio_final_B_P_iva.set(rg)
					except:
						rg=precio_final_B_P.get()/1

						precio_final_B_P_iva.set(rg)



					totalizando2=precio_inicial_dolares_P.get()*porcentaje_P.get()/100+precio_inicial_dolares_P.get()
					ba=format(totalizando2).replace(",", "@").replace(".", ",").replace("@", ".")
					
					
					precio_final_D_P.set(totalizando2)
					try:

						a=precio_final_D_P.get()/porcentaje_P.get()

						precio_final_D_P_iva.set(a)
					except:
						a=precio_final_D_P.get()/1

						precio_final_D_P_iva.set(a)

			finally:
				pass
				
		finally:
			pass
			


	def agrega():
		lista1p.insert('',0,text=identificador_P,values=(producto_P.get(),cantidad_P.get(),precio_inicial_dolares_P.get(),precio_inicial_bolivares_P.get(), porcentaje_P.get(),precio_final_D_P.get(),precio_final_B_P.get()))
		
		
	def borrar_campos_P():
		identificador_P.set('')
		producto_P.set('')
		cantidad_P.set('')
		precio_inicial_dolares_P.set('')
		precio_inicial_bolivares_P.set('')
		porcentaje_P.set('')
		precio_final_D_P.set('')
		precio_final_B_P.set('')
		exento_P.set(0)
	def crear_Productos():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		try:
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(departamento_v.get(), ))
			A=micursor.fetchall()
			for i in A:
				TASA_=i[0]

			precio_final_D_P.set(precio_final_B_P.get()/TASA_)
			B=''
			if exento_P.get()==0:
				w=porcentaje_P.get()
				totalizando=precio_inicial_bolivares_P.get()*porcentaje_P.get()/100+precio_inicial_bolivares_P.get()
					
				a=format(totalizando).replace(",", "@").replace(".", ",").replace("@", ".")
				print(a,'totalizando')
				d=totalizando*IVA.get()/100+totalizando
					


				totalizando2=precio_inicial_dolares_P.get()*porcentaje_P.get()/100+precio_inicial_dolares_P.get()
				ba=format(totalizando2).replace(",", "@").replace(".", ",").replace("@", ".")
				s=totalizando2*IVA.get()/100+totalizando2


				if precio_final_B_P.get()!=d:
					iva=IVA.get()/100+1

					B=precio_final_D_P.get()/iva

					
					
					precio_final_D_P_iva.set(B)

					E=B-precio_inicial_dolares_P.get()

					F=E*100/precio_inicial_dolares_P.get()
					
					A=precio_inicial_dolares_P.get()*iva
					
					C=F
					porcentaje_P.set(C)


					D=precio_final_B_P.get()/iva

					
					precio_final_B_P_iva.set(D)
					

					G=D-precio_inicial_bolivares_P.get()

					H=G*100/precio_inicial_bolivares_P.get()
					
					A=precio_inicial_bolivares_P.get()*iva
					
					J=H
					

	
				
			elif exento_P.get()==1:
				
				
				totalizando=precio_inicial_bolivares_P.get()*porcentaje_P.get()/100+precio_inicial_bolivares_P.get()
					
				a=format(totalizando).replace(",", "@").replace(".", ",").replace("@", ".")

				d=totalizando
				#"precio_final_B_P_iva.set(d)
					


				totalizando2=precio_inicial_dolares_P.get()*porcentaje_P.get()/100+precio_inicial_dolares_P.get()
				ba=format(totalizando2).replace(",", "@").replace(".", ",").replace("@", ".")
				s=totalizando2

				#precio_final_D_P_iva.set(s)

				print(totalizando,precio_final_B_P.get(),'precio')
				if precio_final_B_P.get()!=totalizando:
					#iva=IVA.get()/100+1

					B=precio_final_D_P.get()

					
					
					precio_final_D_P_iva.set(B)

					E=B-precio_inicial_dolares_P.get()

					F=E*100/precio_inicial_dolares_P.get()
					#print(B)
					A=precio_inicial_dolares_P.get()
					
					C=F
					porcentaje_P.set(C)




					D=precio_final_B_P.get()

					
					precio_final_B_P_iva.set(D)
					

					G=D-precio_inicial_bolivares_P.get()

					H=G*100/precio_inicial_bolivares_P.get()
					
					A=precio_inicial_bolivares_P.get()
					
					J=H
					




		except TclError:
			messagebox.showerror('BBDD','Faltan campos por escribir',parent=hija)
			return
		try:
			if precio_final_D_P.get()!='' and precio_final_B_P.get()!='':
				pass
			else:
				#Resultado('1')
				pass
		except TclError:
			#Resultado('1')
			pass
		try:

			if combo.get()=='Unidad':
				unidad_p.set('UND')
		

			elif combo.get()=='Kilogramos':
				unidad_p.set('Kg ')

			elif combo.get()=='Litros':
				unidad_p.set('Lts')

			elif combo.get()=='Metros':
				unidad_p.set('Mts')

			elif combo.get()=='Detallados':
				unidad_p.set('DTL')


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()


			if exento_P.get()==1:

				precio_final_B_P_iva.set(precio_final_B_P.get())


				precio_final_D_P_iva.set(precio_final_D_P.get())
				

			datos=identificador_P.get(),producto_P.get().capitalize(),cantidad_P.get(),unidad_p.get(),exento_P.get(),precio_inicial_dolares_P.get(),precio_inicial_bolivares_P.get(), porcentaje_P.get(),precio_final_D_P.get(),precio_final_B_P.get(),precio_final_D_P_iva.get(),precio_final_B_P_iva.get(),departamento_v.get()
			print(datos)
			micursor.execute("INSERT INTO PRODUCTOS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,NULL,?)",(datos))
			miconexion.commit()
			
		
			buscar_producto_P('1')
			limpiar_campos_P()
			
			borrar_campos_P()
		

		except sqlite3.IntegrityError:
			messagebox.showwarning('Lumina','El identificador ya existe',parent=hija)
			identificador_P.set('')
		

		except sqlite3.OperationalError:
			messagebox.showwarning('Lumina','Base de datos no creada',parent=hija)
		

		except TclError:
			messagebox.showerror('BBDD','Faltan campos por escribir',parent=hija)	
			return
	def leer_todo_P():
		redon1=StringVar()
		redon2=StringVar()
		redon3=StringVar()

		record=lista1p.get_children()
		for element in record:
			lista1p.delete(element)
		
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM PRODUCTOS ORDER BY (NOMBRE_PRODUCTO)DESC")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			x=float(usuarios[8])
			f=float(usuarios[8])
			c=float(usuarios[2])
			a=round(x,2)
			b=round(f,2)
			g=round(c,2)
			
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[13], ))
		
			A=micursor.fetchall()
					
			for i in A:
				eee1=usuarios[8]*i[2]

				
				eee = round(eee1,2)
				
				redon3.set(str(eee))
						
			x1=float(usuarios[8])
			#f=float(usuarios[8]*tasa_del_dolar.get())
			c=float(usuarios[2])
			x = '{:,}'.format(round(x1,2))
			redon1.set(str(x))
			#redon2.set(round(f,2))
			necesario_depar.set(round(c,2))
					
			lista1p.insert('',0,text=usuarios[0],values=(usuarios[1],necesario_depar.get(),usuarios[3],usuarios[13],redon1.get(),redon3.get()))
					
	def leer_todo_con_oferta(event):
		record=lista1p.get_children()
		for element in record:
			lista1p.delete(element)
		hola=StringVar()
		print(ver_producto_con_oferta_P.get())
		if ver_producto_con_oferta_P.get()==0:
			redon1=DoubleVar()
			redon2=DoubleVar()
			redon3=DoubleVar()

			
			
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS  WHERE DEPARTAMENTO NOT IN (SELECT DEPARTAMENTO FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=1)")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				x=float(usuarios[8])
				f=float(usuarios[8])
				c=float(usuarios[2])
				a=round(x,2)
				b=round(f,2)
				g=round(c,2)
				
				
				micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[13], ))
		
				A=micursor.fetchall()
						
				for i in A:
					eee=usuarios[8]*i[2]
					redon3.set(round(eee,2))
							
				x=float(usuarios[8])
				#f=float(usuarios[8]*tasa_del_dolar.get())
				c=float(usuarios[2])
				redon1.set(round(x,2))
				#redon2.set(round(f,2))
				necesario_depar.set(round(c,2))
						
				lista1p.insert('',0,text=usuarios[0],values=(usuarios[1],necesario_depar.get(),usuarios[3],usuarios[13],redon1.get(),redon3.get()))
						

			micursor.execute("SELECT * FROM PRODUCTOS WHERE DEPARTAMENTO IN (SELECT DEPARTAMENTO FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=1)")
			V=micursor.fetchall()
			for M in V:

				micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=?",(M[13], ))
				F=micursor.fetchall()
				for i in F:
					por=i[2]
					r=round(M[2],2)

					micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(M[13], ))
					D=micursor.fetchall()
					for a1 in D:

						t=M[8]*a1[0]
						y=t*i[2]
						u=y/100
						o=t-u
						p=round(o,2)

						o1=o/a1[0]
						p1=round(o1,2)
						j=M[1]+'    (Oferta)'


						lista1p.insert('',0,text=M[0],values=(j, r ,M[3],M[13],p1,p))
			


		else:
			leer_todo_P()
			return


	def comprobacion_de_borrar():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		try:
			lista1p.item(lista1p.selection())['text'][0]


		except IndexError:
			pass
			return

		valor=messagebox.askquestion('Salir', '¿Desea Borrar este producto?',parent=hija)
		if valor=='yes':
			borrar_producto_P()

	def borrar_producto_P():
		name=lista1p.item(lista1p.selection())['text']

		query="DELETE FROM PRODUCTOS WHERE ID=?"
		run_query(query,(name, ))

		buscar_producto_P('1')
		
		

	editar_nombre_a=StringVar()
	editar_cantidad_a=DoubleVar()
	editar_precio_D_a=DoubleVar()
	editar_precio_B_a=DoubleVar()

	def editar_producto_P():

		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return


		tasa_editar=DoubleVar()
		try:
			lista1p.item(lista1p.selection())['text'][0]


		except IndexError:
			pass
			return
		
		ide=lista1p.item(lista1p.selection())['text']
		nombre_a=lista1p.item(lista1p.selection())['values'][0]
		cantidad_a=lista1p.item(lista1p.selection())['values'][1]
		unidad_a=lista1p.item(lista1p.selection())['values'][2]
		departamento_a=lista1p.item(lista1p.selection())['values'][3]
		precio_ini_D_a=lista1p.item(lista1p.selection())['values'][4]
		precio_ini_B_a=lista1p.item(lista1p.selection())['values'][5]


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(departamento_a, ))
		
		A=micursor.fetchall()
					
		for i in A:
			tasa_editar.set(i[2])



		editar_nombre_a.set(nombre_a)
		editar_cantidad_a.set(cantidad_a)
		editar_precio_D_a.set(precio_ini_D_a)
		editar_precio_B_a.set(precio_ini_B_a)



		exento_E=BooleanVar()
		editar=Toplevel(hija)
		editar.config(bg='#b6bdff')
		editar.title('Editar Producto')
		ancho_ventana = 400
		alto_ventana = 550
		x_ventana = editar.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = editar.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		editar.geometry(posicion)
		
		editar.resizable(0,0)
		editar.iconbitmap(logo)

		if unidad_a=='UND':
			num=0

		elif unidad_a=='Kg ':
			num=1
		elif unidad_a=='Lts':
			num=2
		elif unidad_a=='Mts':
			num=3

		def ver_departamentos_e():

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			

			micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
			A=micursor.fetchall()

			departamento_e['values']= (list(f"{str(n[0])}" for n in A))
			contador=0
			for i in A:
				if i[0]==departamento_a:

					departamento_e.current(contador)
				else:
					contador+=1
		
			micursor.execute('SELECT EXENTO FROM PRODUCTOS WHERE ID=?',(ide, ))
			d=micursor.fetchall()
			for i in d:
				if i[0]==1:
					exento_E.set(1)
				else:
					exento_E.set(0)

		Label(editar,text='Nombre ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=10)
		nombre=Entry(editar,textvariable=editar_nombre_a,relief='sunken',font='Helvetica 12',fg='black',bd=10,state='readonly')
		nombre.place(x=140,y=10)
		nombre.focus()


		Label(editar,text='Cantidad ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=80)
		cantidad=Entry(editar,textvariable=editar_cantidad_a,relief='sunken',font='Helvetica 12',fg='black',bd=10)
		cantidad.place(x=140,y=80)

		Label(editar,text='Unidad ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=150)
		

		unidad=ttk.Combobox(editar)
		unidad.config(font='Helvetica 15',state='readonly',width=16,height=100)
		unidad['values']=('Unidad','Kilogramos','Litros','Metros')
		unidad.place(x=140,y=150)
		unidad.current(num)

		departamento_e=ttk.Combobox(editar)
		departamento_e.config(font='Helvetica 15',state='readonly',width=16,height=100)
		departamento_e.place(x=140,y=220)
		ver_departamentos_e()
		



		ttk.Style().configure('black.TCheckbutton', foreground='black', background='#b6bdff',font='Helvetica 15')
		ttk.Checkbutton(editar, text="Exento",style='black.TCheckbutton',variable=exento_E, onvalue=1).place(x=140,y=290)


		Label(editar,text='Precio $ ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=360)
		precio_D=Entry(editar,state='readonly',textvariable=editar_precio_D_a,relief='sunken',font='Helvetica 12',fg='black',bd=10)
		precio_D.place(x=140,y=360)

		Label(editar,text='Precio Bs.S',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=430)
		precio_B=Entry(editar,textvariable=editar_precio_B_a,relief='sunken',font='Helvetica 12',fg='black',bd=10)
		precio_B.place(x=140,y=430)


		
		Button(editar,text='Guardar',cursor='hand2',font='Helvetica 12',fg='black',bd=10,relief='raised',width=42,command=lambda:listo(unidad.get(),ide,'1')).place(x=0,y=500)


		def listo(unidad_new,identificador,event):
			if unidad_new=='Unidad':
				unidad_new='UND'
		

			elif unidad_new=='Kilogramos':
				unidad_new='Kg '

			elif unidad_new=='Litros':
				unidad_new='Lts'

			elif unidad_new=='Metros':
				unidad_new='Mts'

			




			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(departamento_e.get(), ))
			C=micursor.fetchall()
			for i in C:
				tasita=i[0]

			try:
			
				a=float(editar_precio_B_a.get())
				precio_f_D=a/tasita
			except ZeroDivisionError:
				messagebox.showerror('BBDD','Tiene que ingresar un precio mayor que 0',parent=editar)
				return


			micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(identificador, ))		
			A=micursor.fetchall()
			for i in A:
				if exento_E.get()==1:
					sub_total_B2222=precio_f_D*tasita
					sub_total_D2222=precio_f_D
					epic=precio_f_D
					fail=precio_f_D*tasita
					
					x=precio_f_D-i[5]
					print(round(precio_f_D,2),i[5],'x',x,'e1')

					

					r=x*100
					total_D2222=epic
					total_B2222=fail
					porcentaje_nuevo=r/i[5]
					#print(r,precio_f_D,'ooooooooooooooooo')

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					parametro=(sub_total_D2222,sub_total_B2222,porcentaje_nuevo,departamento_e.get(),total_D2222,total_B2222,exento_E.get(),editar_cantidad_a.get(),unidad_new,identificador);print(parametro,'HOLLLLALLALALLA')
					print(parametro),print(porcentaje_nuevo,'pro')
					if porcentaje_nuevo<0:
						Valor=messagebox.askquestion('BBDD','El porcentaje de ganancia en $ queda por debajo de 0\n ¿Desea continuar?',parent=editar)
						if Valor=='no':
							editar.destroy()
							return

					
					micursor.execute("UPDATE PRODUCTOS SET SUB_TOTAL_D=?, SUB_TOTAL_B=?, PORCENTAJE_GANANCIA=?,DEPARTAMENTO=?,PRECIO_FINAL_D_P=?,PRECIO_FINAL_B_P=?,EXENTO=?,CANTIDAD_PRODUCTO=?,UNIDAD=? WHERE ID=?",(parametro))
					miconexion.commit()

				elif exento_E.get()==0:



					iva=IVA.get()/100+1
					a=precio_f_D*iva

					a0=a-precio_f_D
					sub_total_D2222=precio_f_D-a0


					sub_total_B2222=sub_total_D2222*tasita
					

					epic=precio_f_D
					fail=precio_f_D*tasita
					x=precio_f_D-i[5]
					
					
					total_D2222=epic
					total_B2222=fail


					
					b=precio_f_D/iva
					e=b-i[5]
					print(e,'e')
					f=e*100/i[5]
					print(f,'f')
					c=round(f,1)
					porcentaje_nuevo=c


					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					parametro=(sub_total_D2222,sub_total_B2222,porcentaje_nuevo,departamento_e.get(),total_D2222,total_B2222,exento_E.get(),editar_cantidad_a.get(),unidad_new,identificador);print(parametro,'HOLLLLALLALALLA')
				

					if porcentaje_nuevo<0:
						Valor=messagebox.askquestion('BBDD','El porcentaje de ganancia en $ queda por debajo de 0\n ¿Desea continuar?',parent=editar)
						if Valor=='no':
							editar.destroy()
							return

					micursor.execute("UPDATE PRODUCTOS SET SUB_TOTAL_D=?, SUB_TOTAL_B=?, PORCENTAJE_GANANCIA=?,DEPARTAMENTO=?,PRECIO_FINAL_D_P=?,PRECIO_FINAL_B_P=?,EXENTO=?,CANTIDAD_PRODUCTO=?,UNIDAD=? WHERE ID=?",(parametro))
					miconexion.commit()


			
			buscar_producto_P('1')
		
			editar.destroy()

		#editar.bind_all("<Control-s>", listo(unidad.get(),ide,'1'))


	def agregar_departamento():
		depar=Toplevel(hija)
		depar.config(bg='#b6bdff')
		depar.title('Departamentos')
		ancho_ventana = 300
		alto_ventana = 200
		x_ventana = depar.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = depar.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		depar.geometry(posicion)
		
		depar.resizable(0,0)
		depar.iconbitmap(logo)

		def agregar_departamento_nuevo():
			
			if len(agregar_departamento_depar.get())!=0:
				VALOR=messagebox.askquestion('BBDD','Desea ingresar este Departamento?',parent=depar)
				if VALOR=='yes':
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()

					if tasa_del_dolar.get()==0:
						micursor.execute("SELECT TASA FROM TASA_MONEDA WHERE BOOLEANO=1")
						A=micursor.fetchall()
						for i in A:
							tasa_depa=i[0]

					else:
						tasa_depa=tasa_del_dolar.get()


					datos3=agregar_departamento_depar.get().capitalize(),tasa_depa

					micursor.execute("INSERT INTO DEPARTAMENTOS VALUES(?,NULL,?)",(datos3))
					miconexion.commit()
					ver_departamentos()
					agregar_departamento_depar.set('')
			else:
				pass
				return

		def borrar_departamentos():
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			

			micursor.execute("SELECT DEPARTAMENTO FROM PRODUCTOS WHERE DEPARTAMENTO=?",(depart.get(), ))
			F=micursor.fetchall()
			for i in F:
				if i!='':
					messagebox.showwarning('BBDD','No puede borrar un departamento que tenga productos',parent=depar)
					return
			miconexion.commit()



			Valor=messagebox.askquestion('BBDD','¿Seguro que desea borrar el departamento {}?'.format(depart.get()),parent=depar)
			if Valor=='yes':

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("DELETE FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart.get(), ))
				
				miconexion.commit()
				ver_departamentos()
				depart.current(0)
	
		def ver_departamentos():
	

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			

			micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
			A=micursor.fetchall()

			depart['values']= (list(f"{str(n[0])}" for n in A))
			necesario_depar.set('')
			miconexion.commit()



		combo_day=Frame(depar,bg='silver')
		combo_day.place(x=20,y=100)
		

		depart=ttk.Combobox(combo_day,font='Helvetica 11', state="readonly", height=12,width=20)
		
		
		ver_departamentos()

		
		depart.current(0)
		depart.pack(side=tk.RIGHT)


		Label(depar,bg='#b6bdff',text='Departamento',font='Helvetica 12').place(x=55,y=20)
		Entry(depar,fg='black',bd=7,relief='sunken',font='Helvetica 12',textvariable=agregar_departamento_depar).place(x=10,y=50)
		Button(depar,text='Agregar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=agregar_departamento_nuevo).place(x=210,y=48)

		Button(depar,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=borrar_departamentos).place(x=10,y=150)



	def sub_menu(event):
		try:
			menu.post(event.x_root, event.y_root)
		finally:
			menu.grab_release()
	def limpiar_campos_P():
		identificador_P.set('')
		producto_P.set('')
		cantidad_P.set('')
		combo.current(0)
		precio_inicial_dolares_P.set('')
		precio_inicial_bolivares_P.set('')
		porcentaje_P.set('')
		precio_final_D_P.set('')
		precio_final_B_P.set('')
		exento_P.set(0)


	def buscar_producto_P(event):
		redon1=DoubleVar()
		redon2=DoubleVar()
		redon3=DoubleVar()
		print(event)
		ver_producto_con_oferta=ver_producto_con_oferta_P.get()
		if event!='1':
			if ver_producto_con_oferta_P.get()==1:
				
				ver_producto_con_oferta=0
			else:
				ver_producto_con_oferta=1
		

		print(ver_producto_con_oferta_P.get(),'ver_producto_con_oferta_P.get()')
		if len(Buscar_producto_P.get())==0 and ver_producto_con_oferta==1:
			redon1=DoubleVar()
			redon2=DoubleVar()
			redon3=DoubleVar()

			
			record=lista1p.get_children()
		
			for element in record:
				lista1p.delete(element)
			
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			
			micursor.execute("SELECT * FROM PRODUCTOS WHERE DEPARTAMENTO IN (SELECT DEPARTAMENTO FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=1)  ORDER BY DEPARTAMENTO,NOMBRE_PRODUCTO DESC")
			V=micursor.fetchall()
			for M in V:

				micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=?",(M[13], ))
				F=micursor.fetchall()
				for i in F:
					por=i[2]
					r=round(M[2],2)

					micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(M[13], ))
					D=micursor.fetchall()
					for a1 in D:

						t=M[8]*a1[0]
						y=t*i[2]
						u=y/100
						o=t-u
						p=round(o,2)

						o1=o/a1[0]
						p1=round(o1,2)
						j=M[1]+'    (Oferta)'


						lista1p.insert('',0,text=M[0],values=(j, r ,M[3],M[13],p1,p))
			

			return
		if len(Buscar_producto_P.get())==0:
			record=lista1p.get_children()
		
			for element in record:
				lista1p.delete(element)
			
			
			
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				x=float(usuarios[8])
				f=float(usuarios[8]*tasa_del_dolar.get())
				c=float(usuarios[2])
				a=round(x,2)
				b=round(f,2)
				g=round(c,2)
				
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[13], ))
		
				A=micursor.fetchall()
					
				for i in A:
					eee=usuarios[8]*i[2]
					redon3.set(round(eee,2))
						
				x=float(usuarios[8])
				f=float(usuarios[8]*tasa_del_dolar.get())
				c=float(usuarios[2])
				redon1.set(round(x,2))
				redon2.set(round(f,2))
				necesario_depar.set(round(c,2))
					
				lista1p.insert('',0,text=usuarios[0],values=(usuarios[1],necesario_depar.get(),usuarios[3],usuarios[13],redon1.get(),redon3.get()))
				

		else:
			record=lista1p.get_children()
		
			for element in record:
				lista1p.delete(element)
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:

				r=usuarios[0].startswith(Buscar_producto_P.get())
				k=usuarios[1].startswith(Buscar_producto_P.get().capitalize())
				de=usuarios[13].startswith(Buscar_producto_P.get().capitalize())
				if r==1 or k==1 or de==1:
					
					print(usuarios[13])
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[13], ))
		
					A=micursor.fetchall()
					
					for i in A:
						eee=usuarios[8]*i[2]
						redon3.set(round(eee,2))
						
					x=float(usuarios[8])
					
					c=float(usuarios[2])
					redon1.set(round(x,2))
					
					necesario_depar.set(round(c,2))
					xxxxx=usuarios[0]
					
					if ver_producto_con_oferta==0:
					
						lista1p.insert('',0,text=usuarios[0],values=(usuarios[1],necesario_depar.get(),usuarios[3],usuarios[13],redon1.get(),redon3.get()))
					
					elif ver_producto_con_oferta==1:



						micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=? AND DEPARTAMENTO  IN (SELECT DEPARTAMENTO FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=1)",(xxxxx, ))
						V=micursor.fetchall()
						for M in V:

							micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=?",(M[13], ))
							F=micursor.fetchall()
							for i in F:
								por=i[2]
								r=round(M[2],2)

								micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(M[13], ))
								D=micursor.fetchall()
								for a1 in D:

									t=M[8]*a1[0]
									y=t*i[2]
									u=y/100
									o=t-u
									p=round(o,2)

									o1=o/a1[0]
									p1=round(o1,2)
									j=M[1]+'    (Oferta)'


									lista1p.insert('',0,text=M[0],values=(j, r ,M[3],M[13],p1,p))
						
									
									if j=='':
										
										
										micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
										elusuario=micursor.fetchall()
										for usuarios in elusuario:

											r=usuarios[0].startswith(Buscar_producto_P.get())
											k=usuarios[1].startswith(Buscar_producto_P.get().capitalize())
											de=usuarios[13].startswith(Buscar_producto_P.get().capitalize())
											if r==1 or k==1 or de==1:
												
												print(usuarios[13])
												miconexion=sqlite3.connect('SISTEMA_LUMINA')
												micursor=miconexion.cursor()
												micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[13], ))
									
												A=micursor.fetchall()
												
												for i in A:
													eee=usuarios[8]*i[2]
													redon3.set(round(eee,2))
													
												x=float(usuarios[8])
												
												c=float(usuarios[2])
												redon1.set(round(x,2))
												
												necesario_depar.set(round(c,2))
												xxxxx=usuarios[0]
												print(ver_producto_con_oferta,'qlq')
												if ver_producto_con_oferta==0:
												
													lista1p.insert('',0,text=usuarios[0],values=(usuarios[1],necesario_depar.get(),usuarios[3],usuarios[13],redon1.get(),redon3.get()))
												






			miconexion.commit()

	def ver_departamentos_p():

		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
			

		micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
		A=micursor.fetchall()

		departamento_v['values']= (list(f"{str(n[0])}" for n in A))
		
		miconexion.commit()

	def crear_oferta():

		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		def agregar_oferta_d():

			if licencia_programa.get()=='no':
				Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
				if Valor=='yes':
					informacion_sobre_licencia()

				return

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			if mes_o.get()=='Enero':
				me='01'
			elif mes_o.get()=='Febrero':
				me='02'
			elif mes_o.get()=='Marzo':
				me='03'
			elif mes_o.get()=='Abril':
				me='04'
			elif mes_o.get()=='Mayo':
				me='05'
			elif mes_o.get()=='Junio':
				me='06'
			elif mes_o.get()=='Julio':
				me='07'
			elif mes_o.get()=='Agosto':
				me='08'
			elif mes_o.get()=='Septiembre':
				me='09'
			elif mes_o.get()=='Octubre':
				me='10'
			elif mes_o.get()=='Noviembre':
				me='11'
			elif mes_o.get()=='Diciembre':
				me='12'



			

			a=str(dias_o.get())

			if int(dias_o.get())<10:
				a='0'+a
			b=int(años_o.get())
			c=b-2000
			d=str(c)
			fecha2=a+'/'+me+'/'+d
			print(fecha2)



			datos=departamento_of.get(),descuento_d.get(),fecha,fecha2,1

			micursor.execute("INSERT INTO OFERTAS_DEPARTAMENTOS VALUES(NULL,?,?,?,?,?)",(datos))
			miconexion.commit()

			descuento_d.set('')
			des2.focus()
			departamento_of.current(0)
			ver_ofertas_departamento()

		def ver_ofertas_departamento():
			record=lista_o_d.get_children()
			for element in record:
				lista_o_d.delete(element)
			activar_nombre_departamento()


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE BOOLEANO=?",(1, ))
			A=micursor.fetchall()
			for i in A:

				lista_o_d.insert('',0,text=i[1],values=(i[2],i[3],i[4]))








		def ver_prodcutos_ofertas_TR(event):
			try:
				if descuento_d.get()=='':
					ver_ofertas_departamento()

			except TclError:
				ver_ofertas_departamento()
				return


			record=lista_o_d.get_children()
			if descuento_d.get()==0:
				ver_ofertas_departamento()
				return


			for element in record:
				lista_o_d.delete(element)

			activar_nombre_producto()

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS WHERE DEPARTAMENTO=? ORDER BY (NOMBRE_PRODUCTO)DESC",(departamento_of.get(), ))
			A=micursor.fetchall()
			for i in A:
				DEPAR=i[13]
				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(DEPAR, ))
				B=micursor.fetchall()
				for n in B:
					tasita=n[0]
					a=i[8]*tasita
					#print(a,'a')
					b=a*descuento_d.get()
					#print(b,'b')
					c=b/100
					#print(c,'c')
					d=a-c
					#print(d,'d')
					e=d/tasita
					#print(e,'e')
					f=round(e,3)
					g=round(d,3)

					lista_o_d.insert('',0,text=i[1],values=(i[3],f,g))


		def borrar_oferta_por_departamento():
			try:
				depir=lista_o_d.item(lista_o_d.selection())['text']
				FG=lista_o_d.item(lista_o_d.selection())['values'][0]
			except IndexError:
				pass
				return
			Valor=messagebox.askquestion('BBDD','¿Desea Borrar esta oferta de departamento?',parent=ofer_d)

			if Valor=='yes':
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("DELETE FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=? AND DESCUENTO=? ",(depir,FG))
				miconexion.commit()			
				ver_ofertas_departamento()
				des2.focus()




		def detalles_ofertas_d():

			try:
				lista_o_d.item(lista_o_d.selection())['text'][0]

			except IndexError:
				pass
				return
			
			
			nombre_a=lista_o_d.item(lista_o_d.selection())['values'][0]
			ide=lista_o_d.item(lista_o_d.selection())['text']
			print(nombre_a,'nombre a')

			do=Toplevel(ofer_d)
			do.configure(bg='#b6bdff')
			do.resizable(0,0)
			do.iconbitmap(logo)
			ancho_ventana = 852
			alto_ventana = 373
			x_ventana = do.winfo_screenwidth() // 2 - ancho_ventana // 2
			y_ventana = do.winfo_screenheight() // 2 - alto_ventana // 2
			posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
			do.geometry(posicion)
			
			buscar_producto_o=StringVar()

			
			def leer_todo_ofertas():
				
				record=lista_oferta_d.get_children()
				for element in record:
					lista_oferta_d.delete(element)
					
						
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(ide, ))
				B=micursor.fetchall()
				for n in B:
					tasita=n[0]


				micursor.execute("SELECT * FROM PRODUCTOS WHERE DEPARTAMENTO=? ORDER BY (NOMBRE_PRODUCTO) DESC",(ide, ))
				A=micursor.fetchall()
				for i in A:
					a0=i[8]*tasita
					a1=a0*nombre_a
					a2=a1/100

					a3=a0-a2
					a4=round(a3,2)
					a5=round(a3/tasita,2)

					lista_oferta_d.insert('',0,text=i[0],values=(i[1],i[2],i[3],a5,a4))
					

				



			def buscar_producto_oferta(event):

				if len(buscar_producto_o.get())==0:
					leer_todo_ofertas()
				else:
					record=lista_oferta_d.get_children()
				
					for element in record:
						lista_oferta_d.delete(element)


					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
					elusuario=micursor.fetchall()
					for i in elusuario:

						r=i[0].startswith(buscar_producto_o.get())
						k=i[1].startswith(buscar_producto_o.get().capitalize())
						
						if k==1 or r==1:
							DEPAR=i[13]
							micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(DEPAR, ))
							B=micursor.fetchall()
							for n in B:
	
								tasita=n[0]
								a=i[8]*tasita
								
								b=a*nombre_a
								
								c=b/100
								
								d=a-c
								
								e=d/tasita
								
								f=round(e,3)
								g=round(d,3)
								lista_oferta_d.insert('',0,text=i[0],values=(i[1],i[2],i[4],f,g))
								
					miconexion.commit()
			


			ql=Entry(do,font='Helvetica 12',bd=7,relief='sunken',textvariable=buscar_producto_o)
			ql.place(x=0,y=10)
			Button(do,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_producto_oferta('1')).place(x=205,y=5)
			ql.bind('<KeyRelease>',buscar_producto_oferta)


			style = ttk.Style()
			style.configure("mystyle.Treeview", highlightthickness=0, bd=10,relief='raised', font=('Helvetica', 12))

			lista_oferta_d=ttk.Treeview(do,style="Treeview",height=14,columns=[f"#{n}" for n in range(1, 6)])
			lista_oferta_d.place(x=0,y=70)

			scoll=Scrollbar(do,command=lista_oferta_d.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll.place(x=834,y=93,height=282)

			lista_oferta_d.config(yscrollcommand=scoll.set)

			lista_oferta_d.heading('#0',text='Identificador',anchor=CENTER)
			lista_oferta_d.heading('#1',text='Productos',anchor=CENTER)
			lista_oferta_d.heading('#2',text='Cantidad',anchor=CENTER)
			lista_oferta_d.heading('#3',text='Unidad',anchor=CENTER)
			lista_oferta_d.heading('#4',text='Precio $',anchor=CENTER)
			lista_oferta_d.heading('#5',text='Precio Bs.S',anchor=CENTER)
			

			lista_oferta_d.column("#0",minwidth=70, width = 158)
			lista_oferta_d.column("#1",minwidth=70, width = 200 )
			lista_oferta_d.column("#2",minwidth=70, width = 100 )
			lista_oferta_d.column("#3",minwidth=70, width = 100 )
			lista_oferta_d.column("#4",minwidth=70, width = 158 )
			lista_oferta_d.column("#5",minwidth=70, width = 158 )
			

			leer_todo_ofertas()



		def editar_oferta_d():
			pass



		try:

			oferti=Toplevel(hija)
			oferti.title('Ofertas')
			oferti.geometry('1000x550')
			oferti.iconbitmap(logo)
			oferti.config(bg='#b6bdff')
			oferti.resizable(0,0)
			tab_control=ttk.Notebook(oferti)
			ofer=Frame(tab_control)
			ofer_d=Frame(tab_control)
			
			ofer.config(bg='#b6bdff')
			ofer_d.config(bg='#b6bdff')

			tab_control.add(ofer, text='Oferta Producto')
			tab_control.add(ofer_d, text='Oferta Por Departamento')
			
			tab_control.pack(expand=1, fill='both')
			nombre_a=lista1p.item(lista1p.selection())['values'][0]

			f1=nombre_a.endswith('(Oferta)')
			if f1==1:
				oferti.destroy()
				oferti=Toplevel(hija)
				oferti.title('Ofertas')
				oferti.geometry('1000x550')
				oferti.iconbitmap(logo)
				oferti.config(bg='#b6bdff')
				oferti.resizable(0,0)
				tab_control=ttk.Notebook(oferti)
				ofer=Frame(tab_control)
				ofer_d=Frame(tab_control)
				
				ofer.config(bg='#b6bdff')
				ofer_d.config(bg='#b6bdff')

				#tab_control.add(ofer, text='Oferta Producto')
				tab_control.add(ofer_d, text='Oferta Por Departamento')
				
				tab_control.pack(expand=1, fill='both')

				descuento_d=DoubleVar()
				descuento_d.set('')


				Label(ofer_d,text='Departamento',bg='#b6bdff',font='Helvetica 12').place(x=45,y=10)
				Label(ofer_d,text='Descuento',bg='#b6bdff',font='Helvetica 12').place(x=210,y=10)
				Label(ofer_d,text='Fecha Limite',bg='#b6bdff',font='Helvetica 12').place(x=440,y=0)

				Label(ofer_d,text='Dia',bg='#b6bdff',font='Helvetica 12').place(x=360,y=40)
				Label(ofer_d,text='Mes',bg='#b6bdff',font='Helvetica 12').place(x=475,y=40)
				Label(ofer_d,text='Año',bg='#b6bdff',font='Helvetica 12').place(x=610,y=40)
				
				def ver_departamentos_o():

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
						

					micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
					A=micursor.fetchall()

					departamento_of['values']= (list(f"{str(n[0])}" for n in A))
					
					miconexion.commit()


				departamento_of= ttk.Combobox(ofer_d)
				departamento_of.config(font='Helvetica 15',state='readonly',width=12)
				ver_departamentos_o()
				departamento_of.current(0)
				departamento_of.place(x=20,y=63)

				des2=Entry(ofer_d,relief='sunken',font='Helvetica 12',bd=7,width=7,textvariable=descuento_d)
				des2.place(x=210,y=60,height=41)
				des2.focus()

				des2.bind('<KeyRelease>',ver_prodcutos_ofertas_TR) 

				
				dia_final2=int(time.strftime("%d"))

				dias_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=6)
				dias_o['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
				dias_o.current(dia_final2-1)
				dias_o.pack(side=tk.RIGHT)
				dias_o.place(x=330,y=65)
				



				

				mes_final2=int(time.strftime("%m"))

				mes_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=10)
				mes_o['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
				mes_o.current(mes_final2-1)
				mes_o.pack(side=tk.RIGHT)
				mes_o.place(x=430,y=65)
				


				

				año_final2=time.strftime("%y")
				d2=int(año_final2)
				fech2=d2+2002

				años = list(range(1990, fech2))
				a2=len(años)-2
				años_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=10,values=años)
				años_o.current(a2)
				años_o.pack(side=tk.RIGHT)
				años_o.place(x=570,y=65)





				var2=IntVar()
				spin=Spinbox(ofer_d,from_=1, to=365, width=7,state='readonly',textvariable=var2,font='Helvetica 12')
				#spin.place(x=330,y=60,height=40)
				var2.set(1)

				Button(ofer_d,text='Agregar',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=agregar_oferta_d).place(x=720,y=60)




				lista_o_d=ttk.Treeview(ofer_d,height=14,style="Treeview",columns=[f"#{n}" for n in range(1, 4)])
			
				lista_o_d.place(x=0,y=170)


				scoll4=Scrollbar(ofer_d,command=lista_o_d.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
				scoll4.place(x=978,y=193,height=280)
				lista_o_d.config(yscrollcommand=scoll4.set)

				def activar_nombre_departamento():
				
					lista_o_d.heading('#0',text='Departamento',anchor=CENTER)
					lista_o_d.heading('#1',text='Descuento',anchor=CENTER)
					lista_o_d.heading('#2',text='Fecha al ingresar',anchor=CENTER)
					lista_o_d.heading('#3',text='Fecha Limite',anchor=CENTER)


				activar_nombre_departamento()


				def activar_nombre_producto():
				
					lista_o_d.heading('#0',text='Producto',anchor=CENTER)
					lista_o_d.heading('#1',text='Unidad',anchor=CENTER)
					lista_o_d.heading('#2',text='Precio $',anchor=CENTER)
					lista_o_d.heading('#3',text='Precio Bs.S',anchor=CENTER)

				lista_o_d.column("#0",minwidth=70, width = 255)
				lista_o_d.column("#1",minwidth=70, width = 255)
				lista_o_d.column("#2",minwidth=70, width = 255)
				lista_o_d.column("#3",minwidth=70, width = 255)
				


				frame_o_d=Frame(ofer_d,width=1000,height=100,bg='#b6bdff')
				frame_o_d.place(x=0,y=482)

				Button(frame_o_d,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=borrar_oferta_por_departamento).grid(row=0,column=0,padx=5)



				Button(frame_o_d,text='Detalles',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=detalles_ofertas_d).grid(row=0,column=1)



				ver_ofertas_departamento()



				return
				


		except IndexError:
			oferti.destroy()


			oferti=Toplevel(hija)
			oferti.title('Ofertas')
			oferti.geometry('1000x550')
			oferti.iconbitmap(logo)
			oferti.config(bg='#b6bdff')
			oferti.resizable(0,0)
			tab_control=ttk.Notebook(oferti)
			ofer=Frame(tab_control)
			ofer_d=Frame(tab_control)
			
			ofer.config(bg='#b6bdff')
			ofer_d.config(bg='#b6bdff')

			#tab_control.add(ofer, text='Oferta Producto')
			tab_control.add(ofer_d, text='Oferta Por Departamento')
			
			tab_control.pack(expand=1, fill='both')

			descuento_d=DoubleVar()
			descuento_d.set('')


			Label(ofer_d,text='Departamento',bg='#b6bdff',font='Helvetica 12').place(x=45,y=10)
			Label(ofer_d,text='Descuento',bg='#b6bdff',font='Helvetica 12').place(x=210,y=10)
			Label(ofer_d,text='Fecha Limite',bg='#b6bdff',font='Helvetica 12').place(x=440,y=0)

			Label(ofer_d,text='Dia',bg='#b6bdff',font='Helvetica 12').place(x=360,y=40)
			Label(ofer_d,text='Mes',bg='#b6bdff',font='Helvetica 12').place(x=475,y=40)
			Label(ofer_d,text='Año',bg='#b6bdff',font='Helvetica 12').place(x=610,y=40)
			
			def ver_departamentos_o():

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
					

				micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
				A=micursor.fetchall()

				departamento_of['values']= (list(f"{str(n[0])}" for n in A))
				
				miconexion.commit()


			departamento_of= ttk.Combobox(ofer_d)
			departamento_of.config(font='Helvetica 15',state='readonly',width=12)
			ver_departamentos_o()
			departamento_of.current(0)
			departamento_of.place(x=20,y=63)

			des2=Entry(ofer_d,relief='sunken',font='Helvetica 12',bd=7,width=7,textvariable=descuento_d)
			des2.place(x=210,y=60,height=41)
			des2.focus()

			des2.bind('<KeyRelease>',ver_prodcutos_ofertas_TR) 

			
			dia_final2=int(time.strftime("%d"))

			dias_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=6)
			dias_o['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
			dias_o.current(dia_final2-1)
			dias_o.pack(side=tk.RIGHT)
			dias_o.place(x=330,y=65)
			



			

			mes_final2=int(time.strftime("%m"))

			mes_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=10)
			mes_o['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
			mes_o.current(mes_final2-1)
			mes_o.pack(side=tk.RIGHT)
			mes_o.place(x=430,y=65)
			


			

			año_final2=time.strftime("%y")
			d2=int(año_final2)
			fech2=d2+2002

			años = list(range(1990, fech2))
			a2=len(años)-2
			años_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=10,values=años)
			años_o.current(a2)
			años_o.pack(side=tk.RIGHT)
			años_o.place(x=570,y=65)





			var2=IntVar()
			spin=Spinbox(ofer_d,from_=1, to=365, width=7,state='readonly',textvariable=var2,font='Helvetica 12')
			#spin.place(x=330,y=60,height=40)
			var2.set(1)

			Button(ofer_d,text='Agregar',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=agregar_oferta_d).place(x=720,y=60)




			lista_o_d=ttk.Treeview(ofer_d,height=14,style="Treeview",columns=[f"#{n}" for n in range(1, 4)])
		
			lista_o_d.place(x=0,y=170)


			scoll4=Scrollbar(ofer_d,command=lista_o_d.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll4.place(x=978,y=193,height=280)
			lista_o_d.config(yscrollcommand=scoll4.set)

			def activar_nombre_departamento():
			
				lista_o_d.heading('#0',text='Departamento',anchor=CENTER)
				lista_o_d.heading('#1',text='Descuento',anchor=CENTER)
				lista_o_d.heading('#2',text='Fecha al ingresar',anchor=CENTER)
				lista_o_d.heading('#3',text='Fecha Limite',anchor=CENTER)


			activar_nombre_departamento()


			def activar_nombre_producto():
			
				lista_o_d.heading('#0',text='Producto',anchor=CENTER)
				lista_o_d.heading('#1',text='Unidad',anchor=CENTER)
				lista_o_d.heading('#2',text='Precio $',anchor=CENTER)
				lista_o_d.heading('#3',text='Precio Bs.S',anchor=CENTER)

			lista_o_d.column("#0",minwidth=70, width = 255)
			lista_o_d.column("#1",minwidth=70, width = 255)
			lista_o_d.column("#2",minwidth=70, width = 255)
			lista_o_d.column("#3",minwidth=70, width = 255)
			


			frame_o_d=Frame(ofer_d,width=1000,height=100,bg='#b6bdff')
			frame_o_d.place(x=0,y=482)

			Button(frame_o_d,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=borrar_oferta_por_departamento).grid(row=0,column=0,padx=5)

			Button(frame_o_d,text='Editar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=editar_oferta_d).grid(row=0,column=1)

			Button(frame_o_d,text='Detalles',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=detalles_ofertas_d).grid(row=0,column=2,padx=5)



			ver_ofertas_departamento()



			return
		
		ide=lista1p.item(lista1p.selection())['text']
		nombre_a=lista1p.item(lista1p.selection())['values'][0]
		cantidad_a=lista1p.item(lista1p.selection())['values'][1]
		unidad_a=lista1p.item(lista1p.selection())['values'][2]
		departamento_a=lista1p.item(lista1p.selection())['values'][3]
		precio_ini_D_a=lista1p.item(lista1p.selection())['values'][4]
		precio_ini_B_a=lista1p.item(lista1p.selection())['values'][5]
		


		




		def cuenta_o(event):
			try:
				if descuento_o.get()=='':
					precio_B_final_o.set('')
					precio_D_final_o.set('')
					return

				elif descuento_o.get()==0:
					precio_B_final_o.set(0)
					precio_D_final_o.set(0)
					return


				a=precio_B_o.get()*descuento_o.get()
				b=a/100
				c=precio_B_o.get()-b
				precio_B_final_o.set(c)

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?',(departamento_o.get(), ))
				A=micursor.fetchall()	
				for i in A:
					tasita=i[0]

				d=precio_B_final_o.get()/tasita
				precio_D_final_o.set(d)
			except TclError:
				precio_B_final_o.set('')
				precio_D_final_o.set('')


		def agregar_oferta():
			if licencia_programa.get()=='no':
				Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
				if Valor=='yes':
					informacion_sobre_licencia()

				return

			try:

				if descuento_o.get()=='' and precio_D_final_o.get() =='' and precio_B_final_o.get()=='':
					pass
			except TclError:
				messagebox.showerror('BBDD','Faltan campos por escibir',parent=ofer)
				des.focus()

				return


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()


			micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?',(departamento_o.get(), ))
			A=micursor.fetchall()
			for b in A:
				tasita=b[0]

			micursor.execute('SELECT * FROM PRODUCTOS WHERE NOMBRE_PRODUCTO=?',(producto_o.get(), ))
			d=micursor.fetchall()
			for i in d:
				iden=i[0]
				precio_d_i=i[5]
				depar=i[13]

			precio_b_f=precio_d_i*tasita
				

			if precio_b_f>precio_B_final_o.get():
				Valor=messagebox.askquestion('BBDD','El precio de la oferta queda por debajo del precio de compra \n ¿Desea continuar?',parent=ofer)
				if Valor=='yes':
					pass
				else:
					limpiar_campos_oferta()
					return


				fecha3=fecha.split('/')
				dia_a=int(fecha3[0])
				mes_a=int(fecha3[1])
				año_a=int(fecha3[2])



				f=dia_a+var.get()

				dia_f=str(f)
				mes_f=str(mes_a)

				if f>30:
					f=f-30
					mes_a=mes_a+1


					if mes_a>12:

						año_a=año_a+1


				dia=str(f)
				mes=str(mes_a)
				año=str(año_a)

				if f<10:
					dia='0'+dia

				if mes_a<10:
					mes='0'+mes

				if año_a<10:
					año='0'+año

				fecha_o=dia+'/'+mes+'/'+año


				print(fecha_o)

				datos=iden,producto_o.get(),unidad_a,descuento_o.get(),precio_D_final_o.get(),precio_B_final_o.get(),departamento_o.get(),var.get(),fecha_o,1

				micursor.execute("INSERT INTO OFERTAS VALUES(NULL,?,?,?,?,?,?,?,?,?,?)",(datos))
				miconexion.commit()
				limpiar_campos_oferta()
				ver_ofertas()
			


		def ver_ofertas():
			record=lista_o.get_children()
			for element in record:
				lista_o.delete(element)


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM OFERTAS")
			A=micursor.fetchall()
			for usuarios in A:
				
				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[7], ))
				D=micursor.fetchall()
				for i in D:

					tasita=round(i[0],2)

					totil=round(usuarios[5]*tasita,2)
					z=round(usuarios[5],2)
					lista_o.insert('',0,text=usuarios[2],values=(usuarios[4],usuarios[9],usuarios[3],usuarios[7],z,totil))
	
		

		def borrar_oferta():
			try:
				lista_o.item(lista_o.selection())['text'][0]


			except IndexError:
				pass
				return

			Valor=messagebox.askquestion('BBDD','¿Desea Borrar Esta Oferta?',parent=ofer)
			if Valor=='yes':
			
			
				nombre_o=lista_o.item(lista_o.selection())['text']
				duracion=lista_o.item(lista_o.selection())['values'][1]
				
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("DELETE FROM OFERTAS WHERE PRODUCTO_OFERTA=? AND DURACION=?",(nombre_o,duracion))
				miconexion.commit()
				ver_ofertas()
				des.focus()

		def editar_oferta():
			try:
				lista_o.item(lista_o.selection())['text'][0]

			except IndexError:
				pass
				return
			
			ide=lista_o.item(lista_o.selection())['text']
			nombre_a=lista_o.item(lista_o.selection())['values'][1]
			cantidad_a=lista_o.item(lista_o.selection())['values'][2]
			unidad_a=lista_o.item(lista_o.selection())['values'][3]
			departamento_a=lista_o.item(lista_o.selection())['values'][4]
			precio_ini_D_a=lista_o.item(lista_o.selection())['values'][5]
			


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_PRODUCTO=?",(ide, ))
			B=micursor.fetchall()
			for f in B:

				dolar_o_editar=round(f[8],2)




			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(unidad_a, ))
				
			A=micursor.fetchall()
							
			for i in A:
				bolivar_o_editar=round(i[0]*dolar_o_editar,2)


			porducto_editar_o=StringVar()
			unidad_editar_o=StringVar()
			departamento_editar_o=StringVar()
			precio_D_editar_o=DoubleVar()
			precio_B_editar_o=DoubleVar()
			descuento_editar_o=DoubleVar()
			precio_final_D_editar_o=DoubleVar()
			precio_final_B_editar_o=DoubleVar()

			porducto_editar_o.set(ide)
			unidad_editar_o.set(cantidad_a)
			departamento_editar_o.set(unidad_a)
			precio_D_editar_o.set(dolar_o_editar)
			precio_B_editar_o.set(bolivar_o_editar)

			descuento_editar_o.set('')
			precio_final_D_editar_o.set('')
			precio_final_B_editar_o.set('')


			exento_E=BooleanVar()
			editar=Toplevel(ofer)
			editar.config(bg='#b6bdff')
			editar.title('Editar Oferta')
			editar.geometry('880x280')
			editar.resizable(0,0)
			editar.iconbitmap(logo)


			def cuenta_editar_oferta(event):
				try:
					if descuento_editar_o.get()=='':
						precio_final_D_editar_o.set('')
						precio_final_B_editar_o.set('')
						return

				except TclError:
					precio_final_D_editar_o.set('')
					precio_final_B_editar_o.set('')
					return

				try:

					if descuento_editar_o.get()==0:
						precio_final_D_editar_o.set(0)
						precio_final_B_editar_o.set(0)
						return

				except TclError:
					precio_final_D_editar_o.set(0)
					precio_final_B_editar_o.set(0)
					return


				a=precio_B_editar_o.get()*descuento_editar_o.get()
				b=a/100
				c=precio_B_editar_o.get()-b
				precio_final_B_editar_o.set(c)

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?',(departamento_editar_o.get(), ))
				A=micursor.fetchall()	
				for i in A:
					tasita=i[0]

				d=precio_final_B_editar_o.get()/tasita
				precio_final_D_editar_o.set(d)



			def guardar_cambios_ofertas():
				try:
					if descuento_editar_o.get()=='':
						pass
				except TclError:
					messagebox.showerror('BBDD','Nesecita ingresar un % de descuento',parent=editar)
					return


				if descuento_editar_o.get()==0:
					messagebox.showerror('BBDD','Nesecita ingresar un % de descuento',parent=editar)
					return



				if mes_licen.get()=='Enero':
					me='01'
				elif mes_licen.get()=='Febrero':
					me='02'
				elif mes_licen.get()=='Marzo':
					me='03'
				elif mes_licen.get()=='Abril':
					me='04'
				elif mes_licen.get()=='Mayo':
					me='05'
				elif mes_licen.get()=='Junio':
					me='06'
				elif mes_licen.get()=='Julio':
					me='07'
				elif mes_licen.get()=='Agosto':
					me='08'
				elif mes_licen.get()=='Septiembre':
					me='09'
				elif mes_licen.get()=='Octubre':
					me=10
				elif mes_licen.get()=='Noviembre':
					me=11
				elif mes_licen.get()=='Diciembre':
					me=12

				a=int(años_licen.get())
				b=a-2000
				fechita=str(dia_licen.get())+'/'+str(me)+'/'+str(b)
				print(fechita)




				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=descuento_editar_o.get(),precio_final_D_editar_o.get(),precio_final_B_editar_o.get(),fechita
				micursor.execute("UPDATE OFERTAS SET DESCUENTO=?, TOTAL_OFERTA_D=?, TOTAL_OFERTA_B=?, FECHA_OFERTA=?",(datos))


				miconexion.commit()

				ver_ofertas()
				editar.destroy()
					


			Label(editar,text='Producto',bg='#b6bdff',font='Helvetica 12').place(x=100,y=20)

			Label(editar,text='Departamento',bg='#b6bdff',font='Helvetica 12').place(x=320,y=20)

			Label(editar,text='Precio $',bg='#b6bdff',font='Helvetica 12').place(x=480,y=20)

			Label(editar,text='Precio Bs',bg='#b6bdff',font='Helvetica 12').place(x=640,y=20)


			Label(editar,text='Descuento(%)',bg='#b6bdff',font='Helvetica 12').place(x=750,y=20)

			Label(editar,text='Fecha Limite',bg='#b6bdff',font='Helvetica 12').place(x=150,y=110)


			Label(editar,text='Dia',bg='#b6bdff',font='Helvetica 12').place(x=70,y=160)
			Label(editar,text='Mes',bg='#b6bdff',font='Helvetica 12').place(x=177,y=160)
			Label(editar,text='Año',bg='#b6bdff',font='Helvetica 12').place(x=297,y=160)



			Label(editar,text=unidad_editar_o.get(),font='Helvetica 12', bg='#b6bdff').place(x=260,y=62)



			Entry(editar,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=25,textvariable=porducto_editar_o).place(x=10,y=60,height=41)

			Entry(editar,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=departamento_editar_o).place(x=300,y=60,height=41)


			
			Entry(editar,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_D_editar_o).place(x=455,y=60,height=41)

			Entry(editar,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_B_editar_o).place(x=610,y=60,height=41)

			des=Entry(editar,relief='sunken',font='Helvetica 12',bd=7,width=7,textvariable=descuento_editar_o)
			des.place(x=770,y=60,height=41)
			des.focus()
			des.bind('<KeyRelease>',cuenta_editar_oferta)
			
			Label(editar,text='Precio Final $',bg='#b6bdff',font='Helvetica 12').place(x=470,y=140)

			Label(editar,text='Precio Final Bs',bg='#b6bdff',font='Helvetica 12').place(x=630,y=140)

			Entry(editar,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_final_D_editar_o).place(x=435,y=180,height=41)

			
			Entry(editar,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_final_B_editar_o).place(x=590,y=180,height=41)




			dia_final2=int(time.strftime("%d"))

			dia_licen=ttk.Combobox(editar,font='Helvetica 11', state="readonly", height=12,width=6)
			dia_licen['values']= ('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','Todos')
			dia_licen.current(dia_final2-1)
			dia_licen.pack(side=tk.RIGHT)
				
			dia_licen.place(x=50,y=184)




			mes_final2=int(time.strftime("%m"))

			mes_licen=ttk.Combobox(editar,font='Helvetica 11', state="readonly", height=12,width=10)
			mes_licen['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Prueba','Todos')
			mes_licen.current(mes_final2-1)
			mes_licen.pack(side=tk.RIGHT)
			
			mes_licen.place(x=145,y=184)

		

			año_final2=time.strftime("%y")
			d2=int(año_final2)
			fech2=d2+2051

			años = list(range(2021, fech2))
			a2=len(años)-1
			años_licen=ttk.Combobox(editar,font='Helvetica 11', state="readonly", height=12,width=10,values=años)
			años_licen.current(0)
			años_licen.pack(side=tk.RIGHT)

			años_licen.place(x=270,y=184)


			Button(editar,text='Guardar',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=guardar_cambios_ofertas).place(x=760,y=180)



		def ver_departamentos_o():

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
				

			micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
			A=micursor.fetchall()

			departamento_of['values']= (list(f"{str(n[0])}" for n in A))
			
			miconexion.commit()


		def limpiar_campos_oferta():
			precio_B_final_o.set('')
			precio_D_final_o.set('')
			descuento_o.set('')
			des.focus()



		producto_o=StringVar()
		departamento_o=StringVar()
		precio_B_o=DoubleVar()
		precio_D_o=DoubleVar()
		descuento_o=DoubleVar()
		precio_B_final_o=DoubleVar()
		precio_D_final_o=DoubleVar()



		producto_o.set(nombre_a)
		precio_B_o.set(precio_ini_B_a)
		precio_D_o.set(precio_ini_D_a)
		precio_B_final_o.set('')
		precio_D_final_o.set('')


		descuento_o.set('')
		departamento_o.set(departamento_a)


		Label(ofer,text='Producto',bg='#b6bdff',font='Helvetica 12').place(x=100,y=20)

		Label(ofer,text='Departamento',bg='#b6bdff',font='Helvetica 12').place(x=320,y=20)

		Label(ofer,text='Precio $',bg='#b6bdff',font='Helvetica 12').place(x=480,y=20)

		Label(ofer,text='Precio Bs',bg='#b6bdff',font='Helvetica 12').place(x=640,y=20)


		Label(ofer,text='Descuento(%)',bg='#b6bdff',font='Helvetica 12').place(x=750,y=20)

		Label(ofer,text='Duración(Dias)',bg='#b6bdff',font='Helvetica 12').place(x=860,y=20)


		Label(ofer,text=unidad_a,font='Helvetica 12', bg='#b6bdff').place(x=260,y=62)





		Entry(ofer,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=25,textvariable=producto_o).place(x=10,y=60,height=41)

		Entry(ofer,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=departamento_o).place(x=300,y=60,height=41)

		Entry(ofer,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_D_o).place(x=455,y=60,height=41)

		Entry(ofer,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_B_o).place(x=610,y=60,height=41)

		des=Entry(ofer,relief='sunken',font='Helvetica 12',bd=7,width=7,textvariable=descuento_o)
		des.place(x=770,y=60,height=41)
		des.focus()

		des.bind("<KeyRelease>", cuenta_o)


		Entry(ofer,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_D_final_o).place(x=10,y=180,height=41)

		
		Entry(ofer,relief='sunken',font='Helvetica 12',state='readonly',bd=7,width=15,textvariable=precio_B_final_o).place(x=170,y=180,height=41)


		
		var=IntVar()
		spin=Spinbox(ofer,from_=1, to=30, width=7,state='readonly',textvariable=var,font='Helvetica 12')

		spin.place(x=880,y=60,height=40)
		var.set(1)




		lista_o=ttk.Treeview(ofer,height=10,style="Treeview",columns=[f"#{n}" for n in range(1, 7)])
	
		lista_o.place(x=0,y=250)


		scoll33=Scrollbar(ofer,command=lista_o.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll33.place(x=978,y=273,height=204)
		lista_o.config(yscrollcommand=scoll33.set)
		
		lista_o.heading('#0',text='Productos',anchor=CENTER)
		lista_o.heading('#1',text='Descuento',anchor=CENTER)
		lista_o.heading('#2',text='Fecha Limite',anchor=CENTER)
		lista_o.heading('#3',text='Unidad',anchor=CENTER)
		lista_o.heading('#4',text='Departamento',anchor=CENTER)
		lista_o.heading('#5',text='Precio $',anchor=CENTER)
		lista_o.heading('#6',text='Precio Bs.S',anchor=CENTER)


		lista_o.column("#0",minwidth=70, width = 280)
		lista_o.column("#1",minwidth=70, width = 100)
		lista_o.column("#2",minwidth=70, width = 100)
		lista_o.column("#3",minwidth=70, width = 100)
		lista_o.column("#4",minwidth=70, width = 150)
		lista_o.column("#5",minwidth=70, width = 140)
		lista_o.column("#6",minwidth=70, width = 150)



		Button(ofer,text='Agregar',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=agregar_oferta).place(x=330,y=180)

		frame_o=Frame(ofer,width=1000,height=100,bg='#b6bdff')
		frame_o.place(x=0,y=482)

		Button(frame_o,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=borrar_oferta).grid(row=0,column=0,padx=5)

		Button(frame_o,text='Editar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=editar_oferta).grid(row=0,column=1)


		menu_o = Menu(ofer, tearoff=0)
		menu_o.add_command(label="Agregar                     ",command=agregar_oferta)
		menu_o.add_command(label='Borrar            ',command=borrar_oferta)
		menu_o.add_command(label='Editar            ')
		menu_o.add_separator()
		menu_o.add_command(label='Limpiar            ',command=limpiar_campos_oferta)
		menu_o.add_command(label="Resultado",command=cuenta_o('1'))

		def click_derecho_oferta(event):
			try:
				menu_o.post(event.x_root, event.y_root)
			finally:
				menu_o.grab_release()

		frame_o.bind("<Button-3>", click_derecho_oferta)
		ofer.bind("<Button-3>", click_derecho_oferta)
		lista_o.bind("<Button-3>", click_derecho_oferta)

		ver_ofertas()

#-------------------------
		#--version 2
		def ofer_de():
			pass



		


		descuento_d=DoubleVar()
		descuento_d.set('')


		Label(ofer_d,text='Departamento',bg='#b6bdff',font='Helvetica 12').place(x=45,y=10)
		Label(ofer_d,text='Descuento',bg='#b6bdff',font='Helvetica 12').place(x=210,y=10)
		Label(ofer_d,text='Fecha Limite',bg='#b6bdff',font='Helvetica 12').place(x=440,y=0)

		Label(ofer_d,text='Dia',bg='#b6bdff',font='Helvetica 12').place(x=360,y=40)
		Label(ofer_d,text='Mes',bg='#b6bdff',font='Helvetica 12').place(x=475,y=40)
		Label(ofer_d,text='Año',bg='#b6bdff',font='Helvetica 12').place(x=610,y=40)
		



		departamento_of= ttk.Combobox(ofer_d)
		departamento_of.config(font='Helvetica 15',state='readonly',width=12)
		ver_departamentos_o()
		departamento_of.current(0)
		departamento_of.place(x=20,y=63)

		des2=Entry(ofer_d,relief='sunken',font='Helvetica 12',bd=7,width=7,textvariable=descuento_d)
		des2.place(x=210,y=60,height=41)
		des2.focus()

		des2.bind('<KeyRelease>',ver_prodcutos_ofertas_TR) 

		
		dia_final2=int(time.strftime("%d"))

		dias_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=6)
		dias_o['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
		dias_o.current(dia_final2-1)
		dias_o.pack(side=tk.RIGHT)
		dias_o.place(x=330,y=65)
		



		

		mes_final2=int(time.strftime("%m"))

		mes_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=10)
		mes_o['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
		mes_o.current(mes_final2-1)
		mes_o.pack(side=tk.RIGHT)
		mes_o.place(x=430,y=65)
		


		

		año_final2=time.strftime("%y")
		d2=int(año_final2)
		fech2=d2+2002

		años = list(range(1990, fech2))
		a2=len(años)-2
		años_o=ttk.Combobox(ofer_d,font='Helvetica 15', state="readonly",width=10,values=años)
		años_o.current(a2)
		años_o.pack(side=tk.RIGHT)
		años_o.place(x=570,y=65)





		var2=IntVar()
		spin=Spinbox(ofer_d,from_=1, to=365, width=7,state='readonly',textvariable=var2,font='Helvetica 12')
		#spin.place(x=330,y=60,height=40)
		var2.set(1)

		Button(ofer_d,text='Agregar',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=agregar_oferta_d).place(x=720,y=60)




		lista_o_d=ttk.Treeview(ofer_d,height=14,style="Treeview",columns=[f"#{n}" for n in range(1, 4)])
	
		lista_o_d.place(x=0,y=170)


		scoll4=Scrollbar(ofer_d,command=lista_o_d.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll4.place(x=978,y=193,height=280)
		lista_o_d.config(yscrollcommand=scoll4.set)

		def activar_nombre_departamento():
		
			lista_o_d.heading('#0',text='Departamento',anchor=CENTER)
			lista_o_d.heading('#1',text='Descuento',anchor=CENTER)
			lista_o_d.heading('#2',text='Fecha al ingresar',anchor=CENTER)
			lista_o_d.heading('#3',text='Fecha Limite',anchor=CENTER)


		activar_nombre_departamento()


		def activar_nombre_producto():
		
			lista_o_d.heading('#0',text='Producto',anchor=CENTER)
			lista_o_d.heading('#1',text='Unidad',anchor=CENTER)
			lista_o_d.heading('#2',text='Precio $',anchor=CENTER)
			lista_o_d.heading('#3',text='Precio Bs.S',anchor=CENTER)

		lista_o_d.column("#0",minwidth=70, width = 255)
		lista_o_d.column("#1",minwidth=70, width = 255)
		lista_o_d.column("#2",minwidth=70, width = 255)
		lista_o_d.column("#3",minwidth=70, width = 255)
		


		frame_o_d=Frame(ofer_d,width=1000,height=100,bg='#b6bdff')
		frame_o_d.place(x=0,y=482)

		Button(frame_o_d,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=borrar_oferta_por_departamento).grid(row=0,column=0,padx=5)

		Button(frame_o_d,text='Editar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=editar_oferta_d).grid(row=0,column=1)

		Button(frame_o_d,text='Detalles',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=detalles_ofertas_d).grid(row=0,column=2,padx=5)



		ver_ofertas_departamento()

	nombre_PDF_producto=StringVar()

	def hacer_PDF_producto():
		PDF=Toplevel(hija)
		PDF.geometry('400x150')
		PDF.configure(bg='#b6bdff')
		PDF.iconbitmap(logo)
		PDF.resizable(0,0)

		Label(PDF,font='Helvetica 12',text='Nombre del PDF',bg='#b6bdff').place(x=100,y=20)


		ttt=Entry(PDF,font='Helvetica 12',bd=9,relief='sunken',textvariable=nombre_PDF_producto)
		ttt.place(x=40,y=50,width=240,height=41)
		ttt.focus()

		


		def dt(event):
			hacer_PDF_producto2()
			PDF.destroy()
			return

		ttt.bind('<Return>',dt)

		Button(PDF,font='Helvetica 12',bd=7,width=8,relief='raised',text='Aceptar',cursor='hand2',command=lambda:dt('1')).place(x=285,y=50)



	def hacer_PDF_producto2():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?',parent=hija)
			if Valor=='yes':
				informacion_sobre_licencia()

			return


		if len(nombre_PDF_producto.get())==0:
			messagebox.showerror('BBDD','Debe ingresar un nombre para el PDF',parent=hija)
			return



		def grouper(iterable, n):
		    args = [iter(iterable)] * n
		    return itertools.zip_longest(*args)
		def export_to_pdf(data):
			print(data)
			dsds=nombre_PDF_producto.get()
			fdfd=dsds+'.pdf'
			c = canvas.Canvas(fdfd, pagesize=A4)
			w, h = A4
			max_rows_per_page = 45
		    # Margin.
			x_offset = 50
			y_offset = 50
		    # Space between rows.
			padding = 17
		    
			xlist = [x + x_offset for x in [0, 250, 400 ,500]]
			ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
		    
			for rows in grouper(data, max_rows_per_page):
				rows = tuple(filter(bool, rows))
				c.grid(xlist, ylist[:len(rows) + 1])
				for y, row in zip(ylist[:-1], rows):
					for x, cell in zip(xlist, row):
						c.drawString(x + 2, y - padding + 3, str(cell))
						c.setFont("Helvetica", 14)

				c.showPage()

			c.save()

		data = [("                        PRODUCTOS", 'DEPARTAMENTOS',"  PRECIOS")]
		data2 = [("                                 ", '                   ',"         TOTAL")]
		
		redon1=DoubleVar()
		redon2=DoubleVar()
		redon3=DoubleVar()
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		
		micursor.execute("SELECT * FROM PRODUCTOS ORDER BY DEPARTAMENTO,NOMBRE_PRODUCTO")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			rt=float(usuarios[8])
			f=float(usuarios[8])
			hg=float(usuarios[2])
			a=round(rt,2)
			b=round(f,2)
			g=round(hg,2)

			micursor.execute("SELECT * FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(usuarios[13], ))
		
			A=micursor.fetchall()
					
			for i in A:
				eee=usuarios[8]*i[2]
				redon3.set(round(eee,2))
						
				x=float(usuarios[8])
				gg=float(usuarios[2])
				redon1.set(round(x,2))
				
				necesario_depar.set(round(gg,2))
				
				dinero2 = '{:,}'.format(redon3.get())

				data.append((usuarios[1],usuarios[13],dinero2))

			
			
	

		
		export_to_pdf(data)
		redon3.set(0)
		#export_to_pdf(data2)
		messagebox.showinfo('BBDD','PDF de productos creado con exito',parent=hija)


	def ganancia():
		pass
	def ganancias_productos():

		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

			
		gana=Toplevel(hija)
		gana.title('Ganancia')
		gana.iconbitmap(logo)
		ancho_ventana = 1000
		alto_ventana = 500
		x_ventana = gana.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = gana.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		gana.geometry(posicion)
		#gana.geometry('1000x500')
		gana.resizable(0,0)
		gana.configure(bg='#b6bdff')



		def ver_productos_vendidos_gana():
			try:
				record=lista1g.get_children()
				for element in record:
					lista1g.delete(element)



				if mes_g.get()=='Enero':
					me_g=1
				elif mes_g.get()=='Febrero':
					me_g=2
				elif mes_g.get()=='Marzo':
					me_g=3
				elif mes_g.get()=='Abril':
					me_g=4
				elif mes_g.get()=='Mayo':
					me_g=5
				elif mes_g.get()=='Junio':
					me_g=6
				elif mes_g.get()=='Julio':
					me_g=7
				elif mes_g.get()=='Agosto':
					me_g=8
				elif mes_g.get()=='Septiembre':
					me_g=9
				elif mes_g.get()=='Octubre':
					me_g=10
				elif mes_g.get()=='Noviembre':
					me_g=11
				elif mes_g.get()=='Diciembre':
					me_g=12
				elif mes_g.get()=='Todos':
					me_g='Todos'


				dfdf=int(años_g.get())-2000
				try:
					dia4=int(days_g.get())
				except ValueError:
					pass
				dia3=str(days_g.get())

				try:
					mes3=str(me_g)
					año3=str(dfdf)
					if me_g<10:
						mes3='0'+mes3

					if dia4<10:
						dia3='0'+dia3
				except:
					pass

				
				fechi=dia3+'/'+mes3+'/'+año3



				if me_g=='Todos' and days_g.get()=='Todos':
					c0=fechi.split('/')

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM PRODUCTO_V WHERE CANTIDAD!=0 AND BOOLEANOSS=0")
					f=micursor.fetchall()
					for i in f:


						print(i[17],fechi,'print')
						c1=i[17].split('/')

						if c1[2]==c0[2]:
							fdfda=str(i[3])
							micursor.execute("SELECT CODIGO_PRODUCTO,PRODUCTO,SUM(CANTIDAD),UNIDAD,SUM(PRECIO_TOTAL_D),SUM(PRECIO_TOTAL_B) FROM PRODUCTO_V GROUP BY CODIGO_PRODUCTO HAVING CODIGO_PRODUCTO=? AND FECHA=? ORDER BY CANTIDAD ASC",(fdfda,i[17]))
							elusuario3=micursor.fetchall()
							for i0 in elusuario3:
								d=round(i0[2],3)
								d0=round(i0[4],2)
								d1=round(i0[5],2)
								lista1g.insert('',0,text=i0[0],values=(i0[1],d,i0[3],d0,d1))


					return
				

				

				elif me_g=='Todos':
					d0=fechi.split('/')
					

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
						
					micursor.execute("SELECT * FROM PRODUCTO_V WHERE CANTIDAD!=0 AND BOOLEANOSS=0")
					f=micursor.fetchall()
					for i in f:
						d1=i[17].split('/')

						if d0[0]==d1[0] and d0[2]==d1[2]:
							fdfda=str(i[3])
							micursor.execute("SELECT CODIGO_PRODUCTO,PRODUCTO,SUM(CANTIDAD),UNIDAD,SUM(PRECIO_TOTAL_D),SUM(PRECIO_TOTAL_B) FROM PRODUCTO_V GROUP BY CODIGO_PRODUCTO HAVING CODIGO_PRODUCTO=? AND FECHA=? ORDER BY CANTIDAD ASC",(fdfda,i[17]))
							elusuario3=micursor.fetchall()
							for i0 in elusuario3:
								c=round(i0[2],3)
								c0=round(i0[4],2)
								c1=round(i0[5],2)
								lista1g.insert('',0,text=i0[0],values=(i0[1],c,i0[3],c0,c1))


					return
				elif days_g.get()=='Todos':
					try:


						miconexion=sqlite3.connect('SISTEMA_LUMINA')
						micursor=miconexion.cursor()
						
						micursor.execute("SELECT * FROM PRODUCTO_V WHERE CANTIDAD!=0 AND BOOLEANOSS=0")
						elusuario2=micursor.fetchall()
						for i in elusuario2:


							a0=i[17].split('/')
							a1=fechi.split('/')
							

							if a0[1]==a1[1] and a0[2]==a1[2]:
								
								fdfda=str(i[3])
								
								micursor.execute("SELECT CODIGO_PRODUCTO,PRODUCTO,SUM(CANTIDAD),UNIDAD,SUM(PRECIO_TOTAL_D),SUM(PRECIO_TOTAL_B) FROM PRODUCTO_V GROUP BY CODIGO_PRODUCTO HAVING CODIGO_PRODUCTO=? AND FECHA=?",(fdfda,i[17]))
								elusuario3=micursor.fetchall()
								for i0 in elusuario3:
									b=round(i0[2],3)
									b0=round(i0[4],2)
									b1=round(i0[5],2)
									lista1g.insert('',0,text=i0[0],values=(i0[1],b,i0[3],b0,b1))

					finally:
						continua=1
						

					return

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				
				micursor.execute("SELECT * FROM PRODUCTO_V WHERE FECHA=? GROUP BY PRODUCTO ORDER BY (CANTIDAD) DESC",(fechi, ))
				elusuario2=micursor.fetchall()
				for usuarios2 in elusuario2:
					
					

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					
					micursor.execute("SELECT * FROM PRODUCTO_V WHERE FECHA=? AND CODIGO_PRODUCTO=?",(usuarios2[17],usuarios2[3]))
					elusuario3=micursor.fetchall()

					for usuarios3 in elusuario3:



						total_productos_ven_D.set(usuarios3[10]+total_productos_ven_D.get())
						total_productos_ven_B.set(usuarios3[11]+total_productos_ven_B.get())
						cantidad_productos_ven.set(usuarios3[5]+cantidad_productos_ven.get())
					

						td=round(total_productos_ven_D.get(),2)
						tb=round(total_productos_ven_B.get(),2)
						c=round(cantidad_productos_ven.get(),2)
					lista1g.insert('',0,text=usuarios2[3],values=(usuarios2[4],c,usuarios2[7],td,tb))
				
					


					total_productos_ven_D.set(0)
					total_productos_ven_B.set(0)
					cantidad_productos_ven.set(0)


	    
			finally:
				continua=1



		frax=Frame(gana,bg='#b6bdff')
		frax.grid(row=0,column=0,sticky='NSEW')
		
		Label(frax,width=105,bg='#b6bdff').grid(row=0,column=0,sticky='W')
		frax.columnconfigure(0,weight=1)
		



		frame_combo=Frame(frax,bg='#b6bdff')
		frame_combo.grid(row=1,column=0,sticky='NSEW')

		dia_final=int(time.strftime("%d"))

		days_g=ttk.Combobox(frame_combo,font='Helvetica 11', state="readonly", height=10,width=6)
		days_g['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,'Todos')
		days_g.current(dia_final-1)
		days_g.grid(row=0,column=0)




		

		mes_final=int(time.strftime("%m"))

		mes_g=ttk.Combobox(frame_combo,font='Helvetica 11', state="readonly", height=10,width=10)
		mes_g['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Todos')
		mes_g.current(mes_final-1)
		mes_g.grid(row=0,column=1,padx=10)
			


		

		año_final=time.strftime("%y")
		d=int(año_final)
		fech=d+2001

		años = list(range(1990, fech))
		a=len(años)-1
		años_g=ttk.Combobox(frame_combo,font='Helvetica 11', state="readonly", height=10,width=10,values=años)
		años_g.current(a)
		años_g.grid(row=0,column=2)




		gana.rowconfigure(2,weight=2)
		gana.rowconfigure(3,weight=5)

		gana.columnconfigure(0,weight=5)

		frame_lista=Frame(gana,bg='#b6bdff')
		frame_lista.grid(row=3,column=0,sticky='NSEW',columnspan=2)

		


		lista1g=ttk.Treeview(frame_lista,style='Treeview',columns=[f"#{n}" for n in range(1, 6)])
		lista1g.pack(expand=1,fill=BOTH)
		lista1g.grid(row=0,column=0,sticky='nsew',columnspan=4,rowspan=4)
		frame_lista.rowconfigure(0,weight=5)
		frame_lista.columnconfigure(0,weight=5)



		scoll=Scrollbar(frame_lista,command=lista1g.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.grid(row=0,column=2,sticky='NSEW')


		lista1g.config(yscrollcommand=scoll.set)

		lista1g.heading('#0',text='Codigo')
		lista1g.heading('#1',text='Producto')
		lista1g.heading('#2',text='Cantidad')
		lista1g.heading('#3',text='Unidad')
		lista1g.heading('#4',text='Total $')
		lista1g.heading('#5',text='Total Bs.S')
		

		lista1g.column("#0",minwidth=70, width = 50)
		lista1g.column("#1",minwidth=70, width = 220)
		lista1g.column("#2",minwidth=70, width = 80)
		lista1g.column("#3",minwidth=70, width = 40)
		lista1g.column("#4",minwidth=70, width = 100)
		lista1g.column("#5",minwidth=70, width = 100)
		

		Button(frame_combo,text='Resultado',cursor='hand2',font='Helvetica 12',relief='raised',bd=7,command=ver_productos_vendidos_gana).grid(row=0,column=3,padx=5)
		#ver_productos_vendidos_gana()


		


	def interfaz_producto():
		pass


	menu = Menu(raiz, tearoff=0)
	menu.add_command(label="Agregar                     ",command=crear_Productos)
	menu.add_command(label="Resultado",command=Resultado)
	menu.add_command(label='Agregar Departamento            ',command=agregar_departamento)
	menu.add_command(label='Agregar Formas De Pago            ',command=lambda:agregar_forma_de_pago(hija))
	menu.add_separator()
	menu.add_command(label='Crear Oferta            ',command=crear_oferta)
	menu.add_separator()
	menu.add_command(label="Editar",command=editar_producto_P)
	menu.add_command(label="Borrar",command=comprobacion_de_borrar)
	menu.add_command(label="Limpiar Campos",command=limpiar_campos_P)
	
	


	frame_buscador=Frame(hija,bg='#b6bdff')
	frame_buscador.grid(row=0,column=4,sticky='NSEW',columnspan=6)
	frame_buscador.columnconfigure(0,weight=1)

	Label(frame_buscador,bg='#b6bdff').grid(row=0,column=0,padx=185,pady=20)

	entry=Entry(frame_buscador,relief='sunken',font='Helvetica 12',bd=7,textvariable=Buscar_producto_P)
	entry.grid(row=0,column=1,sticky='E')
	Button(frame_buscador,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_producto_P('1')).grid(row=0,column=2,pady=10,padx=5)

	entry.bind('<Return>',buscar_producto_P)

	botones=Frame(hija)
	botones.configure(bg='#b6bdff')
	botones.grid(row=9,column=0,sticky='NSEW',columnspan=8,rowspan=2,pady=5)

	#hija.rowconfigure(0,weight=1)

	Button(botones,text='Agregar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=crear_Productos).grid(row=0,column=0)
	Button(botones,text='Editar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=editar_producto_P).grid(row=0,column=1)
	Button(botones,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=comprobacion_de_borrar).grid(row=0,column=2)
	Button(botones,text='Crear Oferta',cursor='hand2',width=9,height=1,bd=5,relief='raised',font='Helvetica 12',command=crear_oferta).grid(row=0,column=5)
	Button(botones,text='Ganancias',cursor='hand2',width=9,height=1,bd=5,relief='raised',font='Helvetica 12',command=ganancias_productos).grid(row=0,column=6)

	Button(botones,text='PDF',cursor='hand2',width=9,height=1,bd=5,relief='raised',font='Helvetica 12',command=hacer_PDF_producto).grid(row=0,column=7)



	
	botones.columnconfigure(8,weight=1)

	ttk.Style().configure('black.TCheckbutton', foreground='black', background='#b6bdff',font='Helvetica 15')
	check=ttk.Checkbutton(botones, text="Ver Ofertas",style='black.TCheckbutton',variable=ver_producto_con_oferta_P, onvalue=1)
	check.grid(row=0,column=10,sticky='e')

	check.bind('<Button-1>',buscar_producto_P)

	identificador=Entry(hija,font='Helvetica 12',bd=7,width=25,relief='sunken',textvariable=identificador_P)
	identificador.grid(row=3,column=1,sticky='NSEW',ipady=4)
	
	def focus_identificador():
		identificador.focus()
	focus_identificador()


	productodos=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',textvariable=producto_P)
	productodos.grid(row=5,column=1,sticky='NSEW',columnspan=3,ipady=4)
	
	def productos_focus(event):
		event.widget.tk_focusNext().focus()
		return

	identificador.bind('<Return>', productos_focus)


	
	frame=Frame(hija,bg='#b6bdff',padx=10)
	frame.grid(row=2,column=5,sticky='NSEW',rowspan=2)

	hija.columnconfigure(7,weight=1)

	cantidad=Entry(frame,font='Helvetica 12',width=10,bd=7, relief='sunken',textvariable=cantidad_P)
	cantidad.grid(row=2,column=0,sticky='NSEW',ipady=4)

	def calcular_tasa_d_P(event):
		try:
			if precio_inicial_dolares_P.get()=='':
				pass
		except TclError:
			precio_inicial_bolivares_P.set('')
			return


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(departamento_v.get(), ))
		A=micursor.fetchall()

		for i in A:
			tasita=i[0]


		a=precio_inicial_dolares_P.get()*tasita
		precio_inicial_bolivares_P.set(a)


	def calcular_tasa_B_P(event):
		try:
			if precio_inicial_bolivares_P.get()=='':
				pass
		except TclError:
			precio_inicial_dolares_P.set('')
			
			return


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(departamento_v.get(), ))
		A=micursor.fetchall()

		for i in A:
			tasita=i[0]


		a=precio_inicial_bolivares_P.get()/tasita
		precio_inicial_dolares_P.set(a)




	productodos=Entry(frame,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_inicial_dolares_P)
	productodos.grid(row=2,column=2,sticky='NSEW',padx=10,ipady=4)
	productodos.bind('<KeyRelease>',calcular_tasa_d_P)

	precio_descuento=Entry(frame,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_inicial_bolivares_P)
	precio_descuento.grid(row=2,column=4,sticky='NSEW',ipady=4)
	precio_descuento.bind('<KeyRelease>',calcular_tasa_B_P)

	combo = ttk.Combobox(frame)
	combo.config(font='Helvetica 15',state='readonly',width=12)
	combo['values']= ('Unidad','Kilogramos','Litros','Metros')
	combo.current(0)
	combo.grid(row=2,column=5,padx=10,sticky='SE',pady=4)

	descuento2=Entry(frame,font='Helvetica 12',state='readonly',width=10,bd=7,relief='sunken',textvariable=precio_final_D_P)
	descuento2.grid(row=2,column=6,sticky='NSW',padx=10,ipadx=4)


	frame2=Frame(hija,bg='#b6bdff')
	frame2.grid(row=4,column=5,sticky='NSEW',rowspan=2,padx=10)

	descuento=Entry(frame2,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=porcentaje_P)
	descuento.grid(row=2,column=0,sticky='NSW')


	ttk.Style().configure('black.TCheckbutton', foreground='black', background='#b6bdff',font='Helvetica 15')

	Button(frame2,text='Resultado',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=lambda:Resultado('1')).grid(row=2,column=2,sticky='W',padx=2)
	ttk.Checkbutton(frame2, text="Exento",style='black.TCheckbutton',variable=exento_P, onvalue=1).grid(row=2,column=1,sticky='e',padx=20)

	departamento_v= ttk.Combobox(frame2)
	departamento_v.config(font='Helvetica 15',state='readonly',width=12)
	ver_departamentos_p()
	departamento_v.current(0)
	departamento_v.grid(row=2,column=3,padx=20,sticky='SE',pady=4)



	descuento3=Entry(frame2,font='Helvetica 12',bd=7,width=12,relief='sunken',textvariable=precio_final_B_P)
	descuento3.grid(row=2,column=4,sticky='NSW')

#--------------------------------LABEL-----------------------------------

	

	identificadorL=Label(hija,text='Codigo',font='Helvetica 12',bg='#b6bdff')
	identificadorL.grid(row=2,column=1,sticky='NSEW',pady=10)

	#hija.rowconfigure(1,weight=1)
	
	#hija.rowconfigure(11,weight=2)



	nombre_descuentoL=Label(hija,text='Producto',font='Helvetica 12',bg='#b6bdff')
	nombre_descuentoL.grid(row=4,column=1,sticky='NSEW',pady=10)

	

	productoL2=Label(frame,text='Cantidad',font='Helvetica 12',bg='#b6bdff')
	productoL2.grid(row=1,column=0,pady=10)

	productoL=Label(frame,text='Precio $',font='Helvetica 12',bg='#b6bdff')
	productoL.grid(row=1,column=2,pady=10)

	cantidadL=Label(frame,text='Precio Bs.S',font='Helvetica 12',bg='#b6bdff')
	cantidadL.grid(row=1,column=4,pady=10)

	porcentanjeL2=Label(frame,text='P. Final $',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL2.grid(row=1,column=6,sticky='w',pady=10,padx=20)



	porcentanjeL=Label(frame2,text='% Ganancia',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL.grid(row=1,column=0,sticky='w',pady=10,padx=7)


	

	porcentanjeL2=Label(frame2,text='P. Final Bs.S',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL2.grid(row=1,column=4,sticky='w',padx=10)

	#Label(hija,bg='#b6bdff').grid(row=10,column=3,pady=10,sticky='w')

#---------------------------

	hija.columnconfigure(0,weight=1)
	hija.columnconfigure(8,weight=1)
	hija.rowconfigure(6,weight=1)
	

	frame_lista_P=Frame(hija)
	frame_lista_P.grid(row=7,column=0,sticky='NSEW',columnspan=12)
	style2 = ttk.Style()
	style2.configure("Treeview", font=('Helvetica', 10))
	

	lista1p=ttk.Treeview(frame_lista_P,style="Treeview",columns=[f"#{n}" for n in range(1, 7)])
	lista1p.pack(expand=1,fill=BOTH)
	lista1p.grid(row=0,column=0,sticky='NSEW',rowspan=8)

	frame_lista_P.rowconfigure(0,weight=5)
	frame_lista_P.columnconfigure(0,weight=5)
	hija.rowconfigure(7,weight=5)
	

	scoll=Scrollbar(frame_lista_P,command=lista1p.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=0,column=2,sticky='NSEW')

	lista1p.config(yscrollcommand=scoll.set)

	lista1p.heading('#0',text='Codigo',anchor=CENTER)
	lista1p.heading('#1',text='Productos',anchor=CENTER)
	lista1p.heading('#2',text='Cantidad',anchor=CENTER)
	lista1p.heading('#3',text='Unidad',anchor=CENTER)
	lista1p.heading('#4',text='Departamento',anchor=CENTER)
	lista1p.heading('#5',text='Precio $',anchor=CENTER)
	lista1p.heading('#6',text='Precio Bs.S',anchor=CENTER)


	lista1p.column("#0",minwidth=70, width = 150)
	lista1p.column("#1",minwidth=70, width = 380)
	lista1p.column("#2",minwidth=70, width = 50)
	lista1p.column("#3",minwidth=70, width = 50)
	lista1p.column("#4",minwidth=70, width = 150)
	lista1p.column("#5",minwidth=70, width = 100)
	lista1p.column("#6",minwidth=70, width = 140)
	
	lista1p.bind("<Button-3>", sub_menu)
	hija.bind("<Button-3>", sub_menu)
	frame2.bind("<Button-3>", sub_menu)
	frame.bind("<Button-3>", sub_menu)
	botones.bind("<Button-3>", sub_menu)
	frame_buscador.bind("<Button-3>", sub_menu)


	
	leer_todo_P()
	borrar_campos_P()

	def inventario_inicial():
		pass

	def Inv_inicio():
		window=Toplevel()
		window.configure(bg='#b6bdff')
		window.resizable(0,0)
		window.iconbitmap(logo)
		window.geometry('852x373')
#--------------------------------
		buscar_producto_P2=StringVar()
		cantidad_P2=StringVar()
		precio_inicial_dolares_P2=StringVar()
		precio_inicial_bolivares_P2=StringVar()
		porcentaje_P2=StringVar()

		def leer_todo_P2():
			record=lista1p2.get_children()
			for element in record:
				lista1p2.delete(element)
	
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				if usuarios[4]==1:
					n='Si'
				else:
					n='No'
				lista1p2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[2],usuarios[3],n,usuarios[5],usuarios[6],usuarios[7]))

		def buscar_producto_P_window():

			if len(buscar_producto_P2.get())==0:
				record=lista1p2.get_children()
			
				for element in record:
					lista1p2.delete(element)
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					if usuarios[4]==1:
						n='Si'
					else:
						n='No'
					x=float(usuarios[8])
					f=float(usuarios[8]*tasa_del_dolar.get())
					c=float(usuarios[2])
					a=round(usuarios[5],2)
					b=round(usuarios[6],2)
					g=round(c,2)
					lista1p2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[2],usuarios[3],n,a,b,usuarios[7]))
					

			else:
				record=lista1p2.get_children()
			
				for element in record:
					lista1p2.delete(element)
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
				elusuario=micursor.fetchall()
				for usuarios in elusuario:

					r=usuarios[0].startswith(buscar_producto_P2.get())
					k=usuarios[1].startswith(buscar_producto_P2.get().capitalize())
					
					if k==1 or r==1:
						if usuarios[4]==1:
							n='Si'
						else:
							n='No'
						x=float(usuarios[8])
						f=float(usuarios[8]*tasa_del_dolar.get())
						c=float(usuarios[2])
						a=round(usuarios[5],2)
						b=round(usuarios[6],2)
						g=round(c,2)
						lista1p2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[2],usuarios[3],n,a,b,usuarios[7]))
						
				miconexion.commit()
		
		

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


		Entry(window,font='Helvetica 12',bd=7,relief='sunken',textvariable=buscar_producto_P2).place(x=0,y=10)
		Button(window,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=buscar_producto_P_window).place(x=205,y=5)



		style = ttk.Style()
		style.configure("mystyle.Treeview", highlightthickness=0, bd=10,relief='raised', font=('Helvetica', 12))

		lista1p2=ttk.Treeview(window,style="Treeview",height=14,columns=[f"#{n}" for n in range(1, 8)])
		lista1p2.place(x=0,y=70)

		scoll=Scrollbar(window,command=lista1p2.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=834,y=93,height=282)

		lista1p2.config(yscrollcommand=scoll.set)

		lista1p2.heading('#0',text='Identificador',anchor=CENTER)
		lista1p2.heading('#1',text='Productos',anchor=CENTER)
		lista1p2.heading('#2',text='Cantidad',anchor=CENTER)
		lista1p2.heading('#3',text='Unidad',anchor=CENTER)
		lista1p2.heading('#4',text='Exento',anchor=CENTER)
		lista1p2.heading('#5',text='Precio $',anchor=CENTER)
		lista1p2.heading('#6',text='Precio Bs.S',anchor=CENTER)
		lista1p2.heading('#7',text='Ganancia(%)',anchor=CENTER)

		lista1p2.column("#0",minwidth=70, width = 100)
		lista1p2.column("#1",minwidth=70, width = 200 )
		lista1p2.column("#2",minwidth=70, width = 100 )
		lista1p2.column("#3",minwidth=70, width = 100 )
		lista1p2.column("#4",minwidth=70, width = 50 )
		lista1p2.column("#5",minwidth=70, width = 100 )
		lista1p2.column("#6",minwidth=70, width = 100 )
		lista1p2.column("#7",minwidth=70, width = 100 )
		
		leer_todo_P2()


	Button(botones,text='Inv. Inicial',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=Inv_inicio).grid(row=0,column=4)
	
	

	#--------------PROVEEDORES-----------------------
#com
	pro.config(bg='#b6bdff')
	def proveedores():
		pass

	def limpiar_campos_pro():
		proveedor_pro.set('')
		rif_pro.set('')
		direccion_pro.set('')
		telefono_pro.set('')



	def crear_proveedor_pro():

		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		try:
			if len(proveedor_pro.get())!=0 and len(rif_pro.get())!=0:
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=proveedor_pro.get().capitalize(),rif_pro.get(),telefono_pro.get(),direccion_pro.get()

				micursor.execute("INSERT INTO PROVEEDORES VALUES(NULL,?,?,?,?)",(datos))
				miconexion.commit()
				limpiar_campos_pro()
				leer_todo_pro()
			else:
				messagebox.showwarning('BBDD','Se necesita al menos un nombre y un rif',parent=pro)

		except sqlite3.IntegrityError:
			messagebox.showwarning('Lumina','El rif ya existe',parent=pro)
			rif_pro.set('')
			return
		except sqlite3.OperationalError:
			messagebox.showwarning('Lumina','Base de datos no creada',parent=pro)
			return
		except TclError:
			messagebox.showerror('BBDD','Faltan campos por escribir',parent=pro)	
			return

	def leer_todo_pro():
		record=lista1pro.get_children()
		for element in record:
			lista1pro.delete(element)


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		micursor.execute("SELECT * FROM PROVEEDORES")
		a=micursor.fetchall()
		for usuarios in a:
			lista1pro.insert('',0,text=usuarios[1],values=(usuarios[2],usuarios[3],usuarios[4]))


		miconexion.commit()

	def comprobacion_de_borrar_pro():
		try:
			rif_pp=lista1pro.item(lista1pro.selection())['text']
			nom_pp=lista1pro.item(lista1pro.selection())['values'][0]
		except TclError:
			pass
			return

		except IndexError:
			pass
			return

		valor=messagebox.askquestion('BBDD','¿Desea Borrar este proveedor?',parent=pro)
		if valor=='yes':
			borrar_proveedor_pro()

	def borrar_proveedor_pro():
		try:
			rif_pp=lista1pro.item(lista1pro.selection())['values'][0]

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("DELETE  FROM PROVEEDORES WHERE RIF_PROVEEDOR=?",(rif_pp, ))
			miconexion.commit()
			leer_todo_pro()
		except sqlite3.OperationalError:
			pass
			return
	

	prove=Entry(pro,font='Helvetica 12',bd=7,relief='sunken',textvariable=proveedor_pro)
	prove.grid(row=2,column=0,sticky='NSEW',columnspan=5)
	prove.focus()

	pro.columnconfigure(0,weight=1)

	rifc=Entry(pro,font='Helvetica 12',bd=7,relief='sunken',textvariable=rif_pro)
	rifc.grid(row=5,column=0,sticky='NSEW',columnspan=5)

	

	tel=Entry(pro,font='Helvetica 12',bd=7,relief='sunken',textvariable=telefono_pro)
	tel.grid(row=7,column=0,sticky='NSEW',columnspan=5)

	direc=Entry(pro,font='Helvetica 12',bd=7,relief='sunken',textvariable=direccion_pro)
	direc.grid(row=9,column=0,sticky='NSEW',columnspan=5)


	
#--------------------------------LABEL-----------------------------------

	Label(pro,bg='#b6bdff').grid(row=5,column=6,padx=10,pady=10)
	Label(pro,bg='#b6bdff').grid(row=2,column=6,padx=10,pady=10)
	Label(pro,bg='#b6bdff').grid(row=7,column=6,padx=10,pady=10)
	Label(pro,bg='#b6bdff').grid(row=9,column=6,padx=10,pady=10)



	

	identificadorL=Label(pro,text='Proveedor',font='Helvetica 12',bg='#b6bdff')
	identificadorL.grid(row=1,column=0,pady=10,sticky='W',padx=120)

	pro.rowconfigure(0,weight=1)
	
	pro.rowconfigure(11,weight=2)



	nombre_descuentoL=Label(pro,text='RIF',font='Helvetica 12',bg='#b6bdff')
	nombre_descuentoL.grid(row=4,column=0,sticky='w',pady=10,padx=140)


	porcentanjeL=Label(pro,text='Telefono',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL.grid(row=6,column=0,sticky='w',pady=10,padx=120)


	porcentanjeL2=Label(pro,text='Direccion',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL2.grid(row=8,column=0,sticky='w',pady=10,padx=120)
	
	botonsitos=Frame(pro,bg='#b6bdff')
	botonsitos.grid(row=11,column=0,sticky='SEW',columnspan=7)
	#Label(botonsitos,width=4,height=1,bg='#b6bdff').grid(row=0,column=0)
	Button(botonsitos,text='Agregar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=crear_proveedor_pro).grid(row=0,column=1,sticky='W')
	Button(botonsitos,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=comprobacion_de_borrar_pro).grid(row=0,column=2,sticky='W',padx=5)
	#Button(botonsitos,text='Detalles',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12').grid(row=0,column=3,sticky='W')

	ttk.Style().configure('black.TCheckbutton', foreground='black', background='#b6bdff',font='Helvetica 15')
	

#---------------------------

	
	
	
	pro.columnconfigure(7,weight=20)
	frame_lista_pro=Frame(pro)
	frame_lista_pro.grid(row=0,column=7,sticky='NSEW',rowspan=12,columnspan=4)
	style2 = ttk.Style()
	style2.configure("Treeview", font=('Helvetica', 10))
	

	lista1pro=ttk.Treeview(frame_lista_pro,style="Treeview",columns=[f"#{n}" for n in range(1, 4)])
	lista1pro.pack(expand=1,fill=BOTH)
	lista1pro.grid(row=0,column=0,sticky='NSEW',rowspan=8)

	frame_lista_pro.rowconfigure(0,weight=5)
	frame_lista_pro.columnconfigure(0,weight=5)
	pro.columnconfigure(4,weight=5)
	

	scoll=Scrollbar(frame_lista_pro,command=lista1pro.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=0,column=1,sticky='NSEW')

	lista1pro.config(yscrollcommand=scoll.set)

	lista1pro.heading('#0',text='Proveedores',anchor=CENTER)
	lista1pro.heading('#1',text='RIF',anchor=CENTER)
	lista1pro.heading('#2',text='Telefono',anchor=CENTER)
	lista1pro.heading('#3',text='Direccion',anchor=CENTER)
	

	lista1pro.column("#0",minwidth=100, width = 200)
	lista1pro.column("#1",minwidth=70, width = 100 )
	lista1pro.column("#2",minwidth=70, width = 162 )
	lista1pro.column("#3",minwidth=70, width = 200 )
	


	leer_todo_pro()




	
#----------------------------------------------------------------------------
#def inventario_Combo():
	
	
	#ventana.configure(bg='silver')
	def combos():
		pass
	
#CCCCCCCCCCCCCCCCTTTTTTTTTTTTTTTNNNNNNNNNN

	
	CTN.configure(bg='#b6bdff')
	def clientes():
		pass

	def agregar_CTN():

		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		if len(nombre_cliente_CTN.get())==0 or len(cedula_cliente_CTN.get())==0:
		
		
			messagebox.showerror('BBDD','Se requiere al menos Nombre y Cedula del cliente',parent=CTN)
			return
		if len(direccion_cliente_CTN.get())==0:
			direccion_cliente_CTN.set('Nulo')

		if len(telefono_cliente_CTN.get())==0:
			telefono_cliente_CTN.set('Nulo')

		try:

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=nombre_cliente_CTN.get().capitalize(),apellido_cliente_CTN.get().capitalize(),cedula_cliente_CTN.get(),direccion_cliente_CTN.get(),telefono_cliente_CTN.get(),fecha
			micursor.execute("INSERT INTO CLIENTES VALUES(?,?,?,?,?,?,NULL)",(datos))
			miconexion.commit()
			borrar_campos_CTN()
			leer_todo_CTN5()
			NOMBRE.focus()
			
			
		except sqlite3.IntegrityError:
			messagebox.showwarning('BBDD','El Cliente ya esta registrado',parent=CTN)
			identificador_.set('')
		except sqlite3.OperationalError:
			messagebox.showwarning('BBDD','Base de datos no creada',parent=CTN)
		except TclError:
			messagebox.showerror('BBDD','Faltan campos por escribir',parent=CTN)

	def leer_todo_CTN5():
		record=lista1CTN.get_children()
		for element in record:
			lista1CTN.delete(element)
    
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM CLIENTES")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			a=usuarios[0]+' '+usuarios[1]
			lista1CTN.insert('',0,text=a,values=(usuarios[2],usuarios[3],usuarios[4],usuarios[5]))
   

	def comprobacion_de_borrar_CTN():
		try:
			lista1CTN.item(lista1CTN.selection())['values'][0]

		except IndexError:
			messagebox.showerror('BBDD','No ha seleccionado ningun cliente',parent=CTN)
			return

		continua2.set(messagebox.askquestion('BBDD','Desea borrar este cliente',parent=CTN))
		if continua2.get()=='yes':
			borrar_cliente_CTN()

	def borrar_cliente_CTN():
		name=lista1CTN.item(lista1CTN.selection())['values'][0]
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("DELETE FROM CLIENTES WHERE CEDULA_CLIENTE=?",(name, ))
		miconexion.commit()
		leer_todo_CTN5()



	def borrar_campos_CTN():
		nombre_cliente_CTN.set('')
		apellido_cliente_CTN.set('')
		cedula_cliente_CTN.set('')
		direccion_cliente_CTN.set('')
		telefono_cliente_CTN.set('')



	def ventana_editar_cliente_CTN():
		try:
			lista1CTN.item(lista1CTN.selection())['text']

			d=lista1CTN.item(lista1CTN.selection())['values'][0]

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(d, ))
			a=micursor.fetchall()
			for i in a:
				nombre_cliente_new=i[0]
				apellido_cliente_new=i[1]
				cedula_cliente_old=i[2]
				direccion_cliente_new=i[3]
				telefono_cliente_new=i[4]

			continua_CTN.set(1)
		except IndexError:
			continua_CTN.set(2)
			return
		if continua.get()!=2:
			editar=Toplevel(CTN)
			editar.config(bg='#b6bdff')
			editar.title('Editar Cliente')
			editar.geometry('400x350')
			editar.resizable(0,0)
			editar.iconbitmap(logo)

			Label(editar,text='Nombre ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=20)
			nombre2323=Entry(editar,textvariable=StringVar(editar,nombre_cliente_new),relief='sunken',font='Helvetica 12',fg='black',bd=10)
			nombre2323.place(x=140,y=20)
			nombre2323.focus()

			Label(editar,text='Apellido',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=80)
			apellido_2323=Entry(editar,textvariable=StringVar(editar,apellido_cliente_new),relief='sunken',font='Helvetica 12',fg='black',bd=10)
			apellido_2323.place(x=140,y=80)
			
			Label(editar,text='Cedula',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=140)
			cedula__CTN=Entry(editar,textvariable=IntVar(editar,cedula_cliente_old),relief='sunken',font='Helvetica 12',bd=10,fg='black',state='readonly')
			cedula__CTN.place(x=140,y=140)

			Label(editar,text='Direccion',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=200)
			direccion__CTN=Entry(editar,textvariable=StringVar(editar,direccion_cliente_new),relief='sunken',font='Helvetica 12',bd=10,fg='black')
			direccion__CTN.place(x=140,y=200)

			Label(editar,text='Telefono',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=260)
			telefono__CTN=Entry(editar,textvariable=IntVar(editar,telefono_cliente_new),relief='sunken',font='Helvetica 12',bd=10,fg='black')
			telefono__CTN.place(x=140,y=260)

			Button(editar,text='Guardar',cursor='hand2',font='Helvetica 12',fg='black',bd=10,relief='raised',width=42,command=lambda:editar_cliente_CTN(nombre2323.get(),apellido_2323.get(),direccion__CTN.get(),telefono__CTN.get(),cedula_cliente_old)).place(x=0,y=305)


			def editar_cliente_CTN(nuevo_nombre,nuevo_apellido,nueva_direccion,nuevo_telefono,cedula):
				query='UPDATE CLIENTES SET NOMBRE_CLIENTE=?,APELLIDO_CLIENTE=?,DIRECCION_CLIENTE=?,TELEFONO_CLIENTE=? WHERE CEDULA_CLIENTE=?'
				datos=nuevo_nombre,nuevo_apellido,nueva_direccion,nuevo_telefono,cedula
				run_query(query,(datos))
				leer_todo_CTN5()
				editar.destroy()

		else:
			messagebox.showerror('BBDD','No ha seleccionado ningun Cliente',parent=CTN)

	







	NOMBRE=Entry(CTN,font='Helvetica 12',bd=7,relief='sunken',textvariable=nombre_cliente_CTN)
	NOMBRE.grid(row=2,column=0,sticky='NSEW',columnspan=5)
	NOMBRE.focus()

	CTN.columnconfigure(0,weight=1)

	rifc=Entry(CTN,font='Helvetica 12',bd=7,relief='sunken',textvariable=apellido_cliente_CTN)
	rifc.grid(row=5,column=0,sticky='NSEW',columnspan=5)

	

	tel=Entry(CTN,font='Helvetica 12',bd=7,relief='sunken',textvariable=cedula_cliente_CTN)
	tel.grid(row=7,column=0,sticky='NSEW',columnspan=5)

	direc=Entry(CTN,font='Helvetica 12',bd=7,relief='sunken',textvariable=direccion_cliente_CTN)
	direc.grid(row=9,column=0,sticky='NSEW',columnspan=5)

	direct=Entry(CTN,font='Helvetica 12',bd=7,relief='sunken',textvariable=telefono_cliente_CTN)
	direct.grid(row=11,column=0,sticky='NSEW',columnspan=5)
	
#--------------------------------LABEL-----------------------------------

	Label(CTN,bg='#b6bdff').grid(row=5,column=6,padx=25,pady=10)
	Label(CTN,bg='#b6bdff').grid(row=2,column=6,padx=25,pady=10)
	Label(CTN,bg='#b6bdff').grid(row=7,column=6,padx=25,pady=10)
	Label(CTN,bg='#b6bdff').grid(row=9,column=6,padx=25,pady=10)
	Label(CTN,bg='#b6bdff').grid(row=11,column=6,padx=25,pady=10)


	

	identificadorL=Label(CTN,text='Nombre',font='Helvetica 12',bg='#b6bdff')
	identificadorL.grid(row=1,column=0,pady=10,sticky='W',padx=120)

	CTN.rowconfigure(0,weight=1)
	
	CTN.rowconfigure(12,weight=2)



	nombre_descuentoL=Label(CTN,text='Apellido',font='Helvetica 12',bg='#b6bdff')
	nombre_descuentoL.grid(row=4,column=0,sticky='w',pady=10,padx=120)


	porcentanjeL=Label(CTN,text='Cedula',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL.grid(row=6,column=0,sticky='w',pady=10,padx=120)


	porcentanjeL2=Label(CTN,text='Direccion',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL2.grid(row=8,column=0,sticky='w',pady=10,padx=120)
	
	porcentanjeL2=Label(CTN,text='Telefono',font='Helvetica 12',bg='#b6bdff')
	porcentanjeL2.grid(row=10,column=0,sticky='w',pady=10,padx=120)
	
	botonsitos=Frame(CTN,bg='#b6bdff')
	botonsitos.grid(row=13,column=0,sticky='SEW',columnspan=7)
	
	Button(botonsitos,text='Agregar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=agregar_CTN).grid(row=0,column=1,sticky='W')
	Button(botonsitos,text='Editar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=ventana_editar_cliente_CTN).grid(row=0,column=2,sticky='W',padx=5)
	Button(botonsitos,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=comprobacion_de_borrar_CTN).grid(row=0,column=3,sticky='W')

#---------------------------

	
	
	CTN.columnconfigure(8,weight=20)

	frame_lista_pro=Frame(CTN)
	frame_lista_pro.grid(row=0,column=8,sticky='NSEW',rowspan=14,columnspan=4)
	style2 = ttk.Style()
	style2.configure("Treeview", font=('Helvetica', 10))
	

	lista1CTN=ttk.Treeview(frame_lista_pro,style="Treeview",columns=[f"#{n}" for n in range(1, 5)])
	lista1CTN.pack(expand=1,fill=BOTH)
	lista1CTN.grid(row=0,column=0,sticky='NSEW',rowspan=8)

	frame_lista_pro.rowconfigure(0,weight=5)
	frame_lista_pro.columnconfigure(0,weight=5)
	CTN.columnconfigure(4,weight=5)
	

	scoll=Scrollbar(frame_lista_pro,command=lista1CTN.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=0,column=1,sticky='NSEW')

	lista1CTN.config(yscrollcommand=scoll.set)

	lista1CTN.heading('#0',text='Nombre',anchor=CENTER)
	lista1CTN.heading('#1',text='Cedula',anchor=CENTER)
	lista1CTN.heading('#2',text='Direccion',anchor=CENTER)
	lista1CTN.heading('#3',text='Telefono',anchor=CENTER)
	lista1CTN.heading('#4',text='Fecha',anchor=CENTER)

	lista1CTN.column("#0",minwidth=100, width = 200)
	lista1CTN.column("#1",minwidth=70, width = 80 )
	lista1CTN.column("#2",minwidth=70, width = 162 )
	lista1CTN.column("#3",minwidth=70, width = 90 )
	lista1CTN.column("#4",minwidth=70, width = 80 )





	
	leer_todo_CTN5()

	def ventas():
		pass
	ven.configure(bg='#b6bdff')


	def buscar_venta_en_V():
		if Buscar_venta_VEN.get()=='':
			leer_todo_VEN()
			return


		record=lista1v.get_children()
		
		for element in record:
			lista1v.delete(element)
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 ORDER BY(ID_VENTAS)DESC")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:

			A=str(usuarios[0])
			B=str(usuarios[1])
			r=A.startswith(Buscar_venta_VEN.get())
			k=B.startswith(Buscar_venta_VEN.get())
			f=usuarios[8].startswith(Buscar_venta_VEN.get())
			if r==1 or k==1 or f==1:
				a1=round(usuarios[2],2)
				a2=round(usuarios[3],2)
				a3=round(usuarios[4],2)
				a4=round(usuarios[5],2)
				a5=round(usuarios[7],2)
				a6=round(usuarios[6],2)
				lista1v.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],a1,a2,a3,a4,a5,a6))
			
		miconexion.commit()



	def leer_todo_VEN():
		record=lista1v.get_children()
		for element in record:
			lista1v.delete(element)
    
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		
		micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 ORDER BY(ID_VENTAS)DESC")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			a1=round(usuarios[2],2)
			a2=round(usuarios[3],2)

			b1=round(usuarios[4],2)
			b2=round(usuarios[5],2)

			c1=round(usuarios[6],2)
			c2=round(usuarios[7],2)


			lista1v.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],a1,a2,b1,b2,c2,c1))
			

	def Detalles_VEN(event):
		try:
			id_ventas=lista1v.item(lista1v.selection())['text']
			cedula_cliente=lista1v.item(lista1v.selection())['values'][0]
			sub_total_D=lista1v.item(lista1v.selection())['values'][1]
			sub_total_B=lista1v.item(lista1v.selection())['values'][2]
			iva_D=lista1v.item(lista1v.selection())['values'][3]
			iva_B=lista1v.item(lista1v.selection())['values'][4]
			total_D=lista1v.item(lista1v.selection())['values'][5]
			total_B=lista1v.item(lista1v.selection())['values'][6]


		except IndexError:
			pass
			return
		HORA=StringVar()
		FECHA=StringVar()
		TASA=DoubleVar()
		vpv=Toplevel(ven)
		vpv.title('Detalles')
		vpv.geometry('700x532')
		vpv.iconbitmap(logo)
		vpv.resizable(0,0)
		vpv.configure(bg='#b6bdff')
		tab_control = ttk.Notebook(vpv)
		hija=Frame(tab_control)
		ventana=Frame(tab_control)
		identifi=StringVar()

		tab_control.add(hija, text='Detalles')
		#tab_control.add(ventana, text='Mas')
		tab_control.pack(expand=1, fill='both')
		hija.config(bg='#b6bdff')
		ventana.config(bg='#b6bdff')


		def ver_productos_de_la_venta_VPV():
			record=lista_pV.get_children()
			for element in record:
				lista_pV.delete(element)
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=id_ventas,cedula_cliente
			micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:

				ad=round(usuarios[10],2)
				asd=round(usuarios[11],2)
				lista_pV.insert('',0,text=usuarios[3],values=(usuarios[4],usuarios[5],usuarios[7],ad,asd))
				

		def ver_fecha_y_hora_VPV():
			record=lista_pV.get_children()
			for element in record:
				lista_pV.delete(element)
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND ID_VENTAS=? ORDER BY(ID_VENTAS)DESC",(id_ventas, ))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				a=str(usuarios[8])
				b=str(usuarios[9])
				FECHA.set(a)
				HORA.set(b)
				TASA.set(usuarios[10])

				sub_total_BB=usuarios[3]
				sub_total_DD=usuarios[2]
				iva_BB=usuarios[5]
				iva_DD=usuarios[4]
				total_BB=usuarios[6]
				total_DD=usuarios[7]

				cajero=usuarios[12]
				caja=usuarios[13]

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(cedula_cliente, ))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				nombre_cliente=usuarios[0]+' '+usuarios[1]


			limpiar_cuadros_Text_VPV()
			agregar_a_suma_VPV(TASA.get(),nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD,cajero,caja)



	
		def limpiar_cuadros_Text_VPV():
			tasa.configure(state='normal')
			tasa.delete('1.0', END)
			tasa.configure(state='disabled')

			cliente_tex.configure(state='normal')
			cliente_tex.delete('1.0',END)
			cliente_tex.configure(state='disabled')

			Total_B22.configure(state='normal')
			Total_B22.delete('1.0', END)
			Total_B22.configure(state='disabled')

			Total_D22.configure(state='normal')
			Total_D22.delete('1.0',END)
			Total_D22.configure(state='disabled')

			Total_D33.configure(state='normal')
			Total_D33.delete('1.0',END)
			Total_D33.configure(state='disabled')
	


		def agregar_a_suma_VPV(tasad,nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD,cajero,caja):
	

			tasa.configure(state='normal')
			tasa_f = '{:,}'.format(round(tasad,2))
			tasa.insert(END, tasa_f)
			tasa.configure(state='disabled')

			cliente_tex.configure(state='normal')
			cliente_tex.insert(END,nombre_cliente)
			cliente_tex.configure(state='disabled')



			Total_B22.configure(state='normal')
			dinero = '{:,}'.format(round(sub_total_BB,2))
			dinero2 = '{:,}'.format(round(sub_total_DD,2))
			a=dinero,'(',dinero2,')'
			Total_B22.insert(END, a)
			Total_B22.configure(state='disabled')



			Total_D22.configure(state='normal')
			dinero5 = '{:,}'.format(round(iva_BB,2))
			dinero6 = '{:,}'.format(round(iva_DD,2))
			c=dinero5,'(',dinero6,')'
			Total_D22.insert(END,c)
			Total_D22.configure(state='disabled')


			Total_D33.configure(state='normal')
			dinero3 = '{:,}'.format(round(total_BB,2))
			dinero4 = '{:,}'.format(round(total_DD,2))
			b=dinero3,'(',dinero4,')'
			Total_D33.insert(END,b)
			Total_D33.configure(state='disabled')

			Label(hija,text=FECHA.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=0)

			Label(hija,text=HORA.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=40)



			cajero_la.config(text=cajero)
			caja_la.config(text=caja)
			return

		nombre_pdf_ventas_detal=StringVar()
		def hacer_pdf_ventas_detalles():
			
			

			total_pdf_D=DoubleVar()
			total_pdf_B=DoubleVar()

			iva_pdf_D=DoubleVar()
			iva_pdf_B=DoubleVar()

			sub_total_pdf_D=DoubleVar()
			sub_total_pdf_B=DoubleVar()

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM VENTAS WHERE ID_VENTAS=?",(id_ventas, ))
			B=micursor.fetchall()
			for g in B:
				if g[0]<10:
					numero_de_factura='00000'+str(g[0])
				elif g[0]<100:
					numero_de_factura='0000'+str(g[0])

				elif g[0]<1000:
					numero_de_factura='000'+str(g[0])

				elif g[0]<10000:
					numero_de_factura='00'+str(g[0])

				elif g[0]<100000:
					numero_de_factura='0'+str(g[0])

				else:
					numero_de_factura=str(g[0])





			a0='Factura '+numero_de_factura+'.pdf'
			c=canvas.Canvas(a0,pagesize=letter)


			text = c.beginText(200, 730)
			text.setFont("Helvetica", 16)
			text.textLines(" .         INVERSIONES\nWILLIAMS DIOKSELY, C.A\n.       RIF.J-41238423-6")
			c.drawText(text)



			text2 = c.beginText(155, 680)
			text2.setFont("Helvetica", 10)
			text2.textLines("Viveres en General, Licores Nocionales e importados, Hortalizas,\n.                        Legumbres,carniceria en General\n.             Vda. 4. Casa No 10. Urb. Hacienda del Medio\n.                                Telefono: (0426) 4134562\n.                           Tucupita - Edo.Delta Amacuro")
			c.drawText(text2)


			text3 = c.beginText(480, 700)
			text3.setFont("Helvetica", 14)
			


			text3.textLines("Factura\nNo  "+numero_de_factura+"\n\nControl\nNo  "+numero_de_factura)
			c.drawText(text3)

			text4 = c.beginText(100, 590)
			text4.setFont("Helvetica", 12)
			micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(cedula_cliente, ))
			A=micursor.fetchall()
			for n in A:
				nombre=n[0]+' '+n[1]
				direccion=n[3]
				telefono=n[4]
			text4.textLines("Fecha: 19 / 02 / 21\nNombre o Razon Social: "+nombre+"\nDireccion: "+direccion+"\nC.I.: "+str(cedula_cliente)+"\nTelf: "+telefono)
			c.drawText(text4)

			def grouper2(iterable, n):
				args = [iter(iterable)] * n
				return itertools.zip_longest(*args)
			def export_to_pdf2(data):
				print(data,'data')
				w, h = A4
				max_rows_per_page = 45
				    # Margin.
				x_offset = 100
				y_offset = 350
				    # Space between rows.
				padding = 15
				    
				xlist = [x + x_offset for x in [0,50,200,270,340,450]]
				ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
				contador=0
				for rows in grouper2(data, max_rows_per_page):
					rows = tuple(filter(bool, rows))
					c.grid(xlist, ylist[:len(rows) + 1])
					for y, row in zip(ylist[:-1], rows):
						for x, cell in zip(xlist, row):
							contador=contador+1
							c.drawString(x+2, y - padding + 3, str(cell))
							print(contador,hola*5)
							if contador==hola*5:
								text5 = c.beginText(x-50, y-50)
								text5.setFont("Helvetica", 12)
								text5.textLines("DESCUENTO %: 0%\n\nSUB-TOTAL: "+str(sub_total_pdf_B.get())+"\nI.V.A.: "+str(iva_pdf_B.get())+"\nTOTAL A PAGAR: "+str(total_pdf_B.get()))
								c.drawText(text5)
					c.showPage()

				c.save()
			data = [('CANT.',"DESCRIPCION", "P.UNIT", "Alic.%", "TOTAL Bs.")]

			contador=0
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=id_ventas,cedula_cliente
			micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
			a=micursor.fetchall()
			for g in a:
				contador=contador+1

				
				total_pdf_B.set(g[9]+total_pdf_B.get())

				sub_total_pdf_B.set(g[12]+sub_total_pdf_B.get())


			iva_pdf_B.set(round(total_pdf_B.get()-sub_total_pdf_B.get(),2))

			total_pdf_B.set(round(total_pdf_B.get(),2))

			sub_total_pdf_B.set(round(sub_total_pdf_B.get(),2))



			datos=id_ventas,cedula_cliente
			micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
			C=micursor.fetchall()
			for i in C:
				b=i[0]   
				hola=contador
				print(str(i[5]),str(i[4]),str(i[9]),str(i[6]),str(i[11]))
				data.append((str(i[5]),str(i[4]),str(round(i[9])),str(round(i[6],2)),str(round(i[11],2))))
			export_to_pdf2(data)
			messagebox.showinfo('BBDD','el Pdf de la Venta No {} fue creado con exito'.format(id_ventas),parent=hija)

		style = ttk.Style()
		style.configure("Treeview", font=('Helvetica', 10))

		lista_pV=ttk.Treeview(hija,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 6)])
		lista_pV.place(x=0,y=160)

		scoll=Scrollbar(hija,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=680,y=185,height=320)
		lista_pV.config(yscrollcommand=scoll.set)

		lista_pV.heading('#0',text='Codigo',anchor=CENTER)
		lista_pV.heading('#1',text='Productos',anchor=CENTER)
		lista_pV.heading('#2',text='Cantidad',anchor=CENTER)
		lista_pV.heading('#3',text='Unidad',anchor=CENTER)
		lista_pV.heading('#4',text='Precio $',anchor=CENTER)
		lista_pV.heading('#5',text='Precio Bs.S',anchor=CENTER)

		lista_pV.column("#0",minwidth=100, width = 100)
		lista_pV.column("#1",minwidth=70, width = 220 )
		lista_pV.column("#2",minwidth=70, width = 60 )
		lista_pV.column("#3",minwidth=70, width = 50 )
		lista_pV.column("#4",minwidth=70, width = 110 )
		lista_pV.column("#5",minwidth=70, width = 160 )

		
		
		Label(hija,text='Fecha',font='Helvetica 12',bg='#b6bdff').place(x=0,y=0)


		Label(hija,text='Hora:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=40)


		Label(hija,text='Tasa:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=80)

		tasa=Text(hija,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
		tasa.place(x=55,y=80)

		Label(hija,text='Cliente:',bg='#b6bdff',font='Helvetica 12').place(x=0,y=120)

		cliente_tex=Text(hija,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
		cliente_tex.place(x=55,y=120)

		Label(hija,text='Cajero:',font='Helvetica 12',bg='#b6bdff').place(x=160,y=0)
		cajero_la=Label(hija,text='Elvin 6',font='Helvetica 12',bg='#b6bdff')
		cajero_la.place(x=220,y=0)

		Label(hija,text='Caja:',font='Helvetica 12',bg='#b6bdff').place(x=160,y=40)
		caja_la=Label(hija,text='Elvin 6',font='Helvetica 12',bg='#b6bdff')
		caja_la.place(x=220,y=40)


		Button(hija,text='PDF',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=hacer_pdf_ventas_detalles).place(x=240,y=120)

		totales=Frame(hija)
		totales.configure(bg='#b8d3ff',width=370,height=157)
		totales.place(x=343,y=0)

		Label(totales,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=20)
		Label(totales,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=60)
		Label(totales,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=100)


		Total_B22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_B22.place(x=115,y=21)

		Total_D22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D22.place(x=115,y=62)

		Total_D33=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D33.place(x=115,y=103)
		ver_fecha_y_hora_VPV()
		ver_productos_de_la_venta_VPV()
	

#--------------------------------------------------------------------------


	def Reportes_VEN():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		rp=Toplevel(ven)
		rp.geometry('730x532')
		rp.title('Reportes')
		rp.iconbitmap(logo)
		rp.resizable(0,0)
		rp.configure(bg='#b6bdff')
		tab_control = ttk.Notebook(rp)
		hija=Frame(tab_control)
		ventana=Frame(tab_control)


		tab_control.add(hija, text='Fechas')
		#tab_control.add(ventana, text='Periodos')
		tab_control.pack(expand=1, fill='both')
		hija.config(bg='#b6bdff')
		ventana.config(bg='#b6bdff')

		


		def limpiar_suma_rp():
			Total_B22.configure(state='normal')
			Total_B22.delete('1.0', END)
			Total_B22.configure(state='disabled')

			Total_D22.configure(state='normal')
			Total_D22.delete('1.0',END)
			Total_D22.configure(state='disabled')

			Total_D33.configure(state='normal')
			Total_D33.delete('1.0',END)
			Total_D33.configure(state='disabled')


		def sumar_ventas_encontradas_rp(sub_total_D,sub_total_B,iva_D,iva_B,total_D,total_B):

			a1=round(sub_total_B,2)
			a2=round(sub_total_D,2)
			sub_D = '{:,}'.format(a1)
			sub_B = '{:,}'.format(a2)
			a=sub_D,'(',sub_B,')'

			Total_B22.configure(state='normal')
			Total_B22.insert(END,a)
			Total_B22.configure(state='disabled')

#----------
			c1=round(iva_B,2)
			c2=round(iva_D,2)
			dinero5 = '{:,}'.format(c1)
			dinero6 = '{:,}'.format(c2)
			c=dinero5,'(',dinero6,')'

			Total_D22.configure(state='normal')
			Total_D22.insert(END,c)
			Total_D22.configure(state='disabled')

#-----------
			b1=round(total_B,2)
			b2=round(total_D,2)
			dinero = '{:,}'.format(b1)
			dinero2 = '{:,}'.format(b2)
			b=dinero,'(',dinero2,')'

			Total_D33.configure(state='normal')
			Total_D33.insert(END,b)
			Total_D33.configure(state='disabled')


		def Detalles_VEN2(event):
			try:
				id_ventas=lista_fV.item(lista_fV.selection())['text']
				cedula_cliente=lista_fV.item(lista_fV.selection())['values'][0]


			except IndexError:
				pass
				return
			HORA=StringVar()
			FECHA=StringVar()
			TASA=DoubleVar()
			vpv=Toplevel(hija)
			vpv.title('Detalles')
			vpv.geometry('700x532')
			vpv.iconbitmap(logo)
			vpv.resizable(0,0)
			vpv.configure(bg='#b6bdff')
			tab_control = ttk.Notebook(vpv)
			hija2=Frame(tab_control)
			identifi=StringVar()
			tab_control.add(hija2, text='Detalles')
			tab_control.pack(expand=1, fill='both')
			hija2.config(bg='#b6bdff')



			def hacer_pdf_ventas_detalles():
			

				total_pdf_D=DoubleVar()
				total_pdf_B=DoubleVar()

				iva_pdf_D=DoubleVar()
				iva_pdf_B=DoubleVar()

				sub_total_pdf_D=DoubleVar()
				sub_total_pdf_B=DoubleVar()

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM VENTAS WHERE ID_VENTAS=?",(id_ventas, ))
				B=micursor.fetchall()
				for g in B:
					if g[0]<10:
						numero_de_factura='00000'+str(g[0])
					elif g[0]<100:
						numero_de_factura='0000'+str(g[0])

					elif g[0]<1000:
						numero_de_factura='000'+str(g[0])

					elif g[0]<10000:
						numero_de_factura='00'+str(g[0])

					elif g[0]<100000:
						numero_de_factura='0'+str(g[0])

					else:
						numero_de_factura=str(g[0])





				a0='Factura '+numero_de_factura+'.pdf'
				c=canvas.Canvas(a0,pagesize=letter)


				text = c.beginText(200, 730)
				text.setFont("Helvetica", 16)
				text.textLines(" .         INVERSIONES\nWILLIAMS DIOKSELY, C.A\n.       RIF.J-41238423-6")
				c.drawText(text)



				text2 = c.beginText(155, 680)
				text2.setFont("Helvetica", 10)
				text2.textLines("Viveres en General, Licores Nocionales e importados, Hortalizas,\n.                        Legumbres,carniceria en General\n.             Vda. 4. Casa No 10. Urb. Hacienda del Medio\n.                                Telefono: (0426) 4134562\n.                           Tucupita - Edo.Delta Amacuro")
				c.drawText(text2)


				text3 = c.beginText(480, 700)
				text3.setFont("Helvetica", 14)
				


				text3.textLines("Factura\nNo  "+numero_de_factura+"\n\nControl\nNo  "+numero_de_factura)
				c.drawText(text3)

				text4 = c.beginText(100, 590)
				text4.setFont("Helvetica", 12)
				micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(cedula_cliente, ))
				A=micursor.fetchall()
				for n in A:
					nombre=n[0]+' '+n[1]
					direccion=n[3]
					telefono=n[4]
				text4.textLines("Fecha: 19 / 02 / 21\nNombre o Razon Social: "+nombre+"\nDireccion: "+direccion+"\nC.I.: "+str(cedula_cliente)+"\nTelf: "+telefono)
				c.drawText(text4)


				def grouper2(iterable, n):
					args = [iter(iterable)] * n
					return itertools.zip_longest(*args)
				def export_to_pdf2(data):
					print(data,'datassss')
					w, h = A4
					max_rows_per_page = 45
					    # Margin.
					x_offset = 100
					y_offset = 350
					    # Space between rows.
					padding = 15
					    
					xlist = [x + x_offset for x in [0,50,200,270,340,450]]
					ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
					contador=0
					for rows in grouper2(data, max_rows_per_page):
						rows = tuple(filter(bool, rows))
						c.grid(xlist, ylist[:len(rows) + 1])
						for y, row in zip(ylist[:-1], rows):
							for x, cell in zip(xlist, row):
								contador=contador+1
								c.drawString(x+2, y - padding + 3, str(cell))
								print(contador,hola*5)
								if contador==hola*5:
									text5 = c.beginText(x-50, y-50)
									text5.setFont("Helvetica", 12)
									text5.textLines("DESCUENTO %: 0%\n\nSUB-TOTAL: "+str(sub_total_pdf_B.get())+"\nI.V.A.: "+str(iva_pdf_B.get())+"\nTOTAL A PAGAR: "+str(total_pdf_B.get()))
									c.drawText(text5)
						c.showPage()

					c.save()
				data = [('CANT.',"DESCRIPCION", "P.UNIT", "Alic.%", "TOTAL Bs.")]

				contador=0
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=id_ventas,cedula_cliente
				micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
				a=micursor.fetchall()
				for g in a:
					contador=contador+1

					
					total_pdf_B.set(g[9]+total_pdf_B.get())

					sub_total_pdf_B.set(g[12]+sub_total_pdf_B.get())


				iva_pdf_B.set(round(total_pdf_B.get()-sub_total_pdf_B.get(),2))

				total_pdf_B.set(round(total_pdf_B.get(),2))

				sub_total_pdf_B.set(round(sub_total_pdf_B.get(),2))



				datos=id_ventas,cedula_cliente
				micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
				C=micursor.fetchall()
				for i in C:

					b=i[0]	
						   
					hola=contador
						

					print(str(i[5]),str(i[4]),str(i[9]),str(16),str(i[11]))
					data.append((str(i[5]),str(i[4]),str(i[9]),'16',str(i[11])))
				export_to_pdf2(data)

				messagebox.showinfo('BBDD','el Pdf de la Venta No {} fue creado con exito'.format(id_ventas),parent=hija2)

















			def ver_productos_de_la_venta_VPV():
				record=lista_pV.get_children()
				for element in record:
					lista_pV.delete(element)
    
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=id_ventas,cedula_cliente
				micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					a=round(usuarios[11],2)
					b=round(usuarios[10],2)
					lista_pV.insert('',0,text=usuarios[3],values=(usuarios[4],usuarios[5],usuarios[7],b,a))
						

			def ver_fecha_y_hora_VPV():
				record=lista_pV.get_children()
				for element in record:
					lista_pV.delete(element)
    
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND ID_VENTAS=? ORDER BY(ID_VENTAS)DESC",(id_ventas, ))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					a=str(usuarios[8])
					b=str(usuarios[9])
					FECHA.set(a)
					HORA.set(b)
					TASA.set(usuarios[10])

					sub_total_BB=usuarios[3]
					sub_total_DD=usuarios[2]
					iva_BB=usuarios[5]
					iva_DD=usuarios[4]
					total_BB=usuarios[6]
					total_DD=usuarios[7]

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(cedula_cliente, ))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					nombre_cliente=usuarios[0]+' '+usuarios[1]


				limpiar_cuadros_Text_VPV()
				agregar_a_suma_VPV(TASA.get(),nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD)



	
			def limpiar_cuadros_Text_VPV():
				tasa.configure(state='normal')
				tasa.delete('1.0', END)
				tasa.configure(state='disabled')

				cliente_tex.configure(state='normal')
				cliente_tex.delete('1.0',END)
				cliente_tex.configure(state='disabled')

				Total_B22.configure(state='normal')
				Total_B22.delete('1.0', END)
				Total_B22.configure(state='disabled')

				Total_D22.configure(state='normal')
				Total_D22.delete('1.0',END)
				Total_D22.configure(state='disabled')

				Total_D33.configure(state='normal')
				Total_D33.delete('1.0',END)
				Total_D33.configure(state='disabled')
			


			def agregar_a_suma_VPV(tasad,nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD):
			

				tasa.configure(state='normal')
				tasa_f = '{:,}'.format(round(tasad,2))
				tasa.insert(END, tasa_f)
				tasa.configure(state='disabled')

				cliente_tex.configure(state='normal')
				cliente_tex.insert(END,nombre_cliente)
				cliente_tex.configure(state='disabled')



				Total_B22.configure(state='normal')
				dinero = '{:,}'.format(round(sub_total_BB,2))
				dinero2 = '{:,}'.format(round(sub_total_DD,2))
				a=dinero,'(',dinero2,')'
				Total_B22.insert(END, a)
				Total_B22.configure(state='disabled')



				Total_D22.configure(state='normal')
				dinero5 = '{:,}'.format(round(iva_BB,2))
				dinero6 = '{:,}'.format(round(iva_DD,2))
				c=dinero5,'(',dinero6,')'
				Total_D22.insert(END,c)
				Total_D22.configure(state='disabled')


				Total_D33.configure(state='normal')
				dinero3 = '{:,}'.format(round(total_BB,2))
				dinero4 = '{:,}'.format(round(total_DD,2))
				b=dinero3,'(',dinero4,')'
				Total_D33.insert(END,b)
				Total_D33.configure(state='disabled')

				Label(hija2,text=FECHA.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=0)

				Label(hija2,text=HORA.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=40)

				return



			style = ttk.Style()
			style.configure("Treeview", font=('Helvetica', 10))

			lista_pV=ttk.Treeview(hija2,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 6)])
			lista_pV.place(x=0,y=160)

			scoll=Scrollbar(hija2,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll.place(x=680,y=185,height=320)
			lista_pV.config(yscrollcommand=scoll.set)

			lista_pV.heading('#0',text='Codigo',anchor=CENTER)
			lista_pV.heading('#1',text='Productos',anchor=CENTER)
			lista_pV.heading('#2',text='Cantidad',anchor=CENTER)
			lista_pV.heading('#3',text='Unidad',anchor=CENTER)
			lista_pV.heading('#4',text='Precio $',anchor=CENTER)
			lista_pV.heading('#5',text='Precio Bs.S',anchor=CENTER)

			lista_pV.column("#0",minwidth=100, width = 100)
			lista_pV.column("#1",minwidth=70, width = 220 )
			lista_pV.column("#2",minwidth=70, width = 60 )
			lista_pV.column("#3",minwidth=70, width = 50 )
			lista_pV.column("#4",minwidth=70, width = 110 )
			lista_pV.column("#5",minwidth=70, width = 160 )

				

			Label(hija2,text='Fecha',font='Helvetica 12',bg='#b6bdff').place(x=0,y=0)


			Label(hija2,text='Hora:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=40)


			Label(hija2,text='Tasa:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=80)

			tasa=Text(hija2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
			tasa.place(x=55,y=80)

			Label(hija2,text='Cliente:',bg='#b6bdff',font='Helvetica 12').place(x=0,y=120)

			cliente_tex=Text(hija2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
			cliente_tex.place(x=55,y=120)


			totales=Frame(hija2)
			totales.configure(bg='#b8d3ff',width=370,height=157)
			totales.place(x=343,y=0)

			Label(totales,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=20)
			Label(totales,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=60)
			Label(totales,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=100)

			Total_B22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
			Total_B22.place(x=115,y=21)

			Total_D22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
			Total_D22.place(x=115,y=62)

			Total_D33=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
			Total_D33.place(x=115,y=103)
			ver_fecha_y_hora_VPV()
			ver_productos_de_la_venta_VPV()


			Button(hija2,text='PDF',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=hacer_pdf_ventas_detalles).place(x=240,y=120)




#-----------------------------------------------------------------
			
		def limpiar2(event):
			limpiar_suma_rp()
				
	
			sub_total_iva_B_rp.set(0)
			sub_total_iva_D_rp.set(0)
			total_iva_B_rp.set(0)
			total_iva_D_rp.set(0)
			total_D_rp.set(0)
			total_B_rp.set(0)

			
			record=lista_fV.get_children()
			for element in record:
				lista_fV.delete(element)

		def filtrar_ventas_dma_rp(event):

			if mess.get()=='Enero':
				me=1
			elif mess.get()=='Febrero':
				me=2
			elif mess.get()=='Marzo':
				me=3
			elif mess.get()=='Abril':
				me=4
			elif mess.get()=='Mayo':
				me=5
			elif mess.get()=='Junio':
				me=6
			elif mess.get()=='Julio':
				me=7
			elif mess.get()=='Agosto':
				me=8
			elif mess.get()=='Septiembre':
				me=9
			elif mess.get()=='Octubre':
				me=10
			elif mess.get()=='Noviembre':
				me=11
			elif mess.get()=='Diciembre':
				me=12


			record=lista_fV.get_children()
		
			for element in record:
				lista_fV.delete(element)

			if days.get()=='Todos' and mess.get()=='Todos':
				


				for m in range(1,13):
					
					mes=str(m)
					if m<10:
						mes='0'+mes

					for d in range(1,32):
						dia=str(d)
						if d<10:
							dia='0'+dia
						d=int(añoss.get())-2000


					
						fechi=dia+'/'+mes+'/'+str(d)




						miconexion=sqlite3.connect('SISTEMA_LUMINA')
						micursor=miconexion.cursor()
						micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 ORDER BY(ID_VENTAS)DESC")
						elusuario=micursor.fetchall()
						for usuarios in elusuario:
							r=usuarios[8].startswith(fechi)

							if r==1:
								lista_fV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))
								sub_total_iva_B_rp.set(usuarios[3]+sub_total_iva_B_rp.get())
								sub_total_iva_D_rp.set(usuarios[2]+sub_total_iva_D_rp.get())

								total_iva_B_rp.set(usuarios[5]+total_iva_B_rp.get())
								total_iva_D_rp.set(usuarios[4]+total_iva_D_rp.get())


								total_D_rp.set(usuarios[7]+total_D_rp.get())
								total_B_rp.set(usuarios[6]+total_B_rp.get())


							miconexion.commit()
							limpiar_suma_rp()
							sumar_ventas_encontradas_rp(sub_total_iva_D_rp.get(),sub_total_iva_B_rp.get(),total_iva_D_rp.get(),total_iva_B_rp.get(),total_D_rp.get(),total_B_rp.get())
				
	
				sub_total_iva_B_rp.set(0)
				sub_total_iva_D_rp.set(0)
				total_iva_B_rp.set(0)
				total_iva_D_rp.set(0)
				total_D_rp.set(0)
				total_B_rp.set(0)

				

				return

			if days.get()=='Todos':
				for i in range(1,32):
					ve=str(me)
					di=str(i)
					

					c=ve

					if me<10:
						c='0'+ve


					x=days.get()


					if i < 10:
						di='0'+di

					d=int(añoss.get())-2000


					
					fechi=di+'/'+c+'/'+str(d)
					


					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 ORDER BY(ID_VENTAS)DESC")
					elusuario=micursor.fetchall()
					for usuarios in elusuario:
						r=usuarios[8].startswith(fechi)

						if r==1:
							lista_fV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))
							sub_total_iva_B_rp.set(usuarios[3]+sub_total_iva_B_rp.get())
							sub_total_iva_D_rp.set(usuarios[2]+sub_total_iva_D_rp.get())

							total_iva_B_rp.set(usuarios[5]+total_iva_B_rp.get())
							total_iva_D_rp.set(usuarios[4]+total_iva_D_rp.get())


							total_D_rp.set(usuarios[7]+total_D_rp.get())
							total_B_rp.set(usuarios[6]+total_B_rp.get())


						miconexion.commit()
						limpiar_suma_rp()
						sumar_ventas_encontradas_rp(sub_total_iva_D_rp.get(),sub_total_iva_B_rp.get(),total_iva_D_rp.get(),total_iva_B_rp.get(),total_D_rp.get(),total_B_rp.get())
			
			

				sub_total_iva_B_rp.set(0)
				sub_total_iva_D_rp.set(0)
				total_iva_B_rp.set(0)
				total_iva_D_rp.set(0)
				total_D_rp.set(0)
				total_B_rp.set(0)

				return




			if mess.get()=='Todos':

				for i in range(1,13):
					
					di=str(i)
					

	

					x=days.get()

					if int(days.get())<10:
						x='0'+days.get()



					if i < 10:
						di='0'+di

					d=int(añoss.get())-2000


					
					fechi=x+'/'+di+'/'+str(d)
					


					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 ORDER BY(ID_VENTAS)DESC")
					elusuario=micursor.fetchall()
					for usuarios in elusuario:
						r=usuarios[8].startswith(fechi)

						if r==1:
							lista_fV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))
							sub_total_iva_B_rp.set(usuarios[3]+sub_total_iva_B_rp.get())
							sub_total_iva_D_rp.set(usuarios[2]+sub_total_iva_D_rp.get())

							total_iva_B_rp.set(usuarios[5]+total_iva_B_rp.get())
							total_iva_D_rp.set(usuarios[4]+total_iva_D_rp.get())


							total_D_rp.set(usuarios[7]+total_D_rp.get())
							total_B_rp.set(usuarios[6]+total_B_rp.get())


						miconexion.commit()
						limpiar_suma_rp()
						sumar_ventas_encontradas_rp(sub_total_iva_D_rp.get(),sub_total_iva_B_rp.get(),total_iva_D_rp.get(),total_iva_B_rp.get(),total_D_rp.get(),total_B_rp.get())
			
			

				sub_total_iva_B_rp.set(0)
				sub_total_iva_D_rp.set(0)
				total_iva_B_rp.set(0)
				total_iva_D_rp.set(0)
				total_D_rp.set(0)
				total_B_rp.set(0)

				return




			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 ORDER BY(ID_VENTAS)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:

				ve=str(me)
				c=ve
				if me<10:
					c='0'+ve
				x=days.get()
				if int(days.get())<10:
					x='0'+days.get()

				d=int(añoss.get())-2000

				fechi=x+'/'+c+'/'+str(d)
				
				r=usuarios[8].startswith(fechi)
				if r==1:
					lista_fV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))
					sub_total_iva_B_rp.set(usuarios[3]+sub_total_iva_B_rp.get())
					sub_total_iva_D_rp.set(usuarios[2]+sub_total_iva_D_rp.get())

					total_iva_B_rp.set(usuarios[5]+total_iva_B_rp.get())
					total_iva_D_rp.set(usuarios[4]+total_iva_D_rp.get())


					total_D_rp.set(usuarios[7]+total_D_rp.get())
					total_B_rp.set(usuarios[6]+total_B_rp.get())


			miconexion.commit()
			limpiar_suma_rp()
			sumar_ventas_encontradas_rp(sub_total_iva_D_rp.get(),sub_total_iva_B_rp.get(),total_iva_D_rp.get(),total_iva_B_rp.get(),total_D_rp.get(),total_B_rp.get())
			
			

			sub_total_iva_B_rp.set(0)
			sub_total_iva_D_rp.set(0)
			total_iva_B_rp.set(0)
			total_iva_D_rp.set(0)
			total_D_rp.set(0)
			total_B_rp.set(0)


		def crear_pdf_ventas():

			PDF=Toplevel(hija)
			PDF.geometry('400x150')
			PDF.configure(bg='#b6bdff')
			PDF.iconbitmap(logo)
			PDF.resizable(0,0)
			nombre_PDF_producto.set('')
			Label(PDF,font='Helvetica 12',text='Nombre del PDF',bg='#b6bdff').place(x=100,y=20)


			ttt=Entry(PDF,font='Helvetica 12',bd=9,relief='sunken',textvariable=nombre_PDF_producto)
			ttt.place(x=40,y=50,width=240,height=41)
			ttt.focus()

			
			def dt(event):
				crear_pdf_ventas2()
				PDF.destroy()
				return

			ttt.bind('<Return>',dt)

			Button(PDF,font='Helvetica 12',bd=7,width=8,relief='raised',text='Aceptar',cursor='hand2',command=lambda:dt('1')).place(x=285,y=50)


		def crear_pdf_ventas2():
			total_pdf_D=DoubleVar()
			total_pdf_B=DoubleVar()

			sub_total_pdf_D=DoubleVar()
			sub_total_pdf_B=DoubleVar()

			iva_pdf_D=DoubleVar()
			iva_pdf_B=DoubleVar()

			contador_ven=0
			def grouper(iterable, n):
				args = [iter(iterable)] * n
				return itertools.zip_longest(*args)
			def export_to_pdf(data):

				dsds=nombre_PDF_producto.get()
				fdfd=dsds+'.pdf'
				c = canvas.Canvas(fdfd, pagesize=A4)
				w, h = A4
				max_rows_per_page = 45
			    # Margin.
				x_offset = 50
				y_offset = 50
			    # Space between rows.
				padding = 17
			    
				xlist = [x + x_offset for x in [0,70, 140, 200, 260, 350, 450, 540]]
				ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
				contador_ven2=0
				for rows in grouper(data, max_rows_per_page):
					rows = tuple(filter(bool, rows))
					c.grid(xlist, ylist[:len(rows) + 1])
					for y, row in zip(ylist[:-1], rows):
						for x, cell in zip(xlist, row):
							c.drawString(x + 2, y - padding + 3, str(cell))
							contador_ven2=contador_ven2+1
						if contador_ven2==contador_ven*7:
							text5 = c.beginText(x-100, y-50)
							text5.setFont("Helvetica", 12)
							text5.textLines(".\n\nSUB-TOTAL: "+str(round(iva_pdf_B.get(),2))+"\nI.V.A.: "+str(round(sub_total_pdf_B.get(),2))+"\nTOTAL A PAGAR: "+str(round(total_pdf_B.get(),2)))
							c.drawText(text5)
					c.showPage()

				c.save()
				sub_total_pdf_B.set(0)
				total_pdf_B.set(0)
				iva_pdf_B.set(0)




			if mess.get()=='Enero':
				me='01'
			elif mess.get()=='Febrero':
				me='02'
			elif mess.get()=='Marzo':
				me='03'
			elif mess.get()=='Abril':
				me='04'
			elif mess.get()=='Mayo':
				me='05'
			elif mess.get()=='Junio':
				me='06'
			elif mess.get()=='Julio':
				me='07'
			elif mess.get()=='Agosto':
				me='08'
			elif mess.get()=='Septiembre':
				me='09'
			elif mess.get()=='Octubre':
				me='10'
			elif mess.get()=='Noviembre':
				me='11'
			elif mess.get()=='Diciembre':
				me='12'
			elif mess.get()=='Todos':
				me='Todos'


			if days.get()=='Todos' and me=='Todos':
				d=int(añoss.get())-2000

				fechi=days.get()+'/'+me+'/'+str(d)
				data = [('CODIGO',"CLIENTE", "FECHA", "HORA", "SUB TOTAL", "IVA", "TOTAL")]

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0")
				A=micursor.fetchall()
				for i0 in A:
					yr=fechi.split('/')
					yr0=i0[8].split('/')

					if yr[2]==yr0[2]:
				
						contador_ven+=1
						a=round(i0[3],2)
						b=round(i0[5],2)
						g=round(i0[6],2)

						total_pdf_B.set(total_pdf_B.get()+i0[6])
						sub_total_pdf_B.set(sub_total_pdf_B.get()+i0[5])
						iva_pdf_B.set(iva_pdf_B.get()+i0[3])	

						a0=i0[0]
						a1=i0[1]
						a2=i0[8]
						data.append((a0,a1,a2,i0[9],a,b,g))


				export_to_pdf(data)

					
				messagebox.showinfo('BBDD','PDF de ventas creado con exito',parent=hija)
				return

			elif days.get()=='Todos':
				d=int(añoss.get())-2000

				fechi=days.get()+'/'+me+'/'+str(d)
				data = [('CODIGO',"CLIENTE", "FECHA", "HORA", "SUB TOTAL", "IVA", "TOTAL")]

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0")
				A=micursor.fetchall()
				for i0 in A:
					yr=fechi.split('/')
					yr0=i0[8].split('/')

					if yr[2]==yr0[2] and yr[1]==yr0[1]:
						contador_ven+=1
	
						a=round(i0[3],2)
						b=round(i0[5],2)
						g=round(i0[6],2)

						total_pdf_B.set(total_pdf_B.get()+i0[6])
						sub_total_pdf_B.set(sub_total_pdf_B.get()+i0[5])
						iva_pdf_B.set(iva_pdf_B.get()+i0[3])	


						a0=i0[0]
						a1=i0[1]
						a2=i0[8]
						data.append((a0,a1,a2,i0[9],a,b,g))


				export_to_pdf(data)

					
				messagebox.showinfo('BBDD','PDF de ventas creado con exito',parent=hija)
				return


			elif me=='Todos':
				d=int(añoss.get())-2000

				fechi=days.get()+'/'+me+'/'+str(d)
				data = [('CODIGO',"CLIENTE", "FECHA", "HORA", "SUB TOTAL", "IVA", "TOTAL")]

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0")
				A=micursor.fetchall()
				for i0 in A:
					yr=fechi.split('/')
					yr0=i0[8].split('/')

					if yr[2]==yr0[2] and yr[0]==yr0[0]:
						contador_ven+=1
						a=round(i0[3],2)
						b=round(i0[5],2)
						g=round(i0[6],2)

						total_pdf_B.set(total_pdf_B.get()+i0[6])
						sub_total_pdf_B.set(sub_total_pdf_B.get()+i0[5])
						iva_pdf_B.set(iva_pdf_B.get()+i0[3])	
	

						a0=i0[0]
						a1=i0[1]
						a2=i0[8]
						data.append((a0,a1,a2,i0[9],a,b,g))
						
				export_to_pdf(data)

					
				messagebox.showinfo('BBDD','PDF de ventas creado con exito',parent=hija)
				return



			elif days.get()!='Todos' and me!='Todos':
				x=days.get()
				if int(days.get())<10:
					x='0'+days.get()

				d=int(añoss.get())-2000

				fechi=x+'/'+me+'/'+str(d)
				print(fechi,'fechi_pdf')

				data = [('CODIGO',"CLIENTE", "FECHA", "HORA", "SUB TOTAL", "IVA", "TOTAL")]
				data2 = [("                                 ", '                   ',"         TOTAL")]
				
				redon1=DoubleVar()
				redon2=DoubleVar()
				redon3=DoubleVar()
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()



				
				micursor.execute("SELECT * FROM VENTAS  WHERE BOOLEANOS=0 AND FECHA=? ORDER BY (ID_VENTAS) ASC",(fechi, ))
				elusuario=micursor.fetchall()
				for i in elusuario:
					contador_ven+=1
					a=round(i[3],2)
					b=round(i[5],2)
					g=round(i[6],2)

					total_pdf_B.set(total_pdf_B.get()+i[6])
					sub_total_pdf_B.set(sub_total_pdf_B.get()+i[5])
					iva_pdf_B.set(iva_pdf_B.get()+i[3])	

					data.append((i[0],i[1],i[8],i[9],a,b,g))
				
				export_to_pdf(data)

				
				messagebox.showinfo('BBDD','PDF de ventas creado con exito',parent=hija)
				return


		
		Label(hija,text='Dia',font='Helvetica 12',bg='#b6bdff').grid(row=0,column=0,pady=10,padx=10)

		Label(hija,text='Mes',font='Helvetica 12',bg='#b6bdff').grid(row=0,column=1,pady=10,padx=10)

		Label(hija,text='Año',font='Helvetica 12',bg='#b6bdff').grid(row=0,column=2,pady=10,padx=10)


		combo_day=Frame(hija,bg='silver')
		combo_day.grid(row=1,column=0,sticky='EW',pady=10,padx=10)
		dia_final=int(time.strftime("%d"))

		days=ttk.Combobox(combo_day,font='Helvetica 11', state="readonly", height=10,width=6)
		days['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,'Todos')
		days.current(dia_final-1)
		days.pack(side=tk.RIGHT)
		



		combo_mes=Frame(hija,bg='silver')
		combo_mes.grid(row=1,column=1,sticky='EW',pady=10,padx=10)

		mes_final=int(time.strftime("%m"))

		mess=ttk.Combobox(combo_mes,font='Helvetica 11', state="readonly", height=10,width=10)
		mess['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Todos')
		mess.current(mes_final-1)
		mess.pack(side=tk.RIGHT)
		


		combo_año=Frame(hija,bg='silver')
		combo_año.grid(row=1,column=2,sticky='EW',pady=10)

		año_final=time.strftime("%y")
		d=int(año_final)
		fech=d+2001

		años = list(range(1990, fech))
		a=len(años)-1
		añoss=ttk.Combobox(combo_año,font='Helvetica 11', state="readonly", height=10,width=10,values=años)
		añoss.current(a)
		añoss.pack(side=tk.RIGHT)

		


		style = ttk.Style()
		style.configure("Treeview", font=('Helvetica', 10))

		lista_fV=ttk.Treeview(hija,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 6)])
		lista_fV.place(x=0,y=160)

		scoll=Scrollbar(hija,command=lista_fV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=710,y=185,height=320)
		lista_fV.config(yscrollcommand=scoll.set)

		lista_fV.heading('#0',text='Codigo',anchor=CENTER)
		lista_fV.heading('#1',text='C.I. Cliente',anchor=CENTER)
		lista_fV.heading('#2',text='Fecha',anchor=CENTER)
		lista_fV.heading('#3',text='Hora',anchor=CENTER)
		lista_fV.heading('#4',text='Total $',anchor=CENTER)
		lista_fV.heading('#5',text='Total Bs.S',anchor=CENTER)

		lista_fV.column("#0",minwidth=100, width = 100)
		lista_fV.column("#1",minwidth=70, width = 220 )
		lista_fV.column("#2",minwidth=70, width = 60 )
		lista_fV.column("#3",minwidth=70, width = 60 )
		lista_fV.column("#4",minwidth=70, width = 120 )
		lista_fV.column("#5",minwidth=70, width = 170 )


		

		total=Frame(hija)
		total.configure(bg='#b8d3ff',width=390,height=160)
		total.place(x=343,y=0)


		Label(total,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=20)
		Label(total,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=60)
		Label(total,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=100)


		Total_B22=Text(total,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_B22.place(x=115,y=21)

		Total_D22=Text(total,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D22.place(x=115,y=62)

		Total_D33=Text(total,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D33.place(x=115,y=103)

		Button(hija,text='Resultado',font='Helvetica 12',bd=7,relief='raised',cursor='hand2',command=lambda:filtrar_ventas_dma_rp('1')).place(x=0,y=118)
		Button(hija,text='Detalles',font='Helvetica 12',bd=7,relief='raised',cursor='hand2',command=lambda:Detalles_VEN2('1')).place(x=100,y=118)
		Button(hija,text='   PDF    ',font='Helvetica 12',bd=7,relief='raised',cursor='hand2',command=crear_pdf_ventas).place(x=185,y=118)

		'''menu2 = Menu(rp, tearoff=0)
		menu2.add_command(label='Resultado           ',command=lambda:filtrar_ventas_dma_rp('1'),underline=1, accelerator="Ctrl+R")
		menu2.add_command(label='Detalles           ',underline=1, accelerator="Ctrl+D",command=lambda:Detalles_VEN2('1'))
		menu2.add_separator()
		menu2.add_command(label='Limpiar           ',underline=1, accelerator="Ctrl+L",command=lambda:limpiar2('1'))

		def sub_menu4(event):
			try:
				menu2.post(event.x_root, event.y_root)
			finally:
				menu2.grab_release()
	
		rp.bind("<Button-3>", sub_menu4)
		lista_fV.bind("<Button-3>", sub_menu4)

		rp.bind_all("<Control-r>", filtrar_ventas_dma_rp)
		rp.bind_all("<Control-d>", Detalles_VEN2)
		rp.bind_all("<Control-l>", limpiar2)
		lista_fV.bind_all("<Control-r>", filtrar_ventas_dma_rp)
		lista_fV.bind_all("<Control-d>", Detalles_VEN2)
		lista_fV.bind_all("<Control-l>", limpiar2)'''



		#-----------------------------------------------------------------

		def limpiar3(event):
			limpiar_suma_ventana_RP()
			sub_total_B_rp.set(0)
			sub_total_D_rp.set(0)
			iva_B_rp.set(0)
			iva_D_rp.set(0)
			suma_total_D_rp.set(0)
			suma_total_B_rp.set(0)

			record=lista_fV2.get_children()
			for element in record:
				lista_fV2.delete(element)




		def limpiar_suma_ventana_RP():

			Total_B222.configure(state='normal')
			Total_B222.delete('1.0',END)
			Total_B222.configure(state='disabled')

			Total_D222.configure(state='normal')
			Total_D222.delete('1.0',END)
			Total_D222.configure(state='disabled')

			Total_D333.configure(state='normal')
			Total_D333.delete('1.0',END)
			Total_D333.configure(state='disabled')


		def agregar_suma_a_ventana_RP(sub_total_B,sub_total_D,iva_B,iva_D,total_B,total_D):



			di=round(sub_total_B,2)
			di2=round(sub_total_D,2)
			dinero = '{:,}'.format(di)
			dinero2 = '{:,}'.format(di2)
			a=dinero,'(',dinero2,')'


			Total_B222.configure(state='normal')
			Total_B222.insert(END, a)
			Total_B222.configure(state='disabled')


			di5=round(iva_B,2)
			di6=round(iva_D,2)
			dinero5 = '{:,}'.format(di5)
			dinero6 = '{:,}'.format(di6)
			c=dinero5,'(',dinero6,')'


			Total_D222.configure(state='normal')
			Total_D222.insert(END,c)
			Total_D222.configure(state='disabled')


			di3=round(total_B,2)
			di4=round(total_D,2)
			dinero3 = '{:,}'.format(di3)
			dinero4 = '{:,}'.format(di4)
			b=dinero4,'(',dinero3,')'



			Total_D333.configure(state='normal')
			Total_D333.insert(END,b)
			Total_D333.configure(state='disabled')
			return


		def Detalles_VEN3(event):
			try:
				id_ventas=lista_fV2.item(lista_fV2.selection())['text']
				cedula_cliente=lista_fV2.item(lista_fV2.selection())['values'][0]


			except IndexError:
				pass
				return
			HORA=StringVar()
			FECHA=StringVar()
			TASA=DoubleVar()
			vpv=Toplevel(ventana)
			vpv.title('Detalles')
			vpv.geometry('700x532')
			vpv.iconbitmap(logo)
			vpv.resizable(0,0)
			vpv.configure(bg='#b6bdff')
			tab_control = ttk.Notebook(vpv)
			hija2=Frame(tab_control)
			
			identifi=StringVar()

			tab_control.add(hija2, text='Detalles')
			tab_control.pack(expand=1, fill='both')
			hija2.config(bg='#b6bdff')
			


			def ver_productos_de_la_venta_VPV():
				record=lista_pV.get_children()
				for element in record:
					lista_pV.delete(element)
    
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=id_ventas,cedula_cliente
				micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_VENTA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					lista_pV.insert('',0,text=usuarios[3],values=(usuarios[4],usuarios[5],usuarios[7],usuarios[10],usuarios[11]))
						

			def ver_fecha_y_hora_VPV():
				record=lista_pV.get_children()
				for element in record:
					lista_pV.delete(element)
    
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND ID_VENTAS=? ORDER BY(ID_VENTAS)DESC",(id_ventas, ))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					a=str(usuarios[8])
					b=str(usuarios[9])
					FECHA.set(a)
					HORA.set(b)
					TASA.set(usuarios[10])

					sub_total_BB=usuarios[3]
					sub_total_DD=usuarios[2]
					iva_BB=usuarios[5]
					iva_DD=usuarios[4]
					total_BB=usuarios[6]
					total_DD=usuarios[7]

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(cedula_cliente, ))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					nombre_cliente=usuarios[0]+' '+usuarios[1]


				limpiar_cuadros_Text_VPV()
				agregar_a_suma_VPV(TASA.get(),nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD)



	
			def limpiar_cuadros_Text_VPV():
				tasa.configure(state='normal')
				tasa.delete('1.0', END)
				tasa.configure(state='disabled')

				cliente_tex.configure(state='normal')
				cliente_tex.delete('1.0',END)
				cliente_tex.configure(state='disabled')

				Total_B22.configure(state='normal')
				Total_B22.delete('1.0', END)
				Total_B22.configure(state='disabled')

				Total_D22.configure(state='normal')
				Total_D22.delete('1.0',END)
				Total_D22.configure(state='disabled')

				Total_D33.configure(state='normal')
				Total_D33.delete('1.0',END)
				Total_D33.configure(state='disabled')
			


			def agregar_a_suma_VPV(tasad,nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD):
			

				tasa.configure(state='normal')
				tasa_f = '{:,}'.format(tasad)
				tasa.insert(END, tasa_f)
				tasa.configure(state='disabled')

				cliente_tex.configure(state='normal')
				cliente_tex.insert(END,nombre_cliente)
				cliente_tex.configure(state='disabled')



				Total_B22.configure(state='normal')
				dinero = '{:,}'.format(sub_total_BB)
				dinero2 = '{:,}'.format(sub_total_DD)
				a=dinero,'(',dinero2,')'
				Total_B22.insert(END, a)
				Total_B22.configure(state='disabled')



				Total_D22.configure(state='normal')
				dinero5 = '{:,}'.format(iva_BB)
				dinero6 = '{:,}'.format(iva_DD)
				c=dinero5,'(',dinero6,')'
				Total_D22.insert(END,c)
				Total_D22.configure(state='disabled')


				Total_D33.configure(state='normal')
				dinero3 = '{:,}'.format(total_BB)
				dinero4 = '{:,}'.format(total_DD)
				b=dinero3,'(',dinero4,')'
				Total_D33.insert(END,b)
				Total_D33.configure(state='disabled')

				Label(hija2,text=FECHA.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=0)

				Label(hija2,text=HORA.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=40)

				return



			style = ttk.Style()
			style.configure("Treeview", font=('Helvetica', 10))

			lista_pV=ttk.Treeview(hija2,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 6)])
			lista_pV.place(x=0,y=160)

			scoll=Scrollbar(hija2,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll.place(x=680,y=185,height=320)
			lista_pV.config(yscrollcommand=scoll.set)

			lista_pV.heading('#0',text='Codigo',anchor=CENTER)
			lista_pV.heading('#1',text='Productos',anchor=CENTER)
			lista_pV.heading('#2',text='Cantidad',anchor=CENTER)
			lista_pV.heading('#3',text='Unidad',anchor=CENTER)
			lista_pV.heading('#4',text='Precio $',anchor=CENTER)
			lista_pV.heading('#5',text='Precio Bs.S',anchor=CENTER)

			lista_pV.column("#0",minwidth=100, width = 100)
			lista_pV.column("#1",minwidth=70, width = 220 )
			lista_pV.column("#2",minwidth=70, width = 60 )
			lista_pV.column("#3",minwidth=70, width = 50 )
			lista_pV.column("#4",minwidth=70, width = 110 )
			lista_pV.column("#5",minwidth=70, width = 160 )

				
				
			Label(hija2,text='Fecha',font='Helvetica 12',bg='#b6bdff').place(x=0,y=0)


			Label(hija2,text='Hora:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=40)


			Label(hija2,text='Tasa:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=80)

			tasa=Text(hija2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
			tasa.place(x=55,y=80)

			Label(hija2,text='Cliente:',bg='#b6bdff',font='Helvetica 12').place(x=0,y=120)

			cliente_tex=Text(hija2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
			cliente_tex.place(x=55,y=120)


			totales=Frame(hija2)
			totales.configure(bg='#b8d3ff',width=370,height=157)
			totales.place(x=343,y=0)

			Label(totales,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=20)
			Label(totales,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=60)
			Label(totales,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=100)

			Total_B22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
			Total_B22.place(x=115,y=21)

			Total_D22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
			Total_D22.place(x=115,y=62)

			Total_D33=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
			Total_D33.place(x=115,y=103)
			ver_fecha_y_hora_VPV()
			ver_productos_de_la_venta_VPV()


		def desde_hasta_RP(event):
			silencio=0
			sub_total_B_rp.set(0)
			sub_total_D_rp.set(0)
			iva_B_rp.set(0)
			iva_D_rp.set(0)
			suma_total_D_rp.set(0)
			suma_total_B_rp.set(0)

			if añoss2.get()==añoss22.get():
				año2=int(añoss22.get())+1
				años222=int(añoss2.get())
				record=lista_fV2.get_children()
				for element in record:
					
					lista_fV2.delete(element)


			elif int(añoss22.get())-int(añoss2.get())>=2:
				messagebox.showerror('BBDD','Maximo 2 años de diferencia',parent=ventana)
				return


			elif añoss2.get()<añoss22.get():
				año2=int(añoss22.get())+1
				años222=int(añoss2.get())
				
				record=lista_fV2.get_children()
				for element in record:
					
					lista_fV2.delete(element)

			elif añoss2.get()>añoss22.get():
				messagebox.showerror('BBDD','No se puede hacer cuentas inversas')
				return


			if mess2.get()=='Enero':
				me='01'
			elif mess2.get()=='Febrero':
				me='02'
			elif mess2.get()=='Marzo':
				me='03'
			elif mess2.get()=='Abril':
				me='04'
			elif mess2.get()=='Mayo':
				me='05'
			elif mess2.get()=='Junio':
				me='06'
			elif mess2.get()=='Julio':
				me='07'
			elif mess2.get()=='Agosto':
				me='08'
			elif mess2.get()=='Septiembre':
				me='09'
			elif mess2.get()=='Octubre':
				me='10'
			elif mess2.get()=='Noviembre':
				me='11'
			elif mess2.get()=='Diciembre':
				me='12'

			a1=int(añoss2.get())
			a=str(a1-2000)
						
			m=str(me)
			d=str(days2.get())
			
			if int(days2.get())<10:
				d='0'+d


			fecha1=d+'/'+me+'/'+a
			a0=fecha1.split('/')
			

			dia1=a0[0]
			mes1=a0[1]
			año1=a0[2]


			print(fecha1,'fecha1')
			print(dia1,mes1,año1,'fechas iniciales')


			if mess22.get()=='Enero':
				me2='01'
			elif mess22.get()=='Febrero':
				me2='02'
			elif mess22.get()=='Marzo':
				me2='03'
			elif mess22.get()=='Abril':
				me2='04'
			elif mess22.get()=='Mayo':
				me2='05'
			elif mess22.get()=='Junio':
				me2='06'
			elif mess22.get()=='Julio':
				me2='07'
			elif mess22.get()=='Agosto':
				me2='08'
			elif mess22.get()=='Septiembre':
				me2='09'
			elif mess22.get()=='Octubre':
				me2='10'
			elif mess22.get()=='Noviembre':
				me2='11'
			elif mess22.get()=='Diciembre':
				me2='12'





			b1=int(añoss2.get())
			b=str(b1-2000)
						
			m0=str(me2)
			d0=str(days22.get())
			
			if int(days22.get())<10:
				d0='0'+d0


			fecha2=d0+'/'+me2+'/'+b
			b0=fecha2.split('/')
			

			dia2=b0[0]
			mes2=b0[1]
			año2=b0[2]


			print(fecha2,'fecha2')
			print(dia2,mes2,año2,'fechas finales')











		def desde_hasta_RP2(event):

			silencio=0
			sub_total_B_rp.set(0)
			sub_total_D_rp.set(0)
			iva_B_rp.set(0)
			iva_D_rp.set(0)
			suma_total_D_rp.set(0)
			suma_total_B_rp.set(0)

				

			if añoss2.get()==añoss22.get():
				año2=int(añoss22.get())+1
				años222=int(añoss2.get())
				record=lista_fV2.get_children()
				for element in record:
					
					lista_fV2.delete(element)


			elif int(añoss22.get())-int(añoss2.get())>=2:
				messagebox.showerror('BBDD','Maximo 2 años de diferencia',parent=ventana)
				return


			elif añoss2.get()<añoss22.get():
				año2=int(añoss22.get())+1
				años222=int(añoss2.get())
				
				record=lista_fV2.get_children()
				for element in record:
					
					lista_fV2.delete(element)

			elif añoss2.get()>añoss22.get():
				messagebox.showerror('BBDD','No se puede hacer cuentas inversas')
				return

			tr=0
			for A in range(años222,año2):
				if tr==1:
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND FECHA=?",(fecha2, ))
					elusuario=micursor.fetchall()
					for usuarios in elusuario:
								
						lista_fV2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))
						sub_total_B_rp.set(usuarios[3]+sub_total_B_rp.get())
						sub_total_D_rp.set(usuarios[2]+sub_total_D_rp.get())

						iva_B_rp.set(usuarios[5]+iva_B_rp.get())
						iva_D_rp.set(usuarios[4]+iva_D_rp.get())


						suma_total_D_rp.set(usuarios[7]+suma_total_D_rp.get())
						suma_total_B_rp.set(usuarios[6]+suma_total_B_rp.get())


					break
		
				
				for M in range(1,13):
					if tr==1:

						miconexion=sqlite3.connect('SISTEMA_LUMINA')
						micursor=miconexion.cursor()
						micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND FECHA=?",(fecha2, ))
						elusuario=micursor.fetchall()
						for usuarios in elusuario:
								
								
							sub_total_B_rp.set(usuarios[3]+sub_total_B_rp.get())
							sub_total_D_rp.set(usuarios[2]+sub_total_D_rp.get())

							iva_B_rp.set(usuarios[5]+iva_B_rp.get())
							iva_D_rp.set(usuarios[4]+iva_D_rp.get())
							print(total_B_rp.get())

							suma_total_D_rp.set(usuarios[7]+suma_total_D_rp.get())
							suma_total_B_rp.set(usuarios[6]+suma_total_B_rp.get())
							lista_fV2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))

						break

					for D in range(1,32):
						if tr==1:
							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND FECHA=?",(fecha2, ))
							elusuario=micursor.fetchall()
							for usuarios in elusuario:
								
								


								sub_total_B_rp.set(usuarios[3]+sub_total_B_rp.get())
								sub_total_D_rp.set(usuarios[2]+sub_total_D_rp.get())

								iva_B_rp.set(usuarios[5]+iva_B_rp.get())
								iva_D_rp.set(usuarios[4]+iva_D_rp.get())


								suma_total_D_rp.set(usuarios[7]+suma_total_D_rp.get())
								suma_total_B_rp.set(usuarios[6]+suma_total_B_rp.get())
								lista_fV2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))

							break

						a=str(A-2000)
						
						m=str(M)
						d=str(D)
						if M<10:
							m='0'+m
						if D<10:
							d='0'+d
						buscar=d+'/'+m+'/'+a
						

					

						if mess2.get()=='Enero':
							me=1
						elif mess2.get()=='Febrero':
							me=2
						elif mess2.get()=='Marzo':
							me=3
						elif mess2.get()=='Abril':
							me=4
						elif mess2.get()=='Mayo':
							me=5
						elif mess2.get()=='Junio':
							me=6
						elif mess2.get()=='Julio':
							me=7
						elif mess2.get()=='Agosto':
							me=8
						elif mess2.get()=='Septiembre':
							me=9
						elif mess2.get()=='Octubre':
							me=10
						elif mess2.get()=='Noviembre':
							me=11
						elif mess2.get()=='Diciembre':
							me=12







						if mess22.get()=='Enero':
							me2=1
						elif mess22.get()=='Febrero':
							me2=2
						elif mess22.get()=='Marzo':
							me2=3
						elif mess22.get()=='Abril':
							me2=4
						elif mess22.get()=='Mayo':
							me2=5
						elif mess22.get()=='Junio':
							me2=6
						elif mess22.get()=='Julio':
							me2=7
						elif mess22.get()=='Agosto':
							me2=8
						elif mess22.get()=='Septiembre':
							me2=9
						elif mess22.get()=='Octubre':
							me2=10
						elif mess22.get()=='Noviembre':
							me2=11
						elif mess22.get()=='Diciembre':
							me2=12


						f=int(añoss2.get())-2000
						g=int(añoss22.get())-2000
						año1=str(f) #=año1
						año2=str(g)#=año2

						dia1=str(days2.get())#=dia1
						dia2=str(days22.get())#=dia2

						mes1=str(me)#=mes1
						mes2=str(me2)#=mes2

						if me<10:
							mes1='0'+mes1

						if me2<10:
							mes2='0'+mes2

						if int(days2.get())<10:
							dia1='0'+dia1

						if int(days22.get())<10:
							dia2='0'+dia2


						fecha1=dia1+'/'+mes1+'/'+año1

						fecha2=dia2+'/'+mes2+'/'+año2
						if fecha2==fecha1:
							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND FECHA=?",(fecha1, ))
							elusuario=micursor.fetchall()
							for usuarios in elusuario:
								

								sub_total_B_rp.set(usuarios[3]+sub_total_B_rp.get())
								sub_total_D_rp.set(usuarios[2]+sub_total_D_rp.get())

								iva_B_rp.set(usuarios[5]+iva_B_rp.get())
								iva_D_rp.set(usuarios[4]+iva_D_rp.get())


								suma_total_D_rp.set(usuarios[7]+suma_total_D_rp.get())
								suma_total_B_rp.set(usuarios[6]+suma_total_B_rp.get())
								print(total_B_rp.get())
								lista_fV2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))
							
								limpiar_suma_ventana_RP()
								agregar_suma_a_ventana_RP(sub_total_B_rp.get(),sub_total_D_rp.get(),iva_B_rp.get(),iva_D_rp.get(),suma_total_D_rp.get(),suma_total_B_rp.get())
					
							miconexion.commit()
							sub_total_B_rp.set(0)
							sub_total_D_rp.set(0)
							iva_B_rp.set(0)
							iva_D_rp.set(0)
							suma_total_D_rp.set(0)
							suma_total_B_rp.set(0)
							return



						b=buscar.startswith(fecha2)		
						if b==1:
							tr=1
							break

						
						
						r=buscar.startswith(fecha1)

						if r==1:
							silencio=1
						if silencio==1:
							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=0 AND FECHA=?",(buscar, ))
							elusuario=micursor.fetchall()
							for usuarios in elusuario:
								
								



								sub_total_B_rp.set(usuarios[3]+sub_total_B_rp.get())
								sub_total_D_rp.set(usuarios[2]+sub_total_D_rp.get())

								iva_B_rp.set(usuarios[5]+iva_B_rp.get())
								iva_D_rp.set(usuarios[4]+iva_D_rp.get())


								suma_total_D_rp.set(usuarios[7]+suma_total_D_rp.get())
								suma_total_B_rp.set(usuarios[6]+suma_total_B_rp.get())
								print(total_B_rp.get())
								lista_fV2.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[8],usuarios[9],usuarios[7],usuarios[6]))

							miconexion.commit()
							limpiar_suma_ventana_RP()
							agregar_suma_a_ventana_RP(sub_total_B_rp.get(),sub_total_D_rp.get(),iva_B_rp.get(),iva_D_rp.get(),suma_total_D_rp.get(),suma_total_B_rp.get())
				
							print(sub_total_B_rp.get(),sub_total_D_rp.get(),iva_B_rp.get(),iva_D_rp.get(),suma_total_D_rp.get(),suma_total_B_rp.get())
							


		#Label(ventana,text='Desde:',font='Helvetica 12',bg='#b6bdff').place(x=120,y=0)


		Label(ventana,text='Dia',font='Helvetica 12',bg='#b6bdff').place(x=30,y=30)

		Label(ventana,text='Mes',font='Helvetica 12',bg='#b6bdff').place(x=130,y=30)

		Label(ventana,text='Año',font='Helvetica 12',bg='#b6bdff').place(x=250,y=30)


		combo_day2=Frame(ventana,bg='silver')
		combo_day2.place(x=10,y=60)
		dia_final2=int(time.strftime("%d"))

		days2=ttk.Combobox(combo_day2,font='Helvetica 11', state="readonly", height=10,width=6)
		days2['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
		days2.current(dia_final2-2)
		days2.pack(side=tk.RIGHT)
		



		combo_mes2=Frame(ventana,bg='silver')
		combo_mes2.place(x=100,y=60)

		mes_final2=int(time.strftime("%m"))

		mess2=ttk.Combobox(combo_mes2,font='Helvetica 11', state="readonly", height=10,width=10)
		mess2['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
		mess2.current(mes_final2-1)
		mess2.pack(side=tk.RIGHT)
		


		combo_año2=Frame(ventana,bg='silver')
		combo_año2.place(x=220,y=60)

		año_final2=time.strftime("%y")
		d2=int(año_final2)
		fech2=d2+2001

		años = list(range(1990, fech2))
		a2=len(años)-1
		añoss2=ttk.Combobox(combo_año2,font='Helvetica 11', state="readonly", height=10,width=10,values=años)
		añoss2.current(a2)
		añoss2.pack(side=tk.RIGHT)


			#----------------

		#Label(ventana,text='Hasta:',font='Helvetica 12',bg='#b6bdff').place(x=120,y=100)


		Label(ventana,text='Dia',font='Helvetica 12',bg='#b6bdff').place(x=30,y=130)

		Label(ventana,text='Mes',font='Helvetica 12',bg='#b6bdff').place(x=130,y=130)

		Label(ventana,text='Año',font='Helvetica 12',bg='#b6bdff').place(x=250,y=130)


		combo_day22=Frame(ventana,bg='silver')
		combo_day22.place(x=10,y=160)
		dia_final22=int(time.strftime("%d"))

		days22=ttk.Combobox(combo_day22,font='Helvetica 11', state="readonly", height=10,width=6)
		days22['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
		days22.current(dia_final22-1)
		days22.pack(side=tk.RIGHT)
		



		combo_mes22=Frame(ventana,bg='silver')
		combo_mes22.place(x=100,y=160)

		mes_final22=int(time.strftime("%m"))

		mess22=ttk.Combobox(combo_mes22,font='Helvetica 11', state="readonly", height=10,width=10)
		mess22['values']= ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
		mess22.current(mes_final2-1)
		mess22.pack(side=tk.RIGHT)
		


		combo_año22=Frame(ventana,bg='silver')
		combo_año22.place(x=220,y=160)

		año_final22=time.strftime("%y")
		d22=int(año_final2)
		fech22=d2+2001

		años2 = list(range(1990, fech22))
		a2=len(años2)-1
		añoss22=ttk.Combobox(combo_año22,font='Helvetica 11', state="readonly", height=10,width=10,values=años)
		añoss22.current(a2)
		añoss22.pack(side=tk.RIGHT)




		lista_fV2=ttk.Treeview(ventana,style="Treeview",height=11,columns=[f"#{n}" for n in range(1, 6)])
		lista_fV2.place(x=0,y=211)

		scoll=Scrollbar(ventana,command=lista_fV2.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=710,y=232,height=225)
		lista_fV2.config(yscrollcommand=scoll.set)

		lista_fV2.heading('#0',text='Codigo',anchor=CENTER)
		lista_fV2.heading('#1',text='C.I. Cliente',anchor=CENTER)
		lista_fV2.heading('#2',text='Fecha',anchor=CENTER)
		lista_fV2.heading('#3',text='Hora',anchor=CENTER)
		lista_fV2.heading('#4',text='Total $',anchor=CENTER)
		lista_fV2.heading('#5',text='Total Bs.S',anchor=CENTER)

		lista_fV2.column("#0",minwidth=100, width = 100)
		lista_fV2.column("#1",minwidth=70, width = 220 )
		lista_fV2.column("#2",minwidth=70, width = 60 )
		lista_fV2.column("#3",minwidth=70, width = 60 )
		lista_fV2.column("#4",minwidth=70, width = 120 )
		lista_fV2.column("#5",minwidth=70, width = 170 )


		
		total2=Frame(ventana)
		total2.configure(bg='#b8d3ff',width=390,height=210)
		total2.place(x=343,y=0)


		Label(total2,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=40)
		Label(total2,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=90)
		Label(total2,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=140)


		Total_B222=Text(total2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_B222.place(x=115,y=40)

		Total_D222=Text(total2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D222.place(x=115,y=92)

		Total_D333=Text(total2,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D333.place(x=115,y=140)



		Button(ventana,text='Resultado',font='Helvetica 12',bd=7,relief='raised',cursor='hand2',command=lambda:desde_hasta_RP('1')).place(x=5,y=460)
		Button(ventana,text='Detalles',font='Helvetica 12',bd=7,relief='raised',cursor='hand2',command=lambda:Detalles_VEN3('1')).place(x=105,y=460)



		menu3 = Menu(ventana, tearoff=0)
		menu3.add_command(label='Resultado           ',underline=1, accelerator="Ctrl+R",command=lambda:desde_hasta_RP('1'))
		menu3.add_command(label='Detalles           ',underline=1, accelerator="Ctrl+D",command=lambda:Detalles_VEN3('1'))
		menu3.add_separator()
		menu3.add_command(label='Limpiar           ',underline=1, accelerator="Ctrl+L",command=lambda:limpiar3('1'))


		def sub_menu3(event):
			try:
				menu3.post(event.x_root, event.y_root)
			finally:
				menu3.grab_release()

		ventana.bind("<Button-3>",sub_menu3)
		lista_fV2.bind("<Button-3>",sub_menu3)

		ventana.bind_all("<Control-r>",desde_hasta_RP)
		ventana.bind_all("<Control-d>",Detalles_VEN3)
		ventana.bind_all("<Control-l>",desde_hasta_RP)

		
#-----------------------------------------------------------------------

	frax=Frame(ven,bg='#b6bdff')
	frax.grid(row=0,column=0,sticky='NSEW')
	Entry(frax,font='Helvetica 12',bd=7,relief='sunken',textvariable=Buscar_venta_VEN).grid(row=0,column=0,sticky='NSW',pady=10,padx=10)



	ven.rowconfigure(1,weight=2)
	ven.rowconfigure(2,weight=5)

	ven.columnconfigure(0,weight=5)

	frame_lista=Frame(ven,bg='#b6bdff')
	frame_lista.grid(row=2,column=0,sticky='NSEW',columnspan=2)

	


	lista1v=ttk.Treeview(frame_lista,style='Treeview',columns=[f"#{n}" for n in range(1, 8)])
	lista1v.pack(expand=1,fill=BOTH)
	lista1v.grid(row=0,column=0,sticky='nsew',columnspan=4,rowspan=4)
	frame_lista.rowconfigure(0,weight=5)
	frame_lista.columnconfigure(0,weight=5)



	scoll=Scrollbar(frame_lista,command=lista1v.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=0,column=2,sticky='NSEW')


	lista1v.config(yscrollcommand=scoll.set)

	lista1v.heading('#0',text='Codigo')
	lista1v.heading('#1',text='C.I. Cliente')
	lista1v.heading('#2',text='Sub total $')
	lista1v.heading('#3',text='Sub total Bs.S')
	lista1v.heading('#4',text='I.V.A. $')
	lista1v.heading('#5',text='I.V.A. Bs.S')
	lista1v.heading('#6',text='Total $')
	lista1v.heading('#7',text='Total Bs.S')
	

	lista1v.column("#0",minwidth=70, width = 50)
	lista1v.column("#1",minwidth=70, width = 140)
	lista1v.column("#2",minwidth=70, width = 100)
	lista1v.column("#3",minwidth=70, width = 140)
	lista1v.column("#4",minwidth=70, width = 100)
	lista1v.column("#5",minwidth=70, width = 100)
	lista1v.column("#6",minwidth=70, width = 100)
	lista1v.column("#7",minwidth=70, width = 140)

#--------------------------------



	frax=Frame(ven,bg='#b6bdff')
	frax.grid(row=0,column=0,sticky='NSEW')
	Entry(frax,font='Helvetica 12',bd=7,relief='sunken',textvariable=Buscar_venta_VEN).grid(row=0,column=0,sticky='NSW',pady=10,padx=10)

	ven.rowconfigure(1,weight=2)
	ven.rowconfigure(2,weight=5)

	ven.columnconfigure(0,weight=5)

	frame_lista=Frame(ven,bg='#b6bdff')
	frame_lista.grid(row=2,column=0,sticky='NSEW',columnspan=2)

	lista1v=ttk.Treeview(frame_lista,style='Treeview',columns=[f"#{n}" for n in range(1, 9)])
	lista1v.pack(expand=1,fill=BOTH)
	lista1v.grid(row=0,column=0,sticky='nsew',columnspan=4,rowspan=4)
	frame_lista.rowconfigure(0,weight=5)
	frame_lista.columnconfigure(0,weight=5)


	scoll=Scrollbar(frame_lista,command=lista1v.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=0,column=2,sticky='NSEW')


	lista1v.config(yscrollcommand=scoll.set)

	lista1v.heading('#0',text='Codigo')
	lista1v.heading('#1',text='C.I. Cliente')
	lista1v.heading('#2',text='Fecha')
	lista1v.heading('#3',text='Sub total $')
	lista1v.heading('#4',text='Sub total Bs.S')
	lista1v.heading('#5',text='I.V.A. $')
	lista1v.heading('#6',text='I.V.A. Bs.S')
	lista1v.heading('#7',text='Total $')
	lista1v.heading('#8',text='Total Bs.S')
	

	lista1v.column("#0",minwidth=70, width = 50)
	lista1v.column("#1",minwidth=70, width = 120)
	lista1v.column("#2",minwidth=70, width = 60)
	lista1v.column("#3",minwidth=70, width = 80)
	lista1v.column("#4",minwidth=70, width = 140)
	lista1v.column("#5",minwidth=70, width = 80)
	lista1v.column("#6",minwidth=70, width = 100)
	lista1v.column("#7",minwidth=70, width = 100)
	lista1v.column("#8",minwidth=70, width = 140)


	def sub_menu2(event):
		try:
			menu2.post(event.x_root, event.y_root)
		finally:
			menu2.grab_release()

	menu2 = Menu(raiz, tearoff=0)
	menu2.add_command(label="Buscar")
	menu2.add_separator()
	menu2.add_command(label="Detalles",underline=1,accelerator='Ctrl+D',command=lambda:Detalles_VEN('1'))
	menu2.add_command(label="Reportes             ",command=Reportes_VEN)
	


	ven.bind("<Button-3>", sub_menu2)
	ven.bind_all("<Control-d>",Detalles_VEN)

	lista1v.bind("<Button-3>", sub_menu2)
	lista1v.bind_all("<Control-d>",Detalles_VEN)


	frame_botones=Frame(ven,bg='#b6bdff')
	frame_botones.grid(row=1,column=0,sticky='SEW',columnspan=2)


	Button(frax,text='Buscar',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,height=1,command=buscar_venta_en_V).grid(row=0,column=1,sticky='W',pady=10)
	Button(frame_botones,text='Detalles',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,height=1,command=lambda:Detalles_VEN('1')).grid(row=0,column=1,sticky='W')
	Button(frame_botones,text='Reportes',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,height=1,command=Reportes_VEN).grid(row=0,column=3,sticky='W',padx=10)

	leer_todo_VEN()



#-------------compras-------------------------------
	def compras():
		pass
	com.config(bg='#a1e79a')

	continua_compra=0
	def leer_todo_compras():

		record=lista1_com.get_children()
		for element in record:
			lista1_com.delete(element)


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM COMPRAS")
		A=micursor.fetchall()
		for i in A:
			lista1_com.insert('',0,text=i[1],values=(i[3],i[4],i[5],i[6],i[7]))
		miconexion.commit()
		





	def limpiar_campos_en_com():
		
		a=messagebox.askquestion('BBDD','¿Desea limpiar todos los campos?',parent=com)
		if a=='yes':
			proveedor_C.set('')
			paquetes_C.set('')
			und_paquete_C.set('')
			precio_D_paquete.set('')
			precio_B_paquete.set('')
			producto_C.set('')
			cantidad_C.set('')
			precio_D_unidad_C.set('')
			precio_B_unidad_C.set('')
			unidad_compra_label.config(text='UND',fg='#d5b8f8',bg='#d5b8f8')


			client.config(state='normal')
			product_compra.config(state='normal')
			borrar_productos_en_true_compras()
			sumar_total_de_compra()
			client.focus()
			borrar_proveedor_c()

	
	cantidad_com.set('')
	precio_D_com.set('')
	precio_B_com.set('')

	def buscar_P_PRO_en_com():
		VP=Toplevel(raiz)
		VP.geometry('600x532')
		VP.iconbitmap(logo)
		VP.resizable(0,0)
		VP.configure(bg='#d5b8f8')
		
		tab_control = ttk.Notebook(VP)
		hija=Frame(tab_control)
		ventana=Frame(tab_control)
		identifi=StringVar()

		tab_control.add(hija, text='Productos')
		tab_control.add(ventana, text='Proveedores')
		tab_control.pack(expand=1, fill='both')
		hija.config(bg='#d5b8f8')
		ventana.config(bg='#d5b8f8')


		def buscar_producto_com(event):

			if len(buscar_productos_en_com.get())==0:
				record=lista_pV.get_children()
			
				for element in record:
					lista_pV.delete(element)
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					x=float(usuarios[8])
					f=float(usuarios[9])
					gr=round(x,2)
					b=round(f,2)

					lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],gr,b))

			else:
				record=lista_pV.get_children()
			
				for element in record:
					lista_pV.delete(element)
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
				elusuario=micursor.fetchall()
				for usuarios in elusuario:

					r=usuarios[0].startswith(buscar_productos_en_com.get())
					k=usuarios[1].startswith(buscar_productos_en_com.get().capitalize())
					if r==1 or k==1:
						x=float(usuarios[8])
						f=float(usuarios[9])
						a=round(x,2)
						b=round(f,2)
						lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],a,b))
						
					
				miconexion.commit()
		


		def ver_productos_en_com():
			record=lista_pV.get_children()
			
			for element in record:
				lista_pV.delete(element)
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				x=float(usuarios[8])
				f=float(usuarios[9])
				a=round(x,2)
				b=round(f,2)
				
				lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],a,b))
			
			miconexion.commit()



		def agregar_producto_a_com():
			try:
				lista_pV.item(lista_pV.selection())['text'][0]

			except IndexError:
				pass
				return
			

			identifis=lista_pV.item(lista_pV.selection())['text']
			

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(identifis, ))
			a=micursor.fetchall()
			for i in a:
				producto_C.set(i[1])
				product_compra.config(state='readonly')
				canti.focus()


		style = ttk.Style()
		style.configure("Treeview", font=('Helvetica', 10))

		lista_pV=ttk.Treeview(hija,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 5)])
		lista_pV.place(x=0,y=160)

		scoll=Scrollbar(hija,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=580,y=185,height=320)
		lista_pV.config(yscrollcommand=scoll.set)

		lista_pV.heading('#0',text='Codigo',anchor=CENTER)
		lista_pV.heading('#1',text='Productos',anchor=CENTER)
		lista_pV.heading('#2',text='Unidad',anchor=CENTER)
		lista_pV.heading('#3',text='Precio $',anchor=CENTER)
		lista_pV.heading('#4',text='Precio Bs.S',anchor=CENTER)

		lista_pV.column("#0",minwidth=100, width = 100)
		lista_pV.column("#1",minwidth=70, width = 190 )
		lista_pV.column("#2",minwidth=70, width = 50 )
		lista_pV.column("#3",minwidth=70, width = 100 )
		lista_pV.column("#4",minwidth=70, width = 160 )
		ver_productos_en_com()


		
		bus=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=buscar_productos_en_com)
		bus.place(x=0,y=10,height=41)
		bus.focus()
		bus.bind('<KeyRelease>',buscar_producto_com)


		Button(hija,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_producto_com('1')).place(x=200,y=10)

		Button(hija,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=agregar_producto_a_com).place(x=0,y=111)
	

	
	

	#---------------------------------------
		
	#---------------------------------------------
	#-----------------------------------------------
	#---------------------------------------------

		

		def ver_proveedores_en_com():
			record=lista_cV.get_children()
			for element in record:
				lista_cV.delete(element)
	    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PROVEEDORES")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				lista_cV.insert('',0,text=usuarios[1],values=(usuarios[2],usuarios[4],usuarios[3]))
	   

		def agregar_proveedores_a_com():
			try:
				lista_cV.item(lista_cV.selection())['text'][0]

			except IndexError:
				pass
				return
			

			identifis=lista_cV.item(lista_cV.selection())['values'][0]
			print(identifis)

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM PROVEEDORES WHERE RIF_PROVEEDOR=?",(identifis, ))
			a=micursor.fetchall()
			for i in a:
				borrar_proveedor_c()
				agregar_proveedor_c(i[1])
				client.config(state='readonly')
				proveedor_C.set(i[2])


		def buscar_proveedor_com(event):

			if len(buscar_proveedores_en_com.get())==0:
				ver_proveedores_en_com()
			

			else:
				record=lista_cV.get_children()
			
				for element in record:
					lista_cV.delete(element)
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM PROVEEDORES")
				elusuario=micursor.fetchall()
				for usuarios in elusuario:

					r=usuarios[1].capitalize().startswith(buscar_proveedores_en_com.get().capitalize())
					k=usuarios[2].capitalize().startswith(buscar_proveedores_en_com.get().capitalize())
					if r==1 or k==1:
						
						lista_cV.insert('',0,text=usuarios[1],values=(usuarios[2],usuarios[4],usuarios[3]))
						
					
				miconexion.commit()



		lista_cV=ttk.Treeview(ventana,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 4)])
		lista_cV.place(x=0,y=160)
		

		scoll3=Scrollbar(ventana,command=lista_cV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll3.place(x=580,y=185,height=320)
		lista_cV.config(yscrollcommand=scoll3.set)

		lista_cV.heading('#0',text='Nombre',anchor=CENTER)
		lista_cV.heading('#1',text='Cedula',anchor=CENTER)
		lista_cV.heading('#2',text='Direccion',anchor=CENTER)
		lista_cV.heading('#3',text='Telefono',anchor=CENTER)

		lista_cV.column("#0",minwidth=100, width = 230)
		lista_cV.column("#1",minwidth=70, width = 80)
		lista_cV.column("#2",minwidth=70, width = 180 )
		lista_cV.column("#3",minwidth=70, width = 110 )


		Button(ventana,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=agregar_proveedores_a_com).place(x=0,y=111)

		si0=Entry(ventana,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=buscar_proveedores_en_com)
		si0.place(x=0,y=10,height=41)
		si0.focus()
		si0.bind('<Key>',buscar_proveedor_com)
		Button(ventana,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_proveedor_com('1')).place(x=200,y=10)






		ver_proveedores_en_com()



	def ver_tasa_monedas_compras():
		tm=Toplevel(com)
		tm.geometry('260x200')
		tm.config(bg='#d5b8f8')
		tm.iconbitmap(logo)
		tm.resizable(0,0)
		tm.title('Tasa Moneda')

		def ver_tasa_moneda_compras():
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT TASA FROM TASA_MONEDA_COMPRAS WHERE BOOLEANO=1")
			A=micursor.fetchall()
			for i in A:
				Tasa_del_dolar_C.set(i[0])



		def agregar_tasa_moneda():
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=Tasa_del_dolar_C.get(),fecha,tiempo.get(),true,false,false
			micursor.execute("INSERT INTO TASA_MONEDA_COMPRAS VALUES(NULL,?,?,?,?,?,?)",(datos))
			miconexion.commit()
			


		def cambiar_tasa_moneda():
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			

			micursor.execute("UPDATE TASA_MONEDA_COMPRAS SET BOOLEANO=0 WHERE BOOLEANO = 1")
			miconexion.commit()


		def ver_tasa_monedas():
			acd=Toplevel(tm)
			acd.geometry('418x365')
			acd.config(bg='#d5b8f8')
			acd.iconbitmap(logo)
			acd.resizable(0,0)

			def ver_tasa_moneda_en_acd():
				record=ver_tasa.get_children()
				for element in record:
					ver_tasa.delete(element)


				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM TASA_MONEDA_COMPRAS")
				A=micursor.fetchall()
				for i in A:

					micursor.execute("SELECT * FROM PROVEEDORES WHERE RIF_PROVEEDOR IN (SELECT RIF_PROVEEDOR FROM COMPRAS WHERE BOOLEANOS=0)")
					B=micursor.fetchall()
					for f in B:


						ver_tasa.insert('',0,text=i[1],values=(i[2],i[3]))



			Buscar_tasa_moneda=StringVar()



			def buscar_tasa_moneda_en_acd(event):
				if len(Buscar_tasa_moneda.get())==0:
					ver_tasa_moneda_en_acd()
					return


				record=ver_tasa.get_children()
				for element in record:
					ver_tasa.delete(element)


				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT* FROM TASA_MONEDA_COMPRAS")
				A=micursor.fetchall()
				for i in A:
					r=str(i[1])
					t=str(i[2])
					y=str(i[3])
					f=r.startswith(Buscar_tasa_moneda.get())
					g=t.startswith(Buscar_tasa_moneda.get())
					
					if f==1 or g==1:
						micursor.execute("SELECT * FROM TASA_MONEDA_COMPRAS WHERE TASA=? AND ID_TASA=?",(i[1],i[0]))
						B=micursor.fetchall()
						for i0 in B:

							ver_tasa.insert('',0,text=i0[1],values=(i0[2],i0[3]))


				fe.focus()

			
			ver_tasa=ttk.Treeview(acd,style="mystyle.Treeview",height=12,columns=[f"#{n}" for n in range(1, 3)])
			
			ver_tasa.place(x=0,y=100)

			
			

			scoll=Scrollbar(acd,command=ver_tasa.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll.place(x=400,y=100,height=270)

			ver_tasa.config(yscrollcommand=scoll.set)

			ver_tasa.heading('#0',text='Tasa',anchor=CENTER)
			ver_tasa.heading('#1',text='Fecha',anchor=CENTER)
			ver_tasa.heading('#2',text='Hora',anchor=CENTER)
			


			ver_tasa.column("#0",minwidth=100, width = 220)
			ver_tasa.column("#1",minwidth=70, width = 100 )
			ver_tasa.column("#2",minwidth=70, width = 110 )
			

			fe=Entry(acd,relief='sunken',font='Helvetica 12',bd=7,textvariable=Buscar_tasa_moneda)
			fe.place(x=0,y=5)
			Button(acd,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_tasa_moneda_en_acd('1')).place(x=200,y=0)
			fe.focus()
			fe.bind("<KeyRelease>", buscar_tasa_moneda_en_acd)
		
			ver_tasa_moneda_en_acd()





		def Aceptar_tasa_moneda():
			Valor=messagebox.askquestion('BBDD','¿Desea cambiar la tasa de Compras por {} ?'.format(Tasa_del_dolar_C.get()),parent=tm)
			if Valor=='yes':

				tasa2.config(state='readonly')
				

				cambiar_tasa_moneda()
				agregar_tasa_moneda()

		def Editar_tasa_moneda():

			tasa2.config(state='normal')

		Label(tm,text='Tasa Moneda',font='Helvetica 12',bg='#d5b8f8').place(x=65,y=5)
		tasa2=Entry(tm,bd=7,relief='sunken',font='Helvetica 12',textvariable=Tasa_del_dolar_C,state='readonly')
		tasa2.place(x=10,y=40,width=240,height=41)

		Button(tm,text='Aceptar',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=8,height=1,command=Aceptar_tasa_moneda).place(x=10,y=90)
		Button(tm,text='Editar',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=8,height=1,command=Editar_tasa_moneda).place(x=160,y=90)
		Button(tm,text='Ver Tasas Monedas',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=25,height=1,command=ver_tasa_monedas).place(x=10,y=150)

		ver_tasa_moneda_compras()


	
#----------------------------------------------------------
#-----------------------------------------------------
	

	def limpiar_todo_compras():
		proveedor_C.set('')
		paquetes_C.set('')
		und_paquete_C.set('')
		precio_D_paquete.set('')
		precio_B_paquete.set('')
		producto_C.set('')
		cantidad_C.set('')
		precio_D_unidad_C.set('')
		precio_B_unidad_C.set('')
		unidad_compra_label.config(text='UND',fg='#d5b8f8',bg='#d5b8f8')

		client.config(state='normal')
		product_compra.config(state='normal')
		borrar_proveedor_c()

		



	def comprar():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()
			return


		


		ae=StringVar()
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT CODIGO_PRODUCTO,PRECIO_TOTAL_D,PRECIO_TOTAL_B,DEPARTAMENTO FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1")
		A=micursor.fetchall()
		for i in A:
			ae.set(i[0])
			id_actual=i[0]
			precio_actual_D=i[1]
			precio_actual_B=i[2]
			depar=i[3]


		if ae.get()=='':
			pass
			return


		values=messagebox.askquestion('BBDD','¿Desea realizar esta compra?',parent=com)
		if values=='no':
			pass
			return

		valor=messagebox.askquestion('BBDD','¿Desea actualizar los precios iniciales de los productos \n y el precio de los productos comprados?',parent=com)
		
		if valor=='yes':
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT CODIGO_PRODUCTO,PRECIO_TOTAL_D,PRECIO_TOTAL_B,DEPARTAMENTO FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1")
			A=micursor.fetchall()
			for i in A:
				ae.set(i[0])
				id_actual=i[0]
				precio_actual_D=i[1]
				precio_actual_B=i[2]
				depar=i[3]
			

				

				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
				T=micursor.fetchall()
				for i1 in T:
					Tasa=i1[0]

					print(Tasa,'tasritaaa')
					print(i[0],'helloo')
					micursor.execute("SELECT EXENTO,PRECIO_D_PRODUCTO,PRECIO_B_PRODUCTO,PORCENTAJE_GANANCIA,PRECIO_FINAL_D_P,PRECIO_FINAL_B_P,SUB_TOTAL_D,SUB_TOTAL_B,DEPARTAMENTO FROM PRODUCTOS WHERE ID=?",(i[0], ))
					C=micursor.fetchall()
					for i2 in C:
						if i2[0]==0:
							a1=precio_actual_D*i2[3]
							a2=a1/100
							a3=a2+precio_actual_D

							a4=a3*IVA.get()
							a5=a4/100
							precio_final_D_a=a5+a3


							precio_final_B_a=precio_final_D_a*Tasa



							sub_total_final_D=a3
							sub_total_final_B=a3*Tasa


						elif i2[0]==1:

							a1=precio_actual_D*i2[3]
							a2=a1/100
							a3=a2+precio_actual_D

							
							precio_final_D_a=a3

							precio_final_B_a=a3*Tasa

							sub_total_final_D=a3
							sub_total_final_B=a3*Tasa



						datos=precio_actual_D, precio_actual_B, precio_final_D_a, precio_final_B_a, sub_total_final_D, sub_total_final_B,i[0]
							
						micursor.execute("UPDATE PRODUCTOS SET PRECIO_D_PRODUCTO=?,PRECIO_B_PRODUCTO=?,PRECIO_FINAL_D_P=?,PRECIO_FINAL_B_P=?,SUB_TOTAL_D=?,SUB_TOTAL_B=? WHERE ID=?",(datos))


		miconexion.commit()
		comprar_esa_broma()
		
			
		




	def cambiar_productos_de_true_a_false():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		micursor.execute("UPDATE PRODUCTOS_COMPRAS SET BOOLEANOSS=0 WHERE BOOLEANOSS=1")
		miconexion.commit()

	codigo_compra=StringVar()
	def comprar_esa_broma():
		codig=Toplevel(com)
		codig.geometry('400x100')
		codig.resizable(0,0)
		codig.configure(bg='#d5b8f8')
		codig.title('Codigo de Factura')
		codig.transient(master=com)
		codig.focus_set()
		ancho_ventana = 300
		alto_ventana = 100
		x_ventana = codig.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = codig.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		codig.geometry(posicion)

		f_codig=Entry(codig,relief='sunken',font='Helvetica 12',bd=7,width=20,textvariable=codigo_compra)
		f_codig.place(x=10,y=50,height=41)
		f_codig.focus()
		f_codig.focus()
		def seguir_compra(event):
			if len(codigo_compra.get())==0:
				pass
				return
			else:
				codig.destroy()
				comprar_esa_broma2()
				limpiar_todo_compras()

				limpiar_suma_compras()
				cambiar_productos_de_true_a_false()


				record=lista_compra.get_children()
				for i in record:
					lista_compra.delete(i)
				codigo_compra.set('')


		Label(codig,text='Codigo Factura',font='Helvetica 12',bg='#d5b8f8').place(x=35,y=20)

		bf=Button(codig,text='Aceptar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=lambda:seguir_compra('1'))
		bf.place(x=210,y=50)
		
		bf.bind('<Return>',seguir_compra)

		codig.bind('<Return>',seguir_compra)
	
	def comprar_esa_broma2():

		
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT PRECIO_TOTAL_D,PRECIO_TOTAL_B,EXENTO,CANTIDAD FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1")
		A=micursor.fetchall()
		for i in A:

			if i[2]==0:
				a0=IVA.get()/100
				iva=a0+1
				
				a=i[0]
				a1=a*iva
				a2=a1-a
				a4=a-a2
				a3=a4*i[3]

				b=i[1]
				b1=b*iva
				b2=b1-b
				b4=b-b2
				b3=b4*i[3]

				
				Sub_total_D_compra.set(Sub_total_D_compra.get()+a3)
				Sub_total_B_compra.set(Sub_total_B_compra.get()+b3)

				iva_D_compra.set(iva_D_compra.get()+a2)
				iva_B_compra.set(iva_B_compra.get()+b2)


			else:
				d1=i[0]*i[3]
				d2=i[1]*i[3]

				Sub_total_D_compra.set(Sub_total_D_compra.get()+d1)
				Sub_total_B_compra.set(Sub_total_B_compra.get()+d2)

				iva_D_compra.set(iva_D_compra.get()+0)
				iva_B_compra.set(iva_B_compra.get()+0)


			c1=i[0]*i[3]
			c2=i[1]*i[3]
			Total_D_compra.set(Total_D_compra.get()+c1)
			Total_B_compra.set(Total_B_compra.get()+c2)

		
		iva_B_compra.set(Total_B_compra.get()-Sub_total_B_compra.get())
		iva_D_compra.set(Total_D_compra.get()-Sub_total_D_compra.get())

		if len(codigo_compra.get())==0:

			micursor.execute("SELECT ID_COMPRA FROM COMPRAS WHERE BOOLEANOS=1")
			for i in micursor.fetchall():
				codigo_compra.set(i[0])


		datos=proveedor_C.get(),Sub_total_D_compra.get(),Sub_total_B_compra.get(),iva_D_compra.get(),iva_B_compra.get(),Total_D_compra.get(),Total_B_compra.get(),fecha,tiempo.get(),Tasa_del_dolar_C.get(),codigo_compra.get()
		
		micursor.execute("UPDATE COMPRAS SET RIF_PROVEEDOR=?,SUB_TOTAL_C_D=?,SUB_TOTAL_C_B=?,IVA_C_D=?,IVA_C_B=?,TOTAL_C_D=?,TOTAL_C_B=?,FECHA=?,HORA=?,TASA_DEL_DIA=?,ID_PIBOTE=? WHERE BOOLEANOS=1",(datos))
		micursor.execute("UPDATE COMPRAS SET BOOLEANOS=0 WHERE BOOLEANOS=1")	
		
		miconexion.commit()
		crear_compra()



	def ver_tasa_moneda_compras():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT TASA FROM TASA_MONEDA_COMPRAS WHERE BOOLEANO=1")
		A=micursor.fetchall()
		for i in A:
			Tasa_del_dolar_C.set(i[0])

	def borrar_productos_en_true_compras():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		
		micursor.execute("SELECT * FROM PRODUCTOS WHERE ID IN (SELECT CODIGO_PRODUCTO FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1)")
		A=micursor.fetchall()
		for i in A:
			
			micursor.execute("SELECT * FROM PRODUCTOS_COMPRAS WHERE CODIGO_PRODUCTO=?",(i[0], ))
			B=micursor.fetchall()
			for it in B:
				
				a0=i[2]-it[5]
				
				micursor.execute("UPDATE PRODUCTOS SET CANTIDAD_PRODUCTO=? WHERE ID=?",(a0,i[0]))


		micursor.execute("DELETE FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1")
		miconexion.commit()


	def comprobacion_borrar_producto_en_compra():
	
		try:
			lista_compra.item(lista_compra.selection())['text'][0]
		except TclError:
			continua2.set('')
			return

		except IndexError:
			continua2.set('')
			return
		
		continua_V.set(messagebox.askquestion('BBDD','Desea borrar este producto',parent=com))
		if continua_V.get()=='yes':
			borrar_producto_en_compra()

	def borrar_producto_en_compra():
		N=0
		ide=lista_compra.item(lista_compra.selection())['text']
		produc=lista_compra.item(lista_compra.selection())['values'][0]
		cantid=lista_compra.item(lista_compra.selection())['values'][1]
		unida=lista_compra.item(lista_compra.selection())['values'][2]
		precio_Do=lista_compra.item(lista_compra.selection())['values'][3]
		precio_Bo=lista_compra.item(lista_compra.selection())['values'][4]
		total_Do=lista_compra.item(lista_compra.selection())['values'][5]
		total_Bo=lista_compra.item(lista_compra.selection())['values'][6]



		
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT CANTIDAD_PRODUCTO FROM PRODUCTOS WHERE ID=?",(ide, ))
		A=micursor.fetchall()
		for i in A:

			cantidad_=i[0]


		print(cantidad_,cantid)

		cantidad=cantidad_-cantid
		print(cantidad)
		micursor.execute("UPDATE PRODUCTOS SET CANTIDAD_PRODUCTO=? WHERE ID=?",(cantidad,ide))
		micursor.execute('DELETE FROM PRODUCTOS_COMPRAS WHERE CODIGO_PRODUCTO=? AND BOOLEANOSS=1',(ide, ))


		miconexion.commit()

		
		sumar_total_de_compra()

	def editar_producto_de_C():
		cantidad_nueva_c=DoubleVar()
		producto_nueva_c=StringVar()
		try:
			lista_compra.item(lista_compra.selection())['text'][0]


		except IndexError:
			pass
			return
		
		ide=lista_compra.item(lista_compra.selection())['text']
		nombre_a=lista_compra.item(lista_compra.selection())['values'][0]
		cantidad_a=lista_compra.item(lista_compra.selection())['values'][1]
		unidad_a=lista_compra.item(lista_compra.selection())['values'][2]
		departamento_a=lista_compra.item(lista_compra.selection())['values'][3]
		precio_ini_D_a=lista_compra.item(lista_compra.selection())['values'][4]
		precio_ini_B_a=lista_compra.item(lista_compra.selection())['values'][5]


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM DEPARTAMENTOS")
		
		A=micursor.fetchall()
					
		for i in A:
			i[2]



		editar_nombre_a.set(nombre_a)
		editar_cantidad_a.set(cantidad_a)
		editar_precio_D_a.set(precio_ini_D_a)
		editar_precio_B_a.set(precio_ini_B_a)



		producto_nueva_c.set(nombre_a)
		cantidad_nueva_c.set(cantidad_a)


		editar=Toplevel(hija)
		editar.geometry('400x200')
		editar.resizable(0,0)
		editar.iconbitmap(logo)
		editar.grab_set()
		editar.config(bg='#d5b8f8')


		def actualizar_producto_compras():
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT CANTIDAD_PRODUCTO FROM PRODUCTOS WHERE ID=?",(ide, ))
			A=micursor.fetchall()
			for i in A:
				a0=i[0]-cantidad_a
				a1=a0+cantidad_nueva_c.get()




				micursor.execute("UPDATE PRODUCTOS_COMPRAS SET CANTIDAD=? WHERE CODIGO_PRODUCTO=?",(cantidad_nueva_c.get(),ide))
				micursor.execute("UPDATE PRODUCTOS SET CANTIDAD_PRODUCTO=? WHERE ID=?",(a1,ide))





			miconexion.commit()
			sumar_total_de_compra()
			editar.destroy()



		Label(editar,text='Producto ',font='Helvetica 12',fg='black',bg='#d5b8f8').place(x=40,y=20)
		nombre2323=Entry(editar,state='readonly',textvariable=producto_nueva_c,relief='sunken',font='Helvetica 12',fg='black',bd=10)
		nombre2323.place(x=140,y=20)
		nombre2323.focus()

		Label(editar,text='Cantidad ',font='Helvetica 12',fg='black',bg='#d5b8f8').place(x=40,y=80)
		cantidad2323=Entry(editar,relief='sunken',font='Helvetica 12',fg='black',bd=10,textvariable=cantidad_nueva_c)
		cantidad2323.place(x=140,y=80)




		Button(editar,text='Guardar',cursor='hand2',font='Helvetica 12',fg='black',bd=10,relief='raised',width=42,command=actualizar_producto_compras).place(x=0,y=155)



	borrar_productos_en_true_compras()


	def limpiar_suma_compras():
		total_compra1.configure(state='normal')
		total_compra1.delete('1.0', END)
		total_compra1.configure(state='disabled')

		total_compra2.configure(state='normal')
		total_compra2.delete('1.0',END)
		total_compra2.configure(state='disabled')

		total_compra3.configure(state='normal')
		total_compra3.delete('1.0',END)
		total_compra3.configure(state='disabled')
		
		

	def agregar_a_suma_compras(dolar,bolivar,no_iva_b,no_iva_d,iva_b,iva_d):
		
		total_compra3.configure(state='normal')

		a0=round(dolar,2)
		a1=round(bolivar,2)
		
		dinero = '{:,}'.format(a0)
		dinero2 = '{:,}'.format(a1)
		
		a=dinero,'(',dinero2,')'
		total_compra3.insert(END, a)
		total_compra3.configure(state='disabled')



		a2=round(iva_b,2)
		a3=round(iva_d,2)


		dinero5 = '{:,}'.format(a2)
		dinero6 = '{:,}'.format(a3)

		c=dinero5,'(',dinero6,')'

		total_compra2.configure(state='normal')
		total_compra2.insert(END,c)
		total_compra2.configure(state='disabled')


		a4=round(no_iva_b,2)
		a5=round(no_iva_d,2)

		dinero3 = '{:,}'.format(a5)
		dinero4 = '{:,}'.format(a4)
		d=' '
		b=dinero3,'(',dinero4,')'



		total_compra1.configure(state='normal')
		total_compra1.insert(END,b)
		total_compra1.configure(state='disabled')
		return


	def sumar_total_de_compra():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT PRECIO_TOTAL_D,PRECIO_TOTAL_B,EXENTO,CANTIDAD FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1")
		A=micursor.fetchall()
		for i in A:

			if i[2]==0:
				a0=IVA.get()/100
				iva=a0+1
				
				a=i[0]
				a1=a*iva
				a2=a1-a
				a4=a-a2
				a3=a4*i[3]

				b=i[1]
				b1=b*iva
				b2=b1-b
				b4=b-b2
				b3=b4*i[3]

				
				Sub_total_D_compra.set(Sub_total_D_compra.get()+a3)
				Sub_total_B_compra.set(Sub_total_B_compra.get()+b3)

				iva_D_compra.set(iva_D_compra.get()+a2)
				iva_B_compra.set(iva_B_compra.get()+b2)


			else:
				d1=i[0]*i[3]
				d2=i[1]*i[3]

				Sub_total_D_compra.set(Sub_total_D_compra.get()+d1)
				Sub_total_B_compra.set(Sub_total_B_compra.get()+d2)

				iva_D_compra.set(iva_D_compra.get()+0)
				iva_B_compra.set(iva_B_compra.get()+0)


			c1=i[0]*i[3]
			c2=i[1]*i[3]
			Total_D_compra.set(Total_D_compra.get()+c1)
			Total_B_compra.set(Total_B_compra.get()+c2)

		miconexion.commit()
		limpiar_suma_compras()
		iva_B_compra.set(Total_B_compra.get()-Sub_total_B_compra.get())
		iva_D_compra.set(Total_D_compra.get()-Sub_total_D_compra.get())


		agregar_a_suma_compras(Total_B_compra.get(),Total_D_compra.get(),Sub_total_D_compra.get(),Sub_total_B_compra.get(),iva_B_compra.get(),iva_D_compra.get())
		

		ver_productos_en_lista_compra()

		Sub_total_D_compra.set(0)
		Sub_total_B_compra.set(0)

		iva_D_compra.set(0)
		iva_B_compra.set(0)
		Total_D_compra.set(0)
		Total_B_compra.set(0)


	def ver_productos_en_lista_compra():
		record=lista_compra.get_children()
		for i in record:
			lista_compra.delete(i)


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=1")
		A=micursor.fetchall()
		for i in A:

			a=i[8]*i[5]
			a1=i[9]*i[5]

			lista_compra.insert('',0,text=i[3],values=(i[4],i[5],i[7],i[13],i[8],i[9],a,a1))


	def ingresar_a_lista_compra():
		global continua_compra

		if proveedor_C.get()=='':
			messagebox.showerror('BBDD','Ingrese RIF proveedor',parent=com)
			return
		try:
			if cantidad_C.get()==0 or cantidad_C.get()=='':

				messagebox.showerror('BBDD','Nesecita ingresar una cantidad',parent=com)
				return
		except TclError:
			messagebox.showerror('BBDD','Nesecita ingresar una cantidad',parent=com)
			return

		try:
			if precio_D_unidad_C.get()==0 or precio_D_unidad_C.get()=='':

				messagebox.showerror('BBDD','Nesecita ingresar un precio de compra',parent=com)
				return
		except TclError:
			messagebox.showerror('BBDD','Nesecita ingresar un precio de compra',parent=com)
			return

		try:
			if precio_B_unidad_C.get()==0 or precio_B_unidad_C.get()=='':

				messagebox.showerror('BBDD','Nesecita ingresar un precio de compra',parent=com)
				return
		except TclError:
			messagebox.showerror('BBDD','Nesecita ingresar un precio de compra',parent=com)
			return




		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()

		micursor.execute("SELECT ID,PORCENTAJE_GANANCIA,EXENTO,UNIDAD,DEPARTAMENTO FROM PRODUCTOS WHERE NOMBRE_PRODUCTO=?",(producto_C.get(), ))
		B=micursor.fetchall()
		for i in B:
			id_producto_c=i[0]
			porcentaje_producto=i[1]
			exento_producto=i[2]
			unidad_producto=i[3]
			departamento_producto=i[4]

		micursor.execute("SELECT ID_COMPRA FROM COMPRAS WHERE BOOLEANOS=1")
		A=micursor.fetchall()
		for i in A:
			id_compra=i[0]

		micursor.execute("SELECT ID_COMPRA FROM COMPRAS WHERE BOOLEANOS=1")
		A=micursor.fetchall()
		for i in A:
			id_compra=i[0]

		if exento_producto==1:
			sub_total_compra_D=precio_D_unidad_C.get()
			sub_total_compra_B=precio_B_unidad_C.get()
		else:
			r0=precio_D_unidad_C.get()*IVA.get()
			r1=r0/100
			sub_total_compra_D=precio_D_unidad_C.get()-r1

			c0=precio_B_unidad_C.get()*IVA.get()
			c1=c0/100
			sub_total_compra_B=precio_B_unidad_C.get()-c1


		datos=id_compra,proveedor_C.get(),id_producto_c,producto_C.get(),cantidad_C.get(),exento_producto,unidad_producto,precio_D_unidad_C.get(),precio_B_unidad_C.get(),porcentaje_producto,fecha,1,departamento_producto,sub_total_compra_D,sub_total_compra_B
		micursor.execute("INSERT INTO PRODUCTOS_COMPRAS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))


		
		

		micursor.execute("SELECT CANTIDAD_PRODUCTO FROM PRODUCTOS WHERE ID=?",(id_producto_c, ))
		cantidad_nueva=DoubleVar()
		cantidad_nueva.set('')
		X=micursor.fetchall()
		for i in X:
			cantidad_nueva.set(i[0]+cantidad_C.get())
			print(cantidad_nueva.get())
		

		try:

			if cantidad_nueva.get()=='':
				pass

			else:
				micursor.execute("UPDATE PRODUCTOS SET CANTIDAD_PRODUCTO=? WHERE ID=?",(cantidad_nueva.get(),id_producto_c ))


		except TclError:
			pass



		miconexion.commit()
		print('sumar_total_de_compra')
		sumar_total_de_compra()
		paquetes_C.set('')
		und_paquete_C.set('')
		precio_D_paquete.set('')
		precio_B_paquete.set('')
		producto_C.set('')
		cantidad_C.set('')
		precio_D_unidad_C.set('')
		precio_B_unidad_C.set('')
		continua_compra=0
		product_compra.config(state='normal')
		unidad_compra_label.config(text='UND',fg='#d5b8f8',bg='#d5b8f8')

	def ingresar_ID_en_compras(event):

		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return
		if len(producto_C.get())==0:
			pass
			return

		global continua_compra
		unidad=StringVar()
		if continua_compra==0:
			if len(producto_C.get())==0:
				siguiente_compras(event)
				return
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()


			micursor.execute("SELECT * FROM PRODUCTOS")
			A=micursor.fetchall()
			for i in A:
				a=producto_C.get().capitalize()
				r=i[1].startswith(a)
				k0=i[0].capitalize()
				k=k0.startswith(a)
				
				if r==1 or k==1:
					producto_C.set(i[1])
					micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(i[0], ))
					x=micursor.fetchall()
					for f in x:
						unidad.set(f[3])

						unidad_compra_label.config(text=unidad.get(),fg='black')
					
						canti.focus()
			print(unidad.get())
			if unidad.get()!='':
				continua_compra=1
				product_compra.config(state='readonly')
				
			else:
				agregar_producto_en_compras()
				return
			

			return
		else:
			if continua_compra==1:
				ingresar_a_lista_compra()
				
			return


			

	


	def verificar_proveedor_C(event):
		PROVEERDOR=StringVar()
		if proveedor_C.get()=='':
			pass
			return
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		
		micursor.execute("SELECT * FROM PROVEEDORES WHERE RIF_PROVEEDOR=?",(proveedor_C.get(), ))
		A=micursor.fetchall()
		for i in A:
			borrar_proveedor_c()
			agregar_proveedor_c(i[1])
			client.config(state='readonly')
			PROVEERDOR.set(i[1])

			e0.focus()
		if PROVEERDOR.get()=='':
			pass
			return

		

		miconexion.commit()


	def calcular_precio_B_unidad(event):
		try:
			if precio_B_unidad_C.get()=='':
				precio_D_unidad_C.set('')
				return
		except TclError:
			precio_D_unidad_C.set('')
			return

		a=precio_B_unidad_C.get()/Tasa_del_dolar_C.get()
		precio_D_unidad_C.set(a)


	def calcular_precio_D_unidad(event):
		try:
			if precio_D_unidad_C.get()=='':
				precio_B_unidad_C.set('')
				return
		except TclError:
			precio_B_unidad_C.set('')
			return

		a=precio_D_unidad_C.get()*Tasa_del_dolar_C.get()
		precio_B_unidad_C.set(a)



	def calcular_precio_B_paquete(event):
		try:
			if cantidad_C.get()=='':
				precio_B_paquete.set(precio_D_paquete.get()*Tasa_del_dolar_C.get())
				return
		except TclError:
			precio_B_paquete.set(precio_D_paquete.get()*Tasa_del_dolar_C.get())

		try:
			if precio_D_paquete.get()=='':
				precio_B_paquete.set('')
				return
		except TclError:
			precio_B_paquete.set('')
			return

		try:
			a2=precio_D_paquete.get()*paquetes_C.get()

		except TclError:
			a2=precio_D_paquete.get()*1



		precio_B_paquete.set(precio_D_paquete.get()*Tasa_del_dolar_C.get())

		a3=a2/cantidad_C.get()


		precio_B_unidad_C.set(a3*Tasa_del_dolar_C.get())
		precio_D_unidad_C.set(a3)



	def calcular_precio_D_paquete(event):

		try:
			if cantidad_C.get()=='':
				precio_D_paquete.set(precio_B_paquete.get()/Tasa_del_dolar_C.get())
				return

		except TclError:
			precio_D_paquete.set(precio_B_paquete.get()/Tasa_del_dolar_C.get())
			return




		try:
			if precio_B_paquete.get()=='':
				precio_D_paquete.set('')
				return
		except TclError:
			precio_D_paquete.set('')
			return

		try:
		
			a2=precio_B_paquete.get()*paquetes_C.get()

		except TclError:
			a2=precio_B_paquete.get()*1

		precio_D_paquete.set(precio_B_paquete.get()/Tasa_del_dolar_C.get())

		a3=a2/cantidad_C.get()


		precio_B_unidad_C.set(a3)
		precio_D_unidad_C.set(a3/Tasa_del_dolar_C.get())



	def agregar_proveedor_c(valor):
		cliente_c_c.configure(state='normal')
		cliente_c_c.insert(END,valor)
		cliente_c_c.configure(state='disabled')

	def borrar_proveedor_c():
		cliente_c_c.configure(state='normal')
		cliente_c_c.delete('1.0',END)
		cliente_c_c.configure(state='disabled')


	def agregar_producto_en_compras():
		Valor=messagebox.askquestion('BBDD','¿Producto no registrado desea registrarlo?',parent=com)
		if Valor=='yes':
			agregar_producto_en_compras2()
	

	def agregar_producto_en_compras2():
		
		prod=Toplevel(com)
		prod.config(bg='#d5b8f8')
		prod.title('Editar Oferta')
		prod.geometry('1020x200')
		prod.resizable(0,0)
		prod.iconbitmap(logo)


		identificador_compra=StringVar()
		producto_compra=StringVar()
		cantidad_producto_compra=DoubleVar()
		porcentaje_compra=DoubleVar()
		precio_inicial_D_compra=DoubleVar()
		precio_inicial_B_compra=DoubleVar()
		precio_final_D_compra=DoubleVar()
		precio_final_B_compra=DoubleVar()

		exento_compra=BooleanVar()


		identificador_compra.set('')
		producto_compra.set('')
		cantidad_producto_compra.set('')
		porcentaje_compra.set('')
		precio_inicial_D_compra.set('')
		precio_inicial_B_compra.set('')
		precio_final_D_compra.set('')
		precio_final_B_compra.set('')

		exento_compra=BooleanVar()



		producto_compra.set(producto_C.get())
		def funcion_provisional():#transmitir precios desde compras hasta agregar productos compras 
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart_c.get(), ))
			A=micursor.fetchall()


			for i in A:
				tasa_c=i[0]


			try:
				cantidad_producto_compra.set(cantidad_C.get())
			except TclError: 
				pass

			try:
				precio_inicial_D_compra.set(precio_B_unidad_C.get()/tasa_c)
			except TclError: 
				pass

			try:
				precio_inicial_B_compra.set(precio_B_unidad_C.get())
			except TclError: 
				pass
			


		def siguiente_compras_productos(event):
			event.widget.tk_focusNext().focus()
			return

		def ver_departamentos_compras():
	

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT DEPARTAMENTO FROM DEPARTAMENTOS")
			A=micursor.fetchall()

			depart_c['values']= (list(f"{str(n[0])}" for n in A))
			
			miconexion.commit()


		def calcular_tasa_compra_bolivar(event):
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart_c.get(), ))
			A=micursor.fetchall()


			for i in A:
				tasa_c=i[0]

			try:

				if precio_inicial_B_compra.get()=='':
					pass
			except:
				precio_inicial_D_compra.set('')
				precio_final_B_compra.set('')
				precio_final_D_compra.set('')

				return

			precio_inicial_D_compra.set(precio_inicial_B_compra.get()/tasa_c)
			calcular_de_precio_inicial('1')



		def calcular_tasa_compra_dolar(event):
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart_c.get(), ))
			A=micursor.fetchall()


			for i in A:
				tasa_c=i[0]

			try:

				if precio_inicial_D_compra.get()=='':
					pass
			except:
				precio_inicial_B_compra.set('')
				precio_final_B_compra.set('')
				precio_final_D_compra.set('')
				return

			precio_inicial_B_compra.set(precio_inicial_D_compra.get()*tasa_c)


			calcular_de_precio_inicial('1')



		

		def calcular_de_precio_inicial(event):

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart_c.get(), ))
			A=micursor.fetchall()
			for i in A:
				tasa_c=i[0]



			try:
				if porcentaje_compra.get()=='':
					pass
					return

			except TclError: 
				precio_final_D_compra.set('')
				precio_final_B_compra.set('')
				return

			try:

				if precio_inicial_B_compra.get()!='':
					pass

			except TclError:
				precio_final_D_compra.set('')
				precio_final_B_compra.set('')
				return



			if exento_compra.get()==1:

				a0=precio_inicial_B_compra.get()*porcentaje_compra.get()
				a1=a0/100

				a2=a1+precio_inicial_B_compra.get()


				precio_final_B_compra.set(a2)
				precio_final_D_compra.set((a2/tasa_c))

			else:
				
				a0=precio_inicial_B_compra.get()*porcentaje_compra.get()
				a1=a0/100
				a11=precio_inicial_B_compra.get()+a1
				a2=a11

				a3=a11*IVA.get()
				a4=a3/100
				
				a6=a4+a2
				precio_final_B_compra.set(a6)
				precio_final_D_compra.set(a6/tasa_c)



		def calcular_porcentaje(event):

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart_c.get(), ))
			A=micursor.fetchall()
			for i in A:
				tasa_c=i[0]

			try:
				if precio_final_B_compra.get()=='':
					pass
			except TclError:
				precio_final_D_compra.set('')
				return



			print('q')

			if exento_compra.get()==1:

				precio_final_D_compra.set(precio_final_B_compra.get()/tasa_c)


				a0=precio_final_D_compra.get()-precio_inicial_D_compra.get()
				print(a0,'a0')


				a1=a0*100
				print(a1,'a1')
				a2=a1/precio_inicial_D_compra.get()

				print(a2,'a2')
				porcentaje_compra.set(round(a2,2))


			else:

				precio_final_D_compra.set(precio_final_B_compra.get()/tasa_c)


				iva=IVA.get()/100+1


				a00=precio_inicial_D_compra.get()*iva
				a0=precio_final_D_compra.get()-a00
				print(a0,'a0')


				a1=a0*100
				print(a1,'a1')
				a2=a1/precio_inicial_D_compra.get()

				print(a2,'a2')
				porcentaje_compra.set(round(a2,2))





		def crear_producto_en_compras():


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depart_c.get(), ))
			A=micursor.fetchall()
			for i in A:
				tasa_c=i[0]



			if len(producto_compra.get())==0 or len(identificador_compra.get())==0:

				messagebox.showerror('BBDD','Faltan Campos por escribir',parent=prod)
				return
			try:
				if cantidad_producto_compra.get()=='' or precio_inicial_D_compra.get()=='' or precio_inicial_B_compra.get()=='' or precio_final_D_compra.get()=='' or precio_final_D_compra.get()=='':
					messagebox.showerror('BBDD','Faltan Campos por escribir',parent=prod)
					return

			except TclError:
				messagebox.showerror('BBDD','Faltan Campos por escribir',parent=prod)
				return



			try:
				unidad_p=StringVar()
				if combo2.get()=='Unidad':
					unidad_p.set('UND')
			

				elif combo2.get()=='Kilogramos':
					unidad_p.set('Kg ')

				elif combo2.get()=='Litros':
					unidad_p.set('Lts')

				elif combo2.get()=='Metros':
					unidad_p.set('Mts')

				print(exento_compra.get(),'execute')
				if exento_compra.get()==1:
					sub_total_D_c=precio_final_D_compra.get()
					sub_total_B_c=precio_final_B_compra.get()


				elif exento_compra.get()==0:
					print('holaaaaa')
					b0=precio_final_B_compra.get()*IVA.get()
					b1=b0/100
					sub_total_B_c=precio_final_B_compra.get()-b1
					sub_total_D_c=sub_total_B_c/tasa_c
					print(sub_total_D_c,'sub_total_D_c2')
					
					print(sub_total_B_c,'sub_total_D_c')
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()


				datos=identificador_compra.get(),producto_compra.get().capitalize(),cantidad_producto_compra.get(),unidad_p.get(),exento_compra.get(),precio_inicial_D_compra.get(),precio_inicial_B_compra.get(), porcentaje_compra.get(),precio_final_D_compra.get(),precio_final_B_compra.get(),sub_total_D_c  ,sub_total_B_c  ,depart_c.get()
				print(datos,'datos_compras')
				micursor.execute("INSERT INTO PRODUCTOS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,NULL,?)",(datos))
				

				miconexion.commit()



				producto_C.set(identificador_compra.get())
				ingresar_ID_en_compras('1')




				prod.destroy()
		

			except sqlite3.IntegrityError:
				messagebox.showwarning('Lumina','El identificador ya existe',parent=prod)
				identificador_compra.set('')
				return

			except sqlite3.OperationalError:
				messagebox.showwarning('Lumina','Base de datos no creada',parent=prod)
				return

			except TclError:
				messagebox.showerror('BBDD','Faltan campos por escribir',parent=prod)	
				return





		identificador=Entry(prod,font='Helvetica 12',bd=7,width=25,relief='sunken',textvariable=identificador_compra)
		identificador.grid(row=3,column=1,sticky='NSEW',ipady=4)
		
		identificador.bind('<Return>',siguiente_compras_productos) 
			
		productodos=Entry(prod,font='Helvetica 12',bd=7,relief='sunken',textvariable=producto_compra)
		productodos.grid(row=5,column=1,sticky='NSEW',columnspan=3,ipady=4)
		productodos.bind('<Return>',siguiente_compras_productos) 



		frame=Frame(prod,bg='#d5b8f8',padx=10)
		frame.grid(row=2,column=5,sticky='NSEW',rowspan=2)

		prod.columnconfigure(7,weight=1)

		cantidad=Entry(frame,font='Helvetica 12',width=10,bd=7, relief='sunken',textvariable=cantidad_producto_compra)
		cantidad.grid(row=2,column=0,sticky='NSEW',ipady=4)
		cantidad.bind('<Return>',siguiente_compras_productos) 



		productodos3=Entry(frame,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_inicial_D_compra)
		productodos3.grid(row=2,column=2,sticky='NSEW',padx=10,ipady=4)
		productodos3.bind('<Return>',siguiente_compras_productos) 


		productodos3.bind('<KeyRelease>',calcular_tasa_compra_dolar)

		precio_descuento=Entry(frame,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_inicial_B_compra)
		precio_descuento.grid(row=2,column=4,sticky='NSEW',ipady=4)
		precio_descuento.bind('<Return>',siguiente_compras_productos)
		precio_descuento.bind('<KeyRelease>',calcular_tasa_compra_bolivar)



		frame2=Frame(prod,bg='#d5b8f8')
		frame2.grid(row=4,column=5,sticky='NSEW',rowspan=2,padx=10)

		descuento=Entry(frame2,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=porcentaje_compra)
		descuento.grid(row=2,column=0,sticky='NSW')
		descuento.bind('<KeyRelease>',calcular_de_precio_inicial)
		descuento.bind('<Return>',siguiente_compras_productos)




		

		


		


		descuento4=Entry(frame2,font='Helvetica 12',bd=7,width=12,relief='sunken',textvariable=precio_final_B_compra)
		descuento4.grid(row=2,column=4,sticky='NSW')

		def focus_agregar_compra(event):
			agregar.focus()

		descuento4.bind('<KeyRelease>',calcular_porcentaje)
		descuento4.bind('<Return>',focus_agregar_compra)






		

		depart_c= ttk.Combobox(frame2)
		depart_c.config(font='Helvetica 15',state='readonly',width=12)
		ver_departamentos_compras()
		
		depart_c.grid(row=2,column=3,padx=20,sticky='SE',pady=4)
		depart_c.current(0)

		funcion_provisional()

		ttk.Style().configure('blue.TCheckbutton', foreground='black', background='#d5b8f8',font='Helvetica 15')

		Button(frame2,text='Resultado',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=lambda:calcular_de_precio_inicial('1')).grid(row=2,column=2,sticky='W',padx=2)
		ch=ttk.Checkbutton(frame2, text="Exento",style='blue.TCheckbutton',variable=exento_compra)
		ch.grid(row=2,column=1,sticky='e',padx=20)
		ch.bind('<KeyRelease>',calcular_de_precio_inicial)



		combo2 = ttk.Combobox(frame)
		combo2.config(font='Helvetica 15',state='readonly',width=12)
		combo2['values']= ('Unidad','Kilogramos','Litros','Metros')
		combo2.current(0)
		combo2.grid(row=2,column=5,padx=10,sticky='SE',pady=4)

		descuento2=Entry(frame,font='Helvetica 12',state='readonly',width=10,bd=7,relief='sunken',textvariable=precio_final_D_compra)
		descuento2.grid(row=2,column=6,sticky='NSW',padx=10,ipadx=4)


	#--------------------------------LABEL-----------------------------------


		identificadorL=Label(prod,text='Codigo',font='Helvetica 12',bg='#d5b8f8')
		identificadorL.grid(row=2,column=1,sticky='NSEW',pady=10)


		nombre_descuentoL=Label(prod,text='Producto',font='Helvetica 12',bg='#d5b8f8')
		nombre_descuentoL.grid(row=4,column=1,sticky='NSEW',pady=10)

		

		productoL2=Label(frame,text='Cantidad',font='Helvetica 12',bg='#d5b8f8')
		productoL2.grid(row=1,column=0,pady=10)

		productoL=Label(frame,text='Precio $',font='Helvetica 12',bg='#d5b8f8')
		productoL.grid(row=1,column=2,pady=10)

		cantidadL=Label(frame,text='Precio Bs.S',font='Helvetica 12',bg='#d5b8f8')
		cantidadL.grid(row=1,column=4,pady=10)

		porcentanjeL2=Label(frame,text='P. Final $',font='Helvetica 12',bg='#d5b8f8')
		porcentanjeL2.grid(row=1,column=6,sticky='w',pady=10,padx=20)



		porcentanjeL=Label(frame2,text='% Ganancia',font='Helvetica 12',bg='#d5b8f8')
		porcentanjeL.grid(row=1,column=0,sticky='w',pady=10,padx=7)


		
		porcentanjeL2=Label(frame2,text='P. Final Bs.S',font='Helvetica 12',bg='#d5b8f8')
		porcentanjeL2.grid(row=1,column=4,sticky='w',padx=10)

		Label(prod,bg='#d5b8f8').grid(row=10,column=3,pady=10,sticky='w')

		agregar=Button(frame2,text='Agregar',cursor='hand2',width=8,height=1,bd=7,relief='raised',font='Helvetica 12',command=crear_producto_en_compras)
		agregar.grid(row=1,column=5,padx=5)


	#---------------------------

		prod.columnconfigure(0,weight=1)
		prod.columnconfigure(8,weight=1)
		prod.rowconfigure(6,weight=1)
		

		


	
	#--------------------------------------------------------------------------------------
	com.configure(bg='#d5b8f8')

	#------------VARIABLES COMPRAS-------------
	def variables_compras():
		pass
		return
	proveedor_C=StringVar()
	paquetes_C=DoubleVar()
	und_paquete_C=DoubleVar()
	precio_D_paquete=DoubleVar()
	precio_B_paquete=DoubleVar()
	producto_C=StringVar()
	cantidad_C=DoubleVar()
	precio_D_unidad_C=DoubleVar()
	precio_B_unidad_C=DoubleVar()
	Tasa_del_dolar_C=DoubleVar()




	Total_D_compra=DoubleVar()
	Total_B_compra=DoubleVar()

	Sub_total_D_compra=DoubleVar()
	Sub_total_B_compra=DoubleVar()

	iva_D_compra=DoubleVar()
	iva_B_compra=DoubleVar()



	ver_tasa_moneda_compras()



	proveedor_C.set('')
	paquetes_C.set('')
	und_paquete_C.set('')
	precio_D_paquete.set('')
	precio_B_paquete.set('')
	producto_C.set('')
	cantidad_C.set('')
	precio_D_unidad_C.set('')
	precio_B_unidad_C.set('')


	def calcular_cantidad_c(event):

		
		try:
			if und_paquete_C.get()=='':
				pass
				return
		except TclError:
			cantidad_C.set('')
			return


		try:
			if paquetes_C.get()=='':
				pass
				
				return

		except TclError:

			a=und_paquete_C.get()*1

			cantidad_C.set(a)
			
			return


		if paquetes_C.get()==0:
			
			a=und_paquete_C.get()*1

			cantidad_C.set(a)
			return

		a=und_paquete_C.get()*paquetes_C.get()

		cantidad_C.set(a)




	def ver_compras():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		window=Toplevel(hija)
		window.title('Compras')
		window.geometry('1000x550')
		window.iconbitmap(logo)
		window.config(bg='#d5b8f8')
		window.resizable(0,0)
		buscar_compra=StringVar()

		def leer_todo_compras():
			record=lista1c.get_children()
			for element in record:
				lista1c.delete(element)
		
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute('SELECT * FROM COMPRAS WHERE BOOLEANOS=0 ')
			A=micursor.fetchall()
			for i in A:
				a0=round(i[2],2)
				a1=round(i[3],2)

				a2=round(i[4],2)
				a3=round(i[5],2)

				a4=round(i[6],2)
				a5=round(i[7],2)

				lista1c.insert('',0,text=i[12],values=(i[1],a0,a1,a2,a3,a4,a5))



		def buscar_compra_c(event):
			record=lista1c.get_children()
			for element in record:
				lista1c.delete(element)
		
		
			if len(buscar_compra.get())==0:
				
				leer_todo_compras()
				return

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute('SELECT * FROM COMPRAS WHERE BOOLEANOS=0 ')
			A=micursor.fetchall()
			for i in A:
				a00=str(i[0])
				r=a00.startswith(buscar_compra.get())
				k=str(i[1]).startswith(buscar_compra.get())
				j=str(i[8]).startswith(buscar_compra.get())


				if r==1 or k==1 or j==1:

					a0=round(i[2],2)
					a1=round(i[3],2)

					a2=round(i[4],2)
					a3=round(i[5],2)

					a4=round(i[6],2)
					a5=round(i[7],2)

					lista1c.insert('',0,text=i[0],values=(i[1],a0,a1,a2,a3,a4,a5))

		def hacer_pdf_compras():
				
			PDF=Toplevel(window)
			PDF.geometry('400x150')
			PDF.configure(bg='#d5b8f8')
			PDF.iconbitmap(logo)
			PDF.resizable(0,0)

			Label(PDF,font='Helvetica 12',text='Nombre del PDF',bg='#d5b8f8').place(x=100,y=20)

			nombre_PDF_producto.set('')
			ttt=Entry(PDF,font='Helvetica 12',bd=9,relief='sunken',textvariable=nombre_PDF_producto)
			ttt.place(x=40,y=50,width=240,height=41)
			ttt.focus()

			


			def dt(event):
				hacer_pdf_compras2()
				PDF.destroy()
				return

			ttt.bind('<Return>',dt)

			Button(PDF,font='Helvetica 12',bd=7,width=8,relief='raised',text='Aceptar',cursor='hand2',command=lambda:dt('1')).place(x=285,y=50)




		def hacer_pdf_compras2():

			def grouper(iterable, n):
				args = [iter(iterable)] * n
				return itertools.zip_longest(*args)
			def export_to_pdf(data):

				dsds=nombre_PDF_producto.get()
				fdfd=dsds+'.pdf'
				c = canvas.Canvas(fdfd, pagesize=A4)
				w, h = A4
				max_rows_per_page = 45
			    # Margin.
				x_offset = 50
				y_offset = 50
			    # Space between rows.
				padding = 17
			    
				xlist = [x + x_offset for x in [0,70, 180, 230, 320, 420, 520]]
				ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
			    
				for rows in grouper(data, max_rows_per_page):
					rows = tuple(filter(bool, rows))
					c.grid(xlist, ylist[:len(rows) + 1])
					for y, row in zip(ylist[:-1], rows):
						for x, cell in zip(xlist, row):
							c.drawString(x + 2, y - padding + 3, str(cell))
							#c.setFont("Helvetica", 12)

					c.showPage()

				c.save()



			if len(buscar_compra.get())==0:
				
				data = [('CODIGO',"RIF", "FECHA", "SUB TOTAL", "IVA", "TOTAL")]

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM COMPRAS WHERE BOOLEANOS=0")
				A=micursor.fetchall()
				for i in A:
					
	
					a0=round(i[2],1)
					a1=round(i[3],1)

					a2=round(i[4],1)
					a3=round(i[5],1)

					a4=round(i[6],1)
					a5=round(i[7],1)

					fec=i[8]
					hor=i[9]


						
					data.append((i[0],i[1],fec,a1,a3,a5))


				export_to_pdf(data)

						
				messagebox.showinfo('BBDD','PDF de Compras creado con exito',parent=window)
					
				return


			data = [('CODIGO',"RIF", "FECHA", "SUB TOTAL", "IVA", "TOTAL")]

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM COMPRAS WHERE BOOLEANOS=0")
			A=micursor.fetchall()
			for i in A:
				a00=str(i[0])
				r=a00.startswith(buscar_compra.get())
				k=i[1].startswith(buscar_compra.get())
				j=i[8].startswith(buscar_compra.get())


				if r==1 or k==1 or j==1:
				
						
					a0=round(i[2],2)
					a1=round(i[3],2)

					a2=round(i[4],2)
					a3=round(i[5],2)

					a4=round(i[6],2)
					a5=round(i[7],2)

					fec=i[8]
					hor=i[9]


					
					data.append((i[0],i[1],fec,a1,a3,a5))


					export_to_pdf(data)

					
				messagebox.showinfo('BBDD','PDF de Compras creado con exito',parent=window)
				return











		def detalles_compras():


			try:
				id_ventas2=lista1c.item(lista1c.selection())['text']
				cedula_cliente=lista1c.item(lista1c.selection())['values'][0]
				sub_total_D=lista1c.item(lista1c.selection())['values'][1]
				sub_total_B=lista1c.item(lista1c.selection())['values'][2]
				iva_D=lista1c.item(lista1c.selection())['values'][3]
				iva_B=lista1c.item(lista1c.selection())['values'][4]
				total_D=lista1c.item(lista1c.selection())['values'][5]
				total_B=lista1c.item(lista1c.selection())['values'][6]


			except IndexError:
				pass
				return
			HORA=StringVar()
			FECHA=StringVar()
			TASA=DoubleVar()




			vpv=Toplevel(window)
			vpv.title('Detalles')
			vpv.geometry('700x532')
			vpv.iconbitmap(logo)
			vpv.resizable(0,0)
			vpv.configure(bg='#d5b8f8')
			tab_control = ttk.Notebook(vpv)
			hija=Frame(tab_control)
			ventana=Frame(tab_control)
			identifi=StringVar()

			tab_control.add(hija, text='Detalles')
			tab_control.pack(expand=1, fill='both')
			hija.config(bg='#d5b8f8')


			style = ttk.Style()
			style.configure("Treeview", font=('Helvetica', 10))

			lista_pV=ttk.Treeview(hija,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 6)])
			lista_pV.place(x=0,y=160)

			scoll=Scrollbar(hija,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll.place(x=680,y=185,height=320)
			lista_pV.config(yscrollcommand=scoll.set)

			lista_pV.heading('#0',text='Codigo',anchor=CENTER)
			lista_pV.heading('#1',text='Productos',anchor=CENTER)
			lista_pV.heading('#2',text='Cantidad',anchor=CENTER)
			lista_pV.heading('#3',text='Unidad',anchor=CENTER)
			lista_pV.heading('#4',text='Precio $',anchor=CENTER)
			lista_pV.heading('#5',text='Precio Bs.S',anchor=CENTER)

			lista_pV.column("#0",minwidth=100, width = 100)
			lista_pV.column("#1",minwidth=70, width = 220 )
			lista_pV.column("#2",minwidth=70, width = 60 )
			lista_pV.column("#3",minwidth=70, width = 50 )
			lista_pV.column("#4",minwidth=70, width = 110 )
			lista_pV.column("#5",minwidth=70, width = 160 )

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=id_ventas2,cedula_cliente
			micursor.execute("SELECT * FROM COMPRAS WHERE BOOLEANOS=0 AND ID_PIBOTE=? AND RIF_PROVEEDOR=? ORDER BY(ID_COMPRA)DESC",(datos))
			for i in micursor.fetchall():
				id_ventas=i[0]

			

			def ver_productos_de_la_venta_VPV():
				record=lista_pV.get_children()
				for element in record:
					lista_pV.delete(element)
	    
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				datos=id_ventas,cedula_cliente
				micursor.execute("SELECT * FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_COMPRA=? AND RIF_PROVEEDOR=? ORDER BY(ID_COMPRA)DESC",(datos))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:

					print(usuarios[5],'usuarios[4]')
					a000=usuarios[9]*usuarios[5]
					a111=usuarios[8]*usuarios[5]


					ad=round(a111,2)
					asd=round(a000,2)
					lista_pV.insert('',0,text=usuarios[3],values=(usuarios[4],usuarios[5],usuarios[7],ad,asd))
					

			def ver_fecha_y_hora_VPV():
				record=lista_pV.get_children()
				for element in record:
					lista_pV.delete(element)
	    
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM COMPRAS WHERE BOOLEANOS=0 AND ID_COMPRA=? ORDER BY(ID_COMPRA)DESC",(id_ventas, ))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					a=str(usuarios[8])
					b=str(usuarios[9])
					FECHA.set(a)
					HORA.set(b)
					TASA.set(usuarios[10])

					sub_total_BB=round(usuarios[3],2)
					sub_total_DD=round(usuarios[2],2)
					iva_BB=round(usuarios[4],2)
					iva_DD=round(usuarios[5],2)
					total_BB=round(usuarios[7],2)
					total_DD=round(usuarios[6],2)

				

				micursor.execute("SELECT * FROM PROVEEDORES WHERE RIF_PROVEEDOR=?",(cedula_cliente, ))
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					nombre_cliente=usuarios[1]


				limpiar_cuadros_Text_VPV()
				agregar_a_suma_VPV(TASA.get(),nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD)



		
			def limpiar_cuadros_Text_VPV():
				tasa.configure(state='normal')
				tasa.delete('1.0', END)
				tasa.configure(state='disabled')

				cliente_tex.configure(state='normal')
				cliente_tex.delete('1.0',END)
				cliente_tex.configure(state='disabled')

				Total_B22.configure(state='normal')
				Total_B22.delete('1.0', END)
				Total_B22.configure(state='disabled')

				Total_D22.configure(state='normal')
				Total_D22.delete('1.0',END)
				Total_D22.configure(state='disabled')

				Total_D33.configure(state='normal')
				Total_D33.delete('1.0',END)
				Total_D33.configure(state='disabled')
		


			def agregar_a_suma_VPV(tasad,nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD):
		

				tasa.configure(state='normal')
				tasa_f = round(tasad,2)
				tasa.insert(END, tasa_f)
				tasa.configure(state='disabled')

				cliente_tex.configure(state='normal')
				cliente_tex.insert(END,nombre_cliente)
				cliente_tex.configure(state='disabled')


				Total_B22.configure(state='normal')
				dinero = sub_total_BB
				dinero2 =sub_total_DD
				a=dinero,'(',dinero2,')'
				Total_B22.insert(END, a)
				Total_B22.configure(state='disabled')



				Total_D22.configure(state='normal')
				dinero5 = iva_BB
				dinero6 =iva_DD
				c=dinero6,'(',dinero5,')'
				Total_D22.insert(END,c)
				Total_D22.configure(state='disabled')


				Total_D33.configure(state='normal')
				dinero3 = total_BB
				dinero4 = total_DD
				b=dinero3,'(',dinero4,')'
				Total_D33.insert(END,b)
				Total_D33.configure(state='disabled')

				Label(hija,text=FECHA.get(),bg='#d5b8f8',font='Helvetica 12').place(x=55,y=0)

				Label(hija,text=HORA.get(),bg='#d5b8f8',font='Helvetica 12').place(x=55,y=40)

				return


			def hacer_pdf_compras_detalles():
			
			

				total_pdf_D=DoubleVar()
				total_pdf_B=DoubleVar()

				iva_pdf_D=DoubleVar()
				iva_pdf_B=DoubleVar()

				sub_total_pdf_D=DoubleVar()
				sub_total_pdf_B=DoubleVar()

				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()

				micursor.execute("SELECT * FROM COMPRAS WHERE ID_PIBOTE=?",(id_ventas2, ))
				B=micursor.fetchall()
				for g in B:
					if g[0]<10:
						numero_de_factura='00000'+str(g[0])
					elif g[0]<100:
						numero_de_factura='0000'+str(g[0])

					elif g[0]<1000:
						numero_de_factura='000'+str(g[0])

					elif g[0]<10000:
						numero_de_factura='00'+str(g[0])

					elif g[0]<100000:
						numero_de_factura='0'+str(g[0])

					else:
						numero_de_factura=str(g[0])
					control_f=str(g[12])
					rif_pro=g[1]
					fechita=g[8]
					tasa2=g[7]
					micursor.execute("SELECT * FROM PROVEEDORES WHERE RIF_PROVEEDOR=?",(g[1], ))
					for i in micursor.fetchall():
						nombre_pro=i[1]
						direccion_pro=i[4]
						tele_pro=i[3]


				a0='Factura '+control_f+'.pdf'
				c=canvas.Canvas(a0,pagesize=letter)



				text = c.beginText(50, 730)
				#Una vez hecho esto, procedemos a configurar a partir del objeto creado los distintos estilos. Por ejemplo, aquí también tenemos un método setFont(), pero que actúa sobre este objeto en particular y no sobre el resto de la hoja.
				text.setFont("Helvetica", 16)
				text.textLines("PROVEEDOR:" +str(nombre_pro)+"\nRIF: "+str(rif_pro))
				c.drawText(text)



				text2 = c.beginText(50, 690)
				#Una vez hecho esto, procedemos a configurar a partir del objeto creado los distintos estilos. Por ejemplo, aquí también tenemos un método setFont(), pero que actúa sobre este objeto en particular y no sobre el resto de la hoja.
				text2.setFont("Helvetica", 16)
				text2.textLines("DIRECCIÓN: "+str(direccion_pro)+"\nTELEFONO: "+str(tele_pro))
				c.drawText(text2)


				text3 = c.beginText(480, 700)
				#Una vez hecho esto, procedemos a configurar a partir del objeto creado los distintos estilos. Por ejemplo, aquí también tenemos un método setFont(), pero que actúa sobre este objeto en particular y no sobre el resto de la hoja.
				text3.setFont("Helvetica", 14)
				text3.textLines("Compra\nNo  "+str(numero_de_factura)+"\n\nCodigo F.\n"+str(control_f))
				c.drawText(text3)

				text4 = c.beginText(50, 650)
				#Una vez hecho esto, procedemos a configurar a partir del objeto creado los distintos estilos. Por ejemplo, aquí también tenemos un método setFont(), pero que actúa sobre este objeto en particular y no sobre el resto de la hoja.
				text4.setFont("Helvetica", 16)
				text4.textLines("Fecha: "+fechita)
				c.drawText(text4)

				

				def grouper2(iterable, n):
					args = [iter(iterable)] * n
					return itertools.zip_longest(*args)
				def export_to_pdf2(data):
					print(data,'data')
					w, h = A4
					max_rows_per_page = 45
					    # Margin.
					x_offset = 100
					y_offset = 250
					    # Space between rows.
					padding = 15
					    
					xlist = [x + x_offset for x in [0,50,200,270,340,450]]
					ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
					contador=0
					for rows in grouper2(data, max_rows_per_page):
						rows = tuple(filter(bool, rows))
						c.grid(xlist, ylist[:len(rows) + 1])
						for y, row in zip(ylist[:-1], rows):
							for x, cell in zip(xlist, row):
								contador=contador+1
								c.drawString(x+2, y - padding + 3, str(cell))
								print(contador,hola*5)
								if contador==hola*5:
									text5 = c.beginText(x-50, y-50)
									text5.setFont("Helvetica", 12)
									text5.textLines("TASA: "+str(tasa2)+"\n\nSUB-TOTAL: "+str(sub_total_pdf_B.get())+"\nI.V.A.: "+str(iva_pdf_B.get())+"\nTOTAL A PAGAR: "+str(total_pdf_B.get()))
									c.drawText(text5)
						c.showPage()

					c.save()
				data = [('CANT.',"DESCRIPCION", "P.UNIT", "Alic.%", "TOTAL Bs.")]

				contador=0
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=id_ventas
				micursor.execute("SELECT * FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_COMPRA=?",(datos, ))
				a=micursor.fetchall()
				for g in a:
					contador=contador+1

					
					total_pdf_B.set(g[9]+total_pdf_B.get())

					sub_total_pdf_B.set(g[15]+sub_total_pdf_B.get())


				iva_pdf_B.set(round(total_pdf_B.get()-sub_total_pdf_B.get(),2))

				total_pdf_B.set(round(total_pdf_B.get(),2))

				sub_total_pdf_B.set(round(sub_total_pdf_B.get(),2))



				datos=id_ventas
				micursor.execute("SELECT * FROM PRODUCTOS_COMPRAS WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_COMPRA=?",(datos, ))
				C=micursor.fetchall()
				for i in C:


					b=i[0]



					hola=contador
					punit=i[9]/i[5]

					print(str(i[5]),str(i[4]),str(round(punit,2)),str(i[6]),str(i[11]))
					data.append((str(i[5]),str(i[4]),str(round(punit,2)),str(i[6]),str(i[9])))
				export_to_pdf2(data)

				messagebox.showinfo('BBDD','el Pdf de la Compra No {} fue creado con exito'.format(id_ventas2),parent=hija)








			
			Label(hija,text='Fecha',font='Helvetica 12',bg='#d5b8f8').place(x=0,y=0)


			Label(hija,text='Hora:',font='Helvetica 12',bg='#d5b8f8').place(x=0,y=40)


			Label(hija,text='Tasa:',font='Helvetica 12',bg='#d5b8f8').place(x=0,y=80)

			tasa=Text(hija,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#d5b8f8')
			tasa.place(x=55,y=80)

			Label(hija,text='Proveedor:',bg='#d5b8f8',font='Helvetica 12').place(x=0,y=120)

			cliente_tex=Text(hija,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#d5b8f8')
			cliente_tex.place(x=85,y=120)
			



			Button(hija,text='PDF',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=hacer_pdf_compras_detalles).place(x=240,y=120)


			totales=Frame(hija)
			totales.configure(bg='#b699f8',width=370,height=157)
			totales.place(x=343,y=0)

			Label(totales,text='Sub Total ($):',font='Helvetica 12',bg='#b699f8',fg='black').place(x=10,y=20)
			Label(totales,text='I.V.A ($):',font='Helvetica 12',bg='#b699f8',fg='black').place(x=45,y=60)
			Label(totales,text='Total ($):',font='Helvetica 12',bg='#b699f8',fg='black').place(x=45,y=100)


			Total_B22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b699f8')
			Total_B22.place(x=115,y=21)

			Total_D22=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b699f8')
			Total_D22.place(x=115,y=62)

			Total_D33=Text(totales,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b699f8')
			Total_D33.place(x=115,y=103)


			ver_fecha_y_hora_VPV()

			ver_productos_de_la_venta_VPV()


			

		lista1c=ttk.Treeview(window,height=20,style='Treeview',columns=[f"#{n}" for n in range(1, 8)])
		lista1c.pack(expand=1,fill=BOTH)
		lista1c.place(x=0,y=80)
		



		scoll=Scrollbar(window,command=lista1c.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=984,y=103,height=403)


		lista1c.config(yscrollcommand=scoll.set)

		lista1c.heading('#0',text='Codigo')
		lista1c.heading('#1',text='Rif Proveedor')
		lista1c.heading('#2',text='Sub total $')
		lista1c.heading('#3',text='Sub total Bs.S')
		lista1c.heading('#4',text='I.V.A. $')
		lista1c.heading('#5',text='I.V.A. Bs.S')
		lista1c.heading('#6',text='Total $')
		lista1c.heading('#7',text='Total Bs.S')
		

		lista1c.column("#0",minwidth=70, width = 120)
		lista1c.column("#1",minwidth=70, width = 127)
		lista1c.column("#2",minwidth=70, width = 127)
		lista1c.column("#3",minwidth=70, width = 127)
		lista1c.column("#4",minwidth=70, width = 127)
		lista1c.column("#5",minwidth=70, width = 127)
		lista1c.column("#6",minwidth=70, width = 127)
		lista1c.column("#7",minwidth=70, width = 127)


		bus2=Entry(window,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=buscar_compra)
		bus2.place(x=0,y=10,height=41)
		Button(window,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=buscar_compra_c('1')).place(x=200,y=10)
		bus2.bind('<KeyRelease>',buscar_compra_c)



		Button(window,text='Detalles',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=detalles_compras).place(x=0,y=508)
		Button(window,text='   PDF  ',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=hacer_pdf_compras).place(x=90,y=508)


		leer_todo_compras()




	style = ttk.Style()
	style.configure("Treeview", highlightthickness=0, bd=0, font=('Helvetica', 10))


	frame_lista_compra=Frame(com,bg='#b699f8')
	frame_lista_compra.grid(row=1,column=0,sticky='NSEW',columnspan=2)

	lista_compra=ttk.Treeview(frame_lista_compra,style='Treeview',columns=[f"#{n}" for n in range(1, 9)])
	lista_compra.pack(expand=1,fill=BOTH)
	lista_compra.grid(row=0,column=0,sticky='nsew',columnspan=4,rowspan=4)
	frame_lista_compra.rowconfigure(1,weight=5)
	frame_lista_compra.columnconfigure(0,weight=5)


	scoll=Scrollbar(frame_lista_compra,command=lista_compra.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=1,column=1,sticky='NSEW')

	

	lista_compra.config(yscrollcommand=scoll.set)

	lista_compra.heading('#0',text='Codigo')
	lista_compra.heading('#1',text='Productos')
	lista_compra.heading('#2',text='Cantidad')
	lista_compra.heading('#3',text='Unidad')
	lista_compra.heading('#4',text='Departamento')
	lista_compra.heading('#5',text='Precio $')
	lista_compra.heading('#6',text='Precio Bs.S')
	lista_compra.heading('#7',text='Total $')
	lista_compra.heading('#8',text='Total Bs.S')


	lista_compra.column("#0",minwidth=70, width = 100)
	lista_compra.column("#1",minwidth=70, width = 240)
	lista_compra.column("#2",minwidth=70, width = 50)
	lista_compra.column("#3",minwidth=70, width = 30)
	lista_compra.column("#4",minwidth=70, width = 100)
	lista_compra.column("#5",minwidth=70, width = 100)
	lista_compra.column("#6",minwidth=70, width = 100)
	lista_compra.column("#7",minwidth=70, width = 100)
	lista_compra.column("#8",minwidth=70, width = 140)
	




	miframe_compra=Frame(com)
	miframe_compra.configure(bg='#b699f8',width=240,height=199)
	miframe_compra.grid(column=1,row=0,sticky='NSE')

	Label(miframe_compra,text='Sub Total ($):',font='Helvetica 14',bg='#b699f8',fg='black').grid(row=3,column=0,pady=20,padx=5)
	Label(miframe_compra,text='I.V.A ($)',font='Helvetica 14',bg='#b699f8',fg='black').grid(row=5,column=0,padx=5)
	Label(miframe_compra,text='Total ($):',font='Helvetica 14',bg='#b699f8',fg='black').grid(row=7,column=0,padx=5,pady=20)


	total_compra1=Text(miframe_compra,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b699f8')
	total_compra1.grid(row=3,column=1,columnspan=2)

	total_compra2=Text(miframe_compra,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b699f8')
	total_compra2.grid(row=5,column=1,columnspan=2)

	total_compra3=Text(miframe_compra,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b699f8')
	total_compra3.grid(row=7,column=1,columnspan=2)

	agregar_a_suma_compras(0.0,0.0,0.0,0.0,0.0,0.0)

	raiz2_compra=Frame(com,bg='#d5b8f8')
	raiz2_compra.grid(row=0,column=0,sticky='nwse')
	miframe_compra.columnconfigure(1,weight=3)
	miframe_compra.rowconfigure(9,weight=6)

	
	Label(raiz2_compra,text='Proveedor',font='Helvetica 12',bg='#d5b8f8',fg='black').grid(row=0,column=0,sticky='w',padx=22,pady=10)
	client=Entry(raiz2_compra,font='Helvetica 12',width=12,fg='black',bd=7,relief='sunken',textvariable=proveedor_C)
	client.grid(row=1,column=0,sticky='wns')
	client.focus()
	
	cliente_c_c=Text(raiz2_compra,font='Helvetica 18',state='disabled',bg='#d5b8f8',relief='flat',height=1,width=25)
	cliente_c_c.grid(row=0,column=0,sticky='w',padx=150,columnspan=2)


	f1_compra=Frame(raiz2_compra,bg='#d5b8f8')
	f1_compra.grid(row=4,column=0,sticky='nswe')
	f1_compra.rowconfigure(0,weight=1)
	
	x=Label(f1_compra,text='Codigo / Producto',font='Helvetica 12',bg='#d5b8f8')
	x.grid(row=7,column=0,pady=10)

	d=Label(f1_compra,text='Cantidad',font='Helvetica 12',bg='#d5b8f8')
	d.grid(row=7,column=1,pady=10)

	Label(f1_compra,text='Precio $',font='Helvetica 12',bg='#d5b8f8').grid(row=7,column=2)
	Label(f1_compra,text='Precio Bs',font='Helvetica 12',bg='#d5b8f8').grid(row=7,column=3)

	
	f2=Frame(f1_compra,bg='#d5b8f8')
	f2.grid(row=5,column=0,columnspan=5,sticky='nsew')
	

	Label(f2,text='Paquetes',font='Helvetica 12',bg='#d5b8f8').grid(row=4,column=0)
	Label(f2,text='Unidades',font='Helvetica 12',bg='#d5b8f8').grid(row=4,column=1)
	Label(f2,text='Precio $',font='Helvetica 12',bg='#d5b8f8').grid(row=4,column=2)
	Label(f2,text='Precio Bs',font='Helvetica 12',bg='#d5b8f8').grid(row=4,column=3)

	e0=Entry(f2,font='Helvetica 12',bd=7,relief='sunken',width=7,textvariable=paquetes_C)
	e0.grid(row=5,column=0,sticky='nsew',padx=1,columnspan=1)

	def siguiente_compras(event):
		event.widget.tk_focusNext().focus()
		return

	e0.bind('<Return>', siguiente_compras)

	e0.bind('<KeyRelease>',calcular_cantidad_c)

	e1=Entry(f2,font='Helvetica 12',bd=7,relief='sunken',width=7,textvariable=und_paquete_C)
	e1.grid(row=5,column=1,sticky='nsew',padx=1)

	e1.bind('<Return>', siguiente_compras)

	e1.bind('<KeyRelease>',calcular_cantidad_c)

	

	e2=Entry(f2,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_D_paquete)
	e2.grid(row=5,column=2,sticky='NSEW',ipady=4)
	e2.bind('<Return>', siguiente_compras)

	e2.bind('<KeyRelease>',calcular_precio_B_paquete)
	
	e3=Entry(f2,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_B_paquete)
	e3.grid(row=5,column=3,sticky='NSEW',ipady=4)
	e3.bind('<Return>', siguiente_compras)

	e3.bind('<KeyRelease>',calcular_precio_D_paquete)

	Label(f2,font='Helvetica 12',bg='#d5b8f8').grid(row=5,column=4,pady=7)


	product_compra=Entry(f1_compra,font='Helvetica 12',bd=7,relief='sunken',textvariable=producto_C)
	product_compra.grid(row=8,column=0,sticky='nsew')
	product_compra.bind('<Return>',ingresar_ID_en_compras)


	

	canti=Entry(f1_compra,font='Helvetica 12',bd=7,relief='sunken',width=7,textvariable=cantidad_C)
	canti.grid(row=8,column=1,sticky='nsew',padx=1)

	canti.bind('<Return>', siguiente_compras)

	precio_D_c_=Entry(f1_compra,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_D_unidad_C)
	precio_D_c_.grid(row=8,column=2,sticky='NSEW',ipady=4)
	
	precio_D_c_.bind('<Return>', siguiente_compras)
	precio_D_c_.bind('<KeyRelease>', calcular_precio_D_unidad)

	precio_B_c_=Entry(f1_compra,font='Helvetica 12',width=10,bd=7,relief='sunken',textvariable=precio_B_unidad_C)
	precio_B_c_.grid(row=8,column=3,sticky='NSEW',ipady=4)
	precio_B_c_.bind('<KeyRelease>', calcular_precio_B_unidad)


	def focus_boton_compras(event):
		boton_c.focus()
		return

	precio_B_c_.bind('<Return>', focus_boton_compras)




	unidad_compra_label=Label(f1_compra,font='Helvetica 12',text='UND',bg='#d5b8f8',fg='#d5b8f8',pady=10)
	unidad_compra_label.grid(row=8,column=4,padx=1)


	Button(raiz2_compra,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:verificar_proveedor_C('1')).grid(row=1,column=0,sticky='w',padx=130)
	client.bind('<Return>',verificar_proveedor_C)


	boton_c=Button(f1_compra,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:ingresar_ID_en_compras('1'))
	boton_c.grid(row=8,column=5)

	boton_c.bind('<Return>', ingresar_ID_en_compras)

	botones_compra=Frame(com)
	botones_compra.configure(bg='#949494',width=1023,height=60)
	botones_compra.grid(row=2,column=0,sticky='ew',columnspan=2)

	Button(botones_compra,text='Borrar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=comprobacion_borrar_producto_en_compra).grid(row=0,column=0,padx=1,pady=5)
	Button(botones_compra,text='Editar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=editar_producto_de_C).grid(row=0,column=1,padx=1,pady=5)
	Button(botones_compra,text='Buscador',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=buscar_P_PRO_en_com).grid(row=0,column=2,padx=1,pady=5)
	Button(botones_compra,text='Tasa C.',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=ver_tasa_monedas_compras).grid(row=0,column=4,padx=1,pady=5)
	Button(botones_compra,text='Compras',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=ver_compras).grid(row=0,column=5,padx=1,pady=5)

	Button(botones_compra,text='Comprar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=comprar).grid(row=0,column=7,sticky='e',padx=5)


	raiz2_compra.rowconfigure(3,weight=10)
	botones_compra.columnconfigure(6,weight=1)
	botones_compra.rowconfigure(0,weight=1)

	com.rowconfigure(0,weight=1)
	com.columnconfigure(1,weight=1)

	com.columnconfigure(0, weight=1)
	com.rowconfigure(1, weight=3)

	

	clock_compras=Label(miframe_compra,text=fecha,font='Consolas 14',fg='#b699f8',bg='#b699f8')
	clock_compras.grid(row=1,column=2,sticky='ne')
	

	Label(miframe_compra,text=fecha,font='Consolas 14',bg='#b699f8',fg='black').grid(row=0,column=2,sticky='ne')





	menu_com = Menu(com, tearoff=0)
	menu_com.add_command(label='Resultado           ',underline=1, accelerator="Ctrl+R")
	menu_com.add_command(label='Detalles           ',underline=1, accelerator="Ctrl+D")
	menu_com.add_separator()
	menu_com.add_command(label='Limpiar           ',underline=1, accelerator="Ctrl+L",command=limpiar_campos_en_com)


	def click_derecho_compras(event):
		try:
			menu_com.post(event.x_root, event.y_root)
		finally:
			menu_com.grab_release()


	
	lista_compra.bind("<Button-3>", click_derecho_compras)
	raiz2_compra.bind("<Button-3>", click_derecho_compras)
	f1.bind("<Button-3>", click_derecho_compras)
	f2.bind("<Button-3>", click_derecho_compras)
	f1_compra.bind("<Button-3>", click_derecho_compras)
	miframe_compra.bind("<Button-3>", click_derecho_compras)
	botones_compra.bind("<Button-3>", click_derecho_compras)





	#----------------DEUDORES----------------------
	def deudores():
		pass
	buscar_deudor=StringVar()
	deu.config(bg='#b6bdff')

	FECHA_d=StringVar()
	HORA_d=StringVar()
	TASA_d=DoubleVar()


	def leer_todo_deudores():
		record=lista1d.get_children()
		for element in record:
			lista1d.delete(element)

		total_sumita_B=DoubleVar()
		total_sumita_D=DoubleVar()

		sub_total_sumita_B=DoubleVar()
		sub_total_sumita_D=DoubleVar()

		iva_total_sumita_D=DoubleVar()
		iva_total_sumita_B=DoubleVar()

		identifici=StringVar()
		cedulin=IntVar()


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM DEUDAS WHERE BOOLEANOS=0")
		sddd=micursor.fetchall()
		for i in sddd:
			identifici.set(i[0])
			cedulin.set(i[1])

			datos=identifici.get(),cedulin.get()
			
			micursor.execute('SELECT * FROM PRODUCTOS_DEUDAS WHERE IDENTIFICADOR_DE_DEUDA=? AND C_CLIENTE=?',(datos))
			A=micursor.fetchall()
			for i0 in A:
				identifi=i0[3]
				micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(identifi, ))
				B=micursor.fetchall()
				for i1 in B:
					micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(i1[13], ))
					C=micursor.fetchall()
					for i2 in C:
						tasa_d=i2[0]

					total_sumita_D.set(round(i[7],2))
					a=tasa_d*i1[8]
					total_sumita_B.set(round(i[6],2))

					iva0=i1[8]-i1[10]
					iva_total_sumita_D.set(round(i[4],2))
					b=iva0*tasa_d
					iva_total_sumita_B.set(round(i[5],2))


					c=i1[10]*tasa_d
					sub_total_sumita_D.set(round(i[3],2))
					sub_total_sumita_B.set(round(i[2],2))

						#------------------------------
					print(total_sumita_B.get(),'nose que pasa')
					

			

			'''micursor.execute('SELECT * FROM PRODUCTOS_DEUDAS WHERE IDENTIFICADOR_DE_DEUDA=?',(i[1], ))
			X=micursor.fetchall()
			for i10 in X:
				total_sumita_D.set(round(total_sumita_D.get()*i10[5],2))
				total_sumita_B.set(round(total_sumita_B.get()*i10[5],2))

						
				iva_total_sumita_D.set(round(i10[5]*iva_total_sumita_D.get(),2))
						
				iva_total_sumita_B.set(round(iva_total_sumita_B.get()*i10[5],2))


						
				sub_total_sumita_D.set(round(sub_total_sumita_D.get()*i10[5],2))
				sub_total_sumita_B.set(round(sub_total_sumita_B.get()*i10[5],2))
						
			print(total_sumita_B.get(),'nose que pasa2')'''

			lista1d.insert('',0,text=i[0],values=(i[1],i[8],sub_total_sumita_D.get(),sub_total_sumita_B.get(),iva_total_sumita_D.get(),iva_total_sumita_B.get(),total_sumita_D.get(),total_sumita_B.get()))
			total_sumita_D.set(0)
			total_sumita_B.set(0)

			iva_total_sumita_D.set(0)
			iva_total_sumita_B.set(0)

			sub_total_sumita_D.set(0)
			sub_total_sumita_B.set(0)




	def buscar_deudores_d():
		total_sumita_B=DoubleVar()
		total_sumita_D=DoubleVar()

		sub_total_sumita_B=DoubleVar()
		sub_total_sumita_D=DoubleVar()

		iva_total_sumita_D=DoubleVar()
		iva_total_sumita_B=DoubleVar()
		if len(buscar_deudor.get())==0:
			record=lista1d.get_children()
		
			leer_todo_deudores()
		
		else:
			record=lista1d.get_children()
		
			for element in record:
				lista1d.delete(element)
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM DEUDAS WHERE BOOLEANOS=0")
			elusuario=micursor.fetchall()
			for i in elusuario:

				r=str(i[0]).startswith(buscar_deudor.get())
				k=str(i[1]).startswith(buscar_deudor.get())
				f=i[8].startswith(buscar_deudor.get())
				if r==1 or k==1 or f==1:
					total_sumita_D.set(round(i[7],2))
					total_sumita_B.set(round(i[6],2))

					iva_total_sumita_D.set(round(i[4],2))
					iva_total_sumita_B.set(round(i[5],2))

					sub_total_sumita_D.set(round(i[3],2))
					sub_total_sumita_B.set(round(i[2],2))

				

					lista1d.insert('',0,text=i[0],values=(i[1],i[8],sub_total_sumita_D.get(),sub_total_sumita_B.get(),iva_total_sumita_D.get(),iva_total_sumita_B.get(),total_sumita_D.get(),total_sumita_B.get()))
					total_sumita_D.set(0)
					total_sumita_B.set(0)

					iva_total_sumita_D.set(0)
					iva_total_sumita_B.set(0)

					sub_total_sumita_D.set(0)
					sub_total_sumita_B.set(0)
					miconexion.commit()

	def Detalles_deu():
		try:
			A1=lista1d.item(lista1d.selection())['text']
			A2=lista1d.item(lista1d.selection())['values'][0]
			A3=lista1d.item(lista1d.selection())['values'][1]
			A4=lista1d.item(lista1d.selection())['values'][2]
			A5=lista1d.item(lista1d.selection())['values'][3]
			A6=lista1d.item(lista1d.selection())['values'][4]
			A7=lista1d.item(lista1d.selection())['values'][5]
			A8=lista1d.item(lista1d.selection())['values'][6]
			A9=lista1d.item(lista1d.selection())['values'][7]


		except IndexError:
			pass
			return
		
		vpv=Toplevel(deu)
		vpv.title('Detalles')
		vpv.geometry('700x562')
		vpv.iconbitmap(logo)
		vpv.resizable(0,0)
		vpv.configure(bg='#b6bdff')
		tab_control = ttk.Notebook(vpv)
		actual=Frame(tab_control)
		viejo=Frame(tab_control)
		
		tab_control.add(actual, text='Actual')
		tab_control.add(viejo, text='Antiguo')
		tab_control.pack(expand=1, fill='both')
		actual.config(bg='#b6bdff')
		viejo.config(bg='#b6bdff')

		style = ttk.Style()
		style.configure("Treeview", font=('Helvetica', 10))

		total_sumita_B=DoubleVar()
		total_sumita_D=DoubleVar()

		sub_total_sumita_B=DoubleVar()
		sub_total_sumita_D=DoubleVar()

		iva_total_sumita_D=DoubleVar()
		iva_total_sumita_B=DoubleVar()
		def ver_productos_de_la_deuda_d():
			record=lista_d_d.get_children()
			for element in record:
				lista_d_d.delete(element)
			
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=A1,A2
			
			micursor.execute("SELECT * FROM PRODUCTOS_DEUDAS WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_DEUDA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				
				micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(usuarios[3], ))
				A=micursor.fetchall()
				for i in A:
					preb=i[8]*usuarios[5]
					pred=i[10]*usuarios[5]



					print(preb)

					micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(i[13], ))
					B=micursor.fetchall()
					for x in B:

						fd=preb*x[0]
						sd=preb

						df=pred*x[0]
						fg=pred
						r=preb-pred
						g=r*x[0]
						print(g,r,fg,df,'qlqlqlqlqlqlqlqlql')
						total_sumita_D.set(sd+total_sumita_D.get())
						total_sumita_B.set(fd+total_sumita_B.get())

						iva_total_sumita_D.set(r+iva_total_sumita_D.get())
						iva_total_sumita_B.set(g+iva_total_sumita_B.get())

						sub_total_sumita_D.set(fg+sub_total_sumita_D.get())
						sub_total_sumita_B.set(df+sub_total_sumita_B.get())


				



						Total_D_d2.configure(state='normal')
						Total_D_d2.delete('1.0',END)
						Total_D_d2.configure(state='disabled')


						Total_D_d2.configure(state='normal')
						b=str(round(total_sumita_B.get(),2))+'('+str(round(total_sumita_D.get(),2))+')'
						Total_D_d2.insert(END,b)
						Total_D_d2.configure(state='disabled')

							#------------------

						Total_D_d.configure(state='normal')
						Total_D_d.delete('1.0',END)
						Total_D_d.configure(state='disabled')


						Total_D_d.configure(state='normal')
						c0=str(round(sub_total_sumita_B.get(),2))+'('+str(round(sub_total_sumita_D.get(),2))+')'

						c=str(round(iva_total_sumita_B.get(),2))+'('+str(round(iva_total_sumita_D.get(),2))+')'
						Total_D_d.insert(END,c)
						Total_D_d.configure(state='disabled')


							#-----------------
						Total_B_d.configure(state='normal')
						Total_B_d.delete('1.0',END)
						Total_B_d.configure(state='disabled')



						Total_B_d.configure(state='normal')
						Total_B_d.insert(END,c0)
						Total_B_d.configure(state='disabled')

						print('holaaa',total_sumita_B.get(),total_sumita_D.get(),iva_total_sumita_D.get(),iva_total_sumita_B.get())
						a0=round(sd,2)
						a1=round(fd,2)
						lista_d_d.insert('',0,text=usuarios[3],values=(usuarios[4],usuarios[5],usuarios[7],a0,a1))
							
				


		def ver_fecha_y_hora_d():
			
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM DEUDAS WHERE BOOLEANOS=0 AND ID_DEUDAS=?",(A1, ))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				a=str(usuarios[8])
				b=str(usuarios[9])
				FECHA_d.set(a)
				HORA_d.set(b)
				TASA_d.set(usuarios[10])

				sub_total_BB=A5
				sub_total_DD=usuarios[2]
				iva_BB=A7
				iva_DD=usuarios[4]
				total_BB=A9
				total_DD=usuarios[7]
				cajero=usuarios[12]
				caja=usuarios[13]


			cajero_la.config(text=cajero)
			caja_la.config(text=caja)

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(A2, ))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				nombre_cliente=usuarios[0]+' '+usuarios[1]


			limpiar_cuadros_Text_d()
			agregar_a_suma_d(tasa_del_dolar.get(),nombre_cliente,sub_total_sumita_B.get(),sub_total_sumita_D.get(),iva_total_sumita_B.get(),iva_total_sumita_D.get(),total_sumita_B.get(),total_sumita_D.get())
			total_sumita_D.set(0)
			total_sumita_B.set(0)

			iva_total_sumita_D.set(0)
			iva_total_sumita_B.set(0)

			sub_total_sumita_D.set(0)
			sub_total_sumita_B.set(0)


	
		def limpiar_cuadros_Text_d():
			tasa_d.configure(state='normal')
			tasa_d.delete('1.0', END)
			tasa_d.configure(state='disabled')

			cliente_tex_d.configure(state='normal')
			cliente_tex_d.delete('1.0',END)
			cliente_tex_d.configure(state='disabled')

			Total_B_d.configure(state='normal')
			Total_B_d.delete('1.0', END)
			Total_B_d.configure(state='disabled')

			Total_D_d.configure(state='normal')
			Total_D_d.delete('1.0',END)
			Total_D_d.configure(state='disabled')

			Total_D_d2.configure(state='normal')
			Total_D_d2.delete('1.0',END)
			Total_D_d2.configure(state='disabled')
	


		def agregar_a_suma_d(tasad,nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD):
	

			tasa_d.configure(state='normal')
			tasa_f = '{:,}'.format(tasad)
			tasa_d.insert(END, tasa_f)
			tasa_d.configure(state='disabled')

			cliente_tex_d.configure(state='normal')
			cliente_tex_d.insert(END,nombre_cliente)
			cliente_tex_d.configure(state='disabled')

			print(sub_total_DD)

			Total_B_d.configure(state='normal')
			d=sub_total_BB
			a=d,'(',sub_total_DD,')'
			Total_B_d.insert(END, a)
			Total_B_d.configure(state='disabled')



			Total_D_d.configure(state='normal')
			f='{:,}'.format(iva_BB)
			c=f,'(',iva_DD,')';print(c,'cccc')
			Total_D_d.insert(END,c)
			Total_D_d.configure(state='disabled')


			Total_D_d2.configure(state='normal')
			e=total_BB
			b=e,'(',total_DD,')'
			Total_D_d2.insert(END,b)
			Total_D_d2.configure(state='disabled')

			Label(actual,text=FECHA_d.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=0)

			Label(actual,text=HORA_d.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=40)

			return


		def verificacion_de_pagar():
			Valor=messagebox.askquestion('BBDD','¿Desea pagar esta deuda?',parent=actual)
			if Valor=='yes':
				formas_de_pago2()


		def formas_de_pago2():
			pago=Toplevel(actual)
			pago.geometry('300x100')
			pago.resizable(0,0)
			pago.configure(bg='#b6bdff')
			pago.title('Formas de Pago')
			pago.transient(master=actual)
			pago.focus_set()
			ancho_ventana = 300
			alto_ventana = 100
			x_ventana = pago.winfo_screenwidth() // 2 - ancho_ventana // 2
			y_ventana = pago.winfo_screenheight() // 2 - alto_ventana // 2
			posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
			pago.geometry(posicion)


			def seguir_venta(event):
				Forma_de_pago.set(f_pago.get())
				pago.destroy()
				pagar_vpv()
				


			Label(pago,text='Formas de Pago',bg='#b6bdff',font='Helvetica 12').place(x=25,y=5)

			f_pago=ttk.Combobox(pago,font='Helvetica 11', state="readonly", height=10,width=18)
			f_pago['values']= ('Punto De Venta','Bio Pago','Transferencia','Pago Movil','Divisa')
			f_pago.current(0)
			f_pago.place(x=10,y=30)



			bf=Button(pago,text='Aceptar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=lambda:seguir_venta('1'))
			bf.place(x=190,y=20)
			bf.focus()
			bf.bind('<Return>',seguir_venta)

			pago.bind('<Return>',seguir_venta)



		def pagar_vpv():



			total_sumita_B=DoubleVar()
			total_sumita_D=DoubleVar()

			sub_total_sumita_B=DoubleVar()
			sub_total_sumita_D=DoubleVar()

			iva_total_sumita_D=DoubleVar()
			iva_total_sumita_B=DoubleVar()

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM VENTAS WHERE BOOLEANOS=1")
			A=micursor.fetchall()
			for i in A:

				identificador_de_venta3.set(i[0])



			micursor.execute("SELECT * FROM PRODUCTOS_DEUDAS WHERE IDENTIFICADOR_DE_DEUDA=? AND BOOLEANOSS=0",(A1, ))
			B=micursor.fetchall()
			for i in B:
				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(i[19], ))
				G=micursor.fetchall()
				for i0 in G:
					tasa_d=i0[0]


					mult1=i[8]*tasa_d
					mult2=i[10]*tasa_d
					mult3=i[13]*tasa_d
					mult4=i[15]*tasa_d

					datos2=identificador_de_venta3.get(),i[2],i[3],i[4],i[5],i[6],i[7],i[8],mult1,i[10],mult2,mult3,i[13],i[14],i[15],mult4,fecha,0,i[19]
					micursor.execute("INSERT INTO PRODUCTO_V VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos2))




			datos=A1,A2
			micursor.execute("SELECT * FROM PRODUCTOS_DEUDAS WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_DEUDA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				
				micursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(usuarios[3], ))
				A=micursor.fetchall()
				for i in A:
					preb=i[8]*usuarios[5]
					pred=i[10]*usuarios[5]



					print(preb)

					micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(i[13], ))
					B=micursor.fetchall()
					for x in B:

						fd=preb*x[0]
						sd=preb

						df=pred*x[0]
						fg=pred
						r=preb-pred
						g=r*x[0]

						total_sumita_D.set(sd+total_sumita_D.get())
						total_sumita_B.set(fd+total_sumita_B.get())

						iva_total_sumita_D.set(r+iva_total_sumita_D.get())
						iva_total_sumita_B.set(g+iva_total_sumita_B.get())

						sub_total_sumita_D.set(fg+sub_total_sumita_D.get())
						sub_total_sumita_B.set(df+sub_total_sumita_B.get())


						print(total_sumita_B.get(),total_sumita_D.get())







			micursor.execute("SELECT * FROM DEUDAS WHERE ID_DEUDAS=? AND BOOLEANOS=0",(A1, ))
			C=micursor.fetchall()
			for i in C:
				datos1=i[1],sub_total_sumita_D.get(),sub_total_sumita_B.get(),iva_total_sumita_D.get(),iva_total_sumita_B.get(),total_sumita_B.get(),total_sumita_D.get(),fecha,tiempo.get(),tasa_del_dolar.get(),nombre_cajero.get(),numero_caja.get(),Forma_de_pago.get()
				micursor.execute("UPDATE VENTAS SET CEDULA_CLIENTE=?, SUB_TOTAL_V_D=?, SUB_TOTAL_V_B=?, IVA_V_D=?, IVA_V_B=?, TOTAL_V_D=?, TOTAL_V_B=?, FECHA=?, HORA=?, TASA_DEL_DIA=?, BOOLEANOS=0, CAJERO=?,NUMERO_CAJA=?,FORMA_DE_PAGO=? WHERE BOOLEANOS=1",(datos1))




			micursor.execute("DELETE FROM DEUDAS WHERE ID_DEUDAS=? AND BOOLEANOS=0",(A1, ))

			micursor.execute("DELETE FROM PRODUCTOS_DEUDAS WHERE IDENTIFICADOR_DE_DEUDA=? AND BOOLEANOSS=0",(A1, ))


			miconexion.commit()

			crear_venta_V()

			messagebox.showinfo('BBDD','Pago realizado con exito',parent=actual)
			buscar_deudores_d()
			total_sumita_D.set(0)
			total_sumita_B.set(0)

			iva_total_sumita_D.set(0)
			iva_total_sumita_B.set(0)

			sub_total_sumita_D.set(0)
			sub_total_sumita_B.set(0)
			leer_todo_VEN()
			vpv.destroy()

		def agregar_producto_a_deuda():
			Buscar_producto=StringVar()
			VP=Toplevel(actual)
			VP.geometry('600x532')
			VP.iconbitmap(logo)
			VP.resizable(0,0)
			VP.configure(bg='#b6bdff')
			cantidad_busca.set('')
			cantidad2_busca.set('')
			tab_control = ttk.Notebook(VP)
			hija=Frame(tab_control)
			ventana=Frame(tab_control)
			identifi=StringVar()

			tab_control.add(hija, text='Productos')
			#tab_control.add(ventana, text='Clientes')
			tab_control.pack(expand=1, fill='both')
			hija.config(bg='#b6bdff')
			ventana.config(bg='#b6bdff')


			def buscar_producto_V(event):

				if len(Buscar_producto.get())==0:
					record=lista_pV.get_children()
				
					for element in record:
						lista_pV.delete(element)
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
					elusuario=micursor.fetchall()
					for usuarios in elusuario:
						depar=usuarios[13]
						micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
						A=micursor.fetchall()	
						for i in A:
							tasita=i[0]

						x=float(usuarios[8])
						f=float(usuarios[8]*tasita)
						gr=round(x,2)
						b=round(f,2)

						lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],gr,b))

				else:
					record=lista_pV.get_children()
				
					for element in record:
						lista_pV.delete(element)
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
					elusuario=micursor.fetchall()
					for usuarios in elusuario:
						depar=usuarios[13]
						micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
						A=micursor.fetchall()	
						for i in A:
							tasita=i[0]
						r=usuarios[0].startswith(Buscar_producto.get())
						k=usuarios[1].startswith(Buscar_producto.get().capitalize())
						if r==1 or k==1:
							x=float(usuarios[8])
							f=float(usuarios[8]*tasita)
							a=round(x,2)
							b=round(f,2)
							lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],a,b))
							
						
					miconexion.commit()
			


			def ver_productos():
				record=lista_pV.get_children()
				
				for element in record:
					lista_pV.delete(element)
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
				elusuario=micursor.fetchall()
				for usuarios in elusuario:
					depar=usuarios[13]
					micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
					A=micursor.fetchall()	
					for i in A:
						tasita=i[0]


					x=float(usuarios[8])
					f=float(usuarios[8]*tasita)
					a=round(x,2)
					b=round(f,2)
					
					lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],a,b))
				
				miconexion.commit()
			   
				

			def ver_combos():
				record=lista_cV.get_children()

				for element in record:
					lista_cV.delete(element)	
				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				micursor.execute('SELECT * FROM COMBOS_C ORDER BY (NOMBRE_COMBO)DESC')
				elusuario=micursor.fetchall()
				for i in elusuario:
					lista_cV.insert('',0,text=i[0],values=(i[1],i[2],i[3]))

				miconexion.commit()

			def limpiar_campos_hija():
				global enlacess
				Buscar_producto.set('')
				producto_ingresar_B.set('')
				cantidad_ingresar_B.set('')
				precio_ingresar_D_B.set('')
				unidad_ingresar_B.set('')
				cantidad_busca.set('')
				producto_busca.set('')
				enlacess=0
				Label(hija,font='Consolas 14',fg='black',bg='#b6bdff',text='   ').place(x=262,y=110)
			limpiar_campos_hija()


			def agregar_producto_desde_lista_pV():
				global enlacess
				try:
					lista_pV.item(lista_pV.selection())['text'][0]

				except IndexError:
					pass
					return
				canti.focus()

				identifis=lista_pV.item(lista_pV.selection())['text']
				identifi.set(identifis)
				

				miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
				mycursor=miconexion_dos.cursor()
				mycursor.execute("SELECT * FROM PRODUCTOS WHERE ID='"+identifi.get()+"'")
				precio_o=mycursor.fetchall()
				for i in precio_o:
					unidad_ingresar_B.set(i[3])
					producto_busca.set(i[1])

				Label(hija,font='Consolas 14',fg='black',bg='#b6bdff',text=unidad_ingresar_B.get()).place(x=262,y=110)
				enlacess=1


			def ingresar_producto_a_lista_pV():
				if licencia_programa.get()=='no':
					Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
					if Valor=='yes':
						informacion_sobre_licencia()

					return

				global enlacess
				try:
					if enlacess==0:
						agregar_producto_desde_lista_pV()
						
						return
					
				except:
					pass
				
				try :
					

					if enlacess==1:

						
						if cedula_cliente_V.get()!='':

							try:
								if cantidad_busca.get()=='':
									cantidad_busca.set(1)

							except TclError:
								cantidad_busca.set(1)


							
							miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
							mycursor=miconexion_dos.cursor()
							mycursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_PRODUCTO='"+producto_busca.get()+"'")
							precio_o=mycursor.fetchall()
							for i in precio_o:
								identificador_ingresar_B.set(i[0])		
								producto_ingresar_B.set(i[1])
								exento_ingresar_B.set(i[4])
								porcentaje_de_gacnancia_B.set(i[7])
								precio_ingresar_D_sin_iva_B.set(i[10])
								precio_ingresar_B_sin_iva_B.set(i[11])
								precio_original_D_B.set(i[5])
								precio_original_B_B.set(i[6])
								unidad_ingresar_B.set(i[3])
								precio_ingresar_D_B.set(i[8])
								precio_ingresar_B_B.set(i[9])





								miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
								mycursor=miconexion_dos.cursor()

								mycursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(identificador_ingresar_B.get(), ))
								precio_o=mycursor.fetchall()
								for i in precio_o:
									depar=i[13]
									exen=i[4]

									mycursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
									A=mycursor.fetchall()
									for a in A:
										tasita=i[0]



								


								if cantidad_busca.get()>i[2]:
									
									messagebox.showwarning('BBDD','No tine suficientes unidades')
									limpiar_campos_hija()
									return







							mycursor.execute('SELECT DEPARTAMENTO FROM PRODUCTOS WHERE NOMBRE_PRODUCTO=? ',(producto_busca.get(), ))
							F=mycursor.fetchall()
							for i in F:
								DEPAR=i[0]


							mycursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=? ',(DEPAR, ))
							F=mycursor.fetchall()
							for i in F:
								TASA_=i[0]




							
							total_D.set(cantidad_busca.get()*precio_ingresar_D_B.get())
							total_B.set(total_D.get()*TASA_)
							
							total_D_sin_iva=cantidad_busca.get()*precio_ingresar_D_sin_iva_B.get()
							total_B_sin_iva=total_D_sin_iva*TASA_

							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							micursor.execute("SELECT ID_VENTAS FROM VENTAS WHERE BOOLEANOS=1")
							a=micursor.fetchall()
							for i in a:
								identificador_de_venta2.set(i[0])
								
				
				
							miconexion.commit()
							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							precio_B_con_tasa_2=total_D.get()*TASA_
							sub_total_con_tasa_2=total_D_sin_iva*TASA_
							precio_original_B_con_tasa_2=precio_original_D_B.get()*TASA_

							identificis=StringVar()
							micursor.execute("SELECT DEPARTAMENTO,EXENTO FROM PRODUCTOS WHERE ID=? ",(identificador_ingresar_B.get(), ))
							S=micursor.fetchall()
							for i in S:
								exen=i[1]
								identificis.set(i[0])



						
							micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=? ',(identificis.get(), ))
							F=micursor.fetchall()
							for i in F:
								TASA_=i[0]

							
							precio_B_con_tasa=precio_ingresar_D_B.get()*TASA_

							sub_total_B_con_tasa=total_D_sin_iva*TASA_

							precio_ori_B_con_tasa=precio_original_D_B.get()*TASA_

							#------

							micursor.execute("SELECT * FROM OFERTAS WHERE CODIGO_PRODUCTO=?",(identificador_ingresar_B.get(), ))
							precio_o3=micursor.fetchall()
							print('oferta')
							for i in precio_o3:	
								cantidad_oferta_B=i[4]
								print(cantidad_oferta_B, '9')
								if cantidad_oferta_B!='':
										

									identificador_ingresar_B.set(i[1])		
									producto_ingresar_B.set(i[2]+'   (Oferta)')


									porcentaje_de_gacnancia_B.set(i[4])


									precio_B_con_tasa=precio_ingresar_D_B.get()*TASA_

									sub_total_B_con_tasa=total_D_sin_iva*TASA_

									precio_ori_B_con_tasa=precio_original_D_B.get()*TASA_


			
									unidad_ingresar_B.set(i[3])
									


									if exen==1:

										total_D.set(i[5]*cantidad_busca.get())
										precio_ingresar_B_B.set(total_D.get()*TASA_*cantidad_busca.get())

										precio_ingresar_D_sin_iva_B.set(i[5]*cantidad_busca.get())
										precio_B_con_tasa_2=total_D.get()*TASA_


										total_D_sin_iva=total_D.get()
										sub_total_con_tasa_2=total_D.get()*TASA_


									if exen==0:
										a=i[5]*IVA.get()
										b=a/100
										c=i[5]-b
										d=c*TASA_

										precio_ingresar_D_sin_iva_B.set(c)
										precio_ingresar_B_sin_iva_B.set(d)


							micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=?",(DEPAR, ))
							TODO=micursor.fetchall()
							for i in TODO:
								if i[2]!='':
									a=total_B.get()

									a1=a*i[2]
									a2=a1/100
									a3=a-a2

									precio_B_con_tasa_2=a3
									total_D.set(a3/TASA_)

									



									b=total_D_sin_iva*TASA_

									b1=b*i[2]
									b2=b1/100
									b3=b-b2

									sub_total_con_tasa_2=b3
									total_D_sin_iva=b3/TASA_




									c=precio_original_D_B.get()*TASA_

									c1=c*i[2]
									c2=c1/100
									c3=c-c2




									precio_original_B_con_tasa_2=c3
									precio_original_D_B.set(c3/TASA_)

									producto_ingresar_B.set(producto_ingresar_B.get()+'   (Oferta)')


										
							datos=identificador_de_venta2.get(),cedula_cliente_V.get(),identificador_ingresar_B.get(),producto_ingresar_B.get(),cantidad_busca.get(),exento_ingresar_B.get(),unidad_ingresar_B.get(),precio_ingresar_D_B.get(),    precio_B_con_tasa     ,total_D.get(),precio_B_con_tasa_2   ,sub_total_con_tasa_2,   total_D_sin_iva,porcentaje_de_gacnancia_B.get(),precio_original_D_B.get(),    precio_original_B_con_tasa_2    ,fecha,true,identificis.get()
							print(datos)
							micursor.execute("INSERT INTO PRODUCTO_V VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))
							




							micursor.execute("SELECT ID_DEUDAS FROM DEUDAS WHERE BOOLEANOS=1")
							A=micursor.fetchall()
							for i in A:
								identificador_de_deuda3.set(i[0])

							datos2=identificador_de_deuda3.get(),cedula_cliente_V.get(),identificador_ingresar_B.get(),producto_ingresar_B.get(),cantidad_busca.get(),exento_ingresar_B.get(),unidad_ingresar_B.get(),precio_ingresar_D_B.get(),precio_ingresar_B_B.get(),total_D.get(),precio_B_con_tasa_2   ,sub_total_con_tasa_2,   total_D_sin_iva,porcentaje_de_gacnancia_B.get(),precio_original_D_B.get(),    precio_original_B_con_tasa_2    ,fecha,true,identificis.get()
							micursor.execute("INSERT INTO PRODUCTOS_DEUDAS VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos2))


							miconexion.commit()


							record=lista1v.get_children()
							for element in record:
								lista1v.delete(element)

							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
							a=micursor.fetchall()
							for i in a:
								total_venta_B.set(round(i[10]+total_venta_B.get(),2))
								total_venta_D.set(round(i[11]+total_venta_D.get(),2))

						

								total_venta_sin_iva_B.set(round(i[12]+total_venta_sin_iva_B.get(),2))
								total_venta_sin_iva_D.set(round(i[13]+total_venta_sin_iva_D.get(),2))

								round1=round(i[8],2)
								round2=round(i[10],2)
								ds=round(i[9],2)
								fd=round(i[11],2)
								lista1v.insert('',0,text=i[3],values=(i[4],i[5],i[7],i[19],round1,ds,round2,fd))
							
				
					
							miconexion=sqlite3.connect('SISTEMA_LUMINA')
							micursor=miconexion.cursor()
							micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND EXENTO=false")
							a=micursor.fetchall()

							for i in a:
								e=i[10]-i[13]

								r=i[11]-i[12]

								total_iva_B.set(round(r+total_iva_B.get(),2))
								total_iva_D.set(round(e+total_iva_D.get(),2))


							limpiar_suma()
							agregar_a_suma(total_venta_D.get(),total_venta_B.get(),total_venta_sin_iva_D.get(),total_venta_sin_iva_B.get(),total_iva_B.get(),total_iva_D.get())
							limpiar_campos_hija()
							total_venta_B.set(0)
							total_venta_D.set(0)
							total_venta_sin_iva_B.set(0)
							total_venta_sin_iva_D.set(0)
							total_iva_B.set(0)
							total_iva_D.set(0)
							limpiar_campos_hija()
							bus.focus()
							enlacess=0
							return
						else:
							limpiar_campos_hija()
							messagebox.showerror('BBDD','Introdusca Cedula del cliente',parent=hija)
							limpiar_campos_hija()
							bus.focus()
							return

			
				finally:
					pass

			style = ttk.Style()
			style.configure("Treeview", font=('Helvetica', 10))

			lista_pV=ttk.Treeview(hija,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 5)])
			lista_pV.place(x=0,y=160)

			scoll=Scrollbar(hija,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
			scoll.place(x=580,y=185,height=320)
			lista_pV.config(yscrollcommand=scoll.set)

			lista_pV.heading('#0',text='Codigo',anchor=CENTER)
			lista_pV.heading('#1',text='Productos',anchor=CENTER)
			lista_pV.heading('#2',text='Unidad',anchor=CENTER)
			lista_pV.heading('#3',text='Precio $',anchor=CENTER)
			lista_pV.heading('#4',text='Precio Bs.S',anchor=CENTER)

			lista_pV.column("#0",minwidth=100, width = 100)
			lista_pV.column("#1",minwidth=70, width = 190 )
			lista_pV.column("#2",minwidth=70, width = 50 )
			lista_pV.column("#3",minwidth=70, width = 100 )
			lista_pV.column("#4",minwidth=70, width = 160 )
			ver_productos()



			




			product=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',state='readonly',textvariable=producto_busca)
			product.place(x=0,y=110,height=41)

			canti=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=cantidad_busca)
			canti.place(x=200,y=110,width=60,height=41)
			Button(hija,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=ingresar_producto_a_lista_pV).place(x=298,y=111)

			bus=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=Buscar_producto)
			bus.place(x=0,y=10,height=41)
			Button(hija,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_producto_V('1')).place(x=200,y=10)

			bus.focus()

			bus.bind("<KeyRelease>", buscar_producto_V)



			


			def sub_menu(event):
				try:
					menu.post(event.x_root, event.y_root)
				finally:
					menu.grab_release()

			menu = Menu(lista_pV, tearoff=0)
			menu.add_command(label="Buscar",command=lambda:buscar_producto_V('1'))
			menu.add_command(label="Aceptar",command=ingresar_producto_a_lista_pV)
			menu.add_separator()
			menu.add_command(label=' limpiar                    ',command=limpiar_campos_hija)
			
			

			lista_pV.bind("<Button-3>", sub_menu)

			hija.bind("<Button-3>", sub_menu)









			

		lista_d_d=ttk.Treeview(actual,style="Treeview",height=15,columns=[f"#{n}" for n in range(1, 6)])
		lista_d_d.place(x=0,y=160)

		scoll=Scrollbar(actual,command=lista_d_d.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=680,y=185,height=300)
		lista_d_d.config(yscrollcommand=scoll.set)

		lista_d_d.heading('#0',text='Codigo',anchor=CENTER)
		lista_d_d.heading('#1',text='Productos',anchor=CENTER)
		lista_d_d.heading('#2',text='Cantidad',anchor=CENTER)
		lista_d_d.heading('#3',text='Unidad',anchor=CENTER)
		lista_d_d.heading('#4',text='Precio $',anchor=CENTER)
		lista_d_d.heading('#5',text='Precio Bs.S',anchor=CENTER)

		lista_d_d.column("#0",minwidth=100, width = 100)
		lista_d_d.column("#1",minwidth=70, width = 220 )
		lista_d_d.column("#2",minwidth=70, width = 60 )
		lista_d_d.column("#3",minwidth=70, width = 50 )
		lista_d_d.column("#4",minwidth=70, width = 110 )
		lista_d_d.column("#5",minwidth=70, width = 160 )

		
		
		Label(actual,text='Fecha',font='Helvetica 12',bg='#b6bdff').place(x=0,y=0)


		Label(actual,text='Hora:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=40)


		Label(actual,text='Tasa:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=80)

		tasa_d=Text(actual,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
		tasa_d.place(x=55,y=80)

		Label(actual,text='Cliente:',bg='#b6bdff',font='Helvetica 12').place(x=0,y=120)

		cliente_tex_d=Text(actual,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
		cliente_tex_d.place(x=55,y=120)


		totales_d=Frame(actual)
		totales_d.configure(bg='#b8d3ff',width=370,height=157)
		totales_d.place(x=343,y=0)

		Label(totales_d,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=20)
		Label(totales_d,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=60)
		Label(totales_d,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=100)


		Total_B_d=Text(totales_d,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_B_d.place(x=115,y=21)

		Total_D_d=Text(totales_d,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D_d.place(x=115,y=62)

		Total_D_d2=Text(totales_d,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D_d2.place(x=115,y=103)
		
		#Button(actual,text='Agregar',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,width=10,command=agregar_producto_a_deuda).place(x=463,y=490)

		Button(actual,text='Pagar',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,width=10,command=verificacion_de_pagar).place(x=583,y=490)

		
		
		Label(actual,text='Cajero:',font='Helvetica 12',bg='#b6bdff').place(x=160,y=0)
		cajero_la=Label(actual,text='Elvin 6',font='Helvetica 12',bg='#b6bdff')
		cajero_la.place(x=220,y=0)

		Label(actual,text='Caja:',font='Helvetica 12',bg='#b6bdff').place(x=160,y=40)
		caja_la=Label(actual,text='Elvin 6',font='Helvetica 12',bg='#b6bdff')
		caja_la.place(x=220,y=40)

		ver_fecha_y_hora_d()
		ver_productos_de_la_deuda_d()





		#-------------------------------------------------------------------------





		def ver_productos_de_la_deuda_d_a():
			record=lista_d_d_a.get_children()
			for element in record:
				lista_d_d_a.delete(element)
			
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			datos=A1,A2
			
			micursor.execute("SELECT * FROM PRODUCTOS_DEUDAS WHERE BOOLEANOSS=0 AND IDENTIFICADOR_DE_DEUDA=? AND C_CLIENTE=? ORDER BY(CODIGO_PRODUCTO)DESC",(datos))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				a=round(usuarios[10],2)
				b=round(usuarios[11],2)
				lista_d_d_a.insert('',0,text=usuarios[3],values=(usuarios[4],usuarios[5],usuarios[7],a,b))
				
				
		def ver_fecha_y_hora_d_a():
			
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM DEUDAS WHERE BOOLEANOS=0 AND ID_DEUDAS=?",(A1, ))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				a=str(usuarios[8])
				b=str(usuarios[9])
				FECHA_d.set(a)
				HORA_d.set(b)
				TASA_d.set(usuarios[10])

				sub_total_BB=usuarios[3]
				sub_total_DD=usuarios[2]
				iva_BB=usuarios[5]
				iva_DD=usuarios[4]
				total_BB=usuarios[6]
				total_DD=usuarios[7]
				cajero=usuarios[12]
				caja=usuarios[13]

			cajero_la2.config(text=cajero)
			caja_la2.config(text=caja)


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE=?",(A2, ))
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				nombre_cliente=usuarios[0]+' '+usuarios[1]


			limpiar_cuadros_Text_d_a()
			agregar_a_suma_d_a(TASA_d.get(),nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD)



	
		def limpiar_cuadros_Text_d_a():
			tasa_d_a.configure(state='normal')
			tasa_d_a.delete('1.0', END)
			tasa_d_a.configure(state='disabled')

			cliente_tex_d_a.configure(state='normal')
			cliente_tex_d_a.delete('1.0',END)
			cliente_tex_d_a.configure(state='disabled')

			Total_B_d_a.configure(state='normal')
			Total_B_d_a.delete('1.0', END)
			Total_B_d_a.configure(state='disabled')

			Total_D_d_a.configure(state='normal')
			Total_D_d_a.delete('1.0',END)
			Total_D_d_a.configure(state='disabled')

			Total_D_d2_a.configure(state='normal')
			Total_D_d2_a.delete('1.0',END)
			Total_D_d2_a.configure(state='disabled')
	


		def agregar_a_suma_d_a(tasad,nombre_cliente,sub_total_BB,sub_total_DD,iva_BB,iva_DD,total_BB,total_DD):
	

			tasa_d_a.configure(state='normal')
			tasa_f = '{:,}'.format(round(tasad,2))
			tasa_d_a.insert(END, tasa_f)
			tasa_d_a.configure(state='disabled')

			cliente_tex_d_a.configure(state='normal')
			cliente_tex_d_a.insert(END,nombre_cliente)
			cliente_tex_d_a.configure(state='disabled')



			Total_B_d_a.configure(state='normal')
			dinero = '{:,}'.format(round(sub_total_BB,2))
			dinero2 = '{:,}'.format(round(sub_total_DD,2))
			a=dinero,'(',dinero2,')'
			Total_B_d_a.insert(END, a)
			Total_B_d_a.configure(state='disabled')



			Total_D_d_a.configure(state='normal')
			dinero5 = '{:,}'.format(round(iva_BB,2))
			dinero6 = '{:,}'.format(round(iva_DD,2))
			c=dinero5,'(',dinero6,')'
			Total_D_d_a.insert(END,c)
			Total_D_d_a.configure(state='disabled')


			Total_D_d2_a.configure(state='normal')
			dinero3 = '{:,}'.format(round(total_BB,2))
			dinero4 = '{:,}'.format(round(total_DD,2))
			b=dinero3,'(',dinero4,')'
			Total_D_d2_a.insert(END,b)
			Total_D_d2_a.configure(state='disabled')

			Label(viejo,text=FECHA_d.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=0)

			Label(viejo,text=HORA_d.get(),bg='#b6bdff',font='Helvetica 12').place(x=55,y=40)

			return





		lista_d_d_a=ttk.Treeview(viejo,style="Treeview",height=18,columns=[f"#{n}" for n in range(1, 6)])
		lista_d_d_a.place(x=0,y=160)

		scoll=Scrollbar(viejo,command=lista_d_d_a.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=680,y=185,height=350)
		lista_d_d_a.config(yscrollcommand=scoll.set)

		lista_d_d_a.heading('#0',text='Codigo',anchor=CENTER)
		lista_d_d_a.heading('#1',text='Productos',anchor=CENTER)
		lista_d_d_a.heading('#2',text='Cantidad',anchor=CENTER)
		lista_d_d_a.heading('#3',text='Unidad',anchor=CENTER)
		lista_d_d_a.heading('#4',text='Precio $',anchor=CENTER)
		lista_d_d_a.heading('#5',text='Precio Bs.S',anchor=CENTER)

		lista_d_d_a.column("#0",minwidth=100, width = 100)
		lista_d_d_a.column("#1",minwidth=70, width = 220 )
		lista_d_d_a.column("#2",minwidth=70, width = 60 )
		lista_d_d_a.column("#3",minwidth=70, width = 50 )
		lista_d_d_a.column("#4",minwidth=70, width = 110 )
		lista_d_d_a.column("#5",minwidth=70, width = 160 )

		
		
		Label(viejo,text='Fecha',font='Helvetica 12',bg='#b6bdff').place(x=0,y=0)


		Label(viejo,text='Hora:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=40)


		Label(viejo,text='Tasa:',font='Helvetica 12',bg='#b6bdff').place(x=0,y=80)

		tasa_d_a=Text(viejo,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
		tasa_d_a.place(x=55,y=80)

		Label(viejo,text='Cliente:',bg='#b6bdff',font='Helvetica 12').place(x=0,y=120)

		cliente_tex_d_a=Text(viejo,relief='flat',state='disabled',height=1,width=25,font='Helvetica 12',bg='#b6bdff')
		cliente_tex_d_a.place(x=55,y=120)


		totales_d_a=Frame(viejo)
		totales_d_a.configure(bg='#b8d3ff',width=370,height=157)
		totales_d_a.place(x=343,y=0)

		Label(totales_d_a,text='Sub Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=10,y=20)
		Label(totales_d_a,text='I.V.A ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=60)
		Label(totales_d_a,text='Total ($):',font='Helvetica 12',bg='#b8d3ff',fg='black').place(x=45,y=100)


		Total_B_d_a=Text(totales_d_a,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_B_d_a.place(x=115,y=21)

		Total_D_d_a=Text(totales_d_a,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D_d_a.place(x=115,y=62)

		Total_D_d2_a=Text(totales_d_a,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
		Total_D_d2_a.place(x=115,y=103)


		Label(viejo,text='Caja:',font='Helvetica 12',bg='#b6bdff').place(x=160,y=40)
		caja_la2=Label(viejo,text='',font='Helvetica 12',bg='#b6bdff')
		caja_la2.place(x=220,y=40)
		
		Label(viejo,text='Cajero:',font='Helvetica 12',bg='#b6bdff').place(x=160,y=0)
		cajero_la2=Label(viejo,text='',font='Helvetica 12',bg='#b6bdff')
		cajero_la2.place(x=220,y=0)



		ver_productos_de_la_deuda_d_a()
		ver_fecha_y_hora_d_a()


	frax2=Frame(deu,bg='#b6bdff')
	frax2.grid(row=0,column=0,sticky='NSEW')
	Entry(frax2,font='Helvetica 12',bd=7,relief='sunken',textvariable=buscar_deudor).grid(row=0,column=0,sticky='NSW',pady=10,padx=10)

	deu.rowconfigure(1,weight=2)
	deu.rowconfigure(2,weight=5)

	deu.columnconfigure(0,weight=5)

	frame_lista_d=Frame(deu,bg='#b6bdff')
	frame_lista_d.grid(row=2,column=0,sticky='NSEW',columnspan=2)

	lista1d=ttk.Treeview(frame_lista_d,style='Treeview',columns=[f"#{n}" for n in range(1, 9)])
	lista1d.pack(expand=1,fill=BOTH)
	lista1d.grid(row=0,column=0,sticky='nsew',columnspan=4,rowspan=4)
	frame_lista_d.rowconfigure(0,weight=5)
	frame_lista_d.columnconfigure(0,weight=5)


	scoll=Scrollbar(frame_lista_d,command=lista1d.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.grid(row=0,column=2,sticky='NSEW')


	lista1d.config(yscrollcommand=scoll.set)

	lista1d.heading('#0',text='Codigo')
	lista1d.heading('#1',text='C.I. Cliente')
	lista1d.heading('#2',text='Fecha')
	lista1d.heading('#3',text='Sub total $')
	lista1d.heading('#4',text='Sub total Bs.S')
	lista1d.heading('#5',text='I.V.A. $')
	lista1d.heading('#6',text='I.V.A. Bs.S')
	lista1d.heading('#7',text='Total $')
	lista1d.heading('#8',text='Total Bs.S')
	

	lista1d.column("#0",minwidth=70, width = 50)
	lista1d.column("#1",minwidth=70, width = 120)
	lista1d.column("#2",minwidth=70, width = 60)
	lista1d.column("#3",minwidth=70, width = 80)
	lista1d.column("#4",minwidth=70, width = 140)
	lista1d.column("#5",minwidth=70, width = 80)
	lista1d.column("#6",minwidth=70, width = 100)
	lista1d.column("#7",minwidth=70, width = 100)
	lista1d.column("#8",minwidth=70, width = 140)


	def sub_menud(event):
		try:
			menud.post(event.x_root, event.y_root)
		finally:
			menud.grab_release()

	menud = Menu(deu, tearoff=0)
	menud.add_command(label="Buscar")
	menud.add_separator()
	menud.add_command(label="Detalles",underline=1,accelerator='Ctrl+D')
	menud.add_command(label="Reportes             ")
	


	deu.bind("<Button-3>", sub_menud)

	lista1d.bind("<Button-3>", sub_menud)


	frame_botones2=Frame(deu,bg='#b6bdff')
	frame_botones2.grid(row=1,column=0,sticky='SEW',columnspan=2)


	Button(frax2,text='Buscar',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,height=1,command=buscar_deudores_d).grid(row=0,column=2,sticky='W',pady=10)
	Button(frame_botones2,text='Detalles',font='Helvetica 12',relief='raised',cursor='hand2',bd=7,height=1,command=Detalles_deu).grid(row=0,column=1,sticky='W')









	leer_todo_deudores()

#------------------Clave----------------------------------

def funcion_clave():
	clave=Toplevel(raiz)
	clave.resizable(0,0)
	clave.configure(bg='#b6bdff')
	clave.iconbitmap(logo)
	clave.geometry('400x100')
	variable_clave.set('')
	clave.transient(master=raiz)

	acceso=Entry(clave,font='Helvetica 12',bd=9,relief='sunken',textvariable=variable_clave)
	acceso.place(x=140,y=20,width=180,height=35)
	acceso.configure(show='*')

	accediendo=Label(clave,font='Helvetica 12',text='Clave de acceso',bg='#b6bdff')
	accediendo.place(x=10,y=20)

	boton_acceso=Button(clave,cursor='hand2',text='O.K.',bg='silver',font='Helvetica 12',width=5,height=1,bd=4,relief='raised',command=accedi)
	boton_acceso.place(x=330,y=20)
	clave.grab_set()



#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG



def accedi():
	if variable_clave.get()=='leiserpro':
		accediendo()
		variable_clave.set('')

	        
	else:
		messagebox.showerror('Sistema Lumina','Clave Incorrecta')
		variable_clave.set('')
#_-------------------------------------------------------------------
def licencia():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM LICENCIA WHERE BOOLEANO=1")
	A=micursor.fetchall()
	for i in A:
		if i[5]==0:
			tipo_l='Prueba'

		else:
			tipo_l='Normal'

		fecha1_l=i[2]
		fecha2_l=i[3]


		if i[1]=='Defecto':
			tipo_l='Sin Licencia'
		
		




	messagebox.showinfo('SysMark',' Version: V1.0 SysMark  \n \n Tipo de licencia: {}  \n \n Fecha Inicial: {} \n \n Fecha Final: {}'.format(tipo_l,fecha1_l,fecha2_l))

def salir():
	valor=messagebox.askquestion('Salir', '¿Desea salir de la aplicacion?')
	if valor=='yes':
		raiz.destroy()

#---------------VENTANA PRINCIPAL FUNCIONES--------------------

def ventana_principal():
	pass


def limpiar_todo_V():
	valor=messagebox.askquestion('Ventas','¿Desea limpiar todos los campos?')
	if valor=='yes':
		limpiar_todo_V2()

def limpiar_todo_V2():
	record=lista1v.get_children()
	for element in record:
		lista1v.delete(element)
	limpiar_suma()
	borrar_productos_en_true_V()
	limpiar_campos_V()
	cambiar_cliente_V()
	borrar_campos_cliente_V()
	borrar_campos_venta()
	agregar_a_suma(0.0,0.0,0.0,0.0,0.0,0.0)

def crear_venta_V():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos=cedula_cliente_V.get(),0,0,0,0,0,0,fecha,tiempo.get(),tasa_del_dolar.get(),true,'','',''
	micursor.execute("INSERT INTO VENTAS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))

	miconexion.commit()

def crear_deuda():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	datos2=cedula_cliente_V.get(),0,0,0,0,0,0,fecha,tiempo.get(),tasa_del_dolar.get(),true,'',''
	micursor.execute("INSERT INTO DEUDAS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos2))

	miconexion.commit()


def crear_compra():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	
	datos2=0,0,0,0,0,0,0,fecha,tiempo.get(),tasa_del_dolar.get(),true,''
	micursor.execute("INSERT INTO COMPRAS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",(datos2))

	miconexion.commit()




def vender_producto():
	
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT ID_VENTAS FROM VENTAS WHERE BOOLEANOS=1")
	a=micursor.fetchall()
	for i in a:
		identificador_de_venta2.set(i[0])
		
		
		
	miconexion.commit()


def nueva_venta():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("UPDATE VENTAS SET BOOLEANOS=0 WHERE BOOLEANOS=1")
	

	miconexion.commit()


def nueva_deuda():

	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()

	micursor.execute("UPDATE DEUDAS SET BOOLEANOS=0 WHERE BOOLEANOS=1")
	miconexion.commit()

def nueva_venta2():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
	a=micursor.fetchall()
	for i in a:
		
		total_venta_B.set(i[10]+total_venta_B.get())
		total_venta_D.set(i[11]+total_venta_D.get())

		total_venta_sin_iva_B.set(i[12]+total_venta_sin_iva_B.get())
		total_venta_sin_iva_D.set(i[13]+total_venta_sin_iva_D.get())


		
			

		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND EXENTO=false")
		a=micursor.fetchall()
		total_iva_B.set(0)
		total_iva_D.set(0)
		for i in a:

			e=i[10]-i[13]

			r=i[11]-i[12]

			total_iva_B.set(r+total_iva_B.get())
			total_iva_D.set(e+total_iva_D.get())


	if total_venta_B.get()!=0 and total_venta_D.get()!=0:
		ver_cajero()
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		datos=cedula_cliente_V.get(),total_venta_sin_iva_D.get(),total_venta_sin_iva_B.get(),total_iva_D.get(),total_iva_B.get(),total_venta_D.get(),total_venta_B.get(),fecha,tiempo.get(),tasa_del_dolar.get(),nombre_cajero.get(),numero_caja.get(),Forma_de_pago.get()
		micursor.execute("UPDATE VENTAS SET CEDULA_CLIENTE=?,SUB_TOTAL_V_D=?,SUB_TOTAL_V_B=?,IVA_V_D=?,IVA_V_B=?,TOTAL_V_D=?,TOTAL_V_B=?,FECHA=?,HORA=?,TASA_DEL_DIA=?, CAJERO=?, NUMERO_CAJA=?, FORMA_DE_PAGO=? WHERE BOOLEANOS=1",(datos))
		

		miconexion.commit()
		
		nueva_venta()
		
		
		crear_venta_V()
		cambiar_cliente_V()
		borrar_campos_cliente_V()
		borrar_campos_venta()
		cambiar_true_a_false_V()
		borrar_difencias_V()
		total_venta_B.set(0)
		total_venta_D.set(0)
		total_venta_sin_iva_B.set(0)
		total_venta_sin_iva_D.set(0)
		total_iva_B.set(0)
		total_iva_D.set(0)
		

	else:
		pass

def nueva_deuda2():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
	a=micursor.fetchall()
	for i in a:
		
		total_venta_B.set(i[10]+total_venta_B.get())
		total_venta_D.set(i[11]+total_venta_D.get())

		total_venta_sin_iva_B.set(i[12]+total_venta_sin_iva_B.get())
		total_venta_sin_iva_D.set(i[13]+total_venta_sin_iva_D.get())


		
			

		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND EXENTO=false")
		a=micursor.fetchall()
		total_iva_B.set(0)
		total_iva_D.set(0)
		for i in a:

			e=i[10]-i[13]

			r=i[11]-i[12]

			total_iva_B.set(r+total_iva_B.get())
			total_iva_D.set(e+total_iva_D.get())


	if total_venta_B.get()!=0 and total_venta_D.get()!=0:

		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		ver_cajero()
		datos2=cedula_cliente_V.get(),total_venta_sin_iva_D.get(),total_venta_sin_iva_B.get(),total_iva_D.get(),total_iva_B.get(),total_venta_D.get(),total_venta_B.get(),fecha,tiempo.get(),tasa_del_dolar.get(),nombre_cajero.get(),numero_caja.get()
		micursor.execute("UPDATE DEUDAS SET CEDULA_CLIENTE=?,SUB_TOTAL_D_D=?,SUB_TOTAL_D_B=?,IVA_D_D=?,IVA_D_B=?,TOTAL_D_D=?,TOTAL_D_B=?,FECHA=?,HORA=?,TASA_DEL_DIA=?,NOMBRE_CAJERO=?,NUMERO_CAJA=? WHERE BOOLEANOS=1",(datos2))

		miconexion.commit()

		nueva_deuda()
		crear_deuda()
		cambiar_cliente_V()
		borrar_campos_cliente_V()
		borrar_campos_venta()
		cambiar_true_a_false_D()
		borrar_difencias_D()

		total_venta_B.set(0)
		total_venta_D.set(0)
		total_venta_sin_iva_B.set(0)
		total_venta_sin_iva_D.set(0)
		total_iva_B.set(0)
		total_iva_D.set(0)

def resta_productos_del_inventario():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
	a=micursor.fetchall()
	for i in a:
		datos=i[5],i[3],i[4]


		micursor.execute("UPDATE PRODUCTOS SET CANTIDAD_PRODUCTO=CANTIDAD_PRODUCTO-? WHERE ID=? AND NOMBRE_PRODUCTO=?",(datos))

	miconexion.commit()


def borrar_difencias_V():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()

	micursor.execute("DELETE FROM PRODUCTOS_DEUDAS WHERE BOOLEANOSS=1")

	miconexion.commit()


def borrar_difencias_D():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()

	micursor.execute("DELETE FROM PRODUCTO_V WHERE BOOLEANOSS=1")

	miconexion.commit()

def deudor():
	b=''
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT PRODUCTO FROM PRODUCTO_V WHERE BOOLEANOSS=1")
	a=micursor.fetchall()
	for i in a:


		b=i[0]


	if b!='':
		a=messagebox.askquestion('BBDD','¿Desea introducir esta venta a deudores?')
		if a=='yes':

			resta_productos_del_inventario()
			limpiar_suma()
			nueva_deuda2()

			messagebox.showinfo('BBDD','Deuda introducida con exito')


def hacer_factura():
	q='factura de prueba'

	filename=tempfile.mktemp('.txt')
	open(filename,'w').write(q)

def vender(event):
	if licencia_programa.get()=='no':
		Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
		if Valor=='yes':
			informacion_sobre_licencia()

		return


	b=''
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT PRODUCTO FROM PRODUCTO_V WHERE BOOLEANOSS=1")
	a=micursor.fetchall()
	for i in a:


		b=i[0]


	if b!='':

		formas_de_pago()

		



		#VALOR=messagebox.askquestion('BBDD','¿Desea imprimir una factura?')


		#if VALOR=='yes':
			
			#hacer_factura()

		
		
	else: 
		pass

def formas_de_pago():
	pago=Toplevel(raiz)
	pago.geometry('300x100')
	pago.resizable(0,0)
	pago.configure(bg='#b6bdff')
	pago.title('Formas de Pago')
	pago.transient(master=raiz)
	pago.focus_set()
	ancho_ventana = 300
	alto_ventana = 100
	x_ventana = pago.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = pago.winfo_screenheight() // 2 - alto_ventana // 2
	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
	pago.geometry(posicion)


	def seguir_venta(event):
		Forma_de_pago.set(f_pago.get())

		resta_productos_del_inventario()
		limpiar_suma()
		nueva_venta2()
		limpiar_campos_V()
		
		pago.destroy()
		messagebox.showinfo('BBDD','Venta Realiazada con exito',parent=raiz)

	def ver_formas_de_pago():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
			
		micursor.execute("SELECT FORMAS_DE_PAGO FROM FORMAS_DE_PAGO")
		A=micursor.fetchall()
		
		f_pago['values']= (list(f"{str(n[0])}" for n in A))



	f_pago=ttk.Combobox(pago,font='Helvetica 11', state="readonly", height=10,width=18)
	ver_formas_de_pago()
	f_pago.current(0)
	f_pago.place(x=10,y=30)



	bf=Button(pago,text='Aceptar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=lambda:seguir_venta('1'))
	bf.place(x=190,y=20)
	bf.focus()
	bf.bind('<Return>',seguir_venta)

	pago.bind('<Return>',seguir_venta)





def borrar_productos_en_true_V():
	try:
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("DELETE  FROM PRODUCTO_V WHERE BOOLEANOSS=1")
		micursor.execute("DELETE  FROM PRODUCTOS_DEUDAS WHERE BOOLEANOSS=1")
		miconexion.commit()
	except sqlite3.OperationalError:
		pass
borrar_productos_en_true_V()

def borrar_campos_cliente_V():
	Nombre_cliente_V.set('')
	Apellido_cliente_V.set('')
	cedula_cliente_V.set('')
	Nombre_cliente_V2.set('')

def borrar_campos_venta():
	identificador_ingresar_V.set('')
	producto_ingresar_V.set('')
	cantidad_ingresar_V.set('')
	precio_ingresar_D_V.set('')
	precio_ingresar_B_V.set('')
borrar_campos_venta()

def borrar_campos_CTN_V():
	nombre_cliente_CTN.set('')
	apellido_cliente_CTN.set('')
	cedula_cliente_CTN.set('')
	direccion_cliente_CTN.set('')
	telefono_cliente_CTN.set('')

def ver_tasa_moneda():
	try:
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		
		
		micursor.execute("SELECT TASA FROM TASA_MONEDA WHERE BOOLEANO = 1")
		tasita=micursor.fetchall()
		for i in tasita:
			tasa_del_dolar.set(i[0])

		miconexion.commit()
	except sqlite3.OperationalError:
		pass

ver_tasa_moneda()

def tasa_moneda(event):
	tm=Toplevel(raiz)
	ancho_ventana = 260
	alto_ventana = 260
	x_ventana = tm.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = tm.winfo_screenheight() // 2 - alto_ventana // 2
	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
	tm.geometry(posicion)
	#tm.geometry('260x260')
	tm.config(bg='#b6bdff')
	tm.iconbitmap(logo)
	tm.resizable(0,0)
	tm.title('Tasa Moneda')

	def agregar_tasa_moneda():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		datos=tasa_del_dolar.get(),fecha,tiempo.get(),true
		micursor.execute("INSERT INTO TASA_MONEDA VALUES(NULL,?,?,?,?)",(datos))
		miconexion.commit()
		


	def cambiar_tasa_moneda():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		
		
		micursor.execute("UPDATE TASA_MONEDA SET BOOLEANO=0 WHERE BOOLEANO = 1")
		miconexion.commit()


	def ver_tasa_monedas():
		acd=Toplevel(tm)
		acd.geometry('418x365')
		acd.config(bg='#b6bdff')
		acd.iconbitmap(logo)
		acd.resizable(0,0)

		def ver_tasa_moneda_en_acd():
			record=ver_tasa.get_children()
			for element in record:
				ver_tasa.delete(element)


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT* FROM TASA_MONEDA")
			A=micursor.fetchall()
			for i in A:
				ver_tasa.insert('',0,text=i[1],values=(i[2],i[3]))
		Buscar_tasa_moneda=StringVar()
		def buscar_tasa_moneda_en_acd(event):
			if Buscar_tasa_moneda=='':
				ver_tasa_moneda_en_acd()
				return


			record=ver_tasa.get_children()
			for element in record:
				ver_tasa.delete(element)


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT* FROM TASA_MONEDA")
			A=micursor.fetchall()
			for i in A:
				r=str(i[1])
				t=str(i[2])
				y=str(i[3])
				f=r.startswith(Buscar_tasa_moneda.get())
				g=t.startswith(Buscar_tasa_moneda.get())
				#h=y.startswith(Buscar_tasa_moneda.get())
				if f==1 or g==1:
					micursor.execute("SELECT * FROM TASA_MONEDA WHERE TASA=?",(i[1], ))
					ver_tasa.insert('',0,text=i[1],values=(i[2],i[3]))


			fe.focus()

		
		ver_tasa=ttk.Treeview(acd,style="mystyle.Treeview",height=12,columns=[f"#{n}" for n in range(1, 3)])
		
		ver_tasa.place(x=0,y=100)

		
		

		scoll=Scrollbar(acd,command=ver_tasa.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=400,y=100,height=270)

		ver_tasa.config(yscrollcommand=scoll.set)

		ver_tasa.heading('#0',text='Tasa',anchor=CENTER)
		ver_tasa.heading('#1',text='Fecha',anchor=CENTER)
		ver_tasa.heading('#2',text='Hora',anchor=CENTER)

		ver_tasa.column("#0",minwidth=100, width = 200)
		ver_tasa.column("#1",minwidth=70, width = 100 )
		ver_tasa.column("#2",minwidth=70, width = 100 )

		fe=Entry(acd,relief='sunken',font='Helvetica 12',bd=7,textvariable=Buscar_tasa_moneda)
		fe.place(x=0,y=5)
		Button(acd,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_tasa_moneda_en_acd('1')).place(x=200,y=0)
		fe.focus()
		fe.bind("<KeyRelease>", buscar_tasa_moneda_en_acd)
	
		ver_tasa_moneda_en_acd()




	def actualizar_productos():
		acd=Toplevel(tm)
		acd.geometry('418x370')
		acd.config(bg='#b6bdff')
		acd.iconbitmap(logo)
		acd.resizable(0,0)
		acd.title('Actualizar departamentos')


		def leer_todo_departamentos():
			record=ver_depar.get_children()
			for element in record:
				ver_depar.delete(element)


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT DEPARTAMENTO,TASA FROM DEPARTAMENTOS")
			A=micursor.fetchall()
			for i in A:
				ver_depar.insert('',0,text=i[0],values=(i[1], ))

			miconexion.commit()



		def actualizar_tasa_departamento():
			try:
				ver_depar.item(ver_depar.selection())['text'][0]


			except IndexError:
				pass
				return

			try:
				if tasa_del_dolar_nueva.get()==0:
					pass
					return
			except TclError:
				pass
				return
			
			dep=ver_depar.item(ver_depar.selection())['text']
			ta=ver_depar.item(ver_depar.selection())['values'][0]
			

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			
			micursor.execute("UPDATE DEPARTAMENTOS SET TASA=? WHERE DEPARTAMENTO=? AND TASA=?",(tasa_del_dolar_nueva.get(),dep,ta))
			miconexion.commit()
			leer_todo_departamentos()




		ver_depar=ttk.Treeview(acd,style="mystyle.Treeview",columns=[f"#{n}" for n in range(1, 2)])
		
		ver_depar.place(x=0,y=100)

		
		

		scoll=Scrollbar(acd,command=ver_depar.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll.place(x=400,y=100,height=227)

		ver_depar.config(yscrollcommand=scoll.set)

		ver_depar.heading('#0',text='Departamentos',anchor=CENTER)
		ver_depar.heading('#1',text='Tasa',anchor=CENTER)
		

		ver_depar.column("#0",minwidth=100, width = 200)
		ver_depar.column("#1",minwidth=70, width = 200 )

		Label(acd,font='Helvetica 12',text='Tasa del Dolar',bg='#b6bdff').place(x=50,y=20)
		tasa_del_dolar_nueva.set('')
		Entry(acd,font='Helvetica 12',fg='black',relief='sunken',bd=5,textvariable=tasa_del_dolar_nueva).place(x=10,y=60)
		
		Button(acd,text='Aceptar',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=8,height=1,command=actualizar_tasa_departamento).place(x=5,y=330)

		leer_todo_departamentos()









	def Aceptar_tasa_moneda():
		Valor=messagebox.askquestion('BBDD','¿Desea cambiar la tasa de todo los departamentos a {}'.format(tasa_del_dolar.get()),parent=tm)
		if Valor=='yes':

			tasa.config(state='readonly')
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			
			micursor.execute("UPDATE DEPARTAMENTOS SET TASA=?",(tasa_del_dolar.get(), ))
			miconexion.commit()


			cambiar_tasa_moneda()
			agregar_tasa_moneda()

	def Editar_tasa_moneda():

		tasa.config(state='normal')

	def comprobacion_de_actualizar_productos():
		valor=messagebox.askquestion('BBDD','¿Seguro que desea actualizar \n el precio en BS.S de los productos \n segun la tasa actual?',parent=tm)
		if valor=='yes':
			pass




	Label(tm,text='Tasa Moneda',font='Helvetica 12',bg='#b6bdff').place(x=65,y=5)
	tasa=Entry(tm,bd=7,relief='sunken',font='Helvetica 12',textvariable=tasa_del_dolar,state='readonly')
	tasa.place(x=10,y=40,width=240,height=41)

	Button(tm,text='Aceptar',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=8,height=1,command=Aceptar_tasa_moneda).place(x=10,y=90)
	Button(tm,text='Editar',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=8,height=1,command=Editar_tasa_moneda).place(x=160,y=90)
	Button(tm,text='Actualizar por departamentos',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=25,height=1,command=actualizar_productos).place(x=10,y=150)
	Button(tm,text='Ver Tasas Monedas',font='Helvetica 12',fg='black',relief='raised',bd=7,cursor='hand2',width=25,height=1,command=ver_tasa_monedas).place(x=10,y=210)

	ver_tasa_moneda()

def ingresar_productos_a_lista_venta():

	miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
	mycursor=miconexion_dos.cursor()
	mycursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_PRODUCTO='"+producto_ingresar_V.get()+"'")
	precio_o=mycursor.fetchall()
	for i in precio_o:
		nombre=i[0]

		if cantidad_ingresar_V.get()>i[2]:
			
			messagebox.showwarning('Inventarios','No tiene suficiente Unidades')

			return
	mycursor.execute('SELECT DEPARTAMENTO FROM PRODUCTOS WHERE ID=? ',(identificador_ingresar_V.get(), ))
	F=mycursor.fetchall()
	for i in F:
		DEPAR=i[0]


	mycursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=? ',(DEPAR, ))
	F=mycursor.fetchall()
	for i in F:
		TASA_=i[0]


	miconexion_dos.commit()


	try:
		total_D.set(cantidad_ingresar_V.get()*precio_ingresar_D_V.get())
		total_B.set(total_D.get()*TASA_)

		total_D_sin_iva=cantidad_ingresar_V.get()*precio_ingresar_D_sin_iva_V.get()
		total_B_sin_iva=total_D_sin_iva*TASA_
	

		if cedula_cliente_V.get()!='':
			
		
			vender_producto()


			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()

			micursor.execute('SELECT DEPARTAMENTO FROM PRODUCTOS WHERE ID=? ',(identificador_ingresar_V.get(), ))
			F=micursor.fetchall()
			for i in F:
				DEPAR=i[0]

			micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=? ',(DEPAR, ))
			F=micursor.fetchall()
			for i in F:
				TASA_=i[0]






			precio_B_con_tasa=precio_ingresar_D_V.get()*TASA_

			sub_total_B_con_tasa=total_D_sin_iva*TASA_

			precio_ori_B_con_tasa=precio_original_D_V.get()*TASA_



			micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=?",(DEPAR, ))
			TODO=micursor.fetchall()
			for i in TODO:
				if i[2]!='':
					a=total_B.get()

					a1=a*i[2]
					a2=a1/100
					a3=a-a2

					total_B.set(a3)
					total_D.set(a3/TASA_)

					b=total_D_sin_iva*TASA_

					b1=b*i[2]
					b2=b1/100
					b3=b-b2

					sub_total_B_con_tasa=b3
					total_D_sin_iva=b3/TASA_

					c=precio_original_D_V.get()*TASA_

					c1=c*i[2]
					c2=c1/100
					c3=c-c2


					precio_ori_B_con_tasa=c3
					precio_original_D_V.set(c3/TASA_)

					producto_ingresar_V.set(producto_ingresar_V.get()+'   (Oferta)')


			datos=identificador_de_venta2.get(),cedula_cliente_V.get(),identificador_ingresar_V.get(),producto_ingresar_V.get(),cantidad_ingresar_V.get(),exento_ingresar_V.get(),unidad_ingresar_V.get(),precio_ingresar_D_V.get(),precio_B_con_tasa   ,total_D.get(),total_B.get(),sub_total_B_con_tasa    ,total_D_sin_iva   ,porcentaje_de_gacnancia_V.get(),precio_original_D_V.get(),precio_ori_B_con_tasa,fecha,true,DEPAR

			
			micursor.execute("INSERT INTO PRODUCTO_V VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))

			micursor.execute("SELECT ID_DEUDAS FROM DEUDAS WHERE BOOLEANOS=1")
			A=micursor.fetchall()
			for i in A:
				identificador_de_deuda2.set(i[0])

			
			datos2=identificador_de_deuda2.get(),cedula_cliente_V.get(),identificador_ingresar_V.get(),producto_ingresar_V.get(),cantidad_ingresar_V.get(),exento_ingresar_V.get(),unidad_ingresar_V.get(),precio_ingresar_D_V.get(),precio_B_con_tasa   ,total_D.get(),total_B.get(),sub_total_B_con_tasa    ,total_D_sin_iva   ,porcentaje_de_gacnancia_V.get(),precio_original_D_V.get(),precio_ori_B_con_tasa,fecha,true,DEPAR
			
			micursor.execute("INSERT INTO PRODUCTOS_DEUDAS VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos2))



			miconexion.commit()




			record=lista1v.get_children()
			for element in record:
				lista1v.delete(element)

			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
			a=micursor.fetchall()
			for i in a:

				total_venta_B.set(round(i[10]+total_venta_B.get(),2))
				total_venta_D.set(round(i[11]+total_venta_D.get(),2))

				

				total_venta_sin_iva_B.set(round(i[12]+total_venta_sin_iva_B.get(),2))
				total_venta_sin_iva_D.set(round(i[13]+total_venta_sin_iva_D.get(),2))


				round1=round(i[8],2)
				round2=round(i[10],2)
				ds=round(i[9],2)
				fd=round(i[11],2)
				lista1v.insert('',0,text=i[3],values=(i[4],i[5],i[7],i[19],round1,ds,round2,fd))
			
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND EXENTO=false")
			a=micursor.fetchall()

			for i in a:
				e=i[10]-i[13]

				r=i[11]-i[12]

				total_iva_B.set(round(r+total_iva_B.get(),2))
				total_iva_D.set(round(e+total_iva_D.get(),2))


			limpiar_suma()
			agregar_a_suma(total_venta_D.get(),total_venta_B.get(),total_venta_sin_iva_D.get(),total_venta_sin_iva_B.get(),total_iva_B.get(),total_iva_D.get())
	
			total_venta_B.set(0)
			total_venta_D.set(0)
			total_venta_sin_iva_B.set(0)
			total_venta_sin_iva_D.set(0)
			total_iva_B.set(0)
			total_iva_D.set(0)
			return
		else:
			messagebox.showerror('BBDD','Introdusca Cedula del cliente')
			return

	finally:
		pass
	


	
def verificar_cliente_V(event):

	if licencia_programa.get()=='no':
		Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
		if Valor=='yes':
			informacion_sobre_licencia()

		return



	cambiar_cedula_de_V()
	try:
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM CLIENTES WHERE CEDULA_CLIENTE="+cedula_cliente_V.get())
		elusuario=micursor.fetchall()
		for usuario in elusuario:
			Nombre_cliente_V.set(usuario[0])
			Apellido_cliente_V.set(usuario[1])
			cedula_cliente_V.set(usuario[2])
			Nombre_cliente_V2.set(usuario[5])
			client.configure(state='readonly')

		product.focus()
		cc=Nombre_cliente_V.get()+' '+Apellido_cliente_V.get()
		limpiar_cliente_v()
		agregar_cliente_v(cc)		
		miconexion.commit()

		

		if len(Nombre_cliente_V.get())==0:
			registro_cliente=messagebox.askquestion('BBDD','Cliente no registrado \n ¿Desea Registrar al cliente?')
			if registro_cliente=='yes':
				registrar_cliente_en_V()
				nombre_cliente_CTN.set(Nombre_cliente_V.get())
				apellido_cliente_CTN.set(Apellido_cliente_V.get())
				cedula_cliente_CTN.set(cedula_cliente_V.get())
				Nombre_cliente_V2.set('')
			
				borrar_campos_cliente_V()

	except sqlite3.OperationalError:
		pass	


def registrar_cliente_en_V():
	login_c=Toplevel(raiz)
	login_c.geometry('313x364')
	login_c.config(bg='#b6bdff')
	login_c.resizable(0,0)
	login_c.iconbitmap(logo)

#--------------------------------------


	def agregar_CTN_en_V():
		try:
			if len(nombre_cliente_CTN.get())!=0 and len(apellido_cliente_CTN.get())!=0:
				if len(direccion_cliente_CTN.get())==0:
					direccion_cliente_CTN.set('Nulo')


				if len(telefono_cliente_CTN.get())==0:
					telefono_cliente_CTN.set('Nulo')


				miconexion=sqlite3.connect('SISTEMA_LUMINA')
				micursor=miconexion.cursor()
				datos=nombre_cliente_CTN.get().capitalize(),apellido_cliente_CTN.get().capitalize(),cedula_cliente_CTN.get(),direccion_cliente_CTN.get(),telefono_cliente_CTN.get(),fecha
				micursor.execute("INSERT INTO CLIENTES VALUES(?,?,?,?,?,?,NULL)",(datos))
				miconexion.commit()

				cedula_cliente_V.set(cedula_cliente_CTN.get())

				verificar_cliente_V('1')
				borrar_campos_CTN_V()
				login_c.destroy()
			else:
				messagebox.showerror('Cliente','Se necesita por lo menos \n Nombre del cliente \n Apellido del cliente \n Cedula del cliente')


		except TclError:
			messagebox.showerror('BBDD','Faltan campos por escribir')

		except sqlite3.OperationalError:
			messagebox.showwarning('BBDD','Base de datos no creada')
		


	Label(login_c,text='Nombre',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=10,y=23)
	nombre2323_c=Entry(login_c,relief='sunken',font='Helvetica 12',fg='black',bd=10,textvariable=nombre_cliente_CTN)
	nombre2323_c.place(x=100,y=20)
	nombre2323_c.focus()

	Label(login_c,text='Apellido',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=10,y=86)
	apellido2323_c=Entry(login_c,relief='sunken',font='Helvetica 12',fg='black',bd=10,textvariable=apellido_cliente_CTN)
	apellido2323_c.place(x=100,y=80)


	Label(login_c,text='Cedula',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=10,y=146)
	cedula2323_c=Entry(login_c,relief='sunken',font='Helvetica 12',fg='black',bd=10,textvariable=cedula_cliente_CTN)
	cedula2323_c.place(x=100,y=140)


	Label(login_c,text='Direccion',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=10,y=206)
	direccion2323_c=Entry(login_c,relief='sunken',font='Helvetica 12',fg='black',bd=10,textvariable=direccion_cliente_CTN)
	direccion2323_c.place(x=100,y=200)

	Label(login_c,text='Telefono',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=10,y=266)
	telefono2323_c=Entry(login_c,relief='sunken',font='Helvetica 12',fg='black',bd=10,textvariable=telefono_cliente_CTN)
	telefono2323_c.place(x=100,y=260)

	Button(login_c,text='Registrar',width=33,height=1,cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',command=agregar_CTN_en_V).place(x=0,y=326)

def cambiar_cedula_de_V():
	try:
		miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
		mycursor=miconexion_dos.cursor()
		datos2=cedula_cliente_V.get()
		mycursor.execute("UPDATE PRODUCTO_V SET C_CLIENTE="+cedula_cliente_V.get()+" WHERE BOOLEANOSS =1")
		miconexion_dos.commit()
	except sqlite3.OperationalError:
		pass

def cambiar_true_a_false_V():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
		
		
	micursor.execute("UPDATE PRODUCTO_V SET BOOLEANOSS=0 WHERE BOOLEANOSS = 1")

	miconexion.commit()

	record=lista1v.get_children()
	for element in record:
		lista1v.delete(element)

def cambiar_true_a_false_D():
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
			
	micursor.execute("UPDATE PRODUCTOS_DEUDAS SET BOOLEANOSS=0 WHERE BOOLEANOSS = 1")


	miconexion.commit()
	record=lista1v.get_children()
	for element in record:
		lista1v.delete(element)
	
def limpiar_cliente_v():
	cliente_v_v.configure(state='normal')
	cliente_v_v.delete('1.0',END)
	cliente_v_v.configure(state='disabled')
	


def agregar_cliente_v(cliente):
	
	cliente_v_v.configure(state='normal')
	cliente_v_v.insert(END, cliente)
	cliente_v_v.configure(state='disabled')


def cambiar_cliente_V2():
	if cedula_cliente_V.get()!='':
		valor=messagebox.askquestion('CTN','¿Desea cambiar el cliente?')
		if valor=='yes':
			cambiar_cliente_V()
def cambiar_cliente_V():
	
	cedula_cliente_V.set('')

	limpiar_cliente_v()


	client.config(state='normal')

	borrar_campos_cliente_V()


def ingresar_ID_en_venta(event):
	if licencia_programa.get()=='no':
		Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
		if Valor=='yes':
			informacion_sobre_licencia()

		return

	global enlace
	if enlace==0:
		miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
		mycursor=miconexion_dos.cursor()

		
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:

			r=usuarios[0].startswith(producto_ingresar_V.get())
			k=usuarios[1].startswith(producto_ingresar_V.get().capitalize())
			if r==1 or k==1:
					

				mycursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(usuarios[0], ))
				precio_o=mycursor.fetchall()
				for i in precio_o:
					depar=i[13]
					mycursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
					A=mycursor.fetchall()
					for a in A:
						tasita=a[0]

					identificador_ingresar_V.set(i[0])		
					producto_ingresar_V.set(i[1])
					exento_ingresar_V.set(i[4])
					porcentaje_de_gacnancia_V.set(i[7])
					precio_ingresar_D_sin_iva_V.set(i[10])
					precio_ingresar_B_sin_iva_V.set(i[11])
					precio_original_D_V.set(i[5])
					precio_original_B_V.set(i[6])
					unidad_ingresar_V.set(i[3])
					precio_ingresar_D_V.set(i[8])
					print(i[8],tasita)
					precio_ingresar_B_V.set(i[8]*tasita)

		

		miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
		mycursor=miconexion_dos.cursor()
		mycursor.execute("SELECT * FROM COMBOS_C WHERE ID_COMBO='"+producto_ingresar_V.get()+"'")
		precio_o2=mycursor.fetchall()

		for i in precio_o2:	
			identificador_ingresar_V.set(i[0])		
			producto_ingresar_V.set(i[1])
			unidad_ingresar_V.set(i[2])
			precio_ingresar_D_V.set(i[2])
			precio_ingresar_B_V.set(i[3])

		miconexion_dos.commit()

		miconexion_dos.commit()
		miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
		mycursor=miconexion_dos.cursor()
		mycursor.execute("SELECT * FROM COMBOS_C WHERE NOMBRE_COMBO='"+producto_ingresar_V.get()+"'")
		precio_o2=mycursor.fetchall()

		for i in precio_o2:	
			identificador_ingresar_V.set(i[0])		
			producto_ingresar_V.set(i[1])
			unidad_ingresar_V.set('CMB')
			precio_ingresar_D_V.set(i[2])
			precio_ingresar_B_V.set(i[3])

			miconexion_dos.commit()
		Label(f1,font='Helvetica 12',fg='black',bg='#b6bdff',text=unidad_ingresar_V.get()).grid(row=4,column=2,padx=1)


		
		if len(unidad_ingresar_V.get())!=0:
			product.config(state='readonly')
			enlace=1
			canti.focus()

	else:
		try:
			if enlace==1:

				if unidad_ingresar_V.get()=='DTL':
					print('Detallado')



				miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
				mycursor=miconexion_dos.cursor()

				mycursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(identificador_ingresar_V.get(), ))
				precio_o=mycursor.fetchall()
				for i in precio_o:
					depar=i[13]
					exen=i[4]

					mycursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
					A=mycursor.fetchall()
					for a in A:
						tasita=a[0]



				mycursor.execute("SELECT * FROM OFERTAS WHERE CODIGO_PRODUCTO=?",(identificador_ingresar_V.get(), ))
				precio_o2=mycursor.fetchall()
				print('oferta')
				for i in precio_o2:	
					cantidad_oferta_V.set(i[4])
					print(cantidad_oferta_V.get(), '9')
					if cantidad_oferta_V.get()!='':
						

						identificador_ingresar_V.set(i[1])	
						producto_ingresar_V.set(i[2]+'   (Oferta)')


						porcentaje_de_gacnancia_V.set(i[4])
						
						
						
						
						unidad_ingresar_V.set(i[3])
						precio_ingresar_D_V.set(i[5])
						precio_ingresar_B_V.set(i[5]*tasita)

						if exen==1:

							precio_ingresar_D_sin_iva_V.set(i[5])
							precio_ingresar_B_sin_iva_V.set(i[5]*tasita)
						if exen==0:
							a=i[5]*IVA.get()
							b=a/100
							c=i[5]-b
							d=c*tasita

							precio_ingresar_D_sin_iva_V.set(c)
							precio_ingresar_B_sin_iva_V.set(d)



				

			
				ingresar_productos_a_lista_venta()
				product.focus()
				producto_ingresar_V.set('')
				cantidad_ingresar_V.set('')
				precio_ingresar_D_V.set('')
				unidad_ingresar_V.set('')
				product.config(state='normal')

				Label(f1,font='Helvetica 12',bg='#b6bdff',text='UND',fg='#b6bdff').grid(row=4,column=2,padx=1)
				
				enlace=0
		except TclError:
			cantidad_ingresar_V.set(1)
			print(precio_ingresar_B_V.get(),'precio_ingresar_B_V',precio_ingresar_D_V.get(),'precio_ingresar_D_V')

			ingresar_productos_a_lista_venta()
			product.focus()
			producto_ingresar_V.set('')
			cantidad_ingresar_V.set('')
			precio_ingresar_D_V.set(0)
			unidad_ingresar_V.set('')
			product.config(state='normal')
			Label(f1,font='Helvetica 12',fg='#b6bdff',bg='#b6bdff',text='UND').grid(row=4,column=2,padx=1)				
			enlace=0
#----------------

def limpiar_campos_V():
	global enlace
	producto_ingresar_V.set('')
	cantidad_ingresar_V.set('')
	precio_ingresar_D_V.set('')
	unidad_ingresar_V.set('')
	cantidad_busca.set('')
	producto_busca.set('')
	product.config(state='normal')
	product.focus()
	Label(f1,font='Helvetica 12',fg='#b6bdff',bg='#b6bdff',text='UND').grid(row=4,column=2,padx=1)

	
	enlace=0
enlacess=0
def ver_productos_en_V(event):
	Buscar_producto=StringVar()
	VP=Toplevel(raiz)
	VP.geometry('600x532')
	VP.iconbitmap(logo)
	VP.resizable(0,0)
	VP.configure(bg='#b6bdff')
	cantidad_busca.set('')
	cantidad2_busca.set('')
	tab_control = ttk.Notebook(VP)
	hija=Frame(tab_control)
	ventana=Frame(tab_control)
	identifi=StringVar()

	tab_control.add(hija, text='Productos')
	tab_control.add(ventana, text='Clientes')
	tab_control.pack(expand=1, fill='both')
	hija.config(bg='#b6bdff')
	ventana.config(bg='#b6bdff')


	def buscar_producto_V(event):

		if len(Buscar_producto.get())==0:
			record=lista_pV.get_children()
		
			for element in record:
				lista_pV.delete(element)
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				depar=usuarios[13]
				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
				A=micursor.fetchall()	
				for i in A:
					tasita=i[0]

				x=float(usuarios[8])
				f=float(usuarios[8]*tasita)
				gr=round(x,2)
				b=round(f,2)

				lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],gr,b))

		else:
			record=lista_pV.get_children()
		
			for element in record:
				lista_pV.delete(element)
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				depar=usuarios[13]
				micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
				A=micursor.fetchall()	
				for i in A:
					tasita=i[0]
				r=usuarios[0].startswith(Buscar_producto.get())
				k=usuarios[1].startswith(Buscar_producto.get().capitalize())
				if r==1 or k==1:
					x=float(usuarios[8])
					f=float(usuarios[8]*tasita)
					a=round(x,2)
					b=round(f,2)
					lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],a,b))
					
				
			miconexion.commit()
	


	def ver_productos():
		record=lista_pV.get_children()
		
		for element in record:
			lista_pV.delete(element)
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM PRODUCTOS ORDER BY(NOMBRE_PRODUCTO)DESC")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			depar=usuarios[13]
			micursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
			A=micursor.fetchall()	
			for i in A:
				tasita=i[0]


			x=float(usuarios[8])
			f=float(usuarios[8]*tasita)
			a=round(x,2)
			b=round(f,2)
			
			lista_pV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[3],a,b))
		
		miconexion.commit()
	   
		

	def ver_combos():
		record=lista_cV.get_children()

		for element in record:
			lista_cV.delete(element)	
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute('SELECT * FROM COMBOS_C ORDER BY (NOMBRE_COMBO)DESC')
		elusuario=micursor.fetchall()
		for i in elusuario:
			lista_cV.insert('',0,text=i[0],values=(i[1],i[2],i[3]))

		miconexion.commit()

	def limpiar_campos_hija():
		global enlacess
		Buscar_producto.set('')
		producto_ingresar_B.set('')
		cantidad_ingresar_B.set('')
		precio_ingresar_D_B.set('')
		unidad_ingresar_B.set('')
		cantidad_busca.set('')
		producto_busca.set('')
		enlacess=0
		Label(hija,font='Consolas 14',fg='black',bg='#b6bdff',text='   ').place(x=262,y=110)
	limpiar_campos_hija()


	def agregar_producto_desde_lista_pV():
		global enlacess
		try:
			lista_pV.item(lista_pV.selection())['text'][0]

		except IndexError:
			pass
			return
		canti.focus()

		identifis=lista_pV.item(lista_pV.selection())['text']
		identifi.set(identifis)
		

		miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
		mycursor=miconexion_dos.cursor()
		mycursor.execute("SELECT * FROM PRODUCTOS WHERE ID='"+identifi.get()+"'")
		precio_o=mycursor.fetchall()
		for i in precio_o:
			unidad_ingresar_B.set(i[3])
			producto_busca.set(i[1])

		Label(hija,font='Consolas 14',fg='black',bg='#b6bdff',text=unidad_ingresar_B.get()).place(x=262,y=110)
		enlacess=1


	def ingresar_producto_a_lista_pV():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return

		global enlacess
		try:
			if enlacess==0:
				agregar_producto_desde_lista_pV()
				
				return
			
		except:
			pass
		
		try :
			

			if enlacess==1:

				
				if cedula_cliente_V.get()!='':

					try:
						if cantidad_busca.get()=='':
							cantidad_busca.set(1)

					except TclError:
						cantidad_busca.set(1)


					
					miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
					mycursor=miconexion_dos.cursor()
					mycursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_PRODUCTO='"+producto_busca.get()+"'")
					precio_o=mycursor.fetchall()
					for i in precio_o:
						identificador_ingresar_B.set(i[0])		
						producto_ingresar_B.set(i[1])
						exento_ingresar_B.set(i[4])
						porcentaje_de_gacnancia_B.set(i[7])
						precio_ingresar_D_sin_iva_B.set(i[10])
						precio_ingresar_B_sin_iva_B.set(i[11])
						precio_original_D_B.set(i[5])
						precio_original_B_B.set(i[6])
						unidad_ingresar_B.set(i[3])
						precio_ingresar_D_B.set(i[8])
						precio_ingresar_B_B.set(i[9])





						miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
						mycursor=miconexion_dos.cursor()

						mycursor.execute("SELECT * FROM PRODUCTOS WHERE ID=?",(identificador_ingresar_B.get(), ))
						precio_o=mycursor.fetchall()
						for i in precio_o:
							depar=i[13]
							exen=i[4]

							mycursor.execute("SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=?",(depar, ))
							A=mycursor.fetchall()
							for a in A:
								tasita=i[0]



						


						if cantidad_busca.get()>i[2]:
							
							messagebox.showwarning('BBDD','No tine suficientes unidades')
							limpiar_campos_hija()
							return







					mycursor.execute('SELECT DEPARTAMENTO FROM PRODUCTOS WHERE NOMBRE_PRODUCTO=? ',(producto_busca.get(), ))
					F=mycursor.fetchall()
					for i in F:
						DEPAR=i[0]


					mycursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=? ',(DEPAR, ))
					F=mycursor.fetchall()
					for i in F:
						TASA_=i[0]




					
					total_D.set(cantidad_busca.get()*precio_ingresar_D_B.get())
					total_B.set(total_D.get()*TASA_)
					
					total_D_sin_iva=cantidad_busca.get()*precio_ingresar_D_sin_iva_B.get()
					total_B_sin_iva=total_D_sin_iva*TASA_

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT ID_VENTAS FROM VENTAS WHERE BOOLEANOS=1")
					a=micursor.fetchall()
					for i in a:
						identificador_de_venta2.set(i[0])
						
		
		
					miconexion.commit()
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					precio_B_con_tasa_2=total_D.get()*TASA_
					sub_total_con_tasa_2=total_D_sin_iva*TASA_
					precio_original_B_con_tasa_2=precio_original_D_B.get()*TASA_

					identificis=StringVar()
					micursor.execute("SELECT DEPARTAMENTO,EXENTO FROM PRODUCTOS WHERE ID=? ",(identificador_ingresar_B.get(), ))
					S=micursor.fetchall()
					for i in S:
						exen=i[1]
						identificis.set(i[0])



				
					micursor.execute('SELECT TASA FROM DEPARTAMENTOS WHERE DEPARTAMENTO=? ',(identificis.get(), ))
					F=micursor.fetchall()
					for i in F:
						TASA_=i[0]

					
					precio_B_con_tasa=precio_ingresar_D_B.get()*TASA_

					sub_total_B_con_tasa=total_D_sin_iva*TASA_

					precio_ori_B_con_tasa=precio_original_D_B.get()*TASA_

					#------

					micursor.execute("SELECT * FROM OFERTAS WHERE CODIGO_PRODUCTO=?",(identificador_ingresar_B.get(), ))
					precio_o3=micursor.fetchall()
					print('oferta')
					for i in precio_o3:	
						cantidad_oferta_B=i[4]
						print(cantidad_oferta_B, '9')
						if cantidad_oferta_B!='':
								

							identificador_ingresar_B.set(i[1])		
							producto_ingresar_B.set(i[2]+'   (Oferta)')


							porcentaje_de_gacnancia_B.set(i[4])


							precio_B_con_tasa=precio_ingresar_D_B.get()*TASA_

							sub_total_B_con_tasa=total_D_sin_iva*TASA_

							precio_ori_B_con_tasa=precio_original_D_B.get()*TASA_


	
							unidad_ingresar_B.set(i[3])
							


							if exen==1:

								total_D.set(i[5]*cantidad_busca.get())
								precio_ingresar_B_B.set(total_D.get()*TASA_*cantidad_busca.get())

								precio_ingresar_D_sin_iva_B.set(i[5]*cantidad_busca.get())
								precio_B_con_tasa_2=total_D.get()*TASA_


								total_D_sin_iva=total_D.get()
								sub_total_con_tasa_2=total_D.get()*TASA_


							if exen==0:
								a=i[5]*IVA.get()
								b=a/100
								c=i[5]-b
								d=c*TASA_

								precio_ingresar_D_sin_iva_B.set(c)
								precio_ingresar_B_sin_iva_B.set(d)


					micursor.execute("SELECT * FROM OFERTAS_DEPARTAMENTOS WHERE DEPARTAMENTO=?",(DEPAR, ))
					TODO=micursor.fetchall()
					for i in TODO:
						if i[2]!='':
							a=total_B.get()

							a1=a*i[2]
							a2=a1/100
							a3=a-a2

							precio_B_con_tasa_2=a3
							total_D.set(a3/TASA_)

							



							b=total_D_sin_iva*TASA_

							b1=b*i[2]
							b2=b1/100
							b3=b-b2

							sub_total_con_tasa_2=b3
							total_D_sin_iva=b3/TASA_




							c=precio_original_D_B.get()*TASA_

							c1=c*i[2]
							c2=c1/100
							c3=c-c2




							precio_original_B_con_tasa_2=c3
							precio_original_D_B.set(c3/TASA_)

							producto_ingresar_B.set(producto_ingresar_B.get()+'   (Oferta)')


								
					datos=identificador_de_venta2.get(),cedula_cliente_V.get(),identificador_ingresar_B.get(),producto_ingresar_B.get(),cantidad_busca.get(),exento_ingresar_B.get(),unidad_ingresar_B.get(),precio_ingresar_D_B.get(),    precio_B_con_tasa     ,total_D.get(),precio_B_con_tasa_2   ,sub_total_con_tasa_2,   total_D_sin_iva,porcentaje_de_gacnancia_B.get(),precio_original_D_B.get(),    precio_original_B_con_tasa_2    ,fecha,true,identificis.get()
					print(datos)
					micursor.execute("INSERT INTO PRODUCTO_V VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))
					




					micursor.execute("SELECT ID_DEUDAS FROM DEUDAS WHERE BOOLEANOS=1")
					A=micursor.fetchall()
					for i in A:
						identificador_de_deuda3.set(i[0])

					datos2=identificador_de_deuda3.get(),cedula_cliente_V.get(),identificador_ingresar_B.get(),producto_ingresar_B.get(),cantidad_busca.get(),exento_ingresar_B.get(),unidad_ingresar_B.get(),precio_ingresar_D_B.get(),precio_ingresar_B_B.get(),total_D.get(),precio_B_con_tasa_2   ,sub_total_con_tasa_2,   total_D_sin_iva,porcentaje_de_gacnancia_B.get(),precio_original_D_B.get(),    precio_original_B_con_tasa_2    ,fecha,true,identificis.get()
					micursor.execute("INSERT INTO PRODUCTOS_DEUDAS VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos2))


					miconexion.commit()


					record=lista1v.get_children()
					for element in record:
						lista1v.delete(element)

					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
					a=micursor.fetchall()
					for i in a:
						total_venta_B.set(round(i[10]+total_venta_B.get(),2))
						total_venta_D.set(round(i[11]+total_venta_D.get(),2))

				

						total_venta_sin_iva_B.set(round(i[12]+total_venta_sin_iva_B.get(),2))
						total_venta_sin_iva_D.set(round(i[13]+total_venta_sin_iva_D.get(),2))

						round1=round(i[8],2)
						round2=round(i[10],2)
						ds=round(i[9],2)
						fd=round(i[11],2)
						lista1v.insert('',0,text=i[3],values=(i[4],i[5],i[7],i[19],round1,ds,round2,fd))
					
		
			
					miconexion=sqlite3.connect('SISTEMA_LUMINA')
					micursor=miconexion.cursor()
					micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND EXENTO=false")
					a=micursor.fetchall()

					for i in a:
						e=i[10]-i[13]

						r=i[11]-i[12]

						total_iva_B.set(round(r+total_iva_B.get(),2))
						total_iva_D.set(round(e+total_iva_D.get(),2))


					limpiar_suma()
					agregar_a_suma(total_venta_D.get(),total_venta_B.get(),total_venta_sin_iva_D.get(),total_venta_sin_iva_B.get(),total_iva_B.get(),total_iva_D.get())
					limpiar_campos_hija()
					total_venta_B.set(0)
					total_venta_D.set(0)
					total_venta_sin_iva_B.set(0)
					total_venta_sin_iva_D.set(0)
					total_iva_B.set(0)
					total_iva_D.set(0)
					limpiar_campos_hija()
					bus.focus()
					enlacess=0
					return
				else:
					limpiar_campos_hija()
					messagebox.showerror('BBDD','Introdusca Cedula del cliente',parent=hija)
					limpiar_campos_hija()
					bus.focus()
					return

	
		finally:
			pass

	style = ttk.Style()
	style.configure("Treeview", font=('Helvetica', 10))

	lista_pV=ttk.Treeview(hija,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 5)])
	lista_pV.place(x=0,y=160)

	scoll=Scrollbar(hija,command=lista_pV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll.place(x=580,y=185,height=320)
	lista_pV.config(yscrollcommand=scoll.set)

	lista_pV.heading('#0',text='Codigo',anchor=CENTER)
	lista_pV.heading('#1',text='Productos',anchor=CENTER)
	lista_pV.heading('#2',text='Unidad',anchor=CENTER)
	lista_pV.heading('#3',text='Precio $',anchor=CENTER)
	lista_pV.heading('#4',text='Precio Bs.S',anchor=CENTER)

	lista_pV.column("#0",minwidth=100, width = 100)
	lista_pV.column("#1",minwidth=70, width = 190 )
	lista_pV.column("#2",minwidth=70, width = 50 )
	lista_pV.column("#3",minwidth=70, width = 100 )
	lista_pV.column("#4",minwidth=70, width = 160 )
	ver_productos()



	




	product=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',state='readonly',textvariable=producto_busca)
	product.place(x=0,y=110,height=41)

	canti=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=cantidad_busca)
	canti.place(x=200,y=110,width=60,height=41)
	Button(hija,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=ingresar_producto_a_lista_pV).place(x=298,y=111)

	bus=Entry(hija,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=Buscar_producto)
	bus.place(x=0,y=10,height=41)
	Button(hija,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_producto_V('1')).place(x=200,y=10)

	bus.focus()

	bus.bind("<KeyRelease>", buscar_producto_V)
	


	def sub_menu(event):
		try:
			menu.post(event.x_root, event.y_root)
		finally:
			menu.grab_release()

	menu = Menu(lista_pV, tearoff=0)
	menu.add_command(label="Buscar",command=lambda:buscar_producto_V('1'))
	menu.add_command(label="Aceptar",command=ingresar_producto_a_lista_pV)
	menu.add_separator()
	menu.add_command(label=' limpiar                    ',command=limpiar_campos_hija)
	
	

	lista_pV.bind("<Button-3>", sub_menu)

	hija.bind("<Button-3>", sub_menu)



#---------------------------------------
	
#---------------------------------------------
#-----------------------------------------------
#---------------------------------------------

	def buscar_cliente_en_V(event):
		s=0

		if len(Buscar_combo2.get())==0:
			ver_clientes_en_V()
			return


		record=lista_cV.get_children()
		for element in record:
			lista_cV.delete(element)
    
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM CLIENTES")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			e=Buscar_combo2.get().capitalize()
			x=usuarios[0].startswith(e)
			a0=str(usuarios[2])
			d=a0.startswith(Buscar_combo2.get())
			
			
			if x==1 or d==1:	
				a=usuarios[0]+' '+usuarios[1]
				lista_cV.insert('',0,text=a,values=(usuarios[2],usuarios[3],usuarios[4],usuarios[5]))
   




	def ver_clientes_en_V():
		record=lista_cV.get_children()
		for element in record:
			lista_cV.delete(element)
    
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM CLIENTES")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			a=usuarios[0]+' '+usuarios[1]
			lista_cV.insert('',0,text=a,values=(usuarios[2],usuarios[3],usuarios[4],usuarios[5]))
   


	def agregar_cliente_a_lista_ventana():
		try:
			lista_cV.item(lista_cV.selection())['text'][0]

		except IndexError:
			pass
			return
		

		cedula=lista_cV.item(lista_cV.selection())['values'][0]
		if len(cedula_cliente_V.get())==0:
			cedula_cliente_V.set(cedula)
			verificar_cliente_V('1')
		else:
			valor=messagebox.askquestion('Ventas','¿Desea cambiar el cliente?',parent=ventana)
			if valor=='yes':
				cambiar_cliente_V()
		



	lista_cV=ttk.Treeview(ventana,style="Treeview",height=16,columns=[f"#{n}" for n in range(1, 4)])
	lista_cV.place(x=0,y=160)
	

	scoll3=Scrollbar(ventana,command=lista_cV.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	scoll3.place(x=580,y=185,height=320)
	lista_cV.config(yscrollcommand=scoll3.set)

	lista_cV.heading('#0',text='Nombre',anchor=CENTER)
	lista_cV.heading('#1',text='Cedula',anchor=CENTER)
	lista_cV.heading('#2',text='Direccion',anchor=CENTER)
	lista_cV.heading('#3',text='Telefono',anchor=CENTER)

	lista_cV.column("#0",minwidth=100, width = 230)
	lista_cV.column("#1",minwidth=70, width = 80)
	lista_cV.column("#2",minwidth=70, width = 180 )
	lista_cV.column("#3",minwidth=70, width = 110 )


	Button(ventana,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=agregar_cliente_a_lista_ventana).place(x=0,y=111)

	qlq=Entry(ventana,font='Helvetica 12',bd=7,relief='sunken',fg='black',textvariable=Buscar_combo2)
	qlq.place(x=0,y=10,height=41)
	Button(ventana,cursor='hand2',text='Buscar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:buscar_cliente_en_V('1')).place(x=200,y=10)
	qlq.bind('<Key>',buscar_cliente_en_V)


	ver_clientes_en_V()
#----------------------------------------------------------
#-----------------------------------------------------

	def limpiar_campos_ventana():
		cantidad2_busca.set('')
		combo_busca.set('')
		identificador_ingresar_B.set('')
		producto_ingresar_B.set('')
		precio_ingresar_D_B.set('')
		precio_ingresar_B_B.set('')
		unidad_ingresar_B.set('')
		cantidad_ingresar_B.set('')
		cantidad2_busca.set('')
		Buscar_combo2.set('')
	limpiar_campos_ventana()
	def agregar_combo_de_lista_cV():
		try:
		
			lista_cV.item(lista_cV.selection())['text'][0]
		except IndexError:
			pass
			return
		canti2.focus()
		nombre=lista_cV.item(lista_cV.selection())['values'][0]
		identificador_de_combo.set(lista_cV.item(lista_cV.selection())['text'])
		combo_busca.set(nombre)

		miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
		mycursor=miconexion_dos.cursor()
		mycursor.execute("SELECT * FROM COMBOS_C WHERE ID_COMBO='"+identificador_de_combo.get()+"'")
		precio_o=mycursor.fetchall()
		for i in precio_o:
			unidad_ingresar_V.set(i[2])


	def buscar_combos_V():
		record=lista_cV.get_children()
		
		for element in record:
			lista_cV.delete(element)
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute("SELECT * FROM COMBOS_C ORDER BY(NOMBRE_COMBO)DESC")
		elusuario=micursor.fetchall()
		for usuarios in elusuario:
			r=usuarios[0].startswith(Buscar_combo2.get())
			k=usuarios[1].startswith(Buscar_combo2.get())
			if r==1:
				lista_cV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[2],usuarios[3]))

			if k==1:
				lista_cV.insert('',0,text=usuarios[0],values=(usuarios[1],usuarios[2],usuarios[3]))
		


		miconexion.commit()

	

	def ingresar_combo_a_lista_V():
		global enlace3
		try:
			if enlace3==0:
				agregar_combo_de_lista_cV()
				enlace3=1
				return

		except:
			pass

		try:
			if enlace3==1:
			
				miconexion_dos=sqlite3.connect('SISTEMA_LUMINA')
				mycursor=miconexion_dos.cursor()
				mycursor.execute("SELECT * FROM COMBOS_C WHERE ID_COMBO='"+identificador_de_combo.get()+"'")
				precio_o=mycursor.fetchall()
				for i in precio_o:
					identificador_ingresar_V.set(i[0])
						
					producto_ingresar_V.set(i[1])
				
					precio_ingresar_D_V.set(i[2])
				
					precio_ingresar_B_V.set(i[3])
				
					unidad_ingresar_V.set('CMB')
					cantidad_ingresar_V.set(cantidad2_busca.get())
				

				miconexion_dos.commit()
				
				ingresar_productos_a_lista_venta()
				cantidad2_busca.set('')
				combo_busca.set('')
				identificador_ingresar_V.set('')
				producto_ingresar_V.set('')
				precio_ingresar_D_V.set('')
				precio_ingresar_B_V.set('')
				unidad_ingresar_V.set('')
				cantidad_ingresar_V.set('')
				cantidad2_busca.set('')
				enlace3=0
		except TclError:
			cantidad_ingresar_V.set(1)
			ingresar_productos_a_lista_venta()
			cantidad2_busca.set('')
			combo_busca.set('')
			identificador_ingresar_V.set('')
			producto_ingresar_V.set('')
			precio_ingresar_D_V.set('')
			precio_ingresar_B_V.set('')
			unidad_ingresar_V.set('')
			cantidad_ingresar_V.set('')
			cantidad2_busca.set('')
			enlace3=0

	def productos_del_combo():
		try:
			lista_cV.item(lista_cV.selection())['text']
		except IndexError:
			messagebox.showerror('Ventas','No ha seleccionado ningun combo',parent=ventana)
			return
		verp=Toplevel(ventana)
		
		ancho_ventana = 300
		alto_ventana = 387
		x_ventana = verp.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = verp.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		verp.geometry(posicion)
		
		verp.resizable(0,0)
		verp.iconbitmap(logo)

		id_produc_c=lista_cV.item(lista_cV.selection())['text']

		def ver_productos_del_combo():
			record=lista_pc.get_children()
			for element in record:
				lista_pc.delete(element)
    
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute("SELECT * FROM PRODUCTOS_C WHERE ID_COMBO='"+id_produc_c+"'")
			elusuario=micursor.fetchall()
			for usuarios in elusuario:
				lista_pc.insert('',0,text=usuarios[1],values=(usuarios[2]))
   


		lista_pc=ttk.Treeview(verp,style="mystyle.Treeview",height=18,columns=2)
		lista_pc.place(x=0,y=0)

		scoll3=Scrollbar(verp,bg='#949494',command=lista_pc.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
		scoll3.place(x=282,y=23,height=361)
		lista_pc.config(yscrollcommand=scoll3.set)

		lista_pc.heading('#0',text='Productos',anchor=CENTER)
		lista_pc.heading('#1',text='Cantidad',anchor=CENTER)


		lista_pc.column("#0",minwidth=70, width = 200)
		lista_pc.column("#1",minwidth=70, width = 100)

		ver_productos_del_combo()


	

	def sub_menu2(event):
		try:
			menu2.post(event.x_root, event.y_root)
		finally:
			menu2.grab_release()

	menu2 = Menu(lista_pV, tearoff=0)
	menu2.add_command(label="Agregar",command=agregar_combo_de_lista_cV)
	menu2.add_command(label="Aceptar",command=ingresar_combo_a_lista_V)
	menu2.add_separator()
	menu2.add_command(label='Limpiar                    ',command=limpiar_campos_ventana)
	menu2.add_command(label='Ver Productos del combo           ',command=productos_del_combo)
	

	lista_cV.bind("<Button-3>", sub_menu2)

	ventana.bind("<Button-3>", sub_menu2)



def editar_producto_en_V(event):
	try:
		lista1v.item(lista1v.selection())['text'][0]

	except IndexError:
		pass
		return

	editar=Toplevel(raiz)
	editar.config(bg='#b6bdff')
	editar.title('Editar Producto')
	editar.geometry('400x200')
	editar.resizable(0,0)
	editar.iconbitmap(logo)
	editar.grab_set()

	ide=lista1v.item(lista1v.selection())['text']
	produc=lista1v.item(lista1v.selection())['values'][0]
	cantid=lista1v.item(lista1v.selection())['values'][1]
	unida=lista1v.item(lista1v.selection())['values'][2]
	precio_Do=lista1v.item(lista1v.selection())['values'][3]
	precio_Bo=lista1v.item(lista1v.selection())['values'][4]
	total_Do=lista1v.item(lista1v.selection())['values'][5]
	total_Bo=lista1v.item(lista1v.selection())['values'][6]

	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos=N,ide,produc,cantid,unida,precio_Do,precio_Bo,total_Do,total_Bo
	micursor.execute("SELECT PRODUCTO FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND ID_VENTA=? AND CODIGO_PRODUCTO=? AND PRODUCTO=? AND CANTIDAD=? AND UNIDAD=? AND PRECIO_D=? AND PRECIO_B=? AND PRECIO_TOTAL_D=? AND PRECIO_TOTAL_B=?",(datos))

	micursor.execute("SELECT ID_DEUDAS FROM DEUDAS WHERE BOOLEANOS=1 ")
	A=micursor.fetchall()
	for i in A:
		identificador_de_deuda.set(i[0])


	miconexion.commit()

	editar_producto_V.set(produc)
	editar_cantidad_producto_V.set(cantid)

	def actualizar_producto_V():
		borrar_producto_en_V()
		producto_ingresar_V.set(produc)
		try:
			cantidad_ingresar_V.set(editar_cantidad_producto_V.get())

		except TclError:
			cantidad_ingresar_V.set(1)

		ingresar_ID_en_venta('1')
		ingresar_productos_a_lista_venta()
		limpiar_campos_V()
		editar.destroy()


	Label(editar,text='Producto ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=20)
	nombre2323=Entry(editar,state='readonly',relief='sunken',textvariable=editar_producto_V,font='Helvetica 12',fg='black',bd=10)
	nombre2323.place(x=140,y=20)
	nombre2323.focus()

	Label(editar,text='Cantidad ',font='Helvetica 12',fg='black',bg='#b6bdff').place(x=40,y=80)
	cantidad2323=Entry(editar,relief='sunken',font='Helvetica 12',textvariable=editar_cantidad_producto_V,fg='black',bd=10)
	cantidad2323.place(x=140,y=80)


	Button(editar,text='Guardar',cursor='hand2',font='Helvetica 12',fg='black',bd=10,relief='raised',width=42,command=actualizar_producto_V).place(x=0,y=155)




def comprobacion_borrar_producto_en_V(event):
	
	try:
		lista1v.item(lista1v.selection())['text'][0]
	except TclError:
		continua2.set('')
		return

	except IndexError:
		continua2.set('')
		return
	
	continua_V.set(messagebox.askquestion('BBDD','Desea borrar este producto'))
	if continua_V.get()=='yes':
		borrar_producto_en_V()

def borrar_producto_en_V():
	N=0
	ide=lista1v.item(lista1v.selection())['text']
	produc=lista1v.item(lista1v.selection())['values'][0]
	cantid=lista1v.item(lista1v.selection())['values'][1]
	unida=lista1v.item(lista1v.selection())['values'][2]
	precio_Do=lista1v.item(lista1v.selection())['values'][3]
	precio_Bo=lista1v.item(lista1v.selection())['values'][4]
	total_Do=lista1v.item(lista1v.selection())['values'][5]
	total_Bo=lista1v.item(lista1v.selection())['values'][6]
	
	if cantid==3:
		cantid=3.0
	
	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	datos=ide,cantid
	micursor.execute("DELETE FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND CODIGO_PRODUCTO=? AND CANTIDAD=? ",(datos))

	datos2=ide,cantid
	micursor.execute("DELETE FROM PRODUCTOS_DEUDAS WHERE BOOLEANOSS=1 AND CODIGO_PRODUCTO=? AND CANTIDAD=? ",(datos2))

	miconexion.commit()

	record=lista1v.get_children()
	for element in record:
		lista1v.delete(element)

	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1")
	a=micursor.fetchall()
	for i in a:
		total_venta_B.set(round(i[10]+total_venta_B.get(),2))
		total_venta_D.set(round(i[11]+total_venta_D.get(),2))

		total_venta_sin_iva_B.set(round(i[12]+total_venta_sin_iva_B.get(),2))
		total_venta_sin_iva_D.set(round(i[13]+total_venta_sin_iva_D.get(),2))

		
	
		lista1v.insert('',0,text=i[3],values=(i[4],i[5],i[7],i[19],i[8],i[9],i[10],i[11]))
			

	miconexion=sqlite3.connect('SISTEMA_LUMINA')
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM PRODUCTO_V WHERE BOOLEANOSS=1 AND EXENTO=false")
	a=micursor.fetchall()
	for i in a:
				
		iva=IVA.get()/100+1
		e=i[10]-i[13]
		h=e

		r=i[11]-i[12]
		j=r
				
	
		total_iva_B.set(round(j+total_iva_B.get(),2))
		total_iva_D.set(round(h+total_iva_D.get(),2))
	limpiar_suma()
	agregar_a_suma(total_venta_D.get(),total_venta_B.get(),total_venta_sin_iva_D.get(),total_venta_sin_iva_B.get(),total_iva_B.get(),total_iva_D.get())
		
	total_iva_D.set(0)
	total_iva_B.set(0)
	total_venta_B.set(0)
	total_venta_D.set(0)
	total_venta_sin_iva_B.set(0)
	total_venta_sin_iva_D.set(0)
		
	

def limpiar_suma():
	Total_B2.configure(state='normal')
	Total_B2.delete('1.0', END)
	Total_B2.configure(state='disabled')

	Total_D2.configure(state='normal')
	Total_D2.delete('1.0',END)
	Total_D2.configure(state='disabled')

	Total_D3.configure(state='normal')
	Total_D3.delete('1.0',END)
	Total_D3.configure(state='disabled')
	


def agregar_a_suma(dolar,bolivar,no_iva_b,no_iva_d,iva_b,iva_d):
	
	Total_D3.configure(state='normal')
	
	dinero = '{:,}'.format(dolar)
	dinero2 = '{:,}'.format(bolivar)
	
	a=dinero,'(',dinero2,')'
	Total_D3.insert(END, a)
	Total_D3.configure(state='disabled')

	dinero5 = '{:,}'.format(iva_b)
	dinero6 = '{:,}'.format(iva_d)

	c=dinero5,'(',dinero6,')'

	Total_D2.configure(state='normal')
	Total_D2.insert(END,c)
	Total_D2.configure(state='disabled')


	dinero3 = '{:,}'.format(no_iva_d)
	dinero4 = '{:,}'.format(no_iva_b)
	d=' '
	b=dinero3,'(',dinero4,')'



	Total_B2.configure(state='normal')
	Total_B2.insert(END,b)
	Total_B2.configure(state='disabled')
	return


def registrar_usuario_V():
	

	login=Toplevel(raiz)
	login.geometry('410x400')
	login.configure(bg='#b6bdff')
	login.title('Registrar Usuarios')
	login.resizable(0,0)

	nombre_usuario=StringVar()
	numero_caja=IntVar()

	def cambiar_de_1_a_0_usu():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute('UPDATE USUARIOS SET BOOLEANO=0 WHERE BOOLEANO=1')
		miconexion.commit()

	def agregar_usuario():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return
		if len(nombre_usuario.get())!=0 and numero_caja.get()!='':
			
			miconexion=sqlite3.connect('SISTEMA_LUMINA')
			micursor=miconexion.cursor()
			micursor.execute('UPDATE USUARIOS SET ESTADO=0 WHERE BOOLEANO=1')
			datos=nombre_usuario.get(),numero_caja.get(),fecha,1,1
			micursor.execute('INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)',(datos))

			miconexion.commit()
			numero_caja.set('')
			nombre_usuario.set('')
			leer_todo_usuarios()
		else:
			messagebox.showerror('BBDD','Faltan Campos por Escribir',parent=login)
			return

	def leer_todo_usuarios():
		recor=lista_usu.get_children()
		for i in recor:
			lista_usu.delete(i)


		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute('SELECT * FROM USUARIOS')
		A=micursor.fetchall()
		for i in A:
			if i[4]==1 and i[5]==1:
				estado='Activo'
			elif i[4]==0 and i[5]==1:
				estado='Inactivo'

			elif i[5]==0:
				estado='Despedido'
			lista_usu.insert('',0,text=i[1],values=(i[2],i[3],estado))


		miconexion.commit()

	def despedir_usuario():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return
		Valor=messagebox.askquestion('BBDD','¿Desea Despedir este Usuario?',parent=login)
		if Valor=='no':
			pass
			return

		try:
			ide=lista_usu.item(lista_usu.selection())['text']
			produc=lista_usu.item(lista_usu.selection())['values'][0]
			cantid=lista_usu.item(lista_usu.selection())['values'][1]
			
			
		except IndexError:
			pass
			return
			

		datos=ide,cantid,produc
		print(datos)
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute('UPDATE USUARIOS SET BOOLEANO=0 WHERE NOMBRE_USUARIO=? AND FECHA=? AND NUMERO_CAJA=?',(datos))
		miconexion.commit()

		leer_todo_usuarios()
	def activar_usuario():
		if licencia_programa.get()=='no':
			Valor=messagebox.askquestion('BBDD','Licencia Agotada Necesita Renovar La licencia \n ¿Desea mas informacion?')
			if Valor=='yes':
				informacion_sobre_licencia()

			return
		Valor=messagebox.askquestion('BBDD','¿Desea Activar este Usuario?',parent=login)
		if Valor=='no':
			pass
			return

		try:
			ide=lista_usu.item(lista_usu.selection())['text']
			produc=lista_usu.item(lista_usu.selection())['values'][0]
			cantid=lista_usu.item(lista_usu.selection())['values'][1]
			
			
		except IndexError:
			pass
			return
			

		datos=ide,cantid,produc
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()



		micursor.execute('SELECT * FROM USUARIOS WHERE NOMBRE_USUARIO=? AND FECHA=? AND NUMERO_CAJA=?',(datos))
		A=micursor.fetchall()
		for i in A:
			if i[5]==0:
				messagebox.showerror('BBDD','Este Usuario Esta Despedido',parent=login)
				return





		micursor.execute('UPDATE USUARIOS SET ESTADO=0')


		micursor.execute('UPDATE USUARIOS SET ESTADO=1 WHERE NOMBRE_USUARIO=? AND FECHA=? AND NUMERO_CAJA=?',(datos))
		miconexion.commit()

		leer_todo_usuarios()


	numero_caja.set('')
	Label(login,text='Nombre de Usuario',font='Helvetica 12',bg='#b6bdff').place(x=30,y=30)
	Label(login,text='Numero de Caja',font='Helvetica 12',bg='#b6bdff').place(x=200,y=30)


	Entry(login,relief='sunken',font='Helvetica 12',bd=7,width=18,textvariable=nombre_usuario).place(x=10,y=60,height=41)

	Entry(login,relief='sunken',font='Helvetica 12',bd=7,width=10,textvariable=numero_caja).place(x=200,y=60,height=41)

	Button(login,text='Agregar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=agregar_usuario).place(x=320,y=60)


	lista_usu=ttk.Treeview(login,height=11,style="Treeview",columns=[f"#{n}" for n in range(1, 4)])
	
	lista_usu.place(x=0,y=105)


	barrita=Scrollbar(login,command=lista_usu.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
	barrita.place(x=392,y=128,height=224)
	lista_usu.config(yscrollcommand=barrita.set)
		
	lista_usu.heading('#0',text='Usuario',anchor=CENTER)
	lista_usu.heading('#1',text='Numero de Caja',anchor=CENTER)
	lista_usu.heading('#2',text='Fecha',anchor=CENTER)
	lista_usu.heading('#3',text='Estado',anchor=CENTER)

	lista_usu.column("#0",minwidth=70, width = 100)
	lista_usu.column("#1",minwidth=70, width = 105)
	lista_usu.column("#2",minwidth=70, width = 102)
	lista_usu.column("#3",minwidth=70, width = 100)

	Button(login,text='Activar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=activar_usuario).place(x=5,y=357)
	Button(login,text='Despedir',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=despedir_usuario).place(x=95,y=357)
	
	leer_todo_usuarios()

def agregar_forma_de_pago(variable):
	pago=Toplevel(variable)
	ancho_ventana = 300
	alto_ventana = 200
	x_ventana = pago.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = pago.winfo_screenheight() // 2 - alto_ventana // 2
	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
	pago.geometry(posicion)

	
	pago.config(bg='#b6bdff')
	pago.title('Formas De Pago')
	
	pago.resizable(0,0)
	pago.iconbitmap(logo)
	forma_de_pago_nueva=StringVar()
	uno=StringVar()

	def ver_formas_de_pago():
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
			
		micursor.execute("SELECT FORMAS_DE_PAGO FROM FORMAS_DE_PAGO")
		A=micursor.fetchall()
		
		f_pago['values']= (list(f"{str(n[0])}" for n in A))

	def crear_nueva_forma_de_pago():
		if len(forma_de_pago_nueva.get())==0:
			pass
			return

		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute('SELECT FORMAS_DE_PAGO FROM FORMAS_DE_PAGO WHERE FORMAS_DE_PAGO=?',(forma_de_pago_nueva.get(), ))
		A=micursor.fetchall()
		for i in A:
			if i[0]!='':
				forma_de_pago_nueva.set('')
				messagebox.showerror('BBDD','Esta forma de pago a existe',parent=pago)
				return

		micursor.execute('INSERT INTO FORMAS_DE_PAGO VALUES(NULL,?)',(forma_de_pago_nueva.get(), ))
		miconexion.commit()
		forma_de_pago_nueva.set('')
		ver_formas_de_pago()

	def borrar_forma_de_pago():
		Valor=messagebox.askquestion('BBDD','¿Desea Borrar la Forma de Pago {}?'.format(f_pago.get()),parent=pago)
		if Valor=='no':
			pass
			return
		miconexion=sqlite3.connect('SISTEMA_LUMINA')
		micursor=miconexion.cursor()
		micursor.execute('DELETE FROM FORMAS_DE_PAGO WHERE FORMAS_DE_PAGO=?',(f_pago.get(), ))
		miconexion.commit()
		ver_formas_de_pago()
		f_pago.current(0)
		forma_de_pago_nueva.set('')

	combo_day=Frame(pago,bg='silver')
	combo_day.place(x=20,y=100)
		

	f_pago=ttk.Combobox(combo_day,font='Helvetica 11', state="readonly", height=12,width=20)
	ver_formas_de_pago()
	f_pago.current(0)
	
	f_pago.pack(side=tk.RIGHT)


	Label(pago,bg='#b6bdff',text='Forma De pago',font='Helvetica 12').place(x=55,y=20)
	Entry(pago,fg='black',bd=7,relief='sunken',font='Helvetica 12',textvariable=forma_de_pago_nueva).place(x=10,y=50)
	Button(pago,text='Agregar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=crear_nueva_forma_de_pago).place(x=210,y=48)

	Button(pago,text='Borrar',cursor='hand2',width=8,height=1,bd=5,relief='raised',font='Helvetica 12',command=borrar_forma_de_pago).place(x=10,y=150)


	

def times():
	tiempo.set(time.strftime('%H:%M:%S'))
	clock.configure(text=tiempo.get(),bg='#b8d3ff',fg='black',font='Consolas 14')
	clock.after(200,times)

def times_compra(hola):
	tiempo.set(time.strftime('%H:%M:%S'))
	hola.configure(text=tiempo.get(),bg='#b8d3ff',fg='black',font='Consolas 14')
	hola.after(200,times)
#--------------Ventana principal----------------------------

def sub_menu(event):
    try:
        menu.post(event.x_root, event.y_root)
    finally:
        menu.grab_release()

'''def show_menu(e):
       w = e.widget
       the_menu.entryconfigure("Cut", command=lambda: w.event_generate("<<Cut>>"))
       the_menu.entryconfigure("Copy", command=lambda: w.event_generate("<<Copy>>"))
       the_menu.entryconfigure("Paste", command=lambda: w.event_generate("<<Paste>>"))
       the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

def display_popup(event):
	menu.post(event.x_root, event.y_root)
    
def popup_copy():
	
	raiz.event_generate("<<Copy>>")


def popup_cut():
	
	raiz.event_generate("<<Cut>>")


def popup_paste():
	
	raiz.event_generate("<<Paste>>")'''



menu = Menu(raiz, tearoff=0)
menu.add_command(label="Borrar",command=lambda:comprobacion_borrar_producto_en_V('1'))
menu.add_command(label="Editar",command=lambda:editar_producto_en_V('1'),underline=1)
menu.add_command(label='Limpiar',command=limpiar_campos_V)
menu.add_separator()
menu.add_command(label='Buscador           ',command=lambda:ver_productos_en_V('1'))
menu.add_command(label='Cambiar Cliente              ',command=cambiar_cliente_V2)
menu.add_command(label='Tasa Moneda               ',command=lambda:tasa_moneda('1'))
menu.add_command(label='Inventarios           ',command=lambda:INVENTARIOS('1'))
menu.add_command(label='Limpiar Todo                         ',command=limpiar_todo_V)
menu.add_command(label='Agregar Forma de Pago                  ',command=lambda:agregar_forma_de_pago(raiz))
menu.add_separator()
menu.add_command(label='Vender',command=lambda:vender('1'))
menu.add_separator()
menu.add_command(label='Salir',command=salir)





raiz.bind_class("Text", "<Control-a>")
raiz.bind("<Button-3>", sub_menu)
raiz.bind_all("<Control-i>", INVENTARIOS)
raiz.bind_all("<Control-t>", tasa_moneda)
raiz.bind_all("<Control-e>", editar_producto_en_V)
raiz.bind_all("<Control-d>", comprobacion_borrar_producto_en_V)
raiz.bind_all("<Control-a>", vender)
raiz.bind("<Control-b>", ver_productos_en_V)



barramenu=Menu(raiz)
raiz.configure(menu=barramenu)
archivomenu=Menu(barramenu,tearoff=0)
archivomenu.add_command(label='Conectar',command=funcion_clave)
archivomenu.add_separator()
archivomenu.add_command(label='Salir',command=salir)
barramenu.add_cascade(label='BBDD',menu=archivomenu)




ayuda=Menu(barramenu,tearoff=0)
ayuda.add_command(label='Acerca de...',command=informacion_sobre_licencia)
ayuda.add_separator()
ayuda.add_command(label='Licencia',command=licencia)
barramenu.add_cascade(label='Ayuda',menu=ayuda)
#--------------------------------------------------------------------------------------
style = ttk.Style()
style.configure("Treeview", highlightthickness=0, bd=0, font=('Helvetica', 10))


frame_lista=Frame(raiz,bg='#b6bdff')
frame_lista.grid(row=1,column=0,sticky='NSEW',columnspan=2)

lista1v=ttk.Treeview(frame_lista,style='Treeview',columns=[f"#{n}" for n in range(1, 9)])
lista1v.pack(expand=1,fill=BOTH)
lista1v.grid(row=0,column=0,sticky='nsew',columnspan=4,rowspan=4)
frame_lista.rowconfigure(0,weight=5)
frame_lista.columnconfigure(0,weight=5)


scoll=Scrollbar(frame_lista,command=lista1v.yview)#PARA HACER LA BARRA DESPLAZADORA DE COMENTARIOS
scoll.grid(row=0,column=1,sticky='NSEW')



lista1v.config(yscrollcommand=scoll.set)

lista1v.heading('#0',text='Codigo')
lista1v.heading('#1',text='Productos')
lista1v.heading('#2',text='Cantidad')
lista1v.heading('#3',text='Unidad')
lista1v.heading('#4',text='Departamento')
lista1v.heading('#5',text='Precio $')
lista1v.heading('#6',text='Precio Bs.S')
lista1v.heading('#7',text='Total $')
lista1v.heading('#8',text='Total Bs.S')


lista1v.column("#0",minwidth=70, width = 100)
lista1v.column("#1",minwidth=70, width = 240)
lista1v.column("#2",minwidth=70, width = 50)
lista1v.column("#3",minwidth=70, width = 30)
lista1v.column("#4",minwidth=70, width = 100)
lista1v.column("#5",minwidth=70, width = 100)
lista1v.column("#6",minwidth=70, width = 100)
lista1v.column("#7",minwidth=70, width = 100)
lista1v.column("#8",minwidth=70, width = 140)
Label(raiz,width=10).grid(row=0,column=1)






miframe=Frame(raiz)
miframe.configure(bg='#b8d3ff',width=240,height=199)
miframe.grid(column=1,row=0,sticky='NSE')

Label(miframe,text='Sub Total ($):',font='Helvetica 14',bg='#b8d3ff',fg='black').grid(row=3,column=0,pady=20,padx=5)
Label(miframe,text='I.V.A ($)',font='Helvetica 14',bg='#b8d3ff',fg='black').grid(row=5,column=0,padx=5)
Label(miframe,text='Total ($):',font='Helvetica 14',bg='#b8d3ff',fg='black').grid(row=7,column=0,padx=5,pady=20)


Total_B2=Text(miframe,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
Total_B2.grid(row=3,column=1,columnspan=2)

Total_D2=Text(miframe,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
Total_D2.grid(row=5,column=1,columnspan=2)

Total_D3=Text(miframe,relief='flat',state='disabled',height=1,width=25,font='Helvetica 14',bg='#b8d3ff')
Total_D3.grid(row=7,column=1,columnspan=2)

raiz2=Frame(raiz,bg='#b6bdff')
raiz2.grid(row=0,column=0,sticky='nwse')



agregar_a_suma(0.0,0.0,0.0,0.0,0.0,0.0)
Label(raiz2,text='C.I. Cliente',font='Helvetica 12',bg='#b6bdff',fg='black').grid(row=0,column=0,sticky='w',padx=22,pady=10)
client=Entry(raiz2,font='Helvetica 12',width=12,fg='black',bd=7,relief='sunken',textvariable=cedula_cliente_V)
client.grid(row=1,column=0,sticky='wns')
client.focus()
client.bind("<Return>", verificar_cliente_V)
cliente_v_v=Text(raiz2,font='Helvetica 18',state='disabled',bg='#b6bdff',relief='flat',height=1,width=25)
cliente_v_v.grid(row=0,column=0,sticky='w',padx=150,columnspan=2)

f1=Frame(raiz2,bg='#b6bdff')
f1.grid(row=3,column=0,sticky='nsw',columnspan=3)



x=Label(f1,text='Codigo / Producto',font='Helvetica 12',bg='#b6bdff')
x.grid(row=3,column=0,pady=10)

d=Label(f1,text='Cantidad',font='Helvetica 12',bg='#b6bdff')
d.grid(row=3,column=1,pady=10)


product=Entry(f1,font='Helvetica 12',bd=7,relief='sunken',textvariable=producto_ingresar_V)
product.grid(row=4,column=0,sticky='nsew')

product.bind("<Return>", ingresar_ID_en_venta)

canti=Entry(f1,font='Helvetica 12',bd=7,relief='sunken',width=7,textvariable=cantidad_ingresar_V)
canti.grid(row=4,column=1,sticky='nsew',padx=1)

canti.bind("<Return>", ingresar_ID_en_venta)


Label(f1,font='Helvetica 12',text='UND',bg='#b6bdff',fg='#b6bdff').grid(row=4,column=2,padx=1)


Button(raiz2,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:verificar_cliente_V('1')).grid(row=1,column=0,sticky='w',padx=130)
Button(f1,cursor='hand2',text='Aceptar',font='Helvetica 12',fg='black',bd=7,relief='raised',command=lambda:ingresar_ID_en_venta('1')).grid(row=4,column=3)

botones=Frame()
botones.configure(bg='#949494',width=1023,height=60)
botones.grid(row=2,column=0,sticky='ew',columnspan=2)

Button(botones,text='Borrar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=lambda:comprobacion_borrar_producto_en_V('1')).grid(row=0,column=0,padx=1,pady=5)
Button(botones,text='Editar',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=lambda:editar_producto_en_V('1')).grid(row=0,column=1,padx=1,pady=5)
Button(botones,text='Buscador',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=lambda:ver_productos_en_V('1')).grid(row=0,column=2,padx=1,pady=5)
Button(botones,text='Inventarios',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=lambda:INVENTARIOS('1')).grid(row=0,column=3,padx=1,pady=5)
Button(botones,text='Tasa',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=lambda:tasa_moneda('1')).grid(row=0,column=4,padx=1,pady=5)
Button(botones,text='Usuarios',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=registrar_usuario_V).grid(row=0,column=5,padx=1,pady=5)



Button(botones,text='Deudor',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=deudor).grid(row=0,column=7,sticky='e',padx=5)
Button(botones,text='Vender',cursor='hand2',font='Helvetica 12',fg='black',bd=5,relief='raised',width=8,height=1,command=lambda:vender('1')).grid(row=0,column=8,sticky='e',padx=5)


botones.columnconfigure(7,weight=1)
botones.rowconfigure(0,weight=1)

raiz.rowconfigure(0,weight=1)
raiz.columnconfigure(1,weight=1)

raiz.columnconfigure(0, weight=5)
raiz.rowconfigure(1, weight=5)

raiz2.rowconfigure(2,weight=3)
raiz2.columnconfigure(0,weight=3)

clock=Label(miframe,font='Consolas 14')
clock.grid(row=0,column=2,sticky='ne')
times()

Label(miframe,text=fecha,font='Consolas 14',bg='#b8d3ff',fg='black').grid(row=1,column=2,sticky='ne')

if __name__=='__main__':

	
	
	raiz.mainloop()