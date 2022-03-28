from flask import Blueprint, render_template, Flask, request
from search import load_posts
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search():
    search_by = request.args['s']
    logging.info(f'слово для поиска: {search_by}')
    posts = [x for x in load_posts() if search_by.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by=search_by, posts=posts)

