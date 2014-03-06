#coding:utf-8
import json
import requests
import webbrowser	
from jinja2 import Template
from lxml import etree

def direccion_viento(cadena):
	if cadena >= 337.5 or cadena >=0 and cadena < 22.5:
		return "N"
	if cadena >= 22.5 and cadena < 67.5:
		return "NE"
	if cadena >= 67.5 and cadena < 112.5:
		return "E"
	if cadena >= 112.5 and cadena < 157.5:
		return "SE"
	if cadena >= 157.5 and cadena < 202.5:
		return "S"
	if cadena >= 202.5 and cadena < 247.5:
		return "SO"
	if cadena >= 247.5 and cadena < 292.5:
		return "O"
	if cadena >= 292.5 and cadena < 337.5:
		return "NO"
	

lista_ciudades = ('Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla')

f = open('plantillah.html','r')
f_html = open('weather-xml.html','w')
html = ''
temp_min = []
temp_max = []
veloc_viento = []
direc_viento = []
provincia = []
url = "http://api.openweathermap.org/data/2.5/weather"



for elemento in lista_ciudades:
	
	dicc_params = {'q':elemento,'mode':'xml','units':'metric','lang':'es'}
	
	provincia.append(elemento)
	
	respuesta = requests.get(url,params=dicc_params)	
			 
	diccionario_xml = etree.fromstring(respuesta.text.encode("utf-8"))
	
	print diccionario_xml
	
	temp_min.append(int(diccionario_json["main"]["temp_min"] - 273))
	
	#temp_max.append(int(diccionario_json["main"]["temp_max"] - 273))
	
	#veloc_viento.append(int(diccionario_json["wind"]["speed"]*1.6))
	
	#direc_viento.append(direccion_viento(diccionario_json["wind"]["deg"]))
	
#for linea in f:
#	html += linea

#plant_template = Template(html)

#salida_html = plant_template.render(lista_ciudades = provincia, temperatura_minima = temp_min, temperatura_maxima = temp_max, viento_velocidad = veloc_viento, viento_direccion = direc_viento)

#f_html.write(salida_html)

#webbrowser.open("weather.html")

	




