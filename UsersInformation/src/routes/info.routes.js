import { Router } from "express";
import infoUser from "../models/infoUsers.model.js";
import { postUser,getAllUsers, deleteUser, updateUser} from "../controllers/postInfo.controller.js";
import bodyParser from "body-parser";

const router = Router();
var jsonParser = bodyParser.json()


router.post('/info',postUser);

router.get('/info',getAllUsers);

router.delete('/info/:id',deleteUser);

router.put('/info/:id',updateUser);


export default router;