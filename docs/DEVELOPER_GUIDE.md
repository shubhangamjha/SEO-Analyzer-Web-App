# Curiate Solutions - Developer Guide

This guide provides information for developers who want to understand, modify, or extend the Curiate Solutions SEO Text Analyzer.

## Project Structure

```
curiate-solutions/
├── app.py                 # Main Flask application
├── static/
│   └── app.js             # Client-side JavaScript
├── templates/
│   └── index.html         # HTML template
├── docs/                  # Documentation
│   ├── API.md             # API documentation
│   ├── USER_GUIDE.md      # User guide
│   └── DEVELOPER_GUIDE.md # This file
└── README.md              # Project overview
```

## Technology Stack

- **Backend**: Python 3.6+ with Flask
- **Frontend**: HTML, CSS, and vanilla JavaScript
- **APIs**: TextRazor for entity extraction
- **Libraries**: 
  - `textstat` for readability analysis
  - `flask-cors` for handling CORS
  - `requests` for API calls

## Code Overview

### Backend (app.py)

The backend is a Flask application with the following components:

1. **Routes**:
   - `/` - Serves the main page
   - `/analyze` - Analyzes text for readability and keywords
   - `/insert` - Inserts keywords into text

2. **Key Functions**:
   - `analyze()` - Processes text using textstat and TextRazor API
   - `insert_keyword()` - Intelligently inserts keywords into text

3. **External API Integration**:
   - TextRazor API for entity extraction and keyword identification

### Frontend (app.js)

The frontend JavaScript handles:

1. **User Interaction**:
   - Form submission
   - Displaying results
   - Keyword insertion

2. **API Communication**:
   - Fetch requests to the backend endpoints
   - JSON parsing and error handling

3. **DOM Manipulation**:
   - Updating the UI with analysis results
   - Creating keyword buttons dynamically

## Development Workflow

### Setting Up Development Environment

1. Clone the repository
2. Install dependencies: `pip install flask flask-cors requests textstat`
3. Set up your TextRazor API key in `.env` or directly in `app.py`
4. Run the application: `python app.py`

### Making Changes

#### Backend Changes

1. Modify the Flask routes or functions in `app.py`
2. Test your changes by running the application and using the API endpoints
3. Add appropriate error handling and logging

#### Frontend Changes

1. Modify the JavaScript in `static/app.js`
2. Update the HTML template in `templates/index.html` if needed
3. Test your changes in the browser

### Adding New Features

To add new features:

1. **New Analysis Type**:
   - Add a new function in `app.py`
   - Create a new endpoint or extend existing ones
   - Update the frontend to display the new analysis results

2. **New UI Components**:
   - Add HTML elements to `templates/index.html`
   - Add JavaScript to handle the new components in `static/app.js`

## API Integration

### TextRazor API

The application uses TextRazor for entity extraction:

```python
payload = {
  "apiKey": API_KEY,
  "text": text,
  "extractors": "entities",
  "cleanup.mode": "cleanHTML"
}
resp = requests.post("https://api.textrazor.com/", data=payload)
```

To modify or extend the API integration:

1. Review the [TextRazor API documentation](https://www.textrazor.com/docs/rest)
2. Update the payload parameters to use different extractors or options
3. Process the response data as needed

## Testing

Currently, the project doesn't have automated tests. To add testing:

1. Create a `tests` directory
2. Add unit tests for backend functions using `pytest` or `unittest`
3. Add frontend tests using a framework like Jest

Example test structure:

```
tests/
├── test_app.py         # Backend tests
└── test_frontend.js    # Frontend tests
```

## Deployment

To deploy the application:

1. Set `debug=False` in `app.py`
2. Use a WSGI server like Gunicorn: `gunicorn app:app`
3. Consider using a reverse proxy like Nginx
4. Set environment variables for API keys instead of hardcoding them

## Contributing

When contributing to this project:

1. Create a new branch for your feature or bugfix
2. Follow the existing code style
3. Add appropriate documentation
4. Test your changes thoroughly
5. Submit a pull request with a clear description of your changes

## Extending the Application

Ideas for extending the application:

1. **Additional Analysis Types**:
   - Sentiment analysis
   - Grammar checking
   - Keyword density analysis

2. **User Experience Improvements**:
   - Save analysis history
   - Export results to PDF or other formats
   - Batch processing of multiple texts

3. **Integration with Other Tools**:
   - Google Search Console integration
   - WordPress plugin
   - Browser extension