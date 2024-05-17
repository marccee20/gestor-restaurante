from tkinter import *
import random
import datetime  # para la fecha y hora de los recibos
from tkinter import filedialog, messagebox

operador = ""

precios_comida = [5500, 6000, 5000, 3500, 2500, 3000, 4000, 2000]
precios_bebida = [2000, 1300, 800, 900, 3500, 2500, 1000, 2400]
precios_postres = [1200, 1000, 1300, 1500, 900, 1200, 1450, 1700]


def click_boton(numero, visor_calculadora):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)

    operador = ""


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variable_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1

    x = 0
    for c in cuadros_bebidas:
        if variable_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == "0":
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set("0")
        x += 1

    x = 0
    for c in cuadros_postres:
        if variable_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (
            float(cantidad.get()) * precios_comida[p]
        )
        p += 1

    sub_total_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas = sub_total_bebidas + (
            float(cantidad.get()) * precios_bebida[p]
        )
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (
            float(cantidad.get()) * precios_postres[p]
        )
        p += 1

    sub_total = sub_total_comida + sub_total_bebidas + sub_total_postres
    impuesto = sub_total * 0.07
    total = sub_total + impuesto

    var_costo_comida.set(f"${round(sub_total_comida,2)}")
    var_costo_bebidas.set(f"${round(sub_total_bebidas,2)}")
    var_costo_postres.set(f"${round(sub_total_postres,2)}")
    var_subtotal.set(f"${round(sub_total,2)}")
    var_impuesto.set(f"${round(impuesto,2)}")
    var_total.set(f"${round(total,2)}")


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N#-{random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year}-{fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 47 + "\n")
    texto_recibo.insert(END, "Items\t\tcant.\tCosto items\n")
    texto_recibo.insert(END, f"-" * 54 + "\n")

    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_comidas[x]}\t\t{comida.get()}\t"
                f"${int(comida.get()) * precios_comida[x]}\n",
            )
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_bebidas[x]}\t\t{bebida.get()}\t"
                f"${int(bebida.get()) * precios_bebida[x]}\n",
            )
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_postres[x]}\t\t{postres.get()}\t"
                f"${int(postres.get()) * precios_postres[x]}\n",
            )
        x += 1

    texto_recibo.insert(END, f"-" * 54 + "\n")

    texto_recibo.insert(END, f"costo de la comida:\t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"costo de la bebida:\t\t\t{var_costo_bebidas.get()}\n")
    texto_recibo.insert(END, f"costo del postre:\t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(END, f"-" * 54 + "\n")

    texto_recibo.insert(END, f"Sub-total:\t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos:\t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total:\t\t\t{var_total.get()}\n")

    texto_recibo.insert(END, f"-" * 54 + "\n")
    texto_recibo.insert(END, "lo esperamos pronto")


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("informacion", "su recibo ha sido guardado")


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebidas:
        texto.set("0")
    for texto in texto_postres:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebidas:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costo_comida.set("")
    var_costo_bebidas.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")


# iniciar tkinter
aplicacion = Tk()

# tamaño
aplicacion.geometry("1420x940")
# titulo
aplicacion.title("MI restaurante")

# color de fondo de la ventana
aplicacion.config(bg="RoyalBlue1")

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
etiqueta_titulo = Label(
    panel_superior,
    text="sistema de facturacion",
    fg="black",
    font=("Dosis", 58),
    bg="LightBlue3",
    width=27,
)
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)


panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4")
panel_costos.pack(side=BOTTOM, fill="both", expand=True)


# panel comidas
panel_comidas = LabelFrame(
    panel_izquierdo,
    text="comida",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)

panel_comidas.pack(side=LEFT)
# panel bebidas
panel_bebidas = LabelFrame(
    panel_izquierdo,
    text="bebidas",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)

panel_bebidas.pack(side=LEFT)
# panel postres
panel_postres = LabelFrame(
    panel_izquierdo,
    text="postres",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)

panel_postres.pack(side=LEFT)
# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel recibo
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="azure4")
panel_calculadora.pack()
# panel calculadora
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="azure4")
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="azure4")
panel_botones.pack()

