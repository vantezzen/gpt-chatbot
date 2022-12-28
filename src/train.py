from dotenv import load_dotenv
from OpenAi import OpenAi
from Pinecone import Pinecone
import os
import glob
load_dotenv()

openai = OpenAi()
pinecone = Pinecone()

# Get all the files in the data directory
files = glob.glob('./training_data/*.txt')

# Loop through all the files
for file in files:
  text = open(file, 'r').read()
  embeds = openai.train_embeddings(text)
  pinecone.insert_embed(embeds, text)
  print(f'Inserted {file} into Pinecone')

print('Done')