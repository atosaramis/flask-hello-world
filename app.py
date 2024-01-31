from flask import Flask
import vanna
from vanna.remote import VannaDefault

app = Flask(__name__)

# Initialize Vanna
vn = VannaDefault(model='chinook', api_key=vanna.get_api_key('my-email@example.com'))
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

@app.route('/top-artists')
def top_artists():
    result = vn.ask('What are the top 10 artists by sales?')
    return result

if __name__ == '__main__':
    app.run()
