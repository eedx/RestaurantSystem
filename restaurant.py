from tkinter import *
import random, datetime
from tkinter import filedialog, messagebox


# ---------------------------------------------------------------------------
# FUNCIONES Y VARIABLES
# ---------------------------------------------------------------------------

# Funcionalidad de la calculadora
operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# Funcionalidad de los botones de la calculadora
def click_boton(numero):
    global operador
    operador += numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# Funcionalidad botón borrar de la calculadora
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


# Funcionalidad botón resultado de la calculadora
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    #operador = '' 
    # Esto reinicia el visor cada vez que 
    # se obtiene un resultado


# Funcionalidad de los check buttons
def revisar_check():
    x = 0
    y = 0
    z = 0

    for c in cuadros_comida:
        if varibles_comida[x].get() == 1:
            cuadros_comida[x].config(state = NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state = DISABLED)
            texto_comida[x].set('0')
        x += 1

    for b in cuadros_bebida:
        if varibles_bebida[y].get() == 1:
            cuadros_bebida[y].config(state = NORMAL)
            if cuadros_bebida[y].get() == '0':
                cuadros_bebida[y].delete(0, END)
            cuadros_bebida[y].focus()
        else:
            cuadros_bebida[y].config(state = DISABLED)
            texto_bebida[y].set('0')
        y += 1

    for p in cuadros_postres:
        if varibles_postres[z].get() == 1:
            cuadros_postres[z].config(state = NORMAL)
            if cuadros_postres[z].get() == '0':
                cuadros_postres[z].delete(0, END)
            cuadros_postres[z].focus()
        else:
            cuadros_postres[z].config(state = DISABLED)
            texto_postres[z].set('0')
        z += 1


# Funcionalidad botón total
def total():
    subtotal_comida = 0
    subtotal_bebida = 0
    subtotal_postres = 0
    i_1 = 0
    i_2 = 0
    i_3 = 0

    for cantidad in texto_comida:
        subtotal_comida += (float(cantidad.get()) * precios_comida[i_1])
        i_1 += 1

    for cantidad in texto_bebida:
        subtotal_bebida += (float(cantidad.get()) * precios_bebida[i_2])
        i_2 += 1

    for cantidad in texto_postres:
        subtotal_postres += (float(cantidad.get()) * precios_postres[i_3])
        i_3 += 1

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postres
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebidas.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postres.set(f'$ {round(subtotal_postres, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


# Funcionalidad botón recibo
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.strftime("%d/%m/%y")} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 37 + '\n\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')

    x = 0
    y = 0
    z = 0

    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'$ {round(int(comida.get()) * precios_comida[x], 2)}\n')
        x += 1

    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[y]}\t\t{bebida.get()}\t'
                                     f'$ {round(int(bebida.get()) * precios_bebida[y], 2)}\n')
        y += 1

    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[z]}\t\t{postres.get()}\t'
                                     f'$ {round(int(postres.get()) * precios_postres[z], 2)}\n')
        z += 1

    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(END, f'Costo de la comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas:\t\t\t{var_costo_bebidas.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres:\t\t\t{var_costo_postres.get()}\n')

    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(END, f'Sub-total:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos:\t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t\t{var_total.get()}\n\n')

    texto_recibo.insert(END, f'*' * 37 + '\n')
    texto_recibo.insert(END, 'Gracias por comer en mi restaurante, vuelva pronto')


# Funcionalidad botón guardar
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')


# Funcionalidad botón resetear
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state = DISABLED)

    for var in varibles_comida:
        var.set(0)
    for var in varibles_bebida:
        var.set(0)
    for var in varibles_postres:
        var.set(0)

    var_costo_comida.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# ---------------------------------------------------------------------------
# PANTALLA GRÁFICA DE TKINTER
# ---------------------------------------------------------------------------

# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar/minimizar
aplicacion.resizable(0, 0)

# Título de la ventana
aplicacion.title('Restaurante - Sistema de facturación')

# Color de fondo de la ventana
aplicacion.config(bg = '#6be1e0')


# ---------------------------------------------------------------------------
# PANEL SUPERIOR
# ---------------------------------------------------------------------------

panel_superior = Frame(aplicacion, bd = 1, relief = FLAT)
panel_superior.pack(side = TOP)

# Etiqueta título
etiqueta_titulo = Label(panel_superior, 
                        text = 'Sistema de Facturación', 
                        fg = '#273434',
                        font = ('Oxygen', 54), 
                        bg = '#6be1e0', 
                        width = 25)
etiqueta_titulo.grid(row = 0, column = 0)


# ---------------------------------------------------------------------------
# PANEL IZQUIERDO Y COMPONENTES
# ---------------------------------------------------------------------------

panel_izquierdo = Frame(aplicacion, bd = 1, relief = FLAT)
panel_izquierdo.pack(side = LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, 
                     bd = 1, 
                     relief = FLAT, 
                     bg = '#273434', 
                     padx = 45,
                     pady = 10)
panel_costos.pack(side = BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, 
                           text = 'Comida', 
                           font = ('Oxygen', 19, 'bold'),
                           bd = 1,
                           relief = FLAT,
                           fg = '#273434',
                           pady = 37)
