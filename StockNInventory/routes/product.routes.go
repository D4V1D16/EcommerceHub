package routes

import (
	"stockInventory/controllers"

	"github.com/gorilla/mux"
)



func SetupProductRoutes() *mux.Router{

	routesProduct := mux.NewRouter()

	//POST -> Creacion de Productos
	routesProduct.HandleFunc("/",controllers.HomeHandler).Methods("POST","GET")

	//GET -> Mostrar Productos

	//DELETE -> Borrar Productos

	


	return routesProduct

}




