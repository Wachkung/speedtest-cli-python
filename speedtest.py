#!/usr/bin/python3
import os
def test():

        #ISP Contracted speed or minimun optimun speed
        # velocidad contratada al ISP o velocidad minima optima para la conexion
        # yo tengo contratado 10 megas pero el contrato del ISP dice que la velocidad puede variar un 30% asi que pongo 7Mbit/s que seria lo minimo aceptable
        speed = 7 #Mbit/s

        # run speedtest-cli
        # corremos speedtest-cli

        print ('Iniciando el test')
        a = os.popen("speedtest-cli --simple").read()
        #split the 3 line result (ping,down,up)
        # Dividimos el resultado del speedtest en 3 lineas
        lines = a.split('\n')
        print (a)
        #extract the values for ping down and up values
        # extraemos los valores del ping download y upload
        p = lines[0][6:11]
        d = lines[1][10:14]
        u = lines[2][8:12]

        #if speedtest could not connect
        #si speedtest no conecta
        if "Cannot" in a:
            print("El internet esta Caido.")
        elif eval(d) < speed:
            print("El Internet esta Lento deberia ser de 10mbps y actualmente esta en " + str(eval(d)) + "Mbit/s")
        else:
            print("La conexion actualmente funciona con normalidad a una velocidad de " + str(eval(d)) + "Mbit/s")
        return

if __name__ == '__main__':
        test()
        print ('Test Completado')
