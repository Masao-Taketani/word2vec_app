import json
import flask
from flask import request
from gensim.models import word2vec
from flask_cors import CORS
from flask import render_template

PORT_NO = 8081

app = flask.Flask(__name__)
CORS(app)

#when accessed to '/'
@app.route('/', methods=['GET'])

def index():
	return render_template('index.html')


@app.route('/', methods=['POST'])
def api():
	#'Content-Type'が'application/json'以外の場合
	if request.headers['Content-Type'] != 'application/json':
		print('Content-Type:',request.headers['Content-Type'])
		#400番エラーを返す
		return flask.jsonify(res='error'), 400
	else:
		print('POST method request accepted!')
		#JSONの値を'data'にて取得
		data = request.get_json()
		#'data'内にあるキー値が'word1'のバリュー値を表示
		print(data['word1'])
		word1 = data['word1']

		model = word2vec.Word2Vec.load('wiki.model')
		result1 = model.most_similar(positive = [word1])
		print("result1", result1)
	return json.dumps({"result1": result1}), 200

@app.route('/api', methods=['POST'])
def api_2():
        #'Content-Type'が'application/json'以外の場合
        if request.headers['Content-Type'] != 'application/json':
                print('Content-Type:',request.headers['Content-Type'])
                #400番エラーを返す
                return flask.jsonify(res='error'), 400
        else:
                print('POST request accepted!')
                #JSONの値を'data'にて取得
                data = request.get_json()
                #'data'内にあるキー値が'word2','word3','word4'のバリュー値を表示
                word2 = data['word2']
                print('word2', word2)
                word3 = data['word3']
                print('word3', word3)
                word4 = data['word4']
                print('word4', word4)

                model = word2vec.Word2Vec.load('wiki.model')
                result2 = model.most_similar(positive = [word3, word4], negative = [word2])
                return json.dumps({"result2": result2}), 200


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=PORT_NO)
