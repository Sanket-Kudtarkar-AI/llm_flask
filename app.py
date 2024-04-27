from llama_cpp import Llama
import re
import tiktoken
from flask import Flask, request, jsonify

app = Flask(__name__)


def num_tokens_from_string(input_text):
    encoding_name = "cl100k_base"

    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(input_text))
    return num_tokens


llm = Llama(model_path="openchat-3.5-1210.Q5_K_M.gguf",
            n_gpu_layers=50,
            n_ctx=5000)


@app.route('/get_llm_response', methods=['POST'])
def get_llm_response():
    request_data = request.get_json()
    prompt = request_data["prompt"]

    prompt_ = f'''GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant:'''

    output = llm(prompt_,
                 max_tokens=2000,
                 echo=True,
                 temperature=0.0,
                 )

    answer = output['choices'][0]['text'].replace(prompt_, "").strip()

    response_data = {"llm_response": answer}

    res = jsonify(response_data)
    return res


if __name__ == '__main__':
    app.run(debug=False, port=5000)
