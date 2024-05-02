from flask import Flask, render_template, request,send_file
import google.generativeai as genai

# Configure generative AI with your API key
GOOGLE_API_KEY = 'AIzaSyCzmEtOwR_9ZmEgI3y-bjwx94r4ooZ6Ogo'
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Flask application
app = Flask(__name__)

# List available models

@app.route('/')
def home():
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    return render_template('Generator.html', models=models)

# Chat with selected model
@app.route('/chat', methods=['POST'])
def chat():
    model_name = request.form.get('model', '')
    prompt = request.form.get('prompt', '')
    if not model_name or not prompt:
        return "Model name or prompt is missing.", 400
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    result = ''.join([p.text for p in response.candidates[0].content.parts])
    return result


if __name__ == '__main__':
    app.run(debug=True)
