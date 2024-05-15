# Quality Log Control System

## Introduction
This project aims to develop a robust logging system capable of capturing logs from multiple APIs and providing a powerful query interface to search through these logs based on various filters. The system is designed to be scalable, efficient, and user-friendly, ensuring seamless log ingestion and retrieval.

## Project Structure
The project is divided into two main components:

- Log Ingestor: Captures and stores logs from various APIs.
- Query Interface: Allows users to search and filter logs based on specific criteria.

![current-log](current-log)
## Technologies Used
- Programming Language: Python
- Database: SQLite (for simplicity and ease of use)
- Framework: Flask (for the web interface)
- Front-end: HTML, CSS, JavaScript (for the query interface)
- Logging: Python's logging module

## Log Ingestor 
The log ingestor is responsible for integrating with multiple APIs and capturing logs. Each API logs messages in a standardized format to designated log files.

### Key Features:
- API Integration: Integrated 8 APIs for demonstration, each writing logs to separate files (log1.log, log2.log, etc.).
Standardized Log Format:
json
```
{
    "level": "error", 
    "log_string": "Inside the Search API",
    "timestamp": "2023-09-15T08:00:00Z",    
    "metadata": {
        "source": "log3.log"
    }
}
```
- Configuration: Logging levels and file paths are configurable via environment variables.
- Error Handling: Robust error handling to ensure logging failures do not disrupt API functionality.
- Scalability: Designed to handle high volumes of logs with efficient file I/O operations.

## Query Interface
The query interface provides a user-friendly platform for searching and filtering logs based on various criteria. It supports full-text search and filtering by log level, log string, timestamp, and source.

### Key Features:
- Web Interface: Built using Flask, HTML, CSS, and JavaScript.
- Filters: Users can filter logs by level, log string, timestamp, and source.
- Efficient Search: Optimized queries to ensure quick retrieval of logs.
- Date Range Search: (Bonus) Allows searching within specific date ranges.
- Regular Expressions: (Bonus) Supports regex for advanced search capabilities.
- Combined Filters: (Bonus) Allows combining multiple filters for more precise search results.
- Real-time Ingestion: (Bonus) Supports real-time log ingestion and search.

## Setup and Running the Project
Prerequisites:
- Python 3.8+
- SQLite

### Steps:
1. Clone the Repository:

```
git clone https://github.com/simranquirky/Quality_log_Control
cd Quality_log_Control
```
2. Install Dependencies:
```
pip install -r requirements.txt
```

3. Run the flask app and Query Interface:
```
python app.py
```

6. Access the Query Interface:
Open your browser and navigate to http://127.0.0.1:5000.

## System Design

### Log Ingestor:
- APIs: Simulated APIs that generate logs.
- Logging Module: Captures logs and writes to designated files.
- Configuration: Environment variables for log levels and paths.
- Error Handling: Ensures seamless operation even when logging fails.

### Query Interface:
- Flask App: Serves the web interface.
- SQLite Database: Stores logs for efficient querying.
- Search Engine: Handles full-text search and filtering.
- Frontend: HTML, CSS, and JavaScript for a responsive user experience.

### Features Implemented
- Log ingestion from multiple APIs.
- Standardized log format.
- Configurable logging levels and paths.
- Robust error handling.
- Web-based query interface.
- Filters for level, log string, timestamp, and source.
- Date range search.
- Combined filter capabilities.
- Real-time log ingestion and search.

### Known Issues
- Currently using SQLite for simplicity; may need to switch to a more robust database for larger volumes.
- Frontend can be improved for better user experience.

### Future design Modifications
![updated-log](enhanced-log)

https://excalidraw.com/#json=qbN0jrX070uKx3zlSAnex,Lo8l0SlVgvt41wooMynEPg 
### Conclusion
This project demonstrates a scalable and efficient system for log ingestion and querying, designed to handle high volumes of logs and provide quick search results. The implementation includes advanced features such as date range search, regex support, and combined filters, ensuring a comprehensive solution for quality log control.