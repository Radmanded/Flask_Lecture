
from flask import Flask, jsonify

app = Flask(__name__)

# Created to pass in the json payload
tasks = []

# Create an end point
@app.route('/tasks', methods=['GET'])
def get_task():
    return jsonify({'tasks': tasks})

# Filter json data
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
   task = next((t for t in tasks if t['id'] == task_id), None)
   if task is None:
       return jsonify({'error': 'Task Not Found'}), 404
   return jsonify({'task': task})

#Entry point of the application
if __name__ == "__main__":
    app.run(debug=True)
