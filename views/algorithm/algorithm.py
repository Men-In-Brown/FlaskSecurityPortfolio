from pathlib import Path
from flask import Blueprint, render_template, request
from .fibonacci import Fibonacci
from .palindrome import Palindrome
from .image import image_data

algorithm_views = Blueprint('algorithm', __name__,
                          url_prefix='/algorithm',
                          template_folder='templates/algorithm',
                          static_folder='static',
                          static_url_path='assets')


@algorithm_views.route('/fibonacci/', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("fibonacci.html", fibonacci=Fibonacci(2))


@algorithm_views.route('/palindrome/', methods=["GET", "POST"])
def palindrome():
    if request.form:
        return render_template("palindrome.html", palindrome=Palindrome(request.form.get("candidate")))
    return render_template("palindrome.html", palindrome=Palindrome("a toyota"))

@algorithm_views.route('/image/')
def image():
    path = Path(algorithm_views.root_path) / "static"
    return render_template('image.html', images=image_data(path))
