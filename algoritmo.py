from clases import nodo
from time import time
class Algoritmo:

	def __init__(self,entrada):
		self.tiempo_inicial = time()
		self.entrada = entrada
		self.lista_nodos = []
		self.camino_final = []
		self.cant_nodos_expandidos = 1
		self.tiene_flor = False
		self.profundidad_arbol = 0
		self.tiempo_ejecucion=0

	#Crea una instancia de la clase nodo y lo returna
	def crear_nodo(self,x,y,peso_anterior,nodo_padre,nodo_meta):
		
		#crea el nodo si es diferente a muro
		if int(self.entrada[y][x])!=1:			
		#if int(self.entrada[y][x])!=1:			
			n=nodo()
			n.x=x
			n.y=y
			n.padre=nodo_padre
			n.profundidad = nodo_padre.profundidad + 1

			self.save_profundidad_arbol(n.profundidad)

			if(nodo_padre.flor==False and self.tiene_flor==False):
				n.peso=self.peso_casilla(x,y)+peso_anterior
				n.flor=False
			elif nodo_padre.flor==True:
				n.peso=1+peso_anterior
				n.flor=True
				self.tiene_flor=False
			else:
				n.peso=1+peso_anterior
				n.flor=True

			print "tiene flor ", n.flor
			
			n.heuristica=self.calcular_heuristica(n,nodo_meta)
			n.heuristica_peso=n.peso+n.heuristica
			return n
		else:
			return False

	#Evalua que exista la casilla que se desea expandir
	def expansion_disponible(self,x,y):
		if x<0 or x >9 or y<0 or y>9:
			return False
		else:
			return True

	def expandirNodo(self,nodo,nodo_meta):
		hijos = []

		if int(self.entrada[nodo.y][nodo.x]) == 3:
			self.tiene_flor = True
			nodo.flor = True
			#actualizamos el nodo actual en la lista no funciona por referencia
			if self.name != "amplitud":
				self.lista_nodos[self.index_nodo_a_expandir()].flor=True
				print "tomo flor"
		
		#expArriba
		if(self.expansion_disponible(nodo.x,nodo.y-1)):
			result=self.crear_nodo(nodo.x,nodo.y-1,nodo.peso,nodo,nodo_meta)
			if(result!=False):
				hijos.append(result)
		#expAbajo
		if(self.expansion_disponible(nodo.x,nodo.y+1)):
			result=self.crear_nodo(nodo.x,nodo.y+1,nodo.peso,nodo,nodo_meta)
			if(result!=False):
				hijos.append(result)
		#expDerecha
		if(self.expansion_disponible(nodo.x+1,nodo.y)):
			result=self.crear_nodo(nodo.x+1,nodo.y,nodo.peso,nodo,nodo_meta)
			if(result!=False):
				hijos.append(result)
		#expIzquierda
		if(self.expansion_disponible(nodo.x-1,nodo.y)):
			result=self.crear_nodo(nodo.x-1,nodo.y,nodo.peso,nodo,nodo_meta)
			if(result!=False):
				hijos.append(result)

		print "numero de hijos expandidos ", len(hijos)
		return hijos

	#Retorna el peso de una casilla
	def peso_casilla(self,x,y):
		if int(self.entrada[y][x])!=4:
			return 1
		else:	
			return 8

	#De forma recursiva, almacena en un array los nodos padre desde el nodo meta, hasta el nodo raiz
	#encontrando asi, el camino que recorrio
	def camino_destino(self,nodo_final,nodo_raiz,camino):
		
		if isinstance(nodo_final, int) is True:
			print "expande es el nodo raiz"
			return False
		else:
			camino.append(nodo_final)
			self.camino_destino(nodo_final.padre,nodo_raiz,camino)

	def calcular_tiempo_ejecucion(self):
		self.tiempo_ejecucion=time() - self.tiempo_inicial
		return self.tiempo_ejecucion

	def mostrar_lista(self):
		print "--------------------------------------"
		for x in self.lista_nodos:
			print "elementos lista nodo ",x.x," ",x.y," g(n)",x.peso," h(n)",x.heuristica," f(n)",x.heuristica_peso," flor",x.flor

	#Almacena la profundidad del arbol
	def save_profundidad_arbol(self,profundidad_nodo):
		if  profundidad_nodo > self.profundidad_arbol:
			self.profundidad_arbol = profundidad_nodo

	#Actualiza la informacion del resumen
	def resumen(self,index):
		print "----------------------------------------------------------------"
		print "el nodo meta esta ",self.lista_nodos[index].x," ",self.lista_nodos[index].y
		#Recuperar el camino de llegada
		print "el peso del camino es", self.lista_nodos[index].peso
		self.camino_destino(self.lista_nodos[index],self.nodo_inicial,self.camino_final)

		print "Se expandieron un total de", self.cant_nodos_expandidos," nodos"
		#CORREGIR!
		print "El arbol tiene una profundidad de", self.profundidad_arbol

		print "Tiempo de ejecucion ", self.calcular_tiempo_ejecucion()

	
	def calcular_heuristica(self,nodo_base,nodo_meta):
		x=abs(nodo_base.x-nodo_meta.x)
		y=abs(nodo_base.y-nodo_meta.y)
		return x+y