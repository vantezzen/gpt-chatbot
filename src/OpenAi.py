import os
import openai

class OpenAi:
  def __init__(self):
    openai.api_key = os.getenv('OPENAI_API_KEY')

  def train_embeddings(self, texts):
    embedding = openai.Embedding.create(
      model="text-embedding-ada-002",
      input=texts
    )
    return [record['embedding'] for record in embedding['data']]

  def get_index_query(self, query):
    return openai.Embedding.create(input=query, engine="text-embedding-ada-002")['data'][0]['embedding']

  def complete(self, prompt, max_tokens=255):
    completion = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=max_tokens,
      stop=["\n", " Human:", " AI:"]
    )
    return completion['choices'][0]['text']
    
  def prepare_full_ai_query(self, query, matches):
    finalQuery = """
Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, tell it to the user

===
Context:
"""
    for match in matches:
        finalQuery = f"{finalQuery}\n* {match['metadata']['text']}\n"

    finalQuery = f"{finalQuery}\n===\nQ: {query}\nA:\n"
    return finalQuery
