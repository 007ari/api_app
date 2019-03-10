from flask import Flask, jsonify, request
import pickle
import requests as api_request

app = Flask(__name__)
 
@app.route("/fetch_data")
def fetch_data():

	uid = request.args.get('user_id')
	
	if uid is None:
		return jsonify('Please Enter a Valid User ID')

	else:

		user = api_request.get('http://localhost:5001/users?', params={'user_id':uid})
		user = user.json()
		comment = api_request.get('http://localhost:5002/comments?', params={'user_id':uid})
		comment = comment.json()
		todo = api_request.get('http://localhost:5003/todos?', params={'user_id':uid})
		todo = todo.json()

		user = user['response']
		comment = comment['response']
		todo = todo['response']

		data = {"user_id":int(uid),
				"name":user['name'],
				"username": user['username'],
				"email": user['email'],
				"comment": comment['body'],
				"todo": todo['title'],
				"todo_status": todo['completed']}

		return jsonify({"response":data})

	# try:
	# 	if uid is None:
	# 		return jsonify({"response":data})
		
	# 	elif int(uid) not in data.keys():
	# 		return jsonify('Id Not Present..')

	# 	else:
	# 		return jsonify({"response":data[int(uid)]})

	# except ValueError as e2:
	# 	return jsonify([])
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True, port=8080)	