mmbot
---
Mattermost Slash Command Server


### Setup
```sh
git clone git@github.com:aldnav/mmbot.git
cd mmbot
pipenv activate  # or `pipenv install --ignore-pipfile`  first time
cp conf.sample.yaml conf.yaml
# edit conf.yaml
python application.py
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
