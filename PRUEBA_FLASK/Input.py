from cherrypy import expose
import cherrypy
from cherrypy import quickstart
from jinja2 import Environment, FileSystemLoader
#from restaurantes import *
from flask import Flask

from pyswip import *

p=Prolog()
p.consult("rest.pl")

#listaRest=imprimirRest()
#restaurantesXtipo(tipoComida)
env = Environment(loader=FileSystemLoader('templates'))
cherrypy.server.socket_host = 'localhost'



class Pagina():

	@expose
	def index(self):
		tmpl = env.get_template('index.html')
		return tmpl.render()

	@expose
	def consulta(self):
		tmpl = env.get_template('consulta.html')
		return tmpl.render()

	@expose
	def agregar(self):
		tmpl = env.get_template('agregar.html')
		return tmpl.render()

	@expose
	def agregarRest(self):
		tmpl = env.get_template('agregarRest.html')
		return tmpl.render()

	@expose
	def agregarPlatillo(self):
		tmpl = env.get_template('agregarPlatillo.html')
		return tmpl.render()


	@expose
	def acercaDe(self):
		tmpl = env.get_template('acercaDe.html')
		return tmpl.render()

	@expose
	def consultas(self):
		tmpl = env.get_template('consulta.html')
		return tmpl.render()

	@expose 
	def consultaTipo(self,tipoComida):
		restaurantesXtipo(tipoComida)
		templateVars = { "resConsulta" : listaTipos }
		tmpl = env.get_template('resultados.html')
		return tmpl.render()#resConsulta=lista)

	@expose
	def todosRestaurantes(self):
		listaRest=[]
		imprimirRest()
		templateVars = { "resConsulta" : listaRest }
		tmpl = env.get_template('resultados.html')
		return tmpl.render(templateVars)



##restPlatillo,nombrePlatillo,saborPlatillo,paisPlatillo,horarioRest

	@expose
	def addRest(self, nombreRest,tipoComida,ubicacionrest,numeroRest,horarioRest):
		agregarRest(nombreRest,tipoComida,ubicacionrest,numeroRest,horarioRest)
		return self.index()
		#def agregarPlatillo(rest,nombrePlat,sabor,PaisOrg,Ingredientes):
	@expose
	def addPlatillo(self,restPlatillo,nombrePlatillo,saborPlatillo,paisPlatillo,ingredientesPlatillo):
		ingredientesPlatillo = ingredientesPlatillo.split(",")
		ingredientesPlatillo = str(ingredientesPlatillo)
		ingredientesPlatillo = ingredientesPlatillo.replace("u'","'")
		ingredientesPlatillo = ingredientesPlatillo.replace(" ","")
		agregarPlatillo(restPlatillo,nombrePlatillo,saborPlatillo,paisPlatillo,ingredientesPlatillo)
		return self.index()

if __name__ == "__main__":
    quickstart(Pagina(),config={

        '/css':
        { 'tools.staticdir.on':True,
          'tools.staticdir.dir': "/templates"
        },

        '/joey_css.css':
        { 'tools.staticfile.on':True,
          'tools.staticfile.filename': "/templates/estilos.css"
        }
    })
    
