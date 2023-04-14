## i0

> input

```text

i want use python to develop a web server in a empty folder `prompt-python`,  which can providing a api to talk to ChatGPT, could you give me some guideline step-by-step.

here is my prefered tech stack
* Django
* semantic-kernel python library

```
> output: active env

```sh
source venv/bin/activate
```

> install django and semantic-kernel

```sh
pip3 install django semantic-kernel
```

## first US

> input

```txt
`US1`:  create a post api; `path` is /tdd-with-gpt/prompt, `request body` is `CodeContext` object, return `CodeResponse` 
AC1: when `CodeContext` is null, return 400 bad request
AC2: when `CodeContext.prompt` is null,  return 400 bad request
AC3: when `CodeContext` not null, should return openapi code complete response correctly

please help implement above `US1` with a new python file
```

> run the server

```sh
python manage.py runserver
```


## 发现

https://community.openai.com/t/how-do-you-maintain-historical-context-in-repeat-api-calls/34395
问题：OpenAI没有提供上下文保持能力，如果准备的onboarding内容和期望的返回内容一次交互就超过了MAX TOKEN的长度，感觉怎么设计Prompt来保持上下文都没有用啊，这对于复杂的业务上下文的软件开发领域相当于死循环，既希望喂给openai尽可能多的信息，有希望得到持续有上下文能力的openai输出。
思考： 基于OpenAI接口的AI应用要解决的问题可能是如何单次Prompt得到期望结果，如何一次性精准描述，还需要压缩输入输出token数量。
疑问：  为啥openai 不把上下文能力提供在api接口里面？ 构建chatgpt的产品壁垒？

解决思路：
* langchain， indexing + memory
* 设计 学习路径 和 体验， 先把单点工作做完；再做成agent或者sk的skills； SK
* 每次只在一个工序的上下文 以及一个场景下 生成
