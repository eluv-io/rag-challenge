# Eluvio Q/A RAG Agent Challenge

## Instructions

Please implement a RAG agent which answers questions about Eluvio. You may use any publicly available information, but a great starting point would be to use our website: https://eluv.io/.

You may use the starter code which will help you run a local http server which users may call to talk with the agent and get back responses. See the provided examples below. 

You are free to use whatever language you are most comfortable with and you are not required to use the starter code. 

## Running your code

Please provide a README.md which clearly explains how to scrape and/or index the reference data as well as run the local server. Please follow the provided example template.

### Example

1. `python index.py` - scrapes https://eluv.io/ and builds a local index file
2. `python server.py` - starts an http server running on `http://localhost:5000`
3. `curl -X POST "http://localhost:5000/ask" -d '{"prompt":"What does eluvio do?"}'
{"response":"Eluvio does..."}

## Indexing/Scraping

Please implement a single 

### Examples

