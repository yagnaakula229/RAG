from langchaincommunity.documentloaders import pyPDFLoader
loader = PyPDFLoader("/workspaces/RAG/data/Langchain.pdf")
docs = loader.load()
print(type(docs))