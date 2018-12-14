mmbot
---
Mattermost Slash Command Server


### Setup
```sh
-------term 0--------
git clone git@github.com:aldnav/mmbot.git
cd mmbot
pipenv activate  # or `pipenv install --ignore-pipfile`  first time
cp conf.sample.yaml conf.yaml
# edit conf.yaml
python application.py
-------term 1--------
# for development purposes
ngrok {port of running application.py}
# copy endpoint
# test in postman (optional)
# test in a separate channel/room
# by pasting link to mm integrations > slash command
```

### Example

route | slash command
------|--------------
/l10n | /translate_cn

### Development

Project uses [Pipenv](https://pipenv.readthedocs.io/en/latest/) for handling environment requirements. DO NOT MANUALLY EDIT `requirements.txt`. It's generated from `pipenv lock -r > requirements.txt`

### TODO
- Add other languages support
  `/translate en 嗨` -> `嗨 \n hi` 
- Add support for translation service providers

### Deployment to AWS Elasticbeanstalk

Simply zip the application and upload. Or through cli.

```sh
pipenv lock -r > requirements.txt
zip ebpackage.zip application.py config.yaml requirements.txt
```
