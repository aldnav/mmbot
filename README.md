mmbot
---
Mattermost Slash Command Server


### Setup
```sh
git clone git@github.com:aldnav/mmbot.git
cd mmbot
pipenv activate
cp conf.sample.yaml conf.yaml
# edit conf.yaml
FLASK_APP=server.py flask run
```


### Example

route | slash command
------|--------------
/l10n | /translate_cn

