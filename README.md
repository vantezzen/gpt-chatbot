# GPT Chatbot

This repository allows preparing data for training a GPT-3 model, training the model and run queries using a CLI.

## Setup

Requirements:

- Python 3.8
- NodeJS 18

Dependencies:

- `pip install -r requirements.txt`
- `npm install`

## Prepare data

### Markdown files

- Add your markdown files in the `source_data/markdown` folder
  - You can also use subdirectories
- Run "npm run add-markdown-data"

## Train model

- Run "python3 src/train.py"

## Run queries

- Run `python3 src/query.py "your query here"`
