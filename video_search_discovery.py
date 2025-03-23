
# set OpenAI api key
import os
os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY"

from llama_index.core import VectorStoreIndex
from llama_index.readers.json import JSONReader

# Load movie metadata for video search
movie_loader = JSONReader().load_data("movie_metadata.json")

# Build an index of the movie metadata
movie_index = VectorStoreIndex.from_documents(movie_loader)

# Create a query engine for video search
movie_query_engine = movie_index.as_query_engine()

# Query for movies about space exploration with philosophical themes
response = movie_query_engine.query("Find movies about space exploration with a philosophical twist.")


print(response)  # Expected output: "Interstellar: A space exploration film with deep philosophical themes."