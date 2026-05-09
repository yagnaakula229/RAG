from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
#syntax for directory loader
# loader = DirectoryLoader(path, glob=pattern, loader_cls=LoaderClass)

loader = DirectoryLoader("/workspaces/RAG/data", glob="**/*.txt",loader_cls=TextLoader)
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)