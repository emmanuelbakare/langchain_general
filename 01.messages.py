from dotenv import load_dotenv
import os
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
load_dotenv()
api_key = os.getenv('CLAUDE_API_KEY')

# print(api_key)

llm = ChatAnthropic(api_key=api_key, model="claude-3-5-sonnet-20240620")

System = SystemMessage(content = "output only the answer and do not add any prefix or suffix description")
messages = [
    SystemMessage(content = "output only the answer and do not add any prefix or suffix description"),
    HumanMessage(content = "write a very short poem")
] 

result = llm.invoke(messages)
content = result.content
print(content)
