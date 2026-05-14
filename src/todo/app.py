from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    todo = {
        "id": len(todos) + 1,
        "title": data["title"],
        "done": False
    }

    todos.append(todo)

    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            return jsonify(todo)

    return jsonify({"error": "Todo not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    
