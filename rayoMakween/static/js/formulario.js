class formulario{
    nombre;
    apellido;
    email;
    usuario;
    pass;
    rut;
    fono;
    //mutadores
    setNombre(nombre){
        this.nombre=nombre;
    }
    setApellido(apellido){
        this.apellido=apellido;
    }
    setEmail(email){
        this.email=email;
    }
    setUsuario(usuario){
        this.usuario=usuario;
    }
    setPass(pass){
        this.pass=pass;
    }
    setRut(rut){
        this.rut=rut;
    }
    setFono(fono){
        this.fono=fono;
    }
    //accesadores
    getNombre(){ return this.nombre;}
    getApellido(){ return this.apellido;}
    getEmail(){ return this.email;}
    getUsuario(){ return this.usuario;}
    getPass(){ return this.pass;}
    getRut(){ return this.rut;}
    getFono(){ return this.fono;}
    //toString
    imprimir(){
        return this.getNombre()+' '+this.getApellido()+' '+this.getEmail();
    }
}