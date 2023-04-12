import os
import openai
import json

from decouple import config

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
openai.organization = config('ORGANIZATION')
openai.api_key = config('OPENAI_API_KEY')


@app.route("/v1/davinci", methods=(["POST"]))
def index():
    if request.method == "POST":
        print(type(request.get_json()))
        print(request.get_json())
        json_obj = request.get_json()
        model = "text-davinci-003"
        prompt = json_obj["prompt"]
        max_tokens = json_obj["max_tokens"]
        temperature = json_obj["temperature"]
        response = openai.Completion.create(
            model = model,
            prompt = prompt,
            max_tokens = max_tokens,
            temperature=temperature
        )
        return response
