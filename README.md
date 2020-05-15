# Dummy Twitter 

This a python/flask application that imitates the functionality of twitter.It includes the following code functionalities..

1.Follow  people 

2.random recomandations on who to follow

3.Image hosting using using [Cloudinary API](https://cloudinary.com/)

4.UI is done wit html and css (some areas done this Flask WTF)

5.Database sqlalchemy


## Installation 


It is a requirement that you have Python3 installed in your computer.

1.clone the project

```bash
git clone https://github.com/codeGiche/twitter_clone.git
```
2.Create a virtual environment
```bash
python -m venv venv
```
3.Activate the virtual environment
```bash
Source venv/Scripts/activate
```
4. Install requirements
```bash
pip install -r reqiurements.txt
```
5.Set flask_app 
```bash
export FLASK_APP=main.py
```
6.Run flask app

BEFORE running the application , make sure u insert the relevant database URI's and the cloudinary api keys.

```bash
flask run
```

## Usage
To view the apps documentation, navigate to your localhost(browser)
```python
127.0.0.1/
```

## Contributing
Feel free to make it better [fork me](https://github.com/codeGiche/twitter_clone.git)

