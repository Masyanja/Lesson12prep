# Сперва импорттируем класс блюпринта
import json

from flask import Blueprint, render_template, request

# Затем создаем новый блюпринт, выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__)
# создаем короткий путь для загрузки картинок
UPLOAD_FOLDER = "uploads/images"


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/add_post_page')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/add_post', methods=["POST", "GET"])
def add_post():
    text_post_added = request.form['content']
    picture = request.files.get("picture")
    filename = picture.filename
    picture.save(f"{UPLOAD_FOLDER}/{filename}")
    with open('posts.json') as f:  # прочитали файл
        posts_json = json.load(f)  # записали содержимое
    with open('posts.json', 'w') as f:
        posts_json.append({'pic': filename, 'content': text_post_added})  # добавили содержимое в список как словарь
        json.dump(posts_json, f, ensure_ascii=False, indent=4, separators=(',', ':'), sort_keys=True)
    print(text_post_added)
    return render_template('post_uploaded.html', image_upload=f"{UPLOAD_FOLDER}/{filename}", text_upload=text_post_added)
