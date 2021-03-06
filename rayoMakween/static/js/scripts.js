function mensaje() {
    alert('hola mundo');
}

function validar() {
    var resp = validarRut();
    if (resp==false){
        return false;
    }
    resp = validarFecha();
    if (resp==false) {
        return false;
    }
    return true;
}

function validarRut(){

    var rut= document.getElementById('txtRut').value;
    if (rut.length !=10 ) {
        //alert('largo de rut incorrecto');
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'largo de rut incorrecto!'
          });
        return false;
    }
    var suma=0;  
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var caracter= rut.slice(index,index+1);
        //alert(caracter+' x '+num);
        suma=suma+(caracter * num)
        num=num-1;
        if (num == 1) {
            num=7;
        }
    }
    //alert('Suma:'+suma);
    var resto= suma % 11;
    //alert('Resto:'+resto);
    var dv= 11-resto;
    if (dv > 9) {
        if (dv == 10) {
            dv='K';
        }else{
            dv=0;
        }
    }
    //alert('DV:'+dv);
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario ) {
        //alert ('rut incorrecto');
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'rut incorrecto!'
          });
        return false;
    }else{
        //alert('rut correcto');
        Swal.fire({
            icon: 'success',
            title: 'rut correcto',
            showConfirmButton: false,
            timer: 1500
          })
        return true;
    }
}   

function validarFecha(){
    var fechaUsuario = document.getElementById('txtFechaNac').value;
    var fechaSistema = new Date();
    console.log('Fecha Usuario:'+fechaUsuario);
    console.log('Fecha Sistema:'+fechaSistema);
    /////////////////////////////////////////////////////
    var ano = fechaUsuario.slice(0,4);
    var mes = fechaUsuario.slice(5,7);
    var dia = fechaUsuario.slice(8,10);
    console.log('Año:'+ano+'Mes:'+mes+'Dia:'+dia);
    var fechaNuevaUsuario = new Date(ano,(mes-1),dia);
    console.log('Fecha Nueva:'+fechaNuevaUsuario);
    /////////////////////////////////////////////////////
    if (fechaNuevaUsuario > fechaSistema) {
        //alert('fecha de nacimiento incorrecta');
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'fecha incorrecta!'
          });
        return false;
    }
    /////////////////////////////////////////////////////
    var elDia = 24 * 60 * 60 * 1000; //transformar día a milisegundos
    var dias = (fechaSistema.getTime()- fechaNuevaUsuario.getTime()) / elDia;
    console.log('Dias:'+dias);
    var anos = Math.trunc ( dias / 365);
    if (anos < 18) {
        //alert('eres menor de edad, tienes '+anos+' años de edad');
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'eres menor de edad, tienes '+anos+' años de edad'
          });
        return false;
    }
    return true;
}
