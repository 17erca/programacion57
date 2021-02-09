Algoritmo sin_titulo
	Definir in, fn, simpar Como Entero
	spar<-0
	simpar<-0
	in<- 1
	Escribir  "ingrese el número"
	leer fn
	Mientras  (in<fn) Hacer
		si ( in mod 2 = 0) Entonces
			spar<- spar + in
		sino 
			simpar<- simpar+in			
		FinSi
		in<- in+1		
	FinMientras
	
	escribir "lasuma de los impares es ",  simpar+fn
FinAlgoritmo
