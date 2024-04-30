import { Router } from "express";
import infoUser from "../models/infoUsers.model.js";
import bodyParser from "body-parser";

const router = Router();
var jsonParser = bodyParser.json()

router.post('/info', jsonParser, async(req,res) => {
    try{
        const user = await infoUser.create(req.body);
        res.status(201).json(user);
    } catch (error) {
        console.log(error);
        res.status(500).send(error);
    }
});


router.get('/info', async(req,res) => {
    try {
        const Users = await infoUser.find({});
        res.status(200).json(Users);
    } catch (error) {
        res.status(500).send(error);
    }
});

router.get('/info/:id', async(req,res) => {
    try {
        const { id } = req.params;
        const user = await infoUser.findById(id);
        res.status(201).json(user);
    } catch (error) {
        res.status(500).send(error);
    }
});


export default router;