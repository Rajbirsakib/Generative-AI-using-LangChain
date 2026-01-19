from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# needs GOOGLE_API_KEY
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

documents = [
    "Shakib Al Hasan is a Bangladeshi cricketer known for his all-round performance and match-winning abilities.",
    "Tamim Iqbal is one of Bangladesh's most successful opening batsmen, known for his consistency and aggressive stroke play.",
    "Mashrafe Bin Mortaza is a former Bangladeshi captain famous for his leadership and contribution to Bangladesh's rise in international cricket.",
    "Mushfiqur Rahim is known for his determined batting and reliability as a wicketkeeper-batsman.",
    "Mustafizur Rahman is a Bangladeshi fast bowler famous for his deceptive cutters and death-over bowling."
]

query = "tell me something about Shakib Al Hasan"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("Query:", query)
print(documents[index])
print("Similarity score:", score)
