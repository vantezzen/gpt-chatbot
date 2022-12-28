import pinecone
import random
import string
import os

class Pinecone:
  def __init__(self):
    self.api_key = os.getenv('PINECONE_API_KEY')
    pinecone.init(
        api_key=self.api_key,
        environment="us-west1-gcp"
    )
    self.index = pinecone.Index('openai')

  def get_random_id(self):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(12))

  def insert_embed(self, embeds, text):
    self.prepare_index(embeds)
    meta = [{'text': text}]
    to_upsert = zip([self.get_random_id()], embeds, meta)
    self.index.upsert(vectors=list(to_upsert))

  def prepare_index(self, embeds):
    if 'openai' not in pinecone.list_indexes():
        pinecone.create_index('openai', dimension=len(embeds[0]))
    self.index = pinecone.Index('openai')

  def search(self, query, k=10):
    return self.index.query([query], top_k=k, include_metadata=True)['matches']

