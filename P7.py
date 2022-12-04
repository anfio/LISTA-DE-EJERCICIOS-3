# 7.Hacer un programa que consulte el valor del dolar (compra y venta ) de la fecha actual
#segun sunat (url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat')

import requests 
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' 

response = requests.get(url)
response.json() 
res=response.json()

print(res)


