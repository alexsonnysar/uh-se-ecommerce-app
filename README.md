# uh-se-ecommerce-app

## Github

### Branch naming convention

``` 
master
dev/stable
dev/user/feature-name or dev/user/bug-fix
```
Copy dev/stable branch to create seperate feature branch. For example: dev/alexsonnysar/address-verification. Once feature branch is complete make a pull request to merge into dev/stable, and then once dev/stable is stable make another pull request to merge into master

## Getting Started

### Prerequisites
  - Python 3.8.2
  - Visual Studio Code
  
### Running the Project
To run the project, you must first create a virtual environment

``` python -m venv venv ```

Then you can either activate the enviroment using command line or the python extension in Visual Studio Code

On Windows run

``` venv\Scripts\activate.bat ```

On Unix or MacOS run

``` source venv/bin/activate ```

You will know if it is activate if you see your virtual enviroment name in your terminal

``` (venv) C:\Users\... ```

After activating, install all packages from requirements.txt by running

``` pip install -r requirements.txt ```

You can then launch the server by running

``` python manage.py runserver ```

### Django Admin
```
Username: admin

Password: password
```

### Auto-Formatter
To format all the .py files within the project please run this command in the root directory

``` black . ```

### requirements.txt

If you fork this repo and add any new packages please run pip freeze

``` pip freeze > requirements.txt ```
