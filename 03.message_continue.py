from dotenv import load_dotenv
import os
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
load_dotenv()
api_key = os.getenv('CLAUDE_API_KEY')

# print(api_key)
def write_to_file(content,filename, extension="txt"):
    if len(content) > 0:
        with open(f"{filename}.{extension}",'w') as file:
            file.write(content)


llm = ChatAnthropic(api_key=api_key, model="claude-3-5-sonnet-20240620")

messages = [
    SystemMessage(content = "output only the answer and do not add any prefix or suffix description. start the output with [output-start] and end it with [output-end]"),
] 

content = ""
full_content=""

while True:
    if content.strip().endswith("[output-end]") or len(content) == 0:
        user_prompt = input("Question>> ")
    else:
        user_prompt = "continue from where you stopped"
        print("please hold while we generate more output...")

    if user_prompt.lower() in ("exit","quit"):
        break

    messages.append(HumanMessage(content = user_prompt))
    result = llm.invoke(messages)
    content = result.content
    full_content += content
    print(content)
    messages.append(AIMessage(content = result.content))

#remove the [output-start] and [output-end] part of the finanl output
clean_content = full_content.replace("[output-start]", "").replace("[output-end]", "").strip()
print(clean_content)
print("="*50)

# get a filename to write the output to
filename = input("specify a filename to write to >> ")
#write the content to the specified output file.
write_to_file(clean_content,filename)