panel_comidas.pack(side = LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, 
                           text = 'Bebidas', 
                           font = ('Oxygen', 19, 'bold'),
                           bd = 1,
                           relief = FLAT,
                           fg = '#273434',
                           pady = 37)
panel_bebidas.pack(side = LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, 
                           text = 'Postres', 
                           font = ('Oxygen', 19, 'bold'),
                           bd = 1,
                           relief = FLAT,
                           fg = '#273434',
                           pady = 37)
panel_postres.pack(side = LEFT)


# ---------------------------------------------------------------------------
# PANEL DERECHO Y COMPONENTES
# ---------------------------------------------------------------------------

panel_derecha = Frame(aplicacion, bd = 1, relief = FLAT)
panel_derecha.pack(side = RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, 
                          bd = 1, 
                          relief = FLAT, 
                          bg = '#6be1e0')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, 
                     bd = 1, 
                     relief = FLAT, 
                     bg = '#6be1e0')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, 
                      bd = 1, 
                      relief = FLAT, 
                      bg = '#6be1e0')
panel_botones.pack()


# ---------------------------------------------------------------------------
# ITEMS Y LISTA DE PRODUCTOS
# ---------------------------------------------------------------------------

# Lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmón', 'Merluza', 'Kebab', 'Pizza 1', 'Pizza 2', 'Pizza 3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino 1', 'Vino 2', 'Cerveza 1', 'Cerveza 2']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Pastel 1', 'Pastel 2', 'Pastel 3']

# ---------------------------------------------------------------------------
# ITEMS DE COMIDA
# ---------------------------------------------------------------------------

# Generar items comida
varibles_comida = []
cuadros_comida = []
texto_comida = []

contador = 0
for comida in lista_comidas:

    # Crear check button
    varibles_comida.append('')
    varibles_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text = comida.title(), 
                         font = ('Oxygen', 16, 'bold'),
                         onvalue = 1,
                         offvalue = 0,
                         variable = varibles_comida[contador],
                         command = revisar_check)
    comida.grid(row = contador, column = 0, sticky = W)

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font = ('Oxygen', 17, 'bold'),
                                     bd = 1,
                                     width = 6,
                                     state = DISABLED,
                                     textvariable = texto_comida[contador])
    cuadros_comida[contador].grid(row = contador, column = 1)

    contador +=  1


# ---------------------------------------------------------------------------
# ITEMS DE BEBIDAS
# ---------------------------------------------------------------------------

# Generar items bebida
varibles_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    # Crear check button
    varibles_bebida.append('')
    varibles_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                         text = bebida.title(), 
                         font = ('Oxygen', 16, 'bold'),
                         onvalue = 1,
                         offvalue = 0,
                         variable = varibles_bebida[contador],
                         command = revisar_check)
    bebida.grid(row = contador, column = 0, sticky = W)

    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font = ('Oxygen', 17, 'bold'),
                                     bd = 1,
                                     width = 6,
                                     state = DISABLED,
                                     textvariable = texto_bebida[contador])
    cuadros_bebida[contador].grid(row = contador, column = 1)

    contador +=  1


# ---------------------------------------------------------------------------
# ITEMS DE POSTRES
# ---------------------------------------------------------------------------

# Generar items postres
varibles_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:

    # Crear check button
    varibles_postres.append('')
    varibles_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, 
                         text = postres.title(), 
                         font = ('Oxygen', 16, 'bold'),
                         onvalue = 1,
                         offvalue = 0,
                         variable = varibles_postres[contador],
                         command = revisar_check)
    postres.grid(row = contador, column = 0, sticky = W)

    # Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font = ('Oxygen', 17, 'bold'),
                                     bd = 1,
                                     width = 6,
                                     state = DISABLED,
                                     textvariable = texto_postres[contador])
    cuadros_postres[contador].grid(row = contador, column = 1)

    contador +=  1


# ---------------------------------------------------------------------------
# VARIABLES DE CUADROS DE TEXTO
# ---------------------------------------------------------------------------

var_costo_comida = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# ---------------------------------------------------------------------------
# ETIQUETAS DE COSTOS
# ---------------------------------------------------------------------------

# Comida
etiqueta_costo_comida = Label(panel_costos,
                              text = 'Costo Comida',
                              font = ('Oxygen', 12, 'bold'),
                              bg = '#273434',
                              fg = 'white')
etiqueta_costo_comida.grid(row = 0, column = 0)

# Bebida
etiqueta_costo_bebidas = Label(panel_costos,
                              text = 'Costo Bebidas',
                              font = ('Oxygen', 12, 'bold'),
                              bg = '#273434',
                              fg = 'white')
etiqueta_costo_bebidas.grid(row = 1, column = 0)

# Postres
etiqueta_costo_postres = Label(panel_costos,
                              text = 'Costo Postres',
                              font = ('Oxygen', 12, 'bold'),
                              bg = '#273434',
                              fg = 'white')
etiqueta_costo_postres.grid(row = 2, column = 0)

