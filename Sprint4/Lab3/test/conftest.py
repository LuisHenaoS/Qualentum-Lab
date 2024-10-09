import tempfile
import os, csv
import pytest
from server import create_app, FileUtils

@pytest.fixture
def client():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as tmp_file:
        file_name = tmp_file.name
        print(f"Temporary file created at: {file_name}")


    app = create_app()
    app.config['TESTING'] = True
    app.file_utils = FileUtils(file_name)

    with app.test_client() as client:
        app.file_utils.create_csv_file()
        yield client

    os.remove(file_name)