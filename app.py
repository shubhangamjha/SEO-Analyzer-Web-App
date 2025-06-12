from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Add this
import requests
import textstat

app = Flask(__name__)
CORS(app)

# Use a free SEO API (Example: TextRazor)
API_KEY = "2d7780f12e628223534cce0df6aa8db309c3a131c769c3f6007ef125"  # Get from https://www.textrazor.com/
SEO_API_URL = "https://api.textrazor.com/"

template = "index.html"


@app.route('/')
def index():
    """
    Renders the main page of the application.

    Returns:
        HTML template: The main index.html template
    """
    return render_template(template)


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyzes the provided text for readability and extracts keywords.

    This endpoint uses the textstat library to calculate the Flesch Reading Ease score
    and the TextRazor API to extract relevant keywords from the text.

    Returns:
        JSON: A JSON object containing:
            - readability: Flesch Reading Ease score (higher is easier to read)
            - keywords: List of extracted keywords

        Error (400): If no text is provided
    """
    text = request.form.get('text','').strip()
    if not text:
        return jsonify(error="No text provided"), 400

    # 1. Readability
    readability = textstat.flesch_reading_ease(text)

    # 2. Call TextRazor properly
    payload = {
      "apiKey": API_KEY,
      "text": text,
      "extractors": "entities",
      "cleanup.mode": "cleanHTML"
    }
    try:
        resp = requests.post("https://api.textrazor.com/", data=payload)
        resp.raise_for_status()
        jr = resp.json()
        # Optional: print(jr) for debugging
        entities = jr.get("response", {}).get("entities", [])
        keywords = sorted(
            [{"keyword": e["entityId"], "score": e["confidenceScore"]}
             for e in entities],
            key=lambda x: x["score"],
            reverse=True
        )
        # Sort & take top 10
        keywords = sorted(keywords, key=lambda x: x[1], reverse=True)[:10]
        keyword_list = [kw for kw,score in keywords]
    except Exception as e:
        # **During debugging, re-raise so you see the real error**
        print("TextRazor API error:", e, getattr(e, 'response', None))
        raise

    return jsonify(readability=readability, keywords=keyword_list)


@app.route('/insert', methods=['POST'])
def insert_keyword():
    """
    Inserts a keyword into the provided text.

    This endpoint takes the original text and a keyword, then intelligently
    inserts the keyword at the end of the text, respecting sentence structure.

    Request JSON:
        - text: The original text
        - keyword: The keyword to insert

    Returns:
        JSON: A JSON object containing:
            - updated_text: The text with the keyword inserted

        Error (400): If the insertion fails
    """
    try:
        data = request.get_json()
        text = data['text']
        keyword = data['keyword']

        # Improved insertion logic
        if text.endswith(('.', '!', '?')):
            updated_text = f"{text} {keyword}"
        else:
            updated_text = f"{text}. {keyword}"

        return jsonify(updated_text=updated_text)

    except Exception as e:
        print("Insert Error:", e)
        return jsonify(error="Insertion failed"), 400


if __name__ == '__main__':
    app.run(debug=True)
