import textwrap
import google.generativeai as genai
from IPython.display import display

GOOGLE_API_KEY=('')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

#model configuration
generation_config = {
  "temperature": 0.2,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 1000,
}

model = genai.GenerativeModel('gemini-1.0-pro-latest' ,generation_config=generation_config)

previous_responses = []

while True:
    meta_prompt_response = model.generate_content("Act as an expert Prompt Engineer.\
    I'll give you an initial prompt.\
    Write the final prompt as an elegant template with clear sections.\
    Make sure you produce a ready-to-use prompt.\
    the final prompt must be small.\
    The final prompt must start with 'Enhanced Prompt'")

    meta_prompt_text = meta_prompt_response.text

    previous_response_text = " ".join([resp.text for resp in previous_responses])

    user_initial_input = input("Enter your prompt: ")
    full_prompt = f"{meta_prompt_text}\nUser prompt based on previous response: {previous_response_text}\nUser prompt: {user_initial_input}"

    response = model.generate_content(full_prompt)
    start_index = response.text.find('Enhanced Prompt')

    if start_index != -1:
        improved_prompt_section = response.text[start_index:]

    response_text = response.text
    solution_response = model.generate_content(response_text)

    previous_responses.append(solution_response)

    print(solution_response.parts[0].text)

    continue_or_exit = input("Press Enter to continue with another prompt or type 'exit' to end: ")
    if continue_or_exit.lower() == "exit":
        break