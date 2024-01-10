# 0x02-i18
## Learning Objectives
### General
* What Internationalization and Localization are
* What ```gettext``` is
* How to use ```gettext``` to create ```Python``` ```locales```
## Requirements
### General
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted/compiled on Ubuntu 16.04 LTS using ```python3``` (version 3.5)
* All your files should end with a new line
* The first line of all your files should be exactly ```#!/usr/bin/env python3```
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* Your code should use the ```pycodestyle``` style (version 2.4)
* All your files must be executable
* The length of your files will be tested using ```wc```
* All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
* All your classes should have a documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```)
* All your functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Tasks
### Mandatory
- [x] **[0. Basic Flask app](./0-app.py)** - First you will setup a basic Flask app in ```0-app.py```. Create a single ```/``` route and an index.html template that simply outputs ```“Welcome to Holberton”``` as page title ```<title>``` and ```“Hello world”``` as header ```<h1>```.
- [x] **[1. Basic Babel setup](./1-app.py)** - Install the Babel Flask extension:
    - In ```1-app.py```, import ```babel``` and create a ```Babel``` instance.
    - Configure the ```LANGUAGES``` and ```BABEL_DEFAULT_LOCALE``` settings.
- [x] **[2. Get locale from request](./2-app.py)** - In this task, you will implement a ```get_locale``` function with the ```babel.localeselector``` decorator. Use the ```request.accept_languages``` to determine the best match with our supported languages.
- [x] **[3. Parametrize templates](./3-app.py)** - Use the ```_``` or ```gettext``` function to parametrize your templates. Use the ```message``` and ```user``` variables as ```_``` arguments.
- [x] **[4. Force locale with URL parameter](./4-app.py)** - In this task, you will implement a way to force a particular locale by passing the ```locale``` argument to your ```render_template``` method.
- [x] **[5. Mock logging in](./5-app.py)** - Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in ```5-app.py```.
- [x] **[6. Use user locale](./6-app.py)** - Change your ```get_locale``` function to use a user's preferred local if it is supported.
- [x] **[7. Infer appropriate time zone](./7-app.py)** - Define a ```get_timezone``` function and use the ```babel.timezoneselector``` decorator.
- [x] **[8. Display the current time](./app.py)** - Based on the ```user_timezone``` value, display the current time.
### Advance :muscle:
- [x] **[9. Get locale from request](./app.py)** - In this task, you will implement a ```get_locale``` function with the ```babel.localeselector``` decorator. Use the ```request.accept_languages``` to determine the best match with our supported languages.
- [x] **[10. Get locale from request](./app.py)** - In this task, you will implement a ```get_locale``` function with the ```babel.localeselector``` decorator. Use the ```request.accept_languages``` to determine the best match with our supported languages.
- [x] **[11. Get locale from request](./app.py)** - In this task, you will implement a ```get_locale``` function with the ```babel.localeselector``` decorator. Use the ```request.accept_languages``` to determine the best match with our supported languages.
- [x] **[12. Get locale from request](./app.py)** - In this task, you will implement a ```get_locale``` function with the ```babel.localeselector``` decorator. Use the ```request.accept_languages``` to determine the best match with our supported languages.
- [x] **[13. Get locale from request](./app.py)** - In this task, you will implement a ```get_locale``` function with the ```babel.localeselector``` decorator. Use the ```request.accept_languages``` to determine the best match with our supported languages.