# Sub-total
etiqueta_subtotal = Label(panel_costos,
                              text = 'Sub-total',
                              font = ('Oxygen', 12, 'bold'),
                              bg = '#273434',
                              fg = 'white')
etiqueta_subtotal.grid(row = 0, column = 2)

# Impuestos
etiqueta_impuesto = Label(panel_costos,
                              text = 'Impuestos',
                              font = ('Oxygen', 12, 'bold'),
                              bg = '#273434',
                              fg = 'white')
etiqueta_impuesto.grid(row = 1, column = 2)

# Total
etiqueta_total = Label(panel_costos,
                              text = 'Total',
                              font = ('Oxygen', 12, 'bold'),
                              bg = '#273434',
                              fg = 'white')
etiqueta_total.grid(row = 2, column = 2)

# ---------------------------------------------------------------------------
# CUADROS DE ENTRADA DE TEXTO (COSTOS)
# ---------------------------------------------------------------------------

# Comida
texto_costo_comida = Entry(panel_costos,
                           font = ('Oxygen', 12, 'bold'),
                           bd = 1,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_costo_comida)
texto_costo_comida.grid(row = 0, column = 1, padx = 41)

# Bedidas
texto_costo_bebidas = Entry(panel_costos,
                           font = ('Oxygen', 12, 'bold'),
                           bd = 1,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_costo_bebidas)
texto_costo_bebidas.grid(row = 1, column = 1, padx = 41)

# Postres
texto_costo_postres = Entry(panel_costos,
                           font = ('Oxygen', 12, 'bold'),
                           bd = 1,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_costo_postres)
texto_costo_postres.grid(row = 2, column = 1, padx = 41)

# Sub-total
texto_subtotal = Entry(panel_costos,
                           font = ('Oxygen', 12, 'bold'),
                           bd = 1,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_subtotal)
texto_subtotal.grid(row = 0, column = 3, padx = 41)

# Impuestos
texto_impuesto = Entry(panel_costos,
                           font = ('Oxygen', 12, 'bold'),
                           bd = 1,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_impuesto)
texto_impuesto.grid(row = 1, column = 3, padx = 41)

# Total
texto_total = Entry(panel_costos,
                           font = ('Oxygen', 12, 'bold'),
                           bd = 1,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_total)
texto_total.grid(row = 2, column = 3, padx = 41)


# ---------------------------------------------------------------------------
# CONFIGURACIÓN DE BOTONES
# ---------------------------------------------------------------------------

botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text = boton.title(),
                   font = ('Oxygen', 14, 'bold'),
                   fg = 'white',
                   bg = '#273434',
                   bd = 1,
                   width = 7)
    botones_creados.append(boton)
    
    boton.grid(row = 0, column = columnas)
    columnas += 1

botones_creados[0].config(command = total)
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)

# ---------------------------------------------------------------------------
# ÁREA DE RECIBO Y CALCULADORA
# ---------------------------------------------------------------------------

texto_recibo = Text(panel_recibo,
                    font = ('Oxygen', 12, 'bold'),
                    bd = 1,
                    width = 34,
                    height = 12)
texto_recibo.grid(row = 0, column = 0)

visor_calculadora = Entry(panel_calculadora,
                          font = ('Oxygen', 16, 'bold'),
                          width = 26,
                          bd = 1)
visor_calculadora.grid(row = 0, column = 0, columnspan = 4)

botones_guardados = []

botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', '*',
                       '=', 'C', '0', '/']
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text = boton.title(),
                   font = ('Oxygen', 16, 'bold'),
                   fg = 'white',
                   bg = '#273434',
                   bd = 1,
                   width = 6)
    botones_guardados.append(boton)

    boton.grid(row = fila, column = columna)

    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0


# ---------------------------------------------------------------------------
# CONFIGURACIÓN DE BOTONES NUMÉRICOS
# ---------------------------------------------------------------------------

botones_guardados[0].config(command = lambda: click_boton('7'))
botones_guardados[1].config(command = lambda: click_boton('8'))
botones_guardados[2].config(command = lambda: click_boton('9'))
botones_guardados[3].config(command = lambda: click_boton('+'))
botones_guardados[4].config(command = lambda: click_boton('4'))
botones_guardados[5].config(command = lambda: click_boton('5'))
botones_guardados[6].config(command = lambda: click_boton('6'))
botones_guardados[7].config(command = lambda: click_boton('-'))
botones_guardados[8].config(command = lambda: click_boton('1'))
botones_guardados[9].config(command = lambda: click_boton('2'))
botones_guardados[10].config(command = lambda: click_boton('3'))
botones_guardados[11].config(command = lambda: click_boton('*'))
botones_guardados[12].config(command = obtener_resultado)
botones_guardados[13].config(command = borrar)
botones_guardados[14].config(command = lambda: click_boton('0'))
botones_guardados[15].config(command = lambda: click_boton('/'))


# ---------------------------------------------------------------------------
# DECLARACIÓN DEL BUCLE PRINCIPAL
# ---------------------------------------------------------------------------

# Evitar que la pantalla se cierre
aplicacion.mainloop()