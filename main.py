import time
from datetime import datetime

#Ruta en la que el servicio va a escribir infinitamente.
path = 'C:/Users/danie/Desktop/testservicio/archivo.txt'
condicion = True





if __name__ == '__main__':
    while condicion:
        try:
            fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            with open(path, 'a', encoding='utf8') as archivo:
                archivo.write('===========================================================================\n')
                time.sleep(1)
                archivo.write(f'{ fecha } Hola este es el servicio de prueba para el servicio Count and Move\n')
                time.sleep(1)
                archivo.write('===========================================================================\n')
                time.sleep(5)
                archivo.write(f'{ fecha } Se estara escribiendo infinitamente texto a menos que de un error...\n')
                time.sleep(1)
                archivo.write('===========================================================================\n')
        except Exception as e:
            with open(path, 'a', encoding='utf8') as archivo:
                # print('Ha ocurrido un error al contar los archivos')
                archivo.write(f'Ha ocurrido un error al contar los archivos, error: {e}\n')
                archivo.close()
                condicion = False