class login{
    usuario;
    pass;
    //mutadores
    setUsuario(usuario){
        this.usuario=usuario;
    }
    setPass(pass){
        this.pass=pass;
    }
    //accesadores
    getUsuario(){ return this.usuario;}
    getPass(){ return this.pass;}
    //toString
    imprimir(){
        return this.getUsuario()+' '+this.getPass();
    }
}