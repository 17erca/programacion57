Algoritmo Expresiones_2
	Escribir "ingrese el valor de x"
	Leer  x;
	a<-x;
	x2<-(a*a);
	pi2<-(pi*pi);
	b<-(x2/(pi2*(x2+(1.0/2.0))))*(1+(x2/(pi2*(x2-(1.0/2.0))^2)));
	escribir pi;
	escribir "el resultado de la expresión es: " b;
	
FinAlgoritmo
