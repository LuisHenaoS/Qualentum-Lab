import os
import csv

class FileUtils:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_data(self) -> str:
        if not os.path.isfile(self.file_name):
            return ""
        with open(self.file_name, mode="r", newline="") as file:
            return file.read()

    def create_csv_file(self) -> None:
        #if not os.path.isfile(self.file_name):
            with open(self.file_name, mode="w", newline="") as file:
                pass

    def write_data(self, data: str) -> None:
        self.create_csv_file()
        with open(self.file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([data])

    def data_exists(self, data: str) -> bool:
        lines = self.read_data().splitlines()
        for line in lines:
            if line.strip() == data:
                return True
        return False

    def replace_data(self, data: str, new_data: str) -> None:
        lines = self.read_data().splitlines()
        updated_lines = []

        for line in lines:
            if line.strip() == data:
                updated_line = new_data.strip()
            else:
                updated_line = line.strip()

            if updated_line:
                updated_lines.append(updated_line)

        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            for updated_line in updated_lines:
                writer.writerow([updated_line])
