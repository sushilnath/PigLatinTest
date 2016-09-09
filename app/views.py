import json
from app import app
from util import pig_translate
from flask import request, jsonify

@app.route('/')
def index():
	return "Welcome to Pig Latin translation service!"

@app.route('/translate', methods=['POST'])
def translate():
	text = request.form['text']
	return jsonify(text_piglatin=pig_translate.translate(text))

@app.errorhandler(400)
def bad_request(e):
	return "Missing or incorrect form params", 400

@app.errorhandler(404)
def page_not_found(e):
	return "What you were looking for is not there", 404
