# set OpenAI api key
import os
os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY"


from llama_index import JSONReader, VectorStoreIndex

# Load advertising data and user preferences from JSON files
ad_loader = JSONReader().load_data("ad_data.json")
user_loader = JSONReader().load_data("user_preferences.json")

# Build indices for both datasets
ad_index = VectorStoreIndex.from_documents(ad_loader)
user_index = VectorStoreIndex.from_documents(user_loader)

# Create a query engine for ad targeting
user_query_engine = user_index.as_query_engine()
ad_query_engine = ad_index.as_query_engine()

# Query for user-specific ad targeting based on preferences
user_context = user_query_engine.query("What genres does user 12345 prefer?")
ad_response = ad_query_engine.query(f"Select ads for genres: {user_context}")

print(ad_response)  # Expected output: "Movie Trailer: Avengers (Target: action, sci-fi)"