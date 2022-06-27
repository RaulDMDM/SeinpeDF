# from tika import parser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fitz
from pathlib import Path
from PyPDF2 import PdfFileReader

def inicio():
    Tk().withdraw()                 #|Cuadro de dialogo para especificar ruta del informe base
    pdf_original = askopenfilename()
    pdf_plantilla = Path(Path.cwd(), "ejemplo/marcaDeAgua.pdf")
    pdf_carga_img = Path(Path.cwd(),"pruebaAdd.pdf")

    num_referencia = capturaNumReferencia(pdf_original)
    list_imgs = [Path(Path.cwd(),"ejemplo/Fotos/20220131110845.jpg"),Path(Path.cwd(),"ejemplo/Fotos/20220131110852.jpg"),Path(Path.cwd(),"ejemplo/Fotos/20220131110858.jpg")]

    agregarPagina(pdf_original, pdf_plantilla, pdf_carga_img)
    generaPdfConImgs(pdf_carga_img, list_imgs)

def agregarPagina(pdf_ruta: Path, pdf_plantilla: Path, pdf_carga_img: Path): #Agrega una nueva pagina con el formato base para añadir fotos
    pdfOriginal = fitz.open(pdf_ruta)
    pdfNuevo = fitz.open(pdf_plantilla)
    
    pdfOriginal.insert_pdf(pdfNuevo)
    nuevaPagina = pdfOriginal.load_page(-1)
    nuevaPagina.set_rotation(0)
    if not nuevaPagina.is_wrapped:
        nuevaPagina.wrap_contents()
    pdfOriginal.save(pdf_carga_img) #Nombre archivo de salidaImagen a inserta

def capturaNumReferencia(pdf_original: Path):
    with open(pdf_original, 'rb') as f:
        pdf = PdfFileReader(f, strict = False)
        pagina = pdf.getPage(0)
        return pagina.extractText()[-10:]

#pdf = parser.from_file(rutaInforme) #Lectura del PDF de informe base

#text = pdf['content'] #Interpretacion del texto de informe base

#print(text)

# agregarPagina(pdf_ruta)

######PRUEBAS DE IMPORTACION Y ESCALADO DE IMAGENES###############

def generaPdfConImgs(pdf_carga_img, list_imgs):
    pdf_salida = Path(Path.cwd(),"pruebaImagenes.pdf") #Nombre archivo de salidaImagen a insertar
    posicionXmin = 50 #
    posicionYmin = 225
    posicionXmax = 275 
    posicionYmax = 400
    # imagenPrueba = open(Path(".\\ejemplo\\naranjito.png"), 'rb').read() 
    # posiciones_img = 
    # 50, 225, 275, 400 - 
    # 320, 225, 545, 400 - 
    # 50, 550, 275, 725 -
    # 320, 550, 545, 725
    fila = 0
    columna= 0
    for img in list_imgs:
        imagen_a_cargar = Path(img).read_bytes()
        posicion_img = fitz.IRect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen
        pdf_modificado = fitz.open(pdf_carga_img) #PDF en el que se insertara la imagen
        nueva_pagina_insertada = pdf_modificado.load_page(-1) #Pagina en la que se insertara la imagen
        columna += 1
        if columna == 2:
            columna = 0
            posicionXmin = 50
            posicionXmax = 275
            posicionYmin += 225
            posicionYmax += 325
        else:
            posicionXmin += 270
            posicionXmax += 270
            posicionYmin = 225
            posicionYmax = 400

        nueva_pagina_insertada.insert_image(posicion_img, stream = imagen_a_cargar, keep_proportion = False) #Inserción de imagen

    pdf_modificado.save(pdf_salida)

inicio()
    


