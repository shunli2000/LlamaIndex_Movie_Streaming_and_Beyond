import os
from llama_index.core import VectorStoreIndex
from llama_index.readers.json import JSONReader

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY"

# Load user reviews and watch history from JSON files
reviews_loader = JSONReader().load_data("user_reviews.json")
history_loader = JSONReader().load_data("user_watch_history.json")

# Build indices for both datasets
review_index = VectorStoreIndex.from_documents(reviews_loader)
history_index = VectorStoreIndex.from_documents(history_loader)

# Create a query engine for personalized content grouping
history_query_engine = history_index.as_query_engine()
review_query_engine = review_index.as_query_engine()

# Query for uplifting movie suggestions based on reviews and watch history
history_context = history_query_engine.query("What movies has user 12345 watched recently?")
playlist_response = review_query_engine.query(f"Create a playlist of uplifting movies based on: {history_context}")
print(playlist_response)
# Expected output: "The Pursuit of Happyness, Forrest Gump"