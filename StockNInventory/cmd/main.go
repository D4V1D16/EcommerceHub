package main

import (
	"fmt"
	"net/http"
	"stockInventory/routes"
	"stockInventory/DB"


)

func main() {

	DB.DBConnection()

	productRoutes := routes.SetupProductRoutes()

	fmt.Print("Sirviendo en el puerto 3000")


	http.ListenAndServe(":3000",productRoutes)
}