import serial
import tkinter as tk

def encenderTodos():
    try:
        print("Encender todos")
        s.write("a".encode())
    except serial.SerialException as e:
        print("Error al intentar encender: ", e)

def apagarTodos():
    try:
        print("Apagar todos")
        s.write("b".encode())
    except serial.SerialException as e:
        print("Error al intentar apagar: ", e)

def encenderAzul():
    try:
        print("Encender azul")
        s.write("c".encode())
    except serial.SerialException as e:
        print("Error al intentar encender: ", e)

def apagarAzul():
    try:
        print("Apagar azul")
        s.write("d".encode())
    except serial.SerialException as e:
        print("Error al intentar apagar: ", e)

def encenderVerde():
    try:
        print("Encender verde")
        s.write("f".encode())
    except serial.SerialException as e:
        print("Error al intentar encender: ", e)

def apagarVerde():
    try:
        print("Apagar verde")
        s.write("g".encode())
    except serial.SerialException as e:
        print("Error al intentar apagar: ", e)

def encenderRojo():
    try:
        print("Encender rojo")
        s.write("h".encode())
    except serial.SerialException as e:
        print("Error al intentar encender: ", e)

def apagarRojo():
    try:
        print("Apagar rojo")
        s.write("i".encode())
    except serial.SerialException as e:
        print("Error al intentar apagar: ", e)

try:
    s = serial.Serial('COM6')
    sc = tk.Tk()
    sc.config(width = 300, height = 200)
    sc.title("Control de Led")

    bT1 = tk.Button(text = "Encender", width = 10, command = encenderTodos)
    bT1.place(x = 200, y = 10)
    bT2 = tk.Button(text = "Apagar", width = 10, command = apagarTodos)
    bT2.place(x = 200, y = 50)

    bR1 = tk.Button(text = "Red on", width = 10, command = encenderRojo)
    bR1.place(x = 10, y = 10)
    bR2 = tk.Button(text = "Red off", width = 10, command = apagarRojo)
    bR2.place(x = 10, y = 50)

    bV1 = tk.Button(text = "Green on", width = 10, command = encenderVerde)
    bV1.place(x = 10, y = 100)
    bV2 = tk.Button(text = "Green off", width = 10, command = apagarVerde)
    bV2.place(x = 10, y = 140)

    bA1 = tk.Button(text = "Blue on", width = 10, command = encenderAzul)
    bA1.place(x = 200, y = 100)
    bA2 = tk.Button(text = "Blue off", width = 10, command = apagarAzul)
    bA2.place(x = 200, y = 140)

    sc.mainloop()
finally:
    s.close()