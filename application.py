import requests as reqs
import yaml
import sys
from flask import Flask, request, jsonify

settings = None
try:
    with open('./conf.yaml', 'r') as f:
        settings = yaml.load(f)
except FileNotFoundError:
    sys.exit('No settings file found. See sample "conf.sample.yaml"')

application = app = Flask(__name__)
endpoint = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


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


if __name__ == '__main__':
    app.run(debug=True)
