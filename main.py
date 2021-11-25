# from speech_converter import Converter
import json
from converter import Converter
from translator import Translator

def Trans():
    try:
        # Khởi tạo converter
        converter = Converter()
        # Khởi tạo translator, cần sửa lại dùng từ ENV
        translator = Translator("https://od-api.oxforddictionaries.com", "82cc5758", "abde664b38ee6e7930e239b11690565e")

        # Chạy chương trình nhận diện giọng nói
        vocal = converter.listen()
        
        # Gọi api sang oxford để hiện nghĩa
        result = translator.translate(vocal)
        
        print(json.dumps(result, indent=2))
        
    except ValueError as exp:
        print("Error", exp)


def TransWord():
    try:
        # Khởi tạo translator, cần sửa lại dùng từ ENV
        translator = Translator("https://od-api.oxforddictionaries.com", "82cc5758", "abde664b38ee6e7930e239b11690565e")
        
        # Tìm từ cần tra từ điển
        
        word = str(input('Nhập từ cần tra: '))
        
        # Gọi api sang oxford để hiện nghĩa
        result = translator.translate(word)
        
        print(json.dumps(result, indent=2))
        
    except ValueError as exp:
        print("Error", exp)

TransWord()