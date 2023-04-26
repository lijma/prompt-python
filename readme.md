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


### 加入星球学习更多、相互交流、谈合作

* ChatGPT帮我实现React前端项目
* ChatGPT帮我实现Python项目
* ChatGPT帮我实现Java后端项目
* [高阶] ChatGPT帮我实现Visual Studio Code插件
* [高阶] ChatGPT帮我实现Python爬虫
* [高阶] ChatGPT帮我实现自动发微信公众号
* [高阶] ChatGPT帮我实现自动发星球动态
* [高阶] ChatGPT帮我爬油管、创造短视频
* [高阶] ChatGPT帮我发送抖音和Tiktok
* 更多课程等你来参与~

![img.png](docs/xq.png)

### 微信加好友了解细节
![img.png](docs/contact.png)


