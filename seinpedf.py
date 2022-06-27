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

imagenPrueba = open("D:\\DevelopProjects\\informeSeinpe\\ejemplo\\naranjito.png", 'rb').read() 

imagenPosicion = fitz.IRect(0,0,50,50) #Posicion y tamaño de la imagen

archivo = fitz.open("D:\\DevelopProjects\\informeSeinpe\\pruebaADD.pdf") #PDF en el que se insertara la imagen
paginaInsercion = archivo[len(archivo) - 1] #Pagina en la que se insertara la imagen

paginaInsercion.insert_image(imagenPosicion, stream = imagenPrueba) #Inserción de imagen

archivo.save(archivoSalida)

    


