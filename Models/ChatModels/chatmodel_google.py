from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Need GOOGLE_API_KEY
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
result = model.invoke('What is the capital of Bangladesh?')

print(result.content)
