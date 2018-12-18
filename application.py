import requests as reqs
import yaml
import sys
import boto3
import os
from flask import Flask, request, jsonify

settings = None
try:
    with open('./conf.yaml', 'r') as f:
        settings = yaml.load(f)
except FileNotFoundError:
    sys.exit('No settings file found. See sample "conf.sample.yaml"')

application = app = Flask(__name__)
endpoint = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


if settings.get('AWS_ACCESS_KEY_ID'):
    print('Using config.yaml AWS_ACCESS_KEY_ID')
    os.environ['AWS_ACCESS_KEY_ID'] = settings.get('AWS_ACCESS_KEY_ID')
if settings.get('AWS_SECRET_ACCESS_KEY'):
    print('Using config.yaml AWS_SECRET_ACCESS_KEY')
    os.environ['AWS_SECRET_ACCESS_KEY'] = settings.get('AWS_SECRET_ACCESS_KEY')


@app.route('/l10n', methods=['POST'])
def localization():
    lang = 'zh'
    text_to_translate = request.values.get('text')
    r = reqs.post(endpoint, params=dict(
        key=settings.get('yandex_key'),
        text=text_to_translate,
        lang=lang
    ))
    response_text = "{}\n{}".format(text_to_translate, r.json()['text'][0])
    return jsonify({
        'response_type': 'in_channel',
        'text': response_text
    })


@app.route('/translate-zh', methods=['POST', 'GET'])
def translate_zh():
    text_to_translate = request.values.get('text')  # zh Hi
    translated = translate_from_aws(text_to_translate)
    return jsonify({
        'response_type': 'in_channel',
        'text': "{}\n{}".format(text_to_translate, translated)
    })


@app.route('/translate-en', methods=['POST', 'GET'])
def translate_en():
    text_to_translate = request.values.get('text')  # zh Hi
    translated = translate_from_aws(text_to_translate, "en", "zh")
    return jsonify({
        'response_type': 'in_channel',
        'text': "{}\n{}".format(text_to_translate, translated)
    })


def translate_from_aws(text, target_lang_code="zh", source_lang_code="en"):
    tfa= boto3.client(service_name='translate', region_name='us-east-2', use_ssl=True) #tfa means translate_from_aws
    result = tfa.translate_text(Text=text, SourceLanguageCode=source_lang_code, TargetLanguageCode=target_lang_code)
    return result.get('TranslatedText')


if __name__ == '__main__':
    app.run(debug=True)
