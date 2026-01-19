from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Need OPENAI_API_KEY
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

result = embedding.embed_query("I love to playing cricket and football.") #it gives vector

print(str(result))
