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

  def complete(self, prompt, max_tokens=100):
    completion = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=max_tokens,
      temperature=0.9,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=["\n", " Human:", " AI:"]
    )
    return completion['choices'][0]['text']
