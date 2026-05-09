from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("/workspaces/RAG/document_loaders/employees_large_dataset.csv")

docs = loader.load()

print(len(docs))
print(type(docs))

print(docs[:5]) # prints 5 rows of the CSV file as documents

print(docs[0].page_content[:100])
print(docs[0].metadata)