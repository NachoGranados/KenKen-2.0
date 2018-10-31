import random as rand

class Generador:
    matriz = []
    coordenadas = []
    juego = []
    bandera = False
    operadores = [[None],["+","*","-","/"],["+","*"]]
    
    def __init__(self,tamanio):
        for i in range(tamanio):
            matrizAux = []
            for j in range(tamanio):
                matrizAux += [0]
            self.matriz += [matrizAux]
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.coordenadas += [(i,j)]
        return
    def getAdyacencias(self,coords):
        adyacencias = []
        i = 0
        while(i<len(self.coordenadas)):
            if self.coordenadas[i] == coords:
                self.coordenadas.pop(i)
            else:
                if ((self.coordenadas[i][0]+1 == coords[0] and self.coordenadas[i][1] == coords[1]) or (self.coordenadas[i][0]-1 == coords[0] and self.coordenadas[i][1] == coords[1]) or (self.coordenadas[i][0] == coords[0] and self.coordenadas[i][1]-1 == coords[1]) or (self.coordenadas[i][0] == coords[0] and self.coordenadas[i][1]+1 == coords[1])):
                    adyacencias += [self.coordenadas[i]]
                    self.coordenadas.pop(i)
                else:
                    i+=1
        return adyacencias
    
    def asignarOperaciones(self):
        while(len(self.coordenadas)>0):
            posCoords = self.coordenadas[rand.randint(0,len(self.coordenadas)-1)]
            adyacencias = self.getAdyacencias(posCoords)
            celdas = [posCoords]
            if len(adyacencias) == 0:
                caso = 0
            if len(adyacencias) == 1:
                caso = rand.randint(0,1)
            if len(adyacencias) > 1:
                caso = rand.randint(0,2)
            operador = self.operadores[caso][rand.randint(0,len(self.operadores[caso])-1)]
            i = 0
            valorOperado = self.matriz[posCoords[0]][posCoords[1]]
            while(i<caso):
                coord = rand.randint(0,len(adyacencias)-1)
                celdas += [adyacencias[coord]]
                if operador == "+":
                    valorOperado += self.matriz[adyacencias[coord][0]][adyacencias[coord][1]]
                if operador == "*":
                    valorOperado *= self.matriz[adyacencias[coord][0]][adyacencias[coord][1]]
                if operador == "-":
                    valorOperado = abs(valorOperado - self.matriz[adyacencias[coord][0]][adyacencias[coord][1]])
                if operador == "/":
                    valorOperado = valorOperado//self.matriz[adyacencias[coord][0]][adyacencias[coord][1]]
                adyacencias.pop(coord)
                i += 1
            self.cargarAdyacenciasNoUsadas(celdas,adyacencias)
            celdas += [valorOperado,operador]
            self.juego += [celdas]
        return
        
    def cargarAdyacenciasNoUsadas(self,celdas,adyacencias):
        j = 0
        for i in range(len(celdas)):
            while(j<len(adyacencias)):
                if adyacencias[j] == celdas[i]:
                    adyacencias.pop(j)
                else:
                    j+=1
        for i in range(len(adyacencias)):
            self.coordenadas += [adyacencias[i]]
        return
        
        
    def generar(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.matriz[i][j] = rand.randint(1,len(self.matriz))
        self.revisar()
        self.asignarOperaciones()
        return self.juego
                    
    def getColumna(self,index):
        columna = []
        for i in range(len(self.matriz)):
                if i == index:
                    for j in range(len(self.matriz)):
                        columna += [self.matriz[j][i]]
        return columna
    
    def getFila(self,index):
        fila = []
        for i in range(len(self.matriz)):
            if i == index:
                for j in range(len(self.matriz[i])):
                    fila += [self.matriz[i][j]]
        return fila
    
    def validar(self,fila):
        repetidos = []
        repetido = False
        for i in range(len(fila)):
            for j in range(len(repetidos)):
                if repetidos[j] == fila[i]:
                    repetido = True
                    break
            if not repetido:
                repetidos += [fila[i]]
            else:
                return [i,repetidos]
        return True
    
    def revisar(self):
        i = 0
        while(i<len(self.matriz)):
            valido = self.validar(self.getFila(i))
            if isinstance(valido,list):
                valido2 = self.validar(self.getColumna(valido[0]))
                if isinstance(valido2,bool) and self.bandera:
                    coord = self.buscarIgual(self.getFila(i),valido[0])
                    self.matriz[i][coord] = rand.randint(1,len(self.matriz))
                    self.bandera = not self.bandera
                else:
                    self.matriz[i][valido[0]] = rand.randint(1,len(self.matriz))
                    self.bandera = not self.bandera
                self.revisar2()
                i = 0
            else:
                i+=1
        return
                
    def revisar2(self):
        i = 0
        while(i<len(self.matriz)):
            valido = self.validar(self.getColumna(i))
            if isinstance(valido,list):
                valido2 = self.validar(self.getFila(valido[0]))
                if isinstance(valido2,bool):
                    coord = self.buscarIgual(self.getColumna(i),valido[0])
                    self.matriz[coord][i] = rand.randint(1,len(self.matriz))
                else:
                    self.matriz[valido[0]][i] = rand.randint(1,len(self.matriz))
            else:
                i+=1
        return
    
    def buscarIgual(self,fila,coord):
        for i in range(len(fila)):
            if fila[i] == fila[coord]:
                return i