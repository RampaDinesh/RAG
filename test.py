from langchain_ollama import ChatOllama

model = ChatOllama(model="mistral",
                   temperature=0.5)

result=model.invoke("explain two pointer approach with example")
print(result.content)