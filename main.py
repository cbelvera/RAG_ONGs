from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import pipeline
from langchain.prompts import PromptTemplate
import yaml

# Load configuration from config.yml
with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Step 1: Load multilingual embedding model
embedding = HuggingFaceEmbeddings(
    model_name=config["embedding"]["name"]
)

# Step 2: Load FAISS vector index from local storage
vectorstore = FAISS.load_local(
    folder_path="faiss_index",
    embeddings=embedding,
    allow_dangerous_deserialization=True,
)

# Step 3: Create retriever from vectorstore (top 3 docs)
retriever = vectorstore.as_retriever(search_kwargs={"k": config["retriever"]["k"]})

# Step 4: Load language model and tokenizer pipeline (GPT2 example)
model_config = config["model"]
hf_pipe = pipeline(
    task=model_config["task"],
    model=model_config["name"],
    tokenizer=model_config["name"],
    max_new_tokens=model_config["max_new_tokens"],
    temperature=model_config["temperature"],
    do_sample=model_config["do_sample"],
)

llm = HuggingFacePipeline(pipeline=hf_pipe)

# Step 5: Define your custom prompt template
prompt_template = config["prompt_template"]

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)

# Step 6: Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt},
)

# Step 7: Ask your question!
#query = config["query"]
query = input("❓ Introduce tu pregunta: ")

response = qa_chain({"query": query})

# Step 8: Print the results
print("🔍 Pregunta:", query)
print("🧠 Respuesta:", response["result"])
print("\n📄 Documentos usados:")
for doc in response["source_documents"]:
    print("-", doc.metadata.get("source", "desconocido"))
