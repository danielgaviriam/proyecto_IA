from algoritmo import *
class Preferente_profundidad(Algoritmo):

	

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
			if self.es_nodo_meta(self.lista_nodos[0]) is True:
				self.resumen(0)
				break

			print "nodo a expandir",self.lista_nodos[0].x," ",self.lista_nodos[0].y

			if self.nodo_fue_expandido(self.lista_nodos[0].padre,self.lista_nodos[0]) == False:
				hijos = self.expandirNodo(self.lista_nodos[0])
			else:
				print "no expande"
				hijos = []

			self.cant_nodos_expandidos = self.cant_nodos_expandidos + len(hijos);

			
			#borra el primer elemento
			self.lista_nodos.pop(0)

			#volteamos la lista para que coloque abc y no cba
			for nodo_hijo in reversed(hijos):
				#agrega cada nodo hijo al principio de la lista
				self.lista_nodos.insert(0, nodo_hijo)


			self.mostrar_lista()
						

			i = i + 1		
			if i == 10:
				#break
				pass
			
		
		return self.camino_final
	
	#evita ciclos
	def nodo_fue_expandido(self,nodo_padre,nodo_a_verificar):
		#llego a la raiz
		if isinstance(nodo_padre, int) is True:
			print "expande es el nodo raiz"
			return False
		#si es igual a algun nodo padre 
		elif nodo_a_verificar.x == nodo_padre.x and nodo_a_verificar.y == nodo_padre.y:
			print "ya se ha expandido no expande"
			return True
		else:
			print "ciclo"
			return self.nodo_fue_expandido(nodo_padre.padre,nodo_a_verificar)
			

			
	def es_nodo_meta(self,nodo):
		if nodo.x == self.nodo_meta.x  and nodo.y == self.nodo_meta.y:
			return True
		else:
			return False