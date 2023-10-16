import tkinter as tk
class Gas:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
    def celsius_fahrenheit(self):
        return (self.fahrenheit - 32) * 5/9

    def fahrenheit_celsius(self):
        return self.fahrenheit * 9/5 + 32

def convertir_a_fahrenheit():
    valor = float(entry.get())
    mi_gas = Gas(valor)
    resultado.set(f'Convertir a Fahrenheit: {mi_gas.fahrenheit_celsius():.1f} grados Fahrenheit')

def convertir_a_celsius():
    valor = float(entry.get())
    mi_gas = Gas(valor)
    resultado.set(f'Convertir a Celsius: {mi_gas.celsius_fahrenheit():.1f} grados Celsius')

def exportar():
    with open('resultados.txt', 'w') as archivo:
        archivo.write(resultado.get())
    print('Resultado exportado a resultados.txt')

ventana = tk.Tk()
ventana.title('Convertir de grados 15%')
ventana.geometry('600x400')

label = tk.Label(ventana, text='Ingrese el valor:')
label.grid(row=0, column=0, columnspan=3)

entry = tk.Entry(ventana)
entry.grid(row=1, column=0, columnspan=3)

boton_fahrenheit = tk.Button(ventana, text='Convertir a Fahrenheit', command=convertir_a_fahrenheit)
boton_fahrenheit.grid(row=2, column=0, padx=10, pady=10)

boton_celsius = tk.Button(ventana, text='Convertir a Celsius', command=convertir_a_celsius)
boton_celsius.grid(row=2, column=1, padx=10, pady=10)

boton_exportar = tk.Button(ventana, text='Exportar ', command=exportar)
boton_exportar.grid(row=2, column=2, padx=10, pady=10)

resultado = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado)
resultado_label.grid(row=3, column=0, columnspan=3)

ventana.mainloop()

