import sys
from dotenv import load_dotenv
from OpenAi import OpenAi
from Pinecone import Pinecone

prompt = sys.argv[1]
print("Prompt: " + prompt)
load_dotenv()

openai = OpenAi()
pinecone = Pinecone()

index_query = openai.get_index_query(prompt)
results = pinecone.search(index_query)
print("Results: " + str(results))

finalQuery = pinecone.prepare_full_ai_query(prompt, results)
print("Final Query: " + finalQuery)

response = openai.complete(finalQuery)
print("Response: " + response)