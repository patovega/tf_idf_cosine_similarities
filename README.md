# tf_idf_cosine_similarities

El siguiente programa analiza archivos de extensión .txt dentro de un directorio (dataset/) y los transforma en vectores con el fin de poder encontrar una similitud entre ellos utilizando TF-IDF y La similutd de Coseno.

Para el calculo de TF-IDF se utilizando *TfidfVectorizer* de la libreria *scikit-learn*, con esto representamos los documentos como vectores. Estos vectores ya vienen normalizados con la norma euclidiana. 

Una vez representados los documentos como vectores, utilizamos *Linear_Kernel* para calcular el coseno del angulo entre dos vectores (archivo 1 y archivo a comparar) con los cual obtenemos la distancia entre ambos, que la medida de similitud de coseno.

# Setup and Dependencies

  * Python 2.7
  * Scikit-Learn <a href = "http://scikit-learn.org" target="blank_" />Sitio web</a>
## About Python
  * Python 2.7.12 <a href = "https://www.python.org/downloads/" target="blank_" > Download </a>
   
## About scikit-learn
  scikit-learn es un módulo de Python de MachineLearning construido sobre SciPy y distribuido bajo la licencia BSD de 3 cláusulas.
  
### Dependencies scikit-learn

  * Python (>= 2.7 or 3.4)
  * Numpy  (>= 1.8.2)
  * SciPy  (>=0.13.3)
  
### User install scikit-learn
  
  para instalar scikit-learn via PIP  
 
     C:\PythonXY\python pip install -U scikit-learn
  
  Esto instalara las dependencias de scikit-learn: Numpy & SciPy
	
  De lo contrario el programa presentara un error de tipo 
	
	File "Path\Program.py", line 3, in <module>
		from sklearn.feature_extraction.text import TfidfVectorizer
		ImportError: No module named sklearn.feature_extraction.text
  
### Documentation scikit-learn

 * HTML documentation (stable release):  <a href = "http://scikit-learn.org" target="blank_" /> http://scikit-learn.org</a>
 * HTML documentation (development version): <a href = "http://scikit-learn.org</a>http://scikit-learn.org/dev/" target="blank_" />http://scikit-learn.org</a>http://scikit-learn.org/dev/</a>
 * FAQ: <a href = "http://scikit-learn.org/stable/faq.html" target="blank_" />http://scikit-learn.org/stable/faq.html</a>
 
# Quick start

Para correr el programa debes abrir Python en tu consola de comandos (CMD) y dirigirte al directorio que aloja el programa.

Una vez en el directorio debes ejecutar el siguiente comando:

    Python Program.py
 
Ejemplo:

	C:\Python27>python C:\Users\Pvega\Diplomado\tareas\_17048470_TF_IDG_Similitud\Program.py
 
El programa procesara los archivos de extensión txt de la carpeta dataset.

# Output

  El siguiente script genera un archivo TXT de nombre similitud.txt en el directorio raíz de python27 (C:\Python27). 
  El archivo contiene tres columnas: 
  
    1. Primera columna: archivo procesado
    2. Segunda columna: archivo más similar al archivo procesado (columna 1)
    3. Tercera columna: distancia entre ambos archivos. (similitud de coseno)
    

