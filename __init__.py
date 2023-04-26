# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import time

"""
    Obtengo el modulo que fueron invocados
"""

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'ImageWork' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from PIL import Image
import numpy as np
import cv2
import imutils
from subprocess import Popen, PIPE

def makeTmpDir(name):
    try:
        os.mkdir("tmp")
        os.mkdir("tmp" + os.sep + name)
    except:
        try:
            os.mkdir("tmp" + os.sep + name)
        except:
            pass

def pdf2Img(pdf, conf, img=None, dim = None):
    global Popen, PIPE

    print("**",pdf)
    env = os.environ.copy()
    base_path = tmp_global_obj["basepath"]

    if img:
        img = img.split(".jpg")[0]
    else:
        img = pdf.split(".pdf")[0]

    print(img)

    scale = ""
    if dim:
        scale += "-W {x} -H {y} -sz".format(x=dim[0], y=dim[1])

    popper = base_path + "modules" + os.sep + "ImageWork" + os.sep + "bin" + os.sep + "pdftoppm.exe" + conf + " -jpeg " + pdf + " " + \
             str(img)
    print(popper)
    con = Popen(popper, env=env, shell=True, stdout=PIPE, stderr=PIPE)

    a = con.communicate()
    return a


module = GetParams("module")

if module == "merge":
    image1 = GetParams("jpg-1").replace("/", os.sep)
    image2 = GetParams("jpg-2").replace("/", os.sep)
    coord = GetParams("coordinates")
    result = GetParams("result")

    try:
        coord = eval(coord)
    except NameError:
        PrintException()
        raise e
    try:

        img1 = Image.open(image1)
        img2 = Image.open(image2)

        img1.paste(img2, coord)

        img1.save(image1)
        if result:
            SetVar(result, True)

    except Exception as e:
        PrintException()
        raise Exception(e)

if module == "toPDF":

    img = GetParams("jpg-folder")
    pdf = GetParams("pdf_path")
    result = GetParams("result")

    try:
        files = os.listdir(img)
        print(files)
        images = []
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                path = img + os.sep + file
                print(path)
                jpg = Image.open(path)
                images.append(jpg)
        print(images)

        images[0].save(pdf, save_all=True)
        for image in images[1:]:
            image.save(pdf, append=image)

        if result:
            SetVar(result, True)
    except Exception as e:
        PrintException()
        raise e
if module == "search":
    img_path = GetParams("img").replace("/", os.sep)
    tem_path = GetParams("template").replace("/", os.sep)
    result = GetParams("result")

    img = cv2.imread(img_path, 0)
    img2 = img.copy()
    template = cv2.imread(tem_path, 0)
    tH, tW = template.shape

    method = cv2.TM_CCOEFF_NORMED
    temp = template.copy()

    for scale in np.linspace(0, 1.0, 20)[::-1]:
        resized = imutils.resize(img2, width=int(img2.shape[1] * scale))
        print(resized.shape[0], tH, resized.shape[1],tW)
        if resized.shape[0] < tH and resized.shape[1] < tW:
            break

    # Apply template Matching
    res = cv2.matchTemplate(resized, temp, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("max", max_loc)
    MPx, MPy = max_loc

    if result:
        SetVar(result, "{},{}".format(MPx, MPy))
        
if module == "searchImage":
    try:
        img_base_path = GetParams("img_base").replace("/", os.sep)
        img_searched_path = GetParams("img_searched").replace("/", os.sep)
        min_val_var = float(GetParams("min_val")) if GetParams("min_val") else 0.9
        result = GetParams("result")
        
        imagen1 = cv2.imread(img_base_path)
        imagen2 = cv2.imread(img_searched_path)
        
        imagen1_gris = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
        imagen2_gris = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
        
        
        resultado = cv2.matchTemplate(imagen1_gris, imagen2_gris, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(resultado)
        
        print("Valor de coincidencia encontrado: ", max_val)
        if max_val < min_val_var:
            print("max_val", max_val)
            SetVar(result, False)
            raise Exception("Image not found")
        else:
            SetVar(result, True)

        
        
        
        
        
    except Exception as e:
        PrintException()
        raise e
    
    
    
    

if module == "readText":

    import pyocr
    import pyocr.tesseract
    import pyocr.builders

    file = GetParams("file")
    coord = GetParams("coordinates")
    page = GetParams("page")
    size = GetParams("size").replace("x", ",")
    result = GetParams("result")

    makeTmpDir("ImageWork")
    if file.endswith(".pdf"):
        image_base = "tmp/ImageWork/image_name.jpg"
        pdf2Img(file, conf="", img=image_base)
        image = "tmp/ImageWork/image_name-{}.jpg".format(page)
    elif file.endswith(".jpg") or file.endswith(".png"):
        image = file
    else:
        raise Exception("Not valid format")

    try:
        if coord:
            coord = eval(coord)
            size = coord[0] + eval(size)[0], coord[1] + eval(size)[1]
            tupl = coord + size
            img = Image.open(image)
            crop_img = img.crop(tupl)
            crop_path = 'tmp/ImageWork/crop.jpg'
            crop_img.save(crop_path)
        else:
            crop_path = image

        pyocr.tesseract.TESSERACT_CMD = os.path.join(base_path, 'modules', 'ImageWork', 'Tesseract-OCR',
                                                     'tesseract.exe')
        img = Image.open(crop_path)
        tool = pyocr.get_available_tools()[0]
        lang = tool.get_available_languages()[0]
        text = tool.image_to_string(
            img,
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )

        if result:
            SetVar(result, text)

    except Exception as e:
        PrintException()
        raise e


if module == "cropImage":
    image_path = GetParams("image")
    path = GetParams("path")
    size = GetParams("size")
    coord = GetParams("coordinates")

    try:
        coord = eval(coord)
        size = eval(size)
        pdf_im = Image.open(image_path)
        pdf_im.crop(coord + size).save(path)
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e
