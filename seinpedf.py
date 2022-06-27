# from tika import parser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from fitz import fitz, Rect
from pathlib import Path
from PyPDF2 import PdfFileReader

def inicio():
    Tk().withdraw() #|Cuadro de dialogo para especificar ruta del informe base
    pdf_original = askopenfilename()
    pdf_plantilla = Path(Path.cwd(), "ejemplo/marcaDeAgua.pdf")
    pdf_aux = Path(Path.cwd(),"pdfAux.pdf")

    num_referencia = capturaNumReferencia(pdf_original)
    list_imgs = [
    Path(Path.cwd(),"ejemplo/Fotos/20220131110845.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110845.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110852.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110858.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110905.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110907.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110918.jpg")
    ]

    subdivision = 4
    listas_imgs = [list_imgs[i:i + subdivision] for i in range(0, len(list_imgs), subdivision)]

    agregarPagina(pdf_original, pdf_plantilla, pdf_aux)
    if Path(Path.cwd(),"pruebaImagenes.pdf").exists():
        archivo = Path(Path.cwd(),"pruebaImagenes.pdf")
    else:
        archivo = pdf_aux
    
    for sublista_img in listas_imgs:
        generaPdfConImgs(archivo, sublista_img)
    
    pdf_aux.unlink()

def agregarPagina(pdf_ruta: Path, pdf_plantilla: Path, pdf_aux: Path): #Agrega una nueva pagina con el formato base para añadir fotos
    pdfOriginal = fitz.open(pdf_ruta)
    pdfNuevo = fitz.open(pdf_plantilla)
    
    pdfOriginal.insert_pdf(pdfNuevo)
    nuevaPagina = pdfOriginal.load_page(-1)
    nuevaPagina.set_rotation(0)
    if not nuevaPagina.is_wrapped:
        nuevaPagina.wrap_contents()
    pdfOriginal.save(pdf_aux) #Nombre archivo de salidaImagen a inserta

def capturaNumReferencia(pdf_original: Path):
    with open(pdf_original, 'rb') as f:
        pdf = PdfFileReader(f, strict = False)
        pagina = pdf.getPage(0)
        return pagina.extractText()[-10:]

######PRUEBAS DE IMPORTACION Y ESCALADO DE IMAGENES###############

def generaPdfConImgs(archivo, list_imgs):
    posicionXmin = 50
    posicionYmin = 225
    posicionXmax = 275 
    posicionYmax = 400
    pos = 0
    pdf_modificado = fitz.open(archivo) #PDF en el que se insertara la imagen

    for img in list_imgs:
        imagen_a_cargar = Path(img).read_bytes()
        posicion_img = fitz.Rect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen
        pdf_ultima_pagina = pdf_modificado.load_page(-1) #Pagina en la que se insertara la imagen

        if pos == 0:
            posicionXmin = 50
            posicionYmin = 225
            posicionXmax = 275 
            posicionYmax = 400
        elif pos == 1:
            posicionXmin = 320
            posicionYmin = 225
            posicionXmax = 545 
            posicionYmax = 400
        elif pos == 2:
            posicionXmin = 50
            posicionYmin = 550
            posicionXmax = 275 
            posicionYmax = 725
        elif pos == 3:
            pos = 0
            posicionXmin = 320
            posicionYmin = 550
            posicionXmax = 545 
            posicionYmax = 725
        pos += 1

        pdf_ultima_pagina.insert_image(posicion_img, stream = imagen_a_cargar, keep_proportion = False) #Inserción de imagen
    
    if Path(Path.cwd(),"pruebaImagenes.pdf").exists():
        pdf_modificado.saveIncr()
    else:
        pdf_modificado.save(Path(Path.cwd(),"pruebaImagenes.pdf"))

inicio()
    


