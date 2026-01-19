from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Need ANTHROPIC_API_KEY / claude
load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke("What is the capital of Bangladesh?")

print(result.content)
