# Imports
import re
from flask import Flask, render_template, request
from converter import Converter
from translator import Translator
import json

# Declaration

app = Flask(__name__)

# Settings


# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('form.html')

    
@app.route('/vocal_dict', methods = ['POST','GET'])
def vocal_dict():


    
    try:
        # Khởi tạo translator, cần sửa lại dùng từ ENV
        translator = Translator("https://od-api.oxforddictionaries.com", "82cc5758", "abde664b38ee6e7930e239b11690565e")
        
        # Tìm từ cần tra từ điển
        
        # word = str(input('Nhập từ cần tra: '))
        word = request.form["word"]
        # Gọi api sang oxford để hiện nghĩa
        
        result = translator.translate(word)
        
        context = json.dumps(result, indent=2)
        print(context)
        
    except ValueError as exp:
        print("Error", exp)
        
    return render_template('form.html', context= context)


# Start here
if __name__ == "__main__":
    app.run(debug=True)