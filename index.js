const fs = require("fs");
const path = require("path");

const yolo = require("./yolo");

const express = require("express");
const app = express();
const server = require("http").createServer();
server.on("request", app);

app.use(require("body-parser").json());
app.use(require("body-parser").urlencoded({ extended: false }));

const PATH_TO_ORIGINAL_IMAGES = "original_images";
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});
app.get("/images", (req, res) => {
  fs.readdir(`${__dirname}\\${PATH_TO_ORIGINAL_IMAGES}`, (err, images) => {
    if (err) console.log(err);
    res.json(images);
    res.status(200);
  });
});

app.get("/images/:image", (req, res) => {
  res.sendFile(`${__dirname}/${PATH_TO_ORIGINAL_IMAGES}/${req.params.image}`);
});

app.get("/detect/:image", async (req, res) => {
  try {
    let pathToDetectedImage = await yolo(req.params.image);
    res.sendFile(pathToDetectedImage);
  } catch (error) {
    console.log(error);
  }
});
server.listen(5000, console.log("Yolo server listening on port 5000"));
