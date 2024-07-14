import os
import qdrant_client

os.environ["REPLICATE_API_TOKEN"] = "r8_aveecybGemnCNrospREsYagtccJ8zOK1gAUBJ"

from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from transformers import AutoTokenizer


llama2_7b_chat = "meta/meta-llama-3-70b-instruct"

Settings.llm = Replicate(
    model=llama2_7b_chat,
    temperature=0.01,
    additional_kwargs={"top_p": 1, "max_new_tokens": 10000},
)

# set tokenizer to match LLM
Settings.tokenizer = AutoTokenizer.from_pretrained(
    "NousResearch/Llama-2-7b-chat-hf"
)

# set the embed model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

client2 = qdrant_client.QdrantClient(
    url="https://22a234ef-2851-4ad1-80bc-ac28df1cbdf9.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key=os.environ["QDRANT_API_KEY"]
)


documents = SimpleDirectoryReader("~/AutonomyToolkit/src/backend/services/LLMRAG").load_data()
vector_store = QdrantVectorStore(client=client2, collection_name="AutonomyToolkit")
index = VectorStoreIndex.from_documents(
    documents,
)

index2 = VectorStoreIndex.from_vector_store(vector_store=vector_store)

query_engine = index.as_query_engine()
query_engine.query("what are these files about?")
