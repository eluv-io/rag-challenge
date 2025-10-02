# Eluvio Q/A RAG Challenge

Your task is to implement a lightweight RAG agent which answers questions about Eluvio! You will scrape publicly available information (our homepage for example https://eluv.io/), index it locally, and expose your agent through a local API.

---

## Project Flow  

**Note**: you may use any language of your choice, but the provided examples and starter code use python. 

1. **Scrape + Index**  
   - Write an `index.py` script which scrapes or downloads reference data from Eluvio’s public site (https://eluv.io/) and/or other publicly available sources.  
   - The script should also build a local searchable index of that data. You may use any search library of your choice. 
   - Save the index to disk so it can be reused when serving requests.
   - Please upload both the index itself as well as the creation script to your github repository.

2. **Run a Local Server**  
   - Create a `server.py` which exposes an HTTP API for users to query over `http://localhost:5000`.
   - We have provided starter code for running an API via Flask. You may use this to save time so you can focus on your agent!
   - The API should accept a question from the user and return an answer generated with the help of your index + language model.

3. **Ask Questions**  
   - Once the server is running, users can POST a question to the `/ask` endpoint and receive a JSON response.

---

## Example User Flow

Please implement the flow below as closely as possible.

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Scrape data and build the local index
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

## Running the LLM

Please use Ollama [https://ollama.com/] to host your LLM. For fairness, use either of the following models: `llama3.2:3b`, `llama3.2:1b`. These models are small and should be able to run on a laptop CPU. We will use ollama to evaluate your agent so you can assume Ollama is already running on the user's `http://localhost:11434`.

## Evaluation

This project is intentionally open ended. You are free to use whatever strategies you can come up with to generate the best responses possible! Please explain your strategy in a README.md, and feel free to write about other things you may have tried or challenges you ran into. Your submission will be assessed by the quality of your agent's responses as well as the writeup of your strategy.

You may include example questions and responses from your agent in your writeup to showcase some examples you are particularly proud of.
