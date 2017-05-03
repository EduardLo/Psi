function myEvaluacion(value){
	var x = x + value;
	document.getElementById("result").innerHTML = x;
	//window.alert(x);
}
function myResultado(cantidadPreguntas,usuario, correo){
	//window.alert(cantidadPreguntas);
	 total=0;
	//window.alert(cantidadPreguntas);
	for (var i = 0; i <cantidadPreguntas; i++) {
		//window.alert(i);
		total=total+parseInt(document.getElementsByName("result")[i].value);
	}
	document.getElementById("total_test").value= total.toString();
	//window.alert(total);
}

function myResultadoGuest(cantidadPreguntas, usuario, correo, edad, male, female,direccion,telefono){
	//window.alert(cantidadPreguntas);
	 total=0;
	//window.alert(cantidadPreguntas);
	for (var i = 0; i <cantidadPreguntas; i++) {
		//window.alert(i);
		total=total+parseInt(document.getElementsByName("result")[i].value);
	}

	if (male == true) {
		sexo="Hombre";
	}
	else
	{
		if (female==true) {
			sexo="mujer";
		}
	}
	document.getElementById("total_test").value= total.toString();
	document.getElementById("usuario").value= usuario;
	document.getElementById("correo").value= correo;
	document.getElementById("edad").value= edad;
	document.getElementById("sexo").value= sexo;
	document.getElementById("direccion").value= direccion;
	document.getElementById("telefono").value= telefono;
	
}