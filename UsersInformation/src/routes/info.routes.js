import { Router } from "express";
import { postUser,getAllUsers, deleteUser, updateUser} from "../controllers/postInfo.controller.js";
import bodyParser from "body-parser";

const router = Router();


router.post('/info',postUser);

router.get('/info',getAllUsers);

router.delete('/info/:id',deleteUser);

router.put('/info/:id',updateUser);


export default router;