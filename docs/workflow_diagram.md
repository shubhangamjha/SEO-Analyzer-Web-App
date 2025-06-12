# SEO Analyzer Web App Workflow Diagram

```mermaid
graph TD
    %% User Interaction
    User[User] -->|Enters text| UI[Web Interface]
    
    %% Frontend Components
    UI -->|Submit form| JS[JavaScript Client]
    JS -->|POST /analyze| Backend[Flask Backend]
    
    %% Backend Processing
    Backend -->|Process text| ReadabilityAnalysis[Readability Analysis]
    Backend -->|API request| KeywordExtraction[Keyword Extraction]
    
    %% External Services
    KeywordExtraction -->|HTTP Request| TextRazorAPI[TextRazor API]
    TextRazorAPI -->|JSON Response| KeywordExtraction
    
    %% Results Processing
    ReadabilityAnalysis -->|Calculate score| Results[Analysis Results]
    KeywordExtraction -->|Extract keywords| Results
    
    %% Return to Frontend
    Results -->|JSON Response| JS
    JS -->|Update DOM| UI
    
    %% Keyword Insertion
    UI -->|Click keyword| JS
    JS -->|POST /insert| Backend
    Backend -->|Process insertion| TextUpdate[Text Update]
    TextUpdate -->|JSON Response| JS
    JS -->|Update preview| UI
    
    %% Display to User
    UI -->|Show results| User
    
    %% Styling
    classDef frontend fill:#f9f,stroke:#333,stroke-width:2px;
    classDef backend fill:#bbf,stroke:#333,stroke-width:2px;
    classDef external fill:#bfb,stroke:#333,stroke-width:2px;
    
    class User,UI,JS frontend;
    class Backend,ReadabilityAnalysis,KeywordExtraction,TextUpdate,Results backend;
    class TextRazorAPI external;
```

## Component Description

### Frontend Components
- **Web Interface**: HTML/CSS interface (index.html)
- **JavaScript Client**: Client-side logic (app.js)

### Backend Components
- **Flask Backend**: Web server handling requests (app.py)
- **Readability Analysis**: Uses textstat library to analyze text readability
- **Keyword Extraction**: Processes text to extract relevant keywords
- **Text Update**: Handles keyword insertion into text

### External Services
- **TextRazor API**: Third-party API for natural language processing

## Data Flow

1. **User Input**:
   - User enters text in the web interface
   - User submits the form for analysis

2. **Text Analysis**:
   - Frontend sends text to backend via POST request to `/analyze`
   - Backend calculates readability score using textstat
   - Backend sends text to TextRazor API for keyword extraction
   - Backend processes and filters keywords
   - Results are sent back to frontend as JSON

3. **Results Display**:
   - Frontend displays readability score
   - Frontend displays clickable keyword buttons
   - Frontend shows original text in preview area

4. **Keyword Insertion**:
   - User clicks on a keyword button
   - Frontend sends text and selected keyword to backend via POST request to `/insert`
   - Backend inserts keyword into text
   - Updated text is sent back to frontend
   - Frontend updates the text preview

## Technical Implementation

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **Dependencies**: Flask, Flask-Cors, requests, textstat
- **External API**: TextRazor for keyword extraction