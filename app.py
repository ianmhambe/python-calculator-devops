from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation', 'add')
        
        result = None
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Cannot divide by zero'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({
            'result': result,
            'operation': operation,
            'num1': num1,
            'num2': num2
        })
    
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'version': os.getenv('APP_VERSION', '1.0.0')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
