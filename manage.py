from flask import Flask, render_template, url_for, session, request, jsonify, redirect
from app import models
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import timedelta
import hashlib as h
import json
from datetime import datetime
from flask_cors import CORS
from dateutil.parser import parse
import random
import string
from app import create_app, db
from werkzeug.utils import secure_filename
from dotenv import load_dotenv


UPLOAD_FOLDER = 'uploads'  # Create a folder named 'uploads' in your Flask app directory

load_dotenv()

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.app_context().push()
app.permanent_session_lifetime = timedelta(weeks=1)
migrate = Migrate(app, db)


def hashblock(req):
    encoded_block = json.dumps(req, sort_keys=True).encode()
    block_encryption = h.sha256()
    block_encryption.update((encoded_block))
    return block_encryption.hexdigest()



@app.route("/signLangAI", methods=["POST"])
def signLangAI():
    if request.method == "POST":
        print("request arrived")
        video = request.form.get("video")
        vid = video.seek(0)
        vid_filename = secure_filename(vid.filename)
        print(vid_filename)
        print("vedio file retrieved")
        print(video)
        return jsonify({"message":"video accepted"})


def is_date(string, fuzzy=True):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except:
        return False

if __name__ == "__main__":
  
    app.run(debug=True, port=5000)
