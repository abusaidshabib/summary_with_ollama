import re
from bs4 import BeautifulSoup
import os


class HTMLCleaner:

    def __init__(self, input_path="data/requested.html", output_path="data/cleaned_text.txt"):
        self.input_path = input_path
        self.output_path = output_path

    def read_html(self):

        try:
            with open(self.input_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: HTML file not found at {self.input_path}")
            return None
        except Exception as e:
            print(f"An error occurred while reading HTML: {e}")
            return None

    def clean_text(self, html_content):

        soup = BeautifulSoup(html_content, "html.parser")
        title = soup.title.text if soup.title else None
        text = soup.get_text(separator='\n')
        clean_text = re.sub(r'\n\s*\n', '\n', text).strip()

        if title:
            clean_text = f"{title}\n\n{clean_text}"

        return clean_text

    def save_text(self, text):

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Cleaned text saved to {self.output_path}")

    def run(self):

        html_content = self.read_html()
        if html_content:
            clean_text = self.clean_text(html_content)
            self.save_text(clean_text)
