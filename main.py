# coding: utf-8

from flask import Flask, request, jsonify
from service.calc_price import CalcPrice
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'message': 'Hello, world'})


@app.route("/omikuji/", methods=["POST"])
def omikuji():
    # TODO おみくじリスト取得
    message = "hello world"
    response_json = {
        "response_type": "in_channel",
        "text": "omikuji list"
    }
    return jsonify(response_json)

@app.route("/calc/inc_tax_price/", methods=["POST"])
def calc_include_tax_price():
    print(request.form)
    calc_price = CalcPrice()
    # textを分解
    base_price, tax_rate = request.form["text"].strip().split()

    # 税込価格を計算
    try:
        include_tax_price = calc_price.include_tax_price(int(base_price), int(tax_rate))
        text = str(base_price) + "円の税込価格は`" + str(include_tax_price) + "`円です。"
    except ValueError:
        text = "本体価格、税率は数値で指定してください。"

    response_json = {
        "response_type": "in_channel",
        "text": text
    }
    return jsonify(response_json)
#
#
# @app.route("/result", methods=["POST"])
# def result():
#     message = "This is paiza"
#     article = request.form["article"]
#     name = request.form["name"]
#     return render_template("form.html", message = message, article = article, name = name)
#
# @app.route("/show/<key_name>")
# def show_data(key_name):
#     d = shelve.open("./myshelve")
#     data = d[key_name]
#     print(data)
#     d.close
#     return ",".join(data)
#
# @app.route("/add/<key_name>/<item_name>")
# def add(key_name, item_name):
#     d = shelve.open("./myshelve")
#     if (key_name in d):
#         data = d[key_name]
#         data.append(item_name)
#         d[key_name] = data
#     else:
#         d[key_name] = [item_name]
#     d.close
#     return key_name + "に" + item_name + "を追加しました。"

# @app.route('/list', methods=['GET', 'POST'])
# @app.route('/list/<int:page>')
# def get_list(page=1):
#     # <int:page> が未指定の場合、page=1が設定される
#
# @app.route('/get_request', methods=['GET'])
# def post_request():
#     output = {　##※ここのJSONフォーマットは自由だよ
#         "version":"1.0",
#         "response":{
#                 "outputSpeech":{
#                     "type":"PlainText",
#                     "text":"ハロー"
#                 }
#             }
#     }
#
#     return jsonify(output)
