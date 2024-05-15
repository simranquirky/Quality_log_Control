import sqlite3

class LogQueryInterface:
    def __init__(self, db_path):
        self.db_path = db_path
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self.get_connection() as conn:
            query = '''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                level TEXT,
                log_string TEXT,
                timestamp TEXT,
                source TEXT
            )
            '''
            conn.execute(query)
            conn.commit()

    def insert_log(self, log_data):
        with self.get_connection() as conn:
            query = '''
            INSERT INTO logs (level, log_string, timestamp, source)
            VALUES (?, ?, ?, ?)
            '''
            conn.execute(query, (
                log_data['level'],
                log_data['log_string'],
                log_data['timestamp'],
                log_data['metadata']['source']
            ))
            conn.commit()

    def search_logs(self, filters):
        with self.get_connection() as conn:
            query = 'SELECT * FROM logs WHERE 1=1'
            params = []

            if 'level' in filters and filters['level']:
                query += ' AND level = ?'
                params.append(filters['level'])
            
            if 'log_string' in filters and filters['log_string']:
                query += ' AND log_string LIKE ?'
                params.append(f"%{filters['log_string']}%")
            
            if 'start_timestamp' in filters and filters['start_timestamp']:
                query += ' AND timestamp >= ?'
                params.append(filters['start_timestamp'])
            
            if 'end_timestamp' in filters and filters['end_timestamp']:
                query += ' AND timestamp <= ?'
                params.append(filters['end_timestamp'])
            
            if 'source' in filters and filters['source']:
                query += ' AND source = ?'
                params.append(filters['source'])
            
            cursor = conn.execute(query, params)
            logs = cursor.fetchall()
            return logs
