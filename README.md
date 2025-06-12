# Curiate Solutions - SEO Text Analyzer

A web application that analyzes text for SEO optimization, providing readability scores and keyword suggestions.

## Overview

Curiate Solutions is a Flask-based web application that helps users optimize their content for search engines. The application:

1. Analyzes text for readability using the Flesch Reading Ease score
2. Extracts relevant keywords using the TextRazor API
3. Allows users to insert suggested keywords into their text

## Features

- Text readability analysis
- Keyword extraction and suggestion
- Interactive keyword insertion
- Real-time text preview

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: TextRazor for entity extraction

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package manager)
- TextRazor API key (get one from [TextRazor](https://www.textrazor.com/))

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/curiate-solutions.git
   cd curiate-solutions
   ```

2. Install dependencies:
   ```
   pip install flask flask-cors requests textstat
   ```

3. Set up your TextRazor API key:
   - Create a `.env` file in the project root
   - Add your API key: `API_KEY=your_textrazor_api_key`
   - Or modify the `API_KEY` variable in `app.py`

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter your text in the provided textarea and click "Analyze SEO"

4. Review the readability score and suggested keywords

5. Click on any keyword to insert it into your text

## API Endpoints

### `/analyze` (POST)

Analyzes the provided text for readability and extracts keywords.

**Request Parameters:**
- `text`: The text to analyze (form data)

**Response:**
```json
{
  "readability": 75.2,
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

### `/insert` (POST)

Inserts a keyword into the provided text.

**Request Body:**
```json
{
  "text": "Your original text.",
  "keyword": "Keyword to insert"
}
```

**Response:**
```json
{
  "updated_text": "Your original text. Keyword to insert"
}
```

## Error Handling

The application provides error messages for:
- Empty text submissions
- API failures
- Keyword insertion issues

## License

[MIT License](LICENSE)

## Documentation

### User Guide

For detailed usage instructions, see the [User Guide](docs/USER_GUIDE.md).

### API Documentation

For API details, see the [API Documentation](docs/API.md).

### System Diagrams

To understand the system architecture and workflow, see the [Diagrams](docs/DIAGRAMS.md) which include:
- Workflow Diagram - Shows data flow through the system
- Sequence Diagram - Shows time-ordered interactions between components
- Component Diagram - Shows structural organization of the system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
