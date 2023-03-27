from "express' import express;
from "mysql2" import createConnection;

const app = express();
const port = 3000;

const connection = createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "banco"
});



