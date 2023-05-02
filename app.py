from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main():
    name : 'joseph'
    return render_template("index.html", name=name)
# untuk route antar halaman

@app.route('/detail/<keyword>')
def detail(keyword):
    keyword = request.args.get('keyword')
    return render_template("detail.html", keyword=keyword)
# untuk route antar halaman

@app.route('/ajax-test')
def ajax_test():
    return render_template("ajax-test.html")

@app.route('/ssr-test')
def ssr_test():
    url = 'https://my-json-server.typicode.com/jjjosephhh/test-db-001/RealtimeCityAir'
    r = requests.get(url)
    response = r.json()
    rows = response['row']
    return render_template("ssr-test.html", rows=rows)



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)