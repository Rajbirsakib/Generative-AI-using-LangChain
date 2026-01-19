from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Need OPENAI_API_KEY
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

documents = [
    "Jamal Bhuyan is the captain of Bangladesh football team",
    "Shakib and Tamim, two best cricketer",
    "People loves to watch football and cricket both"
]

result = embedding.embed_documents(documents) #it gives vector

print(str(result))
