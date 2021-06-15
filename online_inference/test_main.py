from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)


def test_read_main():
    request_data = [35.0, 1.0, 1.0, 122.0, 192.0, 0.0, 1.0, 174.0, 0.0, 0.0, 2.0, 0.0, 2.0, 1.0]
    request_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    i = 0
    response = client.get(
        "http://127.0.0.1:8000/predict/",
        json={"data": [request_data], "features": request_features, "id_": i},
    )
    assert response.status_code == 200
    assert response.json() == '{"id": 0, "isHealty": 1}'



if __name__ == "__main__":
    test_read_main()