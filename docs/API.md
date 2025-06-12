# Curiate Solutions API Documentation

This document provides detailed information about the API endpoints available in the Curiate Solutions SEO Text Analyzer.

## Base URL

When running locally, the base URL is:
```
http://localhost:5000
```

## Endpoints

### 1. Analyze Text

Analyzes the provided text for readability and extracts keywords.

**URL**: `/analyze`

**Method**: `POST`

**Content-Type**: `application/x-www-form-urlencoded`

**Request Parameters**:

| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| text      | string | Yes      | The text to be analyzed    |

**Success Response**:

- **Code**: 200 OK
- **Content**:
  ```json
  {
    "readability": 75.2,
    "keywords": ["keyword1", "keyword2", "keyword3"]
  }
  ```

**Error Response**:

- **Code**: 400 Bad Request
- **Content**:
  ```json
  {
    "error": "No text provided"
  }
  ```

**Notes**:

- The readability score is calculated using the Flesch Reading Ease score (higher is easier to read)
- Keywords are extracted using the TextRazor API
- Only keywords with a confidence score > 0.2 are included
- A maximum of 10 keywords are returned, sorted by confidence score

### 2. Insert Keyword

Inserts a keyword into the provided text.

**URL**: `/insert`

**Method**: `POST`

**Content-Type**: `application/json`

**Request Body**:

```json
{
  "text": "Your original text.",
  "keyword": "Keyword to insert"
}
```

**Success Response**:

- **Code**: 200 OK
- **Content**:
  ```json
  {
    "updated_text": "Your original text. Keyword to insert"
  }
  ```

**Error Response**:

- **Code**: 400 Bad Request
- **Content**:
  ```json
  {
    "error": "Insertion failed"
  }
  ```

**Notes**:

- The keyword is intelligently inserted at the end of the text
- If the text ends with a period, exclamation mark, or question mark, the keyword is inserted after a space
- If the text doesn't end with punctuation, a period is added before inserting the keyword