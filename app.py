from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    data = request.json or {}
    text = data.get("text", "").lower()

    # Simple hardcoded responses for testing
    if "hello" in text:
        reply = "Hello! How can I help you today?"
        return jsonify({"type": "chat", "reply": reply})
    elif "youtube" in text or "play" in text:
        # dummy YouTube response
        results = [{"title": "Test Video", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}]
        return jsonify({"type": "youtube", "items": results})
    else:
        # default reply
        reply = "I heard you: " + text
        return jsonify({"type": "chat", "reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
