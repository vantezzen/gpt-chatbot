const fs = require("fs");
const path = require("path");

const getRandomId = () => (Math.random() + 1).toString(36).substring(7);

module.exports.writeTrainingData = (data) => {
  const id = getRandomId();
  const outputFile = path.join(__dirname, "../", "training_data", `${id}.txt`);

  fs.writeFileSync(outputFile, data);
};
