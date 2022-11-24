# Harbour "Contract dates visualization (Backend)"
### Tech task by Andrii Orlov

## Features
- Upload multiple contracts via UI
- Responsive design
- Date visualisation using calendar
- Ability to check the text snippet where the date has been parsed from
- Ability to check the original contract
- Ability to filter dates on the Calendar by checking/unchecking contracts they belong to

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
