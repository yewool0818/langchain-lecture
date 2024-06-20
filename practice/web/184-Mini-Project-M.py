from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document  # Import the Document class

# Sample text
texts = [
    "광대버섯(Amanita phalloides)은 크고 인상적인 후성(위) 자실체(담자과체)를 가지고 있습니다.",
    "큰 자실체를 가진 버섯은 Amanita phalloides입니다. 일부 품종은 모두 흰색입니다.",
    "A. phalloides, 일명 Death Cap은 알려진 모든 버섯 중에서 가장 독성이 강한 버섯 중 하나입니다.",
]

# Custom text loader function
def load_texts(text_list):
    documents = []
    for text in text_list:
        documents.append(Document(page_content=text, metadata={}))
    return documents

# Load the documents
raw_documents = load_texts(texts)

# initialize the text spliiter and embeddings
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
embeddings = OpenAIEmbeddings()

# Split the documents into chunks
chunks = []
for doc in raw_documents:
    chunks.extend(text_splitter.split_text(doc.page_content))

# Embed each chunk
embedded_chunks = embeddings.embed_documents([chunk for chunk in chunks])

# initialize the vector store with embedded chunks
vector_store = Chroma.from_documents(
    [Document(page_content=chunk, metadata={}) for chunk in chunks],
    embeddings
)

#### vector store를 retriever로 !
# def dynamic_search(question):
#     try:
#         k = int(input("원하는 검색 결과의 수를 입력하세요 (1-3): "))
#         if k < 1 or k > 3:
#             raise ValueError("검색 결과의 수는 1에서 3 사이여야 합니다.")
#     except ValueError as e:
#         print(f"잘못된 입력입니다: {e}")
#         return []

#     # Ensure vector_store is properly initialized and accessible
#     return vector_store.similarity_search_with_score(query=question, k=k)

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.5}  
    #score_threshold": 0.5, 0.8 0.9로 조절하여 정답 갯수를 확인
)

def dynamic_search_with_threshold(question):
    """

    Args:
      question:

    Returns:

    """
    # try:
    #     k = int(input("원하는 검색 결과의 수를 입력하세요 (1-3): "))
    #     if k < 1 or k > 3:
    #         raise ValueError("검색 결과의 수는 1에서 3 사이여야 합니다.")
    # except ValueError as e:
    #     print(f"잘못된 입력입니다: {e}")
    #     return []
    
    results = retriever.get_relevant_documents(question)



    return results

# question = "큰 자실체를 가진 순백색 버섯에 대해 알려주세요"
question = "독성에 대해 알려줘"
search_results = dynamic_search_with_threshold(question)
print(search_results)
search_results_sorted = sorted(search_results, key=lambda x:x[1])
print("검색 결과:", search_results_sorted)

for s in search_results_sorted:
    print(f'{s[1]} / {s[0].page_content}')