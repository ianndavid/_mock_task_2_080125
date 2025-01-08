from flask import Flask
from _init_ import start_app
#for running the app
app = start_app()

if __name__ == '__main__':
    app.run(debug=True)