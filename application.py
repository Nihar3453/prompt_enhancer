from flask import Flask, request, jsonify
from prompter_module import generate_prompt

app = Flask(__name__)

previous_responses = []

@app.route('/generate_solution', methods=['POST'])
def generate_solution():
    data = request.get_json()

    user_input = data.get('user_input', '')
    improved_prompt_section, solution_response = generate_prompt(user_input, previous_responses)

    return jsonify({
        'solution_response': solution_response
    })

if __name__ == '__main__':
    app.run(debug=True)