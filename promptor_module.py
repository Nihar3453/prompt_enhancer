import textwrap
import google.generativeai as genai

GOOGLE_API_KEY = ''

genai.configure(api_key=GOOGLE_API_KEY)

# Model configuration
generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 1000,
}

model = genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generation_config)


def generate_prompt(user_input, previous_responses=[]):
    meta_prompt_response = model.generate_content("Act as an expert Prompt Engineer. "
                                                  "I'll give you an initial prompt. "
                                                  "Write the final prompt as an elegant template with clear sections. "
                                                  "Make sure you produce a ready-to-use prompt. "
                                                  "The final prompt must be small. "
                                                  "The final prompt must start with 'Enhanced Prompt'")

    meta_prompt_text = meta_prompt_response.text

    previous_response_text = " ".join([resp.text for resp in previous_responses])

    full_prompt = f"{meta_prompt_text}\nUser prompt based on previous response: {previous_response_text}\nUser prompt: {user_input}"

    response = model.generate_content(full_prompt)
    start_index = response.text.find('Enhanced Prompt')

    if start_index != -1:
        improved_prompt_section = response.text[start_index:]
    else:
        improved_prompt_section = None

    response_text = response.text
    solution_response = model.generate_content(response_text)

    previous_responses.append(solution_response)

    return improved_prompt_section, solution_response.parts[0].text



