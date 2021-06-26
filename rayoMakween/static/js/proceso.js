var arreglo = new Array();
var x = 0;

function grabar() {
    var nombre= document.getElementById('txtNombre').value;
    var apellido= document.getElementById('txtApellido').value;
    var email= document.getElementById('txtEmail').value;
    var usuario= document.getElementById('txtUsuario').value;
    var pass= document.getElementById('txtPass').value;
    var rut= document.getElementById('txtRut').value;
    var fono= document.getElementById('txtFono').value;
    reg = new formulario();
    reg.setNombre(nombre);
    reg.setApellido(apellido);
    reg.setEmail(email);
    reg.setUsuario(usuario);
    reg.setPass(pass);
    reg.setRut(rut);
    reg.setFono(fono);
    alert(reg.imprimir());
    arreglo[x]=JSON.stringify(reg);
    x++;
    localStorage.setItem('registros',arreglo);
    alert('Registro Almacenado');
}

function listar() {
    var todo='<table border=1>';
    todo = todo + '<tr> <td>Nombre</td> <td>Apellido</td> <td>Email</td> <td>Usuario</td> <td>Pass</td> <td>Rut</td> <td>Fono</td> </tr>'
    var datos = localStorage.getItem('registros');
    var arreglo_temp = new Array();
    datos = datos.split('},{').join('};{');
    arreglo_temp = datos.split(';');
    for (let index = 0; index < arreglo_temp.length; index++) {
        var formulario = arreglo_temp[index];
        var reg = JSON.parse(formulario);
        todo = todo + "<tr> <td>"+reg.nombre+"</td> <td>"+reg.apellido+"</td> <td>"+reg.email+"</td> <td>"+reg.usuario+"</td> <td>"+reg.pass+"</td> <td>"+reg.rut+"</td> <td>"+reg.fono+"</td> </tr>"
    }
    todo = todo + "</table>";
    document.getElementById('listado').innerHTML= todo;
}

