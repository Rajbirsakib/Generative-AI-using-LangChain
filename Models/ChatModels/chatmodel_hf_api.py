from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Need HUGGINGFACEHUB_ACCESS_TOKEN
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    max_new_tokens=50,
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Bangladesh?")

print(result.content)
