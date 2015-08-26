from flask import  request,  jsonify, abort
import random
from app import app

@app.route('/', methods= ['POST'])
def index():
	result = []
	def someObject():
		result = {}
		result['left'] = random.randint(0, 100000)
		result['right'] = random.randint(0, 100000)
		result['middle'] = random.randint(0, 100000)
		return result
	if not request.json or not 'startNum' in request.json or not 'endNum' in request.json:
		abort(400)
	if type(request.json['startNum']) is not int:
		abort(400)
	if type(request.json['endNum']) is not int:
		abort(400)

	for x in xrange(request.json['startNum'],request.json['endNum'] + 1):
		temp = someObject()
		temp['item'] = x
		result.append(temp)


	return jsonify({'result': result})