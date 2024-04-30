import { MongoClient, ServerApiVersion } from 'mongodb';

const uri = "mongodb+srv://davidsantiagojimenez16:kLxzdcyp34opAz4I@infodb.qcvtdg7.mongodb.net/?retryWrites=true&w=majority&appName=InfoDB";

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function testMongoDBConnection() {
  try {
    await client.connect();
    await client.db("admin").command({ ping: 1 });
    console.log("Connected to MongoDB!");
  } catch (error) {
    console.error("Failed to connect to MongoDB:", error);
  } finally {
    await client.close();
  }
}

testMongoDBConnection();