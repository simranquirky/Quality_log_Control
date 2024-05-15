import unittest
import requests
import json

class TestQualityLogControl(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"

    def setUp(self):
        # Setup code if needed (e.g., to reset the state of the server)
        pass

    def test_log_ingestion(self):
        log_data = {
            "level": "error",
            "log_string": "This is an error log for ingestion test",
            "timestamp": "2023-09-15T08:00:00Z",
            "metadata": {
                "source": "log1.log"
            }
        }
        response = requests.post(f"{self.BASE_URL}/api/log", json=log_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')

    def test_log_query_by_level(self):
        # Ingest a log to ensure there is something to search
        log_data = {
            "level": "error",
            "log_string": "This is an error log for testing inside Search API",
            "timestamp": "2023-09-15T08:00:00Z",
            "metadata": {
                "source": "log3.log"
            }
        }
        ingest_response = requests.post(f"{self.BASE_URL}/api/log", json=log_data)
        self.assertEqual(ingest_response.status_code, 200)
        self.assertEqual(ingest_response.json()['status'], 'success')

        # Query logs by level
        response = requests.get(f"{self.BASE_URL}/api/logs/search", params={"level": "error"})
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertEqual(response_data['status'], 'success')
        
        logs = response_data['logs']
        self.assertIsInstance(logs, list)
        self.assertGreater(len(logs), 0)
        
        # Check that the logs contain the ingested log
        found = False
        for log in logs:
            # print(log)
            if 'This is an error log for testing inside Search API' in log['log_string']:
                print("ok")
                found = True
                self.assertEqual(log['level'], log_data['level'])
                self.assertEqual(log['timestamp'], log_data['timestamp'])
                self.assertEqual(log['source'], log_data['metadata']['source'])

        self.assertTrue(found, "The ingested log was not found in the search results")

    # def test_log_query_by_string(self):
    #     # Query logs by log_string
    #     response = requests.get(f"{self.BASE_URL}/api/logs/search", params={"log_string": "Search API"})
    #     self.assertEqual(response.status_code, 200)
        
    #     response_data = response.json()
    #     self.assertEqual(response_data['status'], 'success')
        
    #     logs = response_data['logs']
    #     self.assertIsInstance(logs, list)
    #     self.assertGreater(len(logs), 0)
        
    #     # Check that the logs contain the search string
    #     for log in logs:
    #         self.assertIn('Search API', log['log_string'])

    # def test_log_query_by_source(self):
    #     # Query logs by source
    #     response = requests.get(f"{self.BASE_URL}/api/logs/search", params={"source": "log3.log"})
    #     self.assertEqual(response.status_code, 200)
        
    #     response_data = response.json()
    #     self.assertEqual(response_data['status'], 'success')
        
    #     logs = response_data['logs']
    #     self.assertIsInstance(logs, list)
    #     self.assertGreater(len(logs), 0)
        
    #     # Check that the logs contain the source
    #     for log in logs:
    #         self.assertEqual(log['source'], "log3.log")

    # def test_log_query_by_date_range(self):
    #     # Query logs by date range
    #     response = requests.get(f"{self.BASE_URL}/api/logs/search", params={
    #         "start_timestamp": "2023-09-10T00:00:00Z",
    #         "end_timestamp": "2023-09-15T23:59:59Z"
    #     })
    #     self.assertEqual(response.status_code, 200)
        
    #     response_data = response.json()
    #     self.assertEqual(response_data['status'], 'success')
        
    #     logs = response_data['logs']
    #     self.assertIsInstance(logs, list)
    #     self.assertGreater(len(logs), 0)
        
    #     # Check that the logs fall within the date range
    #     for log in logs:
    #         self.assertGreaterEqual(log['timestamp'], "2023-09-10T00:00:00Z")
    #         self.assertLessEqual(log['timestamp'], "2023-09-15T23:59:59Z")

    # def tearDown(self):
    #     # Teardown code if needed (e.g., to clean up the server state)
    #     pass

if __name__ == "__main__":
    unittest.main()
