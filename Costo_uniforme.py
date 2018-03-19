from algoritmo import *
class Costo_uniforme(Algoritmo):

	lista_nodos = []
	camino_final =[]
	cant_nodos_expandidos=1
	
	def __init__(self,entrada,nodo_inicial,nodo_meta):
		Algoritmo.__init__(self,entrada)
		# agregamos los nuevos atributos
		self.entrada = entrada
		self.nodo_inicial = nodo_inicial
		self.nodo_meta = nodo_meta
		self.lista_nodos.append(self.nodo_inicial)
		print "nodo inicial",self.nodo_inicial.x," ",self.nodo_inicial.y
		print "nodo meta",self.nodo_meta.x," ",self.nodo_meta.y
		self.calcular()

	def calcular(self):
		i = 0
		self.mostrar_lista()
		#inicializamos la lista con los tres primeros hijos
		while True:						
			index=self.index_nodo_a_expandir()
			if self.es_nodo_meta(self.lista_nodos[index]) is True:
				print "el nodo meta esta ",self.lista_nodos[index].x," ",self.lista_nodos[index].y
				#Recuperar el camino de llegada
				print "el peso es", self.lista_nodos[index].peso
				self.camino_destino(self.lista_nodos[index],self.nodo_inicial,self.camino_final)
				#Imprimir el camino:
				for nodo in self.camino_final:
					print nodo.x," ",nodo.y

				print "Se expandieron un total de", self.cant_nodos_expandidos," nodos"
				print "El arbol tiene una profundidad de", len(self.camino_final)
				break

			print "nodo a expandir",self.lista_nodos[index].x," ",self.lista_nodos[index].y
			print "el peso es:",self.lista_nodos[index].peso
			
			
			
			hijos = self.expandirNodo(self.lista_nodos[index])			
			self.cant_nodos_expandidos=self.cant_nodos_expandidos + len(hijos);


			for nodo_hijo in hijos:
				#agrega cada nodo hijo al final de la lista
				self.lista_nodos.append(nodo_hijo)


			#borra el primer elemento
			self.lista_nodos.pop(index)

			self.mostrar_lista()
						

			i = i + 1		
			if i == 25:
				break
				#pass
			
			#print self.lista_nodos
		print "termino for"
		return

	def es_nodo_meta(self,nodo):
		if nodo.x == self.nodo_meta.x  and nodo.y == self.nodo_meta.y:
			return True
		else:
			return False

	def index_nodo_a_expandir(self):
		flag=self.lista_nodos[0]
		for nodo in self.lista_nodos:
			if flag.peso > nodo.peso:
				flag=nodo

		return self.lista_nodos.index(flag)

	def mostrar_lista(self):
		print "--------------------------------------"
		for x in self.lista_nodos:
			print "elementos lista nodo ",x.x," ",x.y


		