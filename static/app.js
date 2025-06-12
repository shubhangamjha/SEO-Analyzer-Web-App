document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('seo-form');
    const resultsDiv = document.getElementById('results');
    const textPreview = document.getElementById('text-preview');
    const textInput = document.getElementById('text-input');
    const errorDiv = document.getElementById('error');
    const loader = document.getElementById('loader');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const text = formData.get('text').trim();
        errorDiv.textContent = '';

        if (!text) {
            errorDiv.textContent = 'Please enter some text';
            return;
        }

        try {
            // Show loader
            loader.style.display = 'block';
            textPreview.value = text;

            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.error) {
                errorDiv.textContent = data.error;
                return;
            }

            // Display results
            document.getElementById('readability').textContent = data.readability;

            // Display keywords
            const container = document.getElementById('keywords-container');
            container.innerHTML = '';

            data.keywords.forEach(keyword => {
                const btn = document.createElement('button');
                btn.className = 'keyword';
                btn.textContent = keyword;
                btn.onclick = () => insertKeyword(keyword);
                container.appendChild(btn);
            });

            resultsDiv.style.display = 'block';

        } catch (error) {
            console.error('Error:', error);
            errorDiv.textContent = 'Analysis failed. Please try again.';
        } finally {
            // Hide loader
            loader.style.display = 'none';
        }
    });

    async function insertKeyword(keyword) {
        const currentText = textPreview.value;

        try {
            const response = await fetch('/insert', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    text: currentText,
                    keyword: keyword
                })
            });

            const data = await response.json();
            if (data.updated_text) {
                textPreview.value = data.updated_text;
            } else if (data.error) {
                errorDiv.textContent = data.error;
            }
        } catch (error) {
            console.error('Insertion error:', error);
            errorDiv.textContent = 'Insertion failed. Please try again.';
        }
    }
});