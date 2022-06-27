# from tika import parser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fitz
from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_img_insertada = Path(Path.cwd(),"seinpeDF/pruebaAdd.pdf")
pdf_modificado = Path(Path.cwd(), 'seinpeDF/ejemplo/marcaDeAgua.pdf')

def agregarPagina(): #Agrega una nueva pagina con el formato base para añadir fotos
    pdfOriginal = fitz.open(rutaInforme)
    pdfNuevo = fitz.open(pdf_modificado)
    
    pdfOriginal.insert_pdf(pdfNuevo)
    nuevaPagina = pdfOriginal[len(pdfOriginal) - 1]
    nuevaPagina.set_rotation(0)
    if not nuevaPagina.is_wrapped:
        nuevaPagina.wrap_contents()
    # pdfOriginal.save("pruebaAdd.pdf")
    pdfOriginal.save(pdf_img_insertada) #Nombre archivo de salidaImagen a inserta


def capturaNumReferencia(pdf_original: Path):
    with open(pdf_original, 'rb') as f:
        pdf = PdfFileReader(f)
        pagina = pdf.getPage(0)
        return pagina.extractText()[-10:]

pdf_original = askopenfilename()

Tk().withdraw()                 #|Cuadro de dialogo para especificar ruta del informe base
rutaInforme = askopenfilename() #|
numReferencia = capturaNumReferencia()
#pdf = parser.from_file(rutaInforme) #Lectura del PDF de informe base

#text = pdf['content'] #Interpretacion del texto de informe base

#print(text)

agregarPagina()

######PRUEBAS DE IMPORTACION Y ESCALADO DE IMAGENES###############

archivoSalida = Path(Path.cwd(),"seinpeDF/pruebaImagenes.pdf") #Nombre archivo de salidaImagen a insertar

# imagenPrueba = open(Path(".\\ejemplo\\naranjito.png"), 'rb').read() 
imagenPrueba = Path(Path.cwd(), "seinpeDF/ejemplo/naranjito.png").read_bytes()

imagenPosicion = fitz.IRect(0,0,50,50) #Posicion y tamaño de la imagen

archivo = fitz.open(pdf_img_insertada) #PDF en el que se insertara la imagen
paginaInsercion = archivo[len(archivo) - 1] #Pagina en la que se insertara la imagen

paginaInsercion.insert_image(imagenPosicion, stream = imagenPrueba) #Inserción de imagen

archivo.save(archivoSalida)

    


