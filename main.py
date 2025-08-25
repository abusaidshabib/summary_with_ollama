from content import WebScraper, HTMLCleaner, LLMSummarizer


def run_pipeline():
    scraper = WebScraper(url="https://www.worldometers.info/")
    scraper.run()

    cleaner = HTMLCleaner(input_path="data/requested.html",
                          output_path="data/cleaned_text.txt")
    cleaner.run()

    summarizer = LLMSummarizer(model_id="llama3.1",
                               input_path="data/cleaned_text.txt", output_path="data/summary.txt")
    summarizer.run()


if __name__ == "__main__":
    run_pipeline()
    print("Pipeline completed successfully!")
