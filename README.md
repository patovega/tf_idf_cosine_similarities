# tf_idf_cosine_similarities

El siguiente programa analiza archivos de extensión .txt dentro de un directorio y los transforma en vectores con el fin de poder encontrar una similitud entre ellos utilizando TF-IDF y La similutd de Coseno.

Para el calculo de TF-IDF se utilizando *TfidfVectorizer* de la libreria *scikit-learn*, con esto representamos los documentos como vectores. Estos vectores ya vienen normalizados con la norma euclidiana. 

Una vez representados los documentos como vectores, utilizamos *Linear_Kernel* para calcular el coseno del angulo entre dos vectores (archivo 1 y archivo a comparar) con los cual obtenemos la distancia entre ambos, que la medida de similitud de coseno.

# Setup and Dependencies

  * Python 2.7
  * Scikit-Learn <a href = "http://scikit-learn.org" target="blank_" />Sitio web</a>
   
# About scikit-learn
  scikit-learn es un módulo de Python para aprendizaje automático construido sobre SciPy y distribuido bajo la licencia BSD de 3 cláusulas.
  
# Dependencies 

  * Python (>= 2.7 or 3.4)
  * Numpy  (>= 1.8.2)
  * SciPy  (>=0.13.3)
  
# User install scikit-learn
  
  para instalar scikit-learn usamos pip
  
  pip install -U scikit-learn
  
# Documentation scikit-learn

 * HTML documentation (stable release):  <a href = "http://scikit-learn.org" target="blank_" /> http://scikit-learn.org</a>
 * HTML documentation (development version): <a href = "http://scikit-learn.org</a>http://scikit-learn.org/dev/" target="blank_" />http://scikit-learn.org</a>http://scikit-learn.org/dev/</a>
 * FAQ: <a href = "http://scikit-learn.org/stable/faq.html" target="blank_" />http://scikit-learn.org/stable/faq.html</a>

# Output

  El siguiente script genera un archivo TXT de nombre similitud.txt en el directorio raíz. 
  El archivo contiene tres columnas: 
  
    1. Primera columna: archivo procesado
    2. Segunda columna: archivo más similar al archivo procesado (columna 1)
    3. Tercera columna: distancia entre ambos archivos. (similitud de coseno)
