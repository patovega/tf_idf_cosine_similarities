# tf_idf_cosine_similarities

El siguiente programa analiza archivos de extensión .txt dentro de un directorio y los transforme en vectores con el fin de poder encontrar una similitud entre ellos.

Para el calculo de TF-IDF se utilizando *TfidfVectorizer* de la libreria *scikit-learn*, con esto representamos los documentos como vectores. Estos vectores ya vienen normalizados con la norma euclidiana. 

Una vez representados los documentos como vectores, utilizamos *Linear_Kernel* para calcular el coseno del angulo entre dos vectores (archivo 1 y archivo a comparar) con los cual obtenemos la distancia entre ambos, que la medida de similitud de coseno.

# Setup and Dependencies

  * Python / Scikit-Learn
  
# Output

  El siguiente script genera un archivo TXT de nombre similitud.txt en el directorio raíz. 
  El archivo contiene tres columnas: 
  
    1. Primera columna: archivo procesado
    2. Segunda columna: archivo más similar al archivo procesado (columna 1)
    3. Tercera columna: distancia entre ambos archivos. (similitud de coseno)
