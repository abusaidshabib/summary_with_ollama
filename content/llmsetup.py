from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
import os


class LLMSummarizer:
    def __init__(self, model_id="llama3.1", input_path="data/cleaned_text.txt", output_path="data/summary.txt"):
        self.model_id = model_id
        self.model = Ollama(model=self.model_id)
        self.input_path = input_path
        self.output_path = output_path

        self.prompt_template = """
You are an expert summarizer. Read the following website content carefully and provide a concise summary that helps someone understand it quickly.

Requirements:
1. State the main purpose of the website.
2. Highlight the most important points or content.
3. Keep it short and informative.
4. Do NOT return in Markdown format; return as a single plain paragraph.

Content:
{content}
"""

    def read_content(self):
        try:
            with open(self.input_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: Input file not found at {self.input_path}")
            return None
        except Exception as e:
            print(f"An error occurred while reading content: {e}")
            return None

    def generate_summary(self, content):

        try:
            prompt = ChatPromptTemplate.from_template(self.prompt_template)
            formatted_prompt = prompt.format(content=content)
            return self.model(formatted_prompt)
        except Exception as e:
            print(f"An error occurred during summarization: {e}")
            return None

    def save_summary(self, summary):

        if summary:
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            with open(self.output_path, "w", encoding="utf-8") as f:
                f.write(summary)
            print(f"Summary saved as {self.output_path}")

    def run(self):
        content = self.read_content()
        if content:
            summary = self.generate_summary(content)
            self.save_summary(summary)
