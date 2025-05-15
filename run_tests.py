#from playwright.sync_api import sync_playwright
from utils.openai_utils import generate_text, load_prompt


def generate_scenarios():
  # Load the prompt for the Contact Us form
  prompt = load_prompt("contact_us_form")

# Generate Gherkin Scenarios
  scenarios = generate_text(prompt)
  print("Generated Gherkin Scenarios:\n", scenarios)

      #.venv\Scripts\python.exe run_tests.py

if __name__ == "__main__":
    generate_scenarios()