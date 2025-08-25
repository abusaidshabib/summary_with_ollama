```markdown
# Web Scraper & LLM Summarization Pipeline

This project is a **Python pipeline** that fetches a website, cleans the HTML content, and generates a concise summary using a large language model (LLM). It is structured using reusable classes for modularity and easy maintenance.

---

## Features

1. **WebScraper**

   - Downloads HTML content from any website.
   - Handles request headers and errors.
   - Saves the webpage as `data/requested.html`.

2. **HTMLCleaner**

   - Reads the saved HTML file.
   - Extracts text and removes unnecessary whitespace.
   - Saves cleaned text to `data/cleaned_text.txt`.

3. **LLMSummarizer**

   - Reads the cleaned text.
   - Generates a concise, informative summary using an LLM.
   - Saves the summary to `data/summary.txt`.

4. **Pipeline Execution**
   - Runs the three steps sequentially: Scraping → Cleaning → Summarization.
   - Easy to extend to other websites or LLM models.

---

## Project Structure
```

web_pipeline/
│
├── content/
│ ├── **init**.py
│ ├── webscraper.py
│ ├── htmlcleaner.py
│ └── llmsummarizer.py
│
└── run_pipeline.py

````

- `content/` contains the three main classes.
- `run_pipeline.py` runs the complete pipeline in sequence.
- `data/` stores all generated files:
  - `requested.html` → Raw HTML
  - `cleaned_text.txt` → Cleaned plain text
  - `summary.txt` → LLM-generated summary

---

## Usage

1. Clone the repository:

```bash
git clone <your-repo-url>
cd web_pipeline
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the pipeline:

```bash
python run_pipeline.py
```

4. Output files will be generated in the `data/` folder.

---

## Example

After running the pipeline on [Worldometers](https://www.worldometers.info/):

- **Raw HTML**: `data/requested.html`
- **Cleaned Text**: `data/cleaned_text.txt`
- **Summary**: `data/summary.txt`

---

## Notes

- Change the URL in `run_pipeline.py` to summarize other websites.
- The LLM model can be swapped by adjusting the `model_id` parameter in `LLMSummarizer`.
- Ensure the `data/` folder exists or let the pipeline create it automatically.

---

```