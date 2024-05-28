import infoUser from "../models/infoUsers.model.js";

export const postUser = async(req,res) => {
    try{
        const user = await infoUser.create(req.body);
        res.status(201).json(user);
    } catch (error) {
        res.status(500).json(
            {
                message:'Se ha producido un error al crear el usuario',
                detail:error
            });
    }
};

export const getAllUsers = async(req,res) => {
    try {
        const Users = await infoUser.find({});
        res.status(200).json(Users);
    } catch (error) {
        res.status(500).json(
            {
                message:'Se ha producido un error al obtener todos los usuarios',
                detail:error
            }
        );
    }
}

export const deleteUser = async(req,res) => {
    try {
        const { id } = req.params;
        const user = await infoUser.findByIdAndDelete(id);

        if(!user){
            return res.status(404).json({message:'No se encontro el usuario'})
        }
        res.status(201).json(user);
    } catch (error) {
        console.log(error)
        res.status(500).json(
            {
                message:'Se ha producido un error al borrar el usuario',
                detail:error
            }
        );
    }
}

export const updateUser = async (req, res) => {
    try {
        const { id } = req.params;
        const updatedInfo = await infoUser.findByIdAndUpdate(id, req.body,{
            new:true
        });

        if (!updatedInfo) {
            return res.status(404).json({ message: 'No se encontró el usuario' });
        }

        
        res.status(200).json({   
            message: 'Se ha actualizado la información con éxito',
            detail: updatedInfo 
        });

    } catch (error) {
        res.status(500).json({
            message: 'Se ha producido un error al actualizar el usuario',
            detail: error.message
        });
    }
};