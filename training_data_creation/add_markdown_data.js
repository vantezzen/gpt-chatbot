const glob = require("glob");
const fs = require("fs");
const path = require("path");
const { writeTrainingData } = require("./utils");

const files = glob.sync(
  path.join(__dirname, "../", "source_data/markdown/**/*.md")
);
console.log(files);

for (let file of files) {
  const data = fs.readFileSync(file, "utf8");
  writeTrainingData(data);

  const paragraphs = data.split("\n\n");

  for (let paragraph of paragraphs) {
    // writeTrainingData(paragraph);
  }
}
