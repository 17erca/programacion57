Algoritmo temperaturas
	Definir solido,liquido,gaseoso, promedio Como Entero
	Escribir "cantidad de temperaturas"
	leer a
	Para i<-1 Hasta a Con Paso 1 Hacer
		Escribir  " temperatura ", i, " en °c"
		leer temp 
		Si temp>= 100 Entonces
			gaseoso=gaseoso+1
		FinSi
		si temp<=0 Entonces
			solido=solido+1
		FinSi
		si 0<temp y temp<100 Entonces
			liquido=liquido+1
		FinSi
		promedio= temp+promedio
		
	Fin Para
	Escribir "RESUMEN DEL ANÁLISIS DE LAS MUESTRAS DE AGUA"
	Escribir "Cantidad de muestras sólidas:", solido 
	Escribir  "Cantidad de muestras líquidas:", liquido
	Escribir  "Cantidad de muestras gaseosas:", gaseoso
	Escribir "Temperatura Promedio °C: " , promedio/a
	Escribir "Temperatura Promedio °F: " , ((promedio/a)*(9/5)+32)
	
	
	
	
FinAlgoritmo
