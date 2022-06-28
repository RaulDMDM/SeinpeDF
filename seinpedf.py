# from tika import parser
import builtins
from fileinput import close
from importlib.resources import path
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import fitz
from pathlib import Path
from PyPDF2 import PdfFileReader

def inicio():
    Tk().withdraw()                 #|Cuadro de dialogo para especificar ruta del informe base
    pdf_original = askopenfilename()
    pdf_plantilla = Path(Path.cwd(),"ejemplo/marcaDeAgua.pdf")
    pdf_carga_img = Path(Path.cwd(),"pruebaAdd.pdf")
    

    num_referencia = capturaNumReferencia(pdf_original)
    list_imgs = [Path(Path.cwd(),"ejemplo/Fotos/20220131110845.jpg"),
                 Path(Path.cwd(),"ejemplo/Fotos/20220131110852.jpg"),
                 Path(Path.cwd(),"ejemplo/Fotos/20220131110905.jpg"),
                 Path(Path.cwd(),"ejemplo/Fotos/20220131110907.jpg"),
                 Path(Path.cwd(),"ejemplo/Fotos/20220131110946.jpg"),
                 Path(Path.cwd(),"ejemplo/Fotos/20220131111039.jpg"),
                 Path(Path.cwd(),"ejemplo/Fotos/20220131110858.jpg")]

    agregarPagina(pdf_original, pdf_plantilla, pdf_carga_img)
    generaPdfConImgs(pdf_carga_img, list_imgs)

def agregarPagina(pdf_ruta: Path, pdf_plantilla: Path, pdf_carga_img: Path): #Agrega una nueva pagina con el formato base para añadir fotos
    pdfOriginal = fitz.open(pdf_ruta)
    pdfNuevo = fitz.open(pdf_plantilla)
    pdfDestino = fitz.open(pdf_carga_img)
    
    pdfOriginal.insert_pdf(pdfNuevo)
    nuevaPagina = pdfOriginal.load_page(-1)
    nuevaPagina.set_rotation(0)
    if not nuevaPagina.is_wrapped:
        nuevaPagina.wrap_contents()
    pdfOriginal.save(pdf_carga_img)
    

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

def generaPdfConImgs(pdf_carga_img, list_imgs): #nombre archivo de salidaImagen a insertar
    pdf_plantilla = Path(Path.cwd(),"ejemplo/marcaDeAgua.pdf")
    pdf_aniadir = Path(Path.cwd(),"pruebaAdd.pdf")
    pdf_modificado = fitz.open(pdf_carga_img) #PDF en el que se insertara la imagen
    nueva_pagina_insertada = pdf_modificado.load_page(-1) #Pagina en la que se insertara la imagen
    # imagenPrueba = open(Path(".\\ejemplo\\naranjito.png"), 'rb').read() 
    # posiciones_img = 
    # 50, 225, 275, 400 - 
    # 320, 225, 545, 400 - 
    # 50, 550, 275, 725 -
    # 320, 550, 545, 725
    columna= 0
    for img in list_imgs:
        imagen_a_cargar = Path(img).read_bytes()
        
        
        if columna == 0:
            posicionXmin = 50
            posicionYmin = 225
            posicionXmax = 275 
            posicionYmax = 400
            columna += 1
            posicion_img = fitz.IRect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen
            
        elif columna == 1:
            posicionXmin += 270
            posicionXmax += 270
            posicionYmin = 225
            posicionYmax = 400
            columna += 1
            posicion_img = fitz.IRect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen
            
        elif columna == 2:
            posicionXmin -= 270
            posicionXmax -= 270
            posicionYmin += 325
            posicionYmax += 325
            columna += 1
            posicion_img = fitz.IRect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen
        
        elif columna == 3:
            columna = 0
            posicionXmin += 270
            posicionXmax += 270
            posicionYmin = 550
            posicionYmax = 725
            posicion_img = fitz.IRect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen

        nueva_pagina_insertada.insert_image(posicion_img, stream = imagen_a_cargar, keep_proportion = False) #Inserción de imagen
       
    pdf_modificado.save(Path(Path.cwd(),"pruebaImagenes.pdf"))

inicio()
    


