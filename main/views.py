# Сперва импортируем класс блюпринта
from flask import Blueprint, render_template, request
import json

# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def index_page():
    return render_template("index.html")


@main_blueprint.route('/search', methods=["POST"])
def search_page():
    with open('posts.json') as f:
        posts_json = json.load(f)
    found_word_list = []
    word_for_search = request.values[
        's']  # request.value - метод кот позволяет забрать вводимые данные из формы по ключу s
    for post in posts_json:
        if word_for_search.lower() in post['content'].lower():  # post['content'] это словарь с id content
            found_word_list.append(post)

    return render_template("post_list.html", word_for_search=word_for_search, posts=found_word_list)