# listas de producto
lista_comidas = [
    "pollo",
    "cordero",
    "empanadas",
    "pizza",
    "sanguches",
    "pastas",
    "milanesa",
    "tartas",
]
lista_bebidas = [
    "coca",
    "manaos",
    "agua",
    "jugo",
    "vino",
    "cerveza",
    "soda",
    "cerveza2",
]
lista_postres = [
    "helado",
    "fruta",
    "flan",
    "torta",
    "brownies",
    "mouse",
    "ensalada de fruta",
    "gelatina",
]
# comida
variable_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variable_comida.append("")
    variable_comida[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variable_comida[contador],
        command=revisar_check,
    )
    comida.grid(row=contador, column=0, sticky=W)
    # crear cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_comida[contador],
    )
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1

# bebidas
cuadros_postres = []
texto_postres = []
variable_postres = []
contador = 0
for postres in lista_postres:
    variable_postres.append("")
    variable_postres[contador] = IntVar()
    postres = Checkbutton(
        panel_postres,
        text=postres.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variable_postres[contador],
        command=revisar_check,
    )
    postres.grid(row=contador, column=0, sticky=W)
    # crearcuadros
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[contador] = StringVar()
    texto_postres[contador].set("0")
    cuadros_postres[contador] = Entry(
        panel_postres,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_postres[contador],
    )
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1

