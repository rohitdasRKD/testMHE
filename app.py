from flask import Flask, request, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route('/add', methods=['GET'])
def add():
    
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = add_numbers(num1, num2)
        return jsonify({"result": result})
    

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=8080)
