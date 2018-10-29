#importamos librerias
#con TfidfVectorizer transformarmos el contenido de nuestros archivos en vecotres TF*IDF
from sklearn.feature_extraction.text import TfidfVectorizer
#con linear_kernel usamos nuestros vectores idf para comparar la similitud en nuestra lista de archivos
from sklearn.metrics.pairwise import linear_kernel
#lo usamos para trackear horario de inicio de comparacion de similitud y fin de esta
import datetime
#os la utilizamos para el manejo de archivos
import os
#con glob tomamos los archivos desde una ruta en especifica
import glob

#las siguientes listas nos ayudaran a manejar nuestros archivos
#documentos: contiene el contenido de cada uno de los archivos de la carpeta dataset/*.txt
documentos = list()
#files: contiene los nombres de los archivos procesados
files = list()

print "Revisando archivos..."

#@books contiene una lista de nombres de archivo de extension TXT
books = glob.glob("dataset/*.txt")
#recorrimos los elementos de la variable @books
#por cada elemento:
#el contenido lo dejamos en la lista documentos
#detalle: para transformar el contenido en vector TF IDF con SKLEAR debe estar en minuscula
#el nombre del documento lo dejamos en files.
for book_file in books:
    with open(book_file, 'r') as content_file:
        # el archivo dataset.txt no nos interesa, lo omitimos
        if(os.path.basename(content_file.name) == 'dataset.txt'):
            continue
        content = content_file.read()
        documentos.append(content.lower())
        files.append(os.path.basename(content_file.name))

#transformarmos en vectores tf idf con scklear y fit_transform
#fit_transform debe recibir un objecto de tipo List
#@tfidf = contiene nuestros documentos vectorizados
tfidf = TfidfVectorizer().fit_transform(documentos)
#tfidf

#las siguientes variables son acumuladores
#nos ayudaran para recorrer nuestro TF IDF vectorizado e ir comparandolo con otro documento
#utilizando la similitud de coseno.
i = 0
j = 1

#registro de inicio del proceso
print "inicio"
print(datetime.datetime.now())

filename = "similitud.txt"
if os.path.exists(filename): os.remove(filename)
#creamos archivo si no existe
f = open(filename, "w")

#recorremos cada uno de los elementos de los documentos
while i < len(documentos):
  #calculamos la similitud de coseno
  cosine_similarities = linear_kernel(tfidf[i:j], tfidf).flatten()
  #encontramos el mas cercano
  related_docs_indices = cosine_similarities.argsort()[:-3:-1]
  #imprimimos en consola
  print ("comparando",files[i],"documento_similar:",files[ related_docs_indices[1] ],"distancia",cosine_similarities[related_docs_indices[1]])

  #guardamos en archivo
  f.write("{}{}{}{}{}".format(files[i]," ",files[ related_docs_indices[1] ], " ", cosine_similarities[related_docs_indices[1]] ))
  f.write("\n")
  #aumentamos accumuladores
  i = i + 1
  j = j + 1
#registro de fin del proceso
print "fin"
print( datetime.datetime.now())
