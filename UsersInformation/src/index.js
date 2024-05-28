import express from 'express';
import {PORT} from './config.js';
import userRoutes from './routes/info.routes.js';
import mongoose from 'mongoose';
const app = express();

app.use(express.json());
app.use(userRoutes);



mongoose.connect('mongodb+srv://davidsantiagojimenez16:kLxzdcyp34opAz4I@infodb.qcvtdg7.mongodb.net/?retryWrites=true&w=majority&appName=InfoDB')
  .then(() => {
    console.log("Connected to MongoDB!");
    app.listen(PORT, () => console.log('Server running on port ' + PORT));
  })
  .catch(() => {
    console.error("Failed to connect to MongoDB!");
  });