from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Need OPENAI_API_KEY
load_dotenv()

# model = ChatOpenAI(model='gpt-4')
model = ChatOpenAI(model='gpt-4', temperature=1.8, max_completion_tokens=12)
result = model.invoke("Write a funny joke.")

print(result.content)
