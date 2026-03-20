from langchain_ollama import ChatOllama

model = ChatOllama(model="mistral",
                   temperature=0.5)

result=model.invoke("about elon musk in 10 words")
print(result.content)