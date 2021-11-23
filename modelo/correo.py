#!/usr/bin/env python3
import smtplib
"Sus dias de prestamo han pasado. Tiene hasta el dia de hoy para acercarse a devolver"

class Correo:
    """Clase que representa a los correos que seran enviados"""
    def __init__(self, emisor='bibliotecaa.2014@gmail.com', contraseña='biblioteca1'):
        self.__emisor = emisor
        self.__contraseña = contraseña


    def enviar(self, mensaje, destinatario):
        try: 
           smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
           smtpserver.ehlo()
           smtpserver.starttls()
           smtserver.ehlo
           smtpserver.login(self.__emisor, self.__contraseña)
           cabecera = 'To:' + destinatario + '\n' + 'From: ' + self.__emisor + '\n' + 'Subject :' + asunto + '\n'
           mensaje = cabecera + mensaje
           smtpserver.sendmail(self.__emisor, destinatario, mensaje)
           smtpserver.close()
        except:
           print("No se pudo conectar")
       

    

     
