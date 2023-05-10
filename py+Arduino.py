from tkinter import*
import serial , time 

arduino=serial.Serial('COM4', 9600)

def cerrarInterfaz():
    arduino.close()
    raiz.destroy()

def adelanteM():
    arduino.write(b'A')
    time.sleep(1)

def atrasM():
    arduino.write(b'D')
    time.sleep(1)

def izquierdaM():
    arduino.write(b'B')
    time.sleep(1)

def derechaM():
    arduino.write(b'C')
    time.sleep(1)

def detenerM():
    arduino.write(b'E')
    time.sleep(1)

raiz =Tk()
raiz.geometry("500x200")
raiz.title("Arduino - Python")

titleFrame=Frame()
titleFrame.config(bg="gray",width="500",height="80")
titleFrame.place(x=0,y=0)
#titulo
lblTitulo=Label(titleFrame, text="MOVIMIENTOS DE ROBOFUT", bg="gray", fg="white",font=("Arial", 15))
lblTitulo.place(x=110 , y=20)

ButtonFrame=Frame()
ButtonFrame.config(bg="orange", width="500",height="120")
ButtonFrame.place(x=0,y=80)

#enceder led ADELANTE
btnEncender=Button(ButtonFrame, text="Adelante", command=adelanteM)
btnEncender.place(x=70,y=40)
#apagar led ATRAS
btnApagar=Button(ButtonFrame, text="Atras", command=atrasM)
btnApagar.place(x=160,y=40)
#apagar led IZQUIERDA
btnApagar=Button(ButtonFrame, text="Izquierda", command=izquierdaM)
btnApagar.place(x=270,y=40)
#apagar led DERECHA
btnApagar=Button(ButtonFrame, text="Derecha", command=derechaM)
btnApagar.place(x=350,y=40)
#detenerMotor
btnCerrar=Button(ButtonFrame, text="Detener", command=detenerM)
btnCerrar.place(x=350,y=90)
#cerrar interfaz
btnCerrar=Button(ButtonFrame, text="Cerrar", command=cerrarInterfaz)
btnCerrar.place(x=420,y=90)

raiz.mainloop()