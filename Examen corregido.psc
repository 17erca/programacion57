Algoritmo Pesos
	Definir prom, b, c Como Real;
	Definir a, d Como Caracter;
     Dimension d[12]
	Dimension a[12];
	Dimension b[12]
	Dimension c[12]
	Escribir  "club de obesidad";
	Para i<- 1 hasta 12 Con Paso 1 Hacer
		Escribir "Nombre: ";
		leer a[i];
		Escribir "Apellido: "
		Leer d[i]
		Escribir  "Insertar peso primera semana: ";
		leer b[i];
		Escribir "Insertar peso segunda semana: ";
		leer c[i];
		
	fin para
	Para i<-1 hasta 12 con paso 1 Hacer
		Si b[i]>c[i] Entonces
			prom<-b[i]-c[i];
			Escribir a[i] " " d[i] " BAJÓ su peso en " prom " kilos";
		fin si
		Si b[i]<c[i] Entonces 
			prom<-c[i]-b[i]
			Escribir a[i] " " d[i] " SUBIÓ su peso en " prom " kilos";
		fin si
		Si b[i]=c[i] Entonces 
			prom=c[i]-b[i]
			Escribir a[i] " " d[i] " MANTUVO su peso en " prom " kilos";
		fin si
	fin para
FinAlgoritmo
