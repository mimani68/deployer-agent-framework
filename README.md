# Deployer Agent Framework

## Installation

```bash
pip install Flask
```
## Run application
```bash
export FLASK_APP=hello
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=3000
```

## Usage

```bash
curl localhost:3000/?cmd=hello
curl localhost:3000/?cmd=deploy&param=12&password=123
```