from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # serve your HTML


@app.route('/main.html')
def main():
    return render_template('main.html')


@app.route('/html/<path:page>')
def html_page(page):
    # Render files under templates/html/, e.g. /html/config.html -> templates/html/config.html
    return render_template(f'html/{page}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
