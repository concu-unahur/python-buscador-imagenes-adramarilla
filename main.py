import logging
from api import PixabayAPI

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'computadoras'
<<<<<<< HEAD
api = PixabayAPI('PONER ACÁ EL API KEY', carpeta_imagenes)
=======
api = PixabayAPI('15392204-778b8867cb956ec976dc3c8db', carpeta_imagenes)
>>>>>>> Initial commit

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 5)

for u in urls:
  logging.info(f'Descargando {u}')
  api.descargar_imagen(u)
