
from flask import Flask, request, jsonify
import os
from FileUtils import FileHandler

DATA_FILE = 'records.csv'

def initialize_app(data_manager=None):
    app = Flask(__name__)
    app.data_manager = data_manager or FileHandler(DATA_FILE)

    @app.route("/add_entry", methods=['POST'])
    def add_entry():
        try:
            entry = request.json.get('entry')
            if not entry:
                return jsonify({"error": "No entry provided"}), 400
            if app.data_manager.entry_exists(entry):
                return jsonify({"error": "Entry already exists"}), 409
            app.data_manager.save_entry(entry)
            return jsonify({"message": f"Entry '{entry}' added successfully"}), 201
        except Exception as err:
            return jsonify({"error": f"Something went wrong: {str(err)}"}), 500

    @app.route("/fetch_entries", methods=['GET'])
    def fetch_entries():
        try:
            entries = app.data_manager.load_entries()
            return jsonify({"data": entries}), 200
        except Exception as err:
            return jsonify({"error": f"Failed to retrieve entries: {str(err)}"}), 500

    return app

if __name__ == '__main__':
    flask_app = initialize_app()
    flask_app.run(debug=True, port=8080)
