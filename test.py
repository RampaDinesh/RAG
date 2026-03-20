from langchain_ollama import ChatOllama

model = ChatOllama(model="mistral",
                   temperature=0.5)

result=model.invoke("explain two pointer approaxch with example")
print(result.content)