package controllers

import "net/http"

func HomeHandler(w http.ResponseWriter, r *http.Request){
	//Crear un Producto
	w.Write([]byte("Home"))
}