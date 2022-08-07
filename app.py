from flask import Flask, request, render_template, send_from_directory
from main.views import *
from loader.views import *

POST_PATH = "posts.json"  # указать путь к файлу json, чтобы потом можно было указать короткий путь
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

#app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
