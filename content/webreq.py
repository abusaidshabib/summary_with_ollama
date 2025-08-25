import requests
import os


class WebScraper:
    def __init__(self, url, save_path="data/requested.html", headers=None, timeout=10):
        self.url = url
        self.save_path = save_path
        self.headers = headers or {"User-Agent": "Mozilla/5.0"}
        self.timeout = timeout

    def fetch(self):
        try:
            response = requests.get(
                self.url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def save(self, content):
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
        with open(self.save_path, 'w', encoding="utf-8") as f:
            f.write(content)
        print(f"Saved as {self.save_path}")

    def run(self):
        content = self.fetch()
        if content:
            self.save(content)