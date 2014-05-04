#<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
from flask import Flask
from flask import render_template
import restaurantes
from flask import request

def hola():
	print "hola"

app=Flask(__name__)
listaRest=""

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/consulta")
def todosRest():
	return render_template('consulta.html')

@app.route("/todosRestaurantes",methods=['GET', 'POST'])
def todosRestaurantes():
	if request.method == 'POST':
		items = []
		lista=restaurantes.imprimirRest()
		items.append(lista)
		print items
		#lista=lista.split('')
		#for item in lista:
		#	print item
		#listaRest=restaurantes.imprimirRest()
		return render_template("resultados.html",entradas=listaRest)

if __name__=="__main__":
	#listaRest=restaurantes.imprimirRest()	
	app.debug=True
	app.run()
