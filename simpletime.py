from flask import Flask
import os
from time import time
app = Flask(__name__)


@app.route('/time/')
def get_epoch():
    return str(int(time()))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)



