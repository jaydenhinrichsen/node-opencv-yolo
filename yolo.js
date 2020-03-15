const child_process = require("child_process");
const script = `${__dirname}\\yolo_object_detection\\yolo.py`;
const yolo = image => {
  const inputFilePath = `${__dirname}\\original_images\\${image}`;
  const outputFilePath = `${__dirname}\\detected_images\\${image}`;

  return new Promise((resolve, reject) => {
    const yoloProcess = child_process.spawn(
      "python3",
      [script, inputFilePath, outputFilePath],
      {
        detached: true,
        stdio: "pipe"
      }
    );
    yoloProcess.stderr.on("data", data => console.log(data.toString()));
    yoloProcess.on("close", code => {
      if (code === 0) resolve(outputFilePath);
      else reject();
    });
  });
};

module.exports = yolo;
