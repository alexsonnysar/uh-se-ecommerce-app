# uh-se-ecommerce-app

## Github

### Branch naming convention

``` 
master
dev
dev/user/feature-name or dev/user/bug-fix
```
Copy dev branch for feature branch example: dev/alexsonnysar/address-verification

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
