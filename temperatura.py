#coding:utf-8

import json
import requests
import webbrowser	
from jinja2 import Template
from lxml import etree



lista_ciudades = ('Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla')
url = "http://api.openweathermap.org/data/2.5/weather"

f = open('plantillah.html','r')
f_html = open('weather-xml.html','w')

html = ''
temp_min = []
temp_max = []	
veloc_viento = []
direc_viento = []
provincia = []




for elemento in lista_ciudades:
	
	dicc_params = {'q':elemento,'mode':'xml','units':'metric','lang':'es'}
	
	provincia.append(elemento)
	
	respuesta = requests.get(url,params=dicc_params)	
			 
	arbol_xml = etree.fromstring(respuesta.text.encode("utf-8"))
	
	temperature = arbol_xml.find("temperature")
	
	temp_min.append(temperature.attrib["min"])
	
	temp_max.append(temperature.attrib["max"]) 
	
	wind_speed = arbol_xml.find("wind/speed")
	
	veloc_viento.append(wind_speed.attrib["value"])
	
	wind_direction = arbol_xml.find("wind/direction")
	
	direc_viento.append(wind_direction.attrib["code"])

	
for linea in f:
	html += linea

plant_template = Template(html)

salida_html = plant_template.render(lista_ciudades = provincia, temperatura_minima = temp_min, temperatura_maxima = temp_max, viento_velocidad = veloc_viento, viento_direccion = direc_viento)

f_html.write(salida_html)

webbrowser.open("weather-xml.html")

	