# bebidas
variable_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebidas in lista_bebidas:
    variable_bebidas.append("")
    variable_bebidas[contador] = IntVar()
    bebidas = Checkbutton(
        panel_bebidas,
        text=bebidas.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variable_bebidas[contador],
        command=revisar_check,
    )
    bebidas.grid(row=contador, column=0, sticky=W)

    # crearcuadros
    cuadros_bebidas.append("")
    texto_bebidas.append("")
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set("0")
    cuadros_bebidas[contador] = Entry(
        panel_bebidas,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=texto_bebidas[contador],
    )
    cuadros_bebidas[contador].grid(row=contador, column=1)
    contador += 1

    # variables
    var_costo_comida = StringVar()
    var_costo_bebidas = StringVar()
    var_costo_postres = StringVar()
    var_subtotal = StringVar()
    var_impuesto = StringVar()
    var_total = StringVar()

    # etiquetas de costo
    etiqueta_costo_comida = Label(
        panel_costos,
        text="costo comida",
        font=("Dosis", 12, "bold"),
        bg="azure4",
        fg="white",
    )
    etiqueta_costo_comida.grid(row=0, column=0)
    # cuadr de entrada
    texto_costo_comida = Entry(
        panel_costos,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=var_costo_comida,
    )
    texto_costo_comida.grid(row=0, column=1, padx=41)

    # etiquetas de costo bebida
    etiqueta_costo_bebidas = Label(
        panel_costos,
        text="costo bebidas",
        font=("Dosis", 12, "bold"),
        bg="azure4",
        fg="white",
    )
    etiqueta_costo_bebidas.grid(row=1, column=0)
    # cuadr de entrada
    texto_costo_bebidas = Entry(
        panel_costos,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=var_costo_bebidas,
    )
    texto_costo_bebidas.grid(row=1, column=1, padx=41)

    # etiquetas de costo postre
    etiqueta_costo_postres = Label(
        panel_costos,
        text="costo postres",
        font=("Dosis", 12, "bold"),
        bg="azure4",
        fg="white",
    )
    etiqueta_costo_postres.grid(row=2, column=0)
    # cuadr de entrada
    texto_costo_postres = Entry(
        panel_costos,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=var_costo_postres,
    )
    texto_costo_postres.grid(row=2, column=1, padx=41)

    # etiquetas de subtotal
    etiqueta_subtotal = Label(
        panel_costos,
        text="subtotal",
        font=("Dosis", 12, "bold"),
        bg="azure4",
        fg="white",
    )
    etiqueta_subtotal.grid(row=0, column=2)
    # cuadr de entrada
    texto_subtotal = Entry(
        panel_costos,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=var_subtotal,
    )
    texto_subtotal.grid(row=0, column=3, padx=41)

    # etiquetas de impuesto
    etiqueta_impuesto = Label(
        panel_costos,
        text="impuesto",
        font=("Dosis", 12, "bold"),
        bg="azure4",
        fg="white",
    )
    etiqueta_impuesto.grid(row=1, column=2)
    # cuadr de entrada
    texto_impuesto = Entry(
        panel_costos,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=var_impuesto,
    )
    texto_impuesto.grid(row=1, column=3, padx=41)

    # etiquetas de total
    etiqueta_total = Label(
        panel_costos,
        text="total",
        font=("Dosis", 12, "bold"),
        bg="azure4",
        fg="white",
    )
    etiqueta_total.grid(row=2, column=2)
    # cuadr de entrada
    texto_total = Entry(
        panel_costos,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=var_total,
    )
    texto_total.grid(row=2, column=3)

    # botones
    botones = ["total", "recibo", "guardar", "resetear"]
    botones_creados = []

    columnas = 0
    for boton in botones:
        boton = Button(
            panel_botones,
            text=boton.title(),
            font=("Doisis", 10, "bold"),
            fg="white",
            bg="black",
            bd=1,
            width=10,
        )

        botones_creados.append(boton)

        boton.grid(row=0, column=columnas)
        columnas += 1

    botones_creados[0].config(command=total)
    botones_creados[1].config(command=recibo)
    botones_creados[2].config(command=guardar)
    botones_creados[3].config(command=resetear)
    # area recibo
    texto_recibo = Text(
        panel_recibo, font=("dosis", 12, "bold"), bd=1, width=45, height=12
    )

    texto_recibo.grid(row=0, column=0)

    # calculadora
    visor_calculadora = Entry(
        panel_calculadora,
        font=("Dosis", 16, "bold"),
        width=30,
        bd=1,
    )
    visor_calculadora.grid(row=0, column=0, columnspan=4)
    botones_calculadora = [
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "-",
        "1",
        "2",
        "3",
        "x",
        "R",
        "B",
        "O",
        "/",
    ]

    botones_guardados = []
    fila = 1
    columna = 0
    for boton in botones_calculadora:
        boton = Button(
            panel_calculadora,
            text=boton.title(),
            font=("Dosis", 16, "bold"),
            fg="white",
            bg="black",
            bd=1,
            width=5,
        )
        botones_guardados.append(boton)

        boton.grid(
            row=fila,
            column=columna,
        )

        if columna == 3:
            fila += 1

        columna += 1

        if columna == 4:
            columna = 0

    botones_guardados[0].config(command=lambda: click_boton("7", visor_calculadora))
    botones_guardados[1].config(command=lambda: click_boton("8", visor_calculadora))
    botones_guardados[2].config(command=lambda: click_boton("9", visor_calculadora))
    botones_guardados[3].config(command=lambda: click_boton("+", visor_calculadora))
    botones_guardados[4].config(command=lambda: click_boton("4", visor_calculadora))
    botones_guardados[5].config(command=lambda: click_boton("5", visor_calculadora))
    botones_guardados[6].config(command=lambda: click_boton("6", visor_calculadora))
    botones_guardados[7].config(command=lambda: click_boton("-", visor_calculadora))
    botones_guardados[8].config(command=lambda: click_boton("1", visor_calculadora))
    botones_guardados[9].config(command=lambda: click_boton("2", visor_calculadora))
    botones_guardados[10].config(command=lambda: click_boton("3", visor_calculadora))
    botones_guardados[11].config(command=lambda: click_boton("*", visor_calculadora))
    botones_guardados[12].config(command=lambda: obtener_resultado())
    botones_guardados[13].config(command=borrar)
    botones_guardados[14].config(command=lambda: click_boton("0", visor_calculadora))
    botones_guardados[15].config(command=lambda: click_boton("/", visor_calculadora))

    # posicion

    etiqueta_titulo.grid(row=1, column=1)


# evitar que se cierre la ventana
aplicacion.mainloop()
