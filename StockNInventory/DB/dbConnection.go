package DB

import (
	"log"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)


var DB *gorm.DB

func DBConnection(){
	var ERROR error;
	DB,ERROR = gorm.Open(postgres.Open(DSN),&gorm.Config{})
	if ERROR != nil {
		log.Fatal(ERROR)
	} else{
		log.Println("DB Connected")
	}
}