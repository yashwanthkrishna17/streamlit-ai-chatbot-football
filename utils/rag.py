from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

emb=HuggingFaceEmbeddings(
model_name=
"sentence-transformers/all-MiniLM-L6-v2"
)

db=FAISS.load_local(
"vectorstore",
emb,
allow_dangerous_deserialization=True
)

def search(q):

    return db.similarity_search(
        q,
        k=3
    )