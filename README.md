# Eluvio Q/A RAG Agent Challenge

Your task is to implement a RAG agent which answers questions about Eluvio! You will build a small system that can answer questions about [Eluvio](https://eluv.io/) by scraping publicly available information, indexing it locally, and exposing a lightweight API for querying.  

---

## Project Flow

The system should follow this flow:  

1. **Scrape + Index**  
   - Write an `index.py` script which scrapes or downloads reference data from Eluvio’s public site (https://eluv.io/) and/or other publicly available sources.  
   - Build a local searchable index of that data. You may use a search library of your choice. 
   - Save the index to disk so it can be reused when serving requests.
   - Please upload both the index itself as well as creation script to the repository. 

2. **Run a Local Server**  
   - Implement a `server.py` which loads the index and exposes an HTTP API over `http://localhost:5000`.  
   - The API should accept a question from the user and return an answer generated with the help of your index + a language model.

3. **Ask Questions**  
   - Once the server is running, users can POST a question to the `/ask` endpoint and receive a JSON response. 

---

## 🚀 Example User Flow

```bash
# 1. Build the index
python index.py

# 2. Start the server
python server.py

# 3. Ask a question
curl -X POST "http://localhost:5000/ask" \
     -H "Content-Type: application/json" \
     -d '{"prompt":"What does eluvio do?"}'

# Example response
{
  "response": "Eluvio is a content fabric platform for streaming, storage, and distribution of premium video."
}
