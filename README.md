# Eluvio Q/A RAG Agent Challenge

Your task is to implement a RAG agent which answers questions about Eluvio! You will build a small system that can answer questions about [Eluvio](https://eluv.io/) by scraping publicly available information, indexing it locally, and exposing a lightweight API for querying.

---

## Project Flow

The system should follow this flow:  

*Note*: you may use any language of your choice, but examples and starter code are provided in python. 

1. **Scrape + Index**  
   - Write an `index.py` script which scrapes or downloads reference data from Eluvio’s public site (https://eluv.io/) and/or other publicly available sources.  
   - Build a local searchable index of that data. You may use a search library of your choice. 
   - Save the index to disk so it can be reused when serving requests.
   - Please upload both the index itself as well as creation script to the repository. 

2. **Run a Local Server**  
   - Implement a `server.py` which loads the index and exposes an HTTP API over `http://localhost:5000`.  
   - The API should accept a question from the user and return an answer generated with the help of your index + a language model.
   - We have provided starter code for running an API via Flask.

3. **Ask Questions**  
   - Once the server is running, users can POST a question to the `/ask` endpoint and receive a JSON response. 

---

## Example User Flow

Please follow the flow below as closely as possible.

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Build the index
python index.py

# 3. Start the server
python server.py

# 4. Ask a question
curl -X POST "http://localhost:5000/ask" \
     -H "Content-Type: application/json" \
     -d '{"prompt":"What does eluvio do?"}'

# Example response
{
  "response": "Eluvio offers a unique platform for streaming, storage, and distribution of video over the internet that is simpler and more cost effective than traditional pipelines."
}
```

---

## Running an LLM

Please use Ollama [https://ollama.com/] to host your LLM. For fairness, please use either of the following models: `llama3.2:3b`, `llama3.2:1b`. These models are small and should be able to run on a laptop CPU. 

## Evaluation

This project is intentionally open ended. You are free to use whatever strategies you can come up with to generate the best responses possible! Please explain your strategy in a README.md, and feel free to write about other things you tried. Your submission will be assessed by the quality of your agent's responses as well as the writeup of your strategy.
