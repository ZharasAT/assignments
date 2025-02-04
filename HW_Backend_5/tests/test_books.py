import requests

def test_update_book():
    # Добавляем новую книгу для редактирования
    data = {
        "title": "Original Title",
        "author": "Original Author",
        "year": 2000,
        "total_pages": 300,
        "genre": "Original Genre"
    }
    response = requests.post("http://localhost:8000/books/new", data=data, allow_redirects=False)
    assert response.status_code == 303

    # Предполагаем, что новая книга получила ID 6
    update_data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "year": 2021,
        "total_pages": 350,
        "genre": "Updated Genre"
    }
    response = requests.post("http://localhost:8000/books/6/edit", data=update_data, allow_redirects=False)
    assert response.status_code == 303

    # Проверяем, что изменения применились
    response = requests.get("http://localhost:8000/books/6")
    assert "Updated Title" in response.text
    assert "Updated Author" in response.text
    assert "2021" in response.text
    assert "350" in response.text
    assert "Updated Genre" in response.text

def test_delete_book():
    # Добавляем книгу для удаления
    data = {
        "title": "Book to Delete",
        "author": "Author",
        "year": 1999,
        "total_pages": 250,
        "genre": "Test Genre"
    }
    response = requests.post("http://localhost:8000/books/new", data=data, allow_redirects=False)
    assert response.status_code == 303

    # Предполагаем, что эта книга получила ID 7
    response = requests.post("http://localhost:8000/books/7/delete", allow_redirects=False)
    assert response.status_code == 303

    # Проверяем, что книга удалена
    response = requests.get("http://localhost:8000/books/7")
    assert response.status_code == 404