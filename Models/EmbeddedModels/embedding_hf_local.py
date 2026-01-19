from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Jamal Bhuyan is the captain of Bangladesh football team",
    "Shakib and Tamim, two best cricketer",
    "People loves to watch football and cricket both"
]

result = embedding.embed_documents(documents) #it gives vector

print(str(result))
