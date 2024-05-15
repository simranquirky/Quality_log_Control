import logging
from flask import Flask, request, jsonify, g, render_template
from log_ingestor import LogIngestor
from log_query_interface import LogQueryInterface

app = Flask(__name__)

log_paths = ['log1.log', 'log2.log', 'log3.log']
log_ingestor = LogIngestor(log_paths)
db_path = 'logs.db'

# Setup logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addlog')
def add_log():
    return render_template('loginsert.html')

def get_log_query_interface():
    if 'log_query_interface' not in g:
        g.log_query_interface = LogQueryInterface(db_path)
    return g.log_query_interface

@app.route('/api/log', methods=['POST'])
def ingest_log():
    log_data = request.get_json()
    logging.debug(f"Received log data: {log_data}")
    if not log_data:
        logging.error("Invalid log data")
        return jsonify({"status": "error", "message": "Invalid log data"}), 400
    log_ingestor.ingest_log(log_data)
    get_log_query_interface().insert_log(log_data)
    return jsonify({"status": "success", "message": "Log ingested successfully."})

@app.route('/api/logs/search', methods=['GET'])
def search_logs():
    filters = {
        "level": request.args.get('level'),
        "log_string": request.args.get('log_string'),
        "start_timestamp": request.args.get('start_timestamp'),
        "end_timestamp": request.args.get('end_timestamp'),
        "source": request.args.get('source')
    }
    logging.debug(f"Received search filters: {filters}")
    logs = get_log_query_interface().search_logs(filters)
    logging.debug(f"Search results: {logs}")

    # Convert list of lists to list of dictionaries
    logs_with_keys = []
    for log in logs:
        log_dict = {
            "id": log[0],
            "level": log[1],
            "log_string": log[2],
            "timestamp": log[3],
            "metadata": {
                "source": log[4]
            }
        }
        logs_with_keys.append(log_dict)

    return jsonify({"status": "success", "logs": logs_with_keys})


if __name__ == '__main__':
    app.run(debug=True)
