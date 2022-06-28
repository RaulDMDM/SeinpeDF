import tkinter
from fitz import fitz
from pathlib import Path
from PyPDF2 import PdfFileReader

def inicio():
    
    pdf_original = tkinter.askopenfilename(title="Selecciona el informe Siebel")
    pdf_peritacion = Path(Path.cwd(), "ejemplo/peritacionGT.pdf")
    pdf_plantilla = Path(Path.cwd(), "ejemplo/marcaDeAgua.pdf")
    pdf_aux = Path(Path.cwd(),"pdfAux.pdf")

    num_referencia = capturaNumReferencia(pdf_original)
    list_imgs = [
    Path(Path.cwd(),"ejemplo/Fotos/20220131110845.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110852.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110858.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110905.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110907.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110918.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110922.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110923.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110928.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110931.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131110935.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131111043.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131111207.jpg"),
    Path(Path.cwd(),"ejemplo/Fotos/20220131111134.jpg"),
    ]
    list_tit = [
        "Texto 1",
        "Texto 2",
        "Texto 3",
        "Texto 4",
        "Texto 5",
        "Texto 6",
        "Texto 7",
        "Texto 8",
        "Texto 9",
        "Texto 10",
        "Texto 11",
        "Texto 12",
        "Texto 13",
        "Texto 14"]
    list_desc = [
        "Texto 1",
        "Texto 2",
        "Texto 3",
        "Texto 4",
        "Texto 5",
        "Texto 6",
        "Texto 7",
        "Texto 8",
        "Texto 9",
        "Texto 10",
        "Texto 11",
        "Texto 12",
        "Texto 13",
        "Texto 14"]
    #subdivision = 4
    #listas_imgs = [list_imgs[i:i + subdivision] for i in range(0, len(list_imgs), subdivision)]
    
    generar_num_paginas = int((len(list_imgs)/4) + 1) #Indica el numero de paginas que tiene que generar en base a la lista de Imagenes

    # if Path(Path.cwd(),"pruebaImagenes.pdf").exists():
    #     archivo = Path(Path.cwd(),"pruebaImagenes.pdf")
    # else:
    #     archivo = pdf_aux
    
    # agregarPagina(pdf_original, pdf_plantilla, pdf_aux, math.floor(len(list_imgs)/subdivision))
    agregarPaginas(pdf_original, pdf_plantilla,pdf_peritacion, pdf_aux, generar_num_paginas)
    generaPdfConImgs(pdf_aux, list_imgs,list_tit, list_desc, generar_num_paginas)
    
    pdf_aux.unlink()
def agregarPaginas(pdf_ruta: Path, pdf_plantilla: Path, pdf_peritacion: Path, pdf_aux: Path, num_paginas: int): #Agrega una nueva pagina con el formato base para añadir fotos
    pdfOriginal = fitz.open(pdf_ruta)
    pdfPeritacion = fitz.open(pdf_peritacion)
    pdfOriginal.insert_pdf(pdfPeritacion)
    for num_paginas in range(0, num_paginas):
        pdfNuevo = fitz.open(pdf_plantilla)
        pdfOriginal.insert_pdf(pdfNuevo)
        ultima_pagina = pdfOriginal.load_page(-1)
        ultima_pagina.set_rotation(0)
        if not ultima_pagina.is_wrapped:
            ultima_pagina.wrap_contents()
        pdfOriginal.save(pdf_aux) #Nombre archivo de salidaImagen a inserta

def capturaNumReferencia(pdf_original: Path):
    with open(pdf_original, 'rb') as f:
        pdf = PdfFileReader(f, strict = False)
        pagina = pdf.getPage(0)
        return pagina.extractText()[-10:]

def generaPdfConImgs(pdf_aux, list_imgs, list_tit, list_desc, paginas_img):

    posicionXmin = 50
    posicionYmin = 180
    posicionXmax = 275 
    posicionYmax = 355
    i = 0
    pdf_modificado = fitz.open(pdf_aux) #PDF en el que se insertara la imagen
    current_page = len(pdf_modificado) - paginas_img #Calcula la longitud del pdf con las plantillas para imagenes y resta el numero de paginas que corresponden a esas plantillas
    print(current_page)
    
    for pos, img in enumerate(list_imgs):
        print(pos)
        print(img)
        imagen_a_cargar = Path(img).read_bytes()
        pdf_ultima_pagina = pdf_modificado.load_page(current_page)

        if i == 0:
            posicionXmin = 50
            posicionYmin = 180
            posicionXmax = 275 
            posicionYmax = 355
            pdf_ultima_pagina.insert_textbox((50,75,275,255), list_tit[pos], align = 1, fontsize = 13, fontname = "hebo")
            pdf_ultima_pagina.insert_textbox((50,120,275,255), list_desc[pos], align = 1, fontsize = 10, fontname = "helv")
            i += 1
        elif i == 1:
            posicionXmin = 320
            posicionYmin = 180
            posicionXmax = 545 
            posicionYmax = 355
            pdf_ultima_pagina.insert_textbox((320,75,545,255), list_tit[pos], align = 1, fontsize = 13, fontname = "hebo")
            pdf_ultima_pagina.insert_textbox((320,120,545,255), list_desc[pos], align = 1, fontsize = 10, fontname = "helv")
            i += 1
        elif i == 2:
            posicionXmin = 50
            posicionYmin = 550
            posicionXmax = 275 
            posicionYmax = 725
            pdf_ultima_pagina.insert_textbox((50,445,275,625), list_tit[pos], align = 1, fontsize = 13, fontname = "hebo")
            pdf_ultima_pagina.insert_textbox((50,490,275,625), list_desc[pos], align = 1, fontsize = 10, fontname = "helv")
            i += 1
        elif i == 3:
            i = 0
            posicionXmin = 320
            posicionYmin = 550
            posicionXmax = 545 
            posicionYmax = 725
            pdf_ultima_pagina.insert_textbox((320,445,545,625), list_tit[pos], align = 1, fontsize = 13, fontname = "hebo")
            pdf_ultima_pagina.insert_textbox((320,490,545,625), list_desc[pos], align = 1, fontsize = 10, fontname = "helv")
            current_page += 1
   
        posicion_img = fitz.Rect(int(posicionXmin),int(posicionYmin), int(posicionXmax), int(posicionYmax)) #Posicion y tamaño de la imagen
        pdf_ultima_pagina.insert_image(posicion_img, stream = imagen_a_cargar, keep_proportion = False) #Inserción de imagen
        
    
        
    # Revisar saveIncr ya que no se está sobrescribiendo
    # if Path(Path.cwd(),"pruebaImagenes.pdf").exists():
    #     pdf_modificado.saveIncr()
    # else:

    pdf_modificado.save(Path(Path.cwd(),"pruebaImagenes.pdf"))
    
raiz = tkinter.Tk
raiz.geometry("900x600")

inicio()

raiz.mainloop()


