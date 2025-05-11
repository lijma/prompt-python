# build chatgpt api service

## introduction

this is backend web api for tdd-with-gpt plugin

a python built service to support GPT text complete function with openai


## Prompt Records

[records](./docs/chatgpt-design-journey.md)

## tech stacks

* pip3
* python > 3.0
* virtualenv
* Django
* semantic-kernel

## run application locally

> export api key and org id

```sh

export OPENAI_API_KEY='sk-XXXX'
export OPENAI_ORG_ID='org-XXX'

```

> go to folder tdd_with_gpt_api and enable virtual environment

```sh
virtualenv venv
venv\Scripts\activate
```

> run application locally

```sh
python manage.py runserver
```


## production environments

* python > 3.0
* pip
* virtualenv
* Django
* semantic-kernel
* gunicorn
* nginx

> run application in production

```sh
gunicorn tdd_with_gpt_api.wsgi:application -D
```

> update nginx conf to redirect requests


