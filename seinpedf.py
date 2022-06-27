from tika import parser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fitz


def agregarPagina(): #Agrega una nueva pagina con el formato base para añadir fotos
    pdfOriginal = fitz.open(rutaInforme)
    pdfNuevo = fitz.open("D:\\DevelopProjects\\informeSeinpe\\ejemplo\\marcaDeAgua.pdf")
    
    pdfOriginal.insert_pdf(pdfNuevo)
    nuevaPagina = pdfOriginal[len(pdfOriginal) - 1]
    nuevaPagina.set_rotation(0)
    if not nuevaPagina.is_wrapped:
        nuevaPagina.wrap_contents()
    pdfOriginal.save("pruebaAdd.pdf")


Tk().withdraw()                 #|Cuadro de dialogo para especificar ruta del informe base
rutaInforme = askopenfilename() #|

#pdf = parser.from_file(rutaInforme) #Lectura del PDF de informe base

#text = pdf['content'] #Interpretacion del texto de informe base

#print(text)

agregarPagina()

######PRUEBAS DE IMPORTACION Y ESCALADO DE IMAGENES###############

archivoSalida = "pruebaImagenes.pdf" #Nombre archivo de salidaImagen a insertar
archivo = fitz.open("D:\\DevelopProjects\\informeSeinpe\\pruebaADD.pdf") #PDF en el que se insertara la imagen
paginaInsercion = archivo[len(archivo) - 1] #Pagina en la que se insertara la imagen

imagenPrueba1 = open("D:\\DevelopProjects\\informeSeinpe\\ejemplo\\fotos\\20220131110852.jpg", 'rb').read()
imagenPosicion1 = fitz.Rect(50,225,275,400)#posicion y tamaño de la imagen
paginaInsercion.insert_image(imagenPosicion1, stream = imagenPrueba1, keep_proportion = False)#Inserción de imagen 1


imagenPrueba2 = open("D:\\DevelopProjects\\informeSeinpe\\ejemplo\\fotos\\20220131110907.jpg", 'rb').read()
imagenPosicion2 = fitz.Rect(320,225,545,400)#posicion y tamaño de la imagen
paginaInsercion.insert_image(imagenPosicion2, stream = imagenPrueba2, keep_proportion = False)#Inserción de imagen 2


imagenPrueba3 = open("D:\\DevelopProjects\\informeSeinpe\\ejemplo\\fotos\\20220131111139.jpg", 'rb').read()
imagenPosicion3 = fitz.Rect(50,550,275,725)#posicion y tamaño de la imagen
paginaInsercion.insert_image(imagenPosicion3, stream = imagenPrueba3, keep_proportion = False)#Inserción de imagen 2


imagenPrueba4 = open("D:\\DevelopProjects\\informeSeinpe\\ejemplo\\fotos\\20220131111059.jpg", 'rb').read()
imagenPosicion4 = fitz.Rect(320,550,545,725)#posicion y tamaño de la imagen
paginaInsercion.insert_image(imagenPosicion4, stream = imagenPrueba4, keep_proportion = False)#Inserción de imagen 2

archivo.save(archivoSalida)

    


