from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

data = None
with open('../data/comments.pickle', 'rb') as f:
	data = pickle.load(f)
 
@app.route("/comments")
def comments():
	
	uid = request.args.get('user_id')
	
	try:
		if uid is None:
			return jsonify({"response":data})
		
		elif int(uid) not in data.keys():
			return jsonify('Id Not Present..')

		else:
			return jsonify({"response":data[int(uid)]})

	except ValueError as e2:
		return jsonify([])
	
		
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True, port=5002)