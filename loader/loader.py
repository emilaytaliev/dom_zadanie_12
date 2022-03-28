from flask import Blueprint, render_template, request
from search import load_posts, uploads
import logging

loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')

@loader_blueprint.route('/form/')
def loader():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['POST'])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        uploads(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split('.')[-1] not in ['png', 'jpeg', 'jpg']:
            logging.info('файл с изображением не найден')
    except FileNotFoundError:
        logging.error('ошибка при загрузке файла')
        return 'Файл не найден'
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)

