from flask import Flask

import db

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    db.Base.metadata.drop_all(bind=db.engine,checkfirst=True)
    db.Base.metadata.create_all(bind=db.engine)
    app.run(debug=True)

