from newspaper import Article
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

urls = [
    "https://theanalyst.com",
    "https://www.bbc.com/sport/football",
    "https://www.goal.com/en"
]

docs=[]

for url in urls:

    print(f"Trying {url}")

    try:

        article = Article(url)

        article.download()

        article.parse()

        txt = article.text

        print(
            "Chars:",
            len(txt)
        )

        if len(txt) > 100:

            docs.append(txt)

    except Exception as e:

        print(
            "FAILED:",
            e
        )

print(
    "Documents:",
    len(docs)
)

if len(docs)==0:

    raise Exception(
        "No documents found"
    )

emb = HuggingFaceEmbeddings(
model_name=
"sentence-transformers/all-MiniLM-L6-v2"
)

db=FAISS.from_texts(
docs,
emb
)

db.save_local(
"vectorstore"
)

print(
"Ingest complete"
)