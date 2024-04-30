import mongoose from "mongoose";

const infoSchema = mongoose.Schema(
  {
    nombre: {
      type: String,
      required: true
    },
    apellido: {
      type: String,
      required: true
    },
    edad: {
      type: String,
      required: true
    },
    telefono: {
      type: String,
      required: true
    },
    email: {
      type: String,
      required: true
    },
    direccionEntrega: {
      type: String,
      required: true
    },
    direccionFacturacion: {
      type: String,
      required: false,
    },
  },
  {
    timestamps: true,
  }
);

const infoUser = mongoose.model("User",infoSchema);
export default infoUser;