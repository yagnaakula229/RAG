# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("data/cricket.txt")

# documents = loader.load()

# print(documents)
# # Output:
# # [Document(page_content='This is an example text file.\nIt contains multiple lines of text.\nThis is the third line.', metadata={})]

# print(type(documents))


from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

prompt = PromptTemplate(
    template='Write a summary for the following text:\n{poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({
    'poem': docs[0].page_content
})

print("\nSUMMARY:\n")

print(result)