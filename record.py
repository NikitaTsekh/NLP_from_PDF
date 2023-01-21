import pytesseract
from PIL import Image
import requests
from io import BytesIO
import json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Getting URL')
    parser.add_argument('url',type=str, help='Input URL for worker invoice')
    args = parser.parse_args()
    url=args.url

    def get_invoice_status(url):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))

            # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            #Выше путь для Windows, для локального запуска скрипта


            text = pytesseract.image_to_string(img, lang='rus')


            msg = "аннулирован"  #Искомая строка

            if msg in str.lower(text):
                list1 = text.split('\n')
                spl_word = 'Дата:'
                result = [item for item in list1 if item.startswith('Дата:')]  # Получаем список
                date = result[0].split(spl_word, 1)[1]
                date = str(date).replace(' ', '')
                data = {

                    "canceled": True,
                    "date": date
                }

                # print('"canceled": true, "date":', date)

            else:
                data = {

                    "canceled": False,

                }


        except Exception as e:

            data = {

                "error": str(e),

            }

        json_string = json.dumps(data)
        return json_string

    print(get_invoice_status(url))
