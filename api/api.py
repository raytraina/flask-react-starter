import time
from flask import Flask

app = Flask(__name__)


# included '/api/' to help with proxying; also good practice to do so
@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    print("Backend App is now running >>>")
    app.run(port=6060)