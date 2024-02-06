import hashlib
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Version 1 Endpoint
@app.route('/reply/<string:code>', methods=['GET'])
def get_reply_v1(code):    
    response = {"message":f"{code}"}
    return make_response(jsonify(response),200)

# Version 2 Endpoint
@app.route('/v2/reply/<int:id>-<string:code>', methods=['GET'])
def get_reply_v2(id, code):
    digits = [int(digit) for digit in str(id)]
    if len(digits) == 2:
        for digit in digits:
            if(digit ==  1):      
                #reverse
                code = code[::-1]                
            elif (digit == 2):
                #md5
                md5 = hashlib.md5()
                md5.update(code.encode('utf-8'))
                code = md5.hexdigest()
            else:
                response = {"message": "Invalid input"}
                return make_response(jsonify(response),400)
    else:
        response = {"message": "Invalid input"}
        return make_response(jsonify(response),400)
    
    response = {"message":f"{code}"}
    
    return make_response(jsonify(response),200)

if __name__ == '__main__':
    app.run(debug=True)
