from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/category/')
def category():
    return render_template('category.html')


@app.route('/product/')
def product():
    return render_template('product.html')


if __name__ == '__main__':
    app.run(debug=True)