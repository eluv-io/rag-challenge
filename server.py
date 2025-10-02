
from flask import Flask, request, jsonify

app = Flask(__name__)

def ask_agent(prompt: str) -> str:
    """
    Handler for returning a response from the agent.

    TODO: YOUR CODE HERE
    """

    return f"You asked: '{prompt}'. This is a mock response."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response_text = ask_agent(prompt)

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
