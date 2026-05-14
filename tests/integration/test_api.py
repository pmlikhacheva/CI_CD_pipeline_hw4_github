from src.todo.app import app

def test_create_todo():
    client = app.test_client()

    response = client.post(
        "/todos",
        json={"title": "Learn GitLab CI"}
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Learn GitLab CI"
    assert data["done"] is False


def test_get_todos():
    client = app.test_client()

    response = client.get("/todos")

    assert response.status_code == 200
    assert isinstance(response.json, list)
    