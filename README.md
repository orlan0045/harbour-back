# Harbour "Contract dates visualization (Backend)"
### Tech task by Andrii Orlov

## Features
- Saving uploaded contracts
- Parsing dates from every contract
- The line where date been found serves as a text snippet

## Tech stack
- aiofiles (to save uploaded pdfs)
- pdfplumber (reading and parsing pdfs)
- datefinder (parsing dates)
- fastapi (server)
- pytest (tests)

## Installation
It is better to use Dockerfile since everything is predefined there and any problems with running server should not be raised
Commands to run (all from the project's root directory):

```sh
docker build -t harbour_back .
docker run -it -p 8000:8000 harbour_back
```
To run tests:
```sh
docker run -it harbour_back pytest
```


## Linters
| Linter | Command to run |
| ------ | ------ |
| Flake8 | docker run -it harbour_back flake8 . |
| Pylint | docker run -it harbour_back pylint --recursive=y .|
