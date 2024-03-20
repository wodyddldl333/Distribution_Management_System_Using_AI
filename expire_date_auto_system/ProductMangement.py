import os
import re
import io
import cv2
from pyzbar import pyzbar
from glob import glob
from dateutil import parser
from google.cloud import vision
import xml.etree.ElementTree as ET

class ProductStorage:
    def __init__(self):
        self.path_list = {'snack': [], 'milk': [], 'gum': []}
        self.barcode = {'barcode': []}
        self.today = 20230625  # Example, replace it with your actual date

    def save_path(self):
        for product_type in self.path_list.keys():
            self.path_list[product_type] = self.get_image_paths('./runs/detect/exp/crops/'+product_type)
        self.barcode['barcode'] = self.get_image_paths('./runs/detect/exp/crops/barcode')

    def get_image_paths(self, pattern):
        if os.path.isdir(pattern):
            return glob(pattern + '/*.jpg')
        return []

class Product:
    def __init__(self, name, image_path):
        self.name = name
        self.image_path = image_path

    def ocr(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GOOGLE_OCR_API_KEY.json"
        for path in self.image_path:
            client = vision.ImageAnnotatorClient()
            file_name = os.path.abspath(path)
            image = cv2.imread(file_name)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
            edged = cv2.Canny(blurred, 0, 90)
            cv2.imwrite(path, blurred)
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = client.text_detection(image=image)
            texts = response.text_annotations
            form = [r'\d{4}\.\d{2}\.\d{2}\n\d{2}:\d{2}', r'\d{2}\.\d{2}\. \d{2}:\d{2}', r'\d{2}\.\d{2}\.\d{2}',
                    r'\d{4}\.\d{2}\.\d{2}']
            for i in form:
                match = re.search(i, texts[0].description)
                if match:
                    datetime_str = match.group(0).replace('\n', ' ')
                    if i ==  r'\d{2}\.\d{2}\. \d{2}:\d{2}':
                        datetime_str = '2023.' + datetime_str
                    parsed_date = parser.parse(datetime_str, yearfirst=True)
                    formatted_string = parsed_date.strftime("%Y%m%d")
                    return formatted_string
        return '20990101'

    def barcode_detect(self):
        for path in self.image_path:
            image = cv2.imread(path)
            barcodes = pyzbar.decode(image)
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            cv2.imshow('image', image)
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
            return barcodeData

    #XML 파일은 샘플 데이터 (실제 식약처 API 사용)
    def XMLParser(self, barcodenum):
        tree = ET.parse('bar_info.xml')
        root = tree.getroot()

        def get_product_info(barcode):
            for product in root.findall('.//product'):
                barcode_element = product.find('barcode').text
                if barcode_element == barcode:
                    info_element = product.find('info').text
                    return info_element
            return None

        # 바코드 번호로 제품 정보를 얻어옴
        barcode_number = barcodenum
        return get_product_info(barcode_number)

class ProductManager:
    def __init__(self):
        self.product_storage = ProductStorage()
        self.product_storage.save_path()

    def save(self):

        for product_type in self.product_storage.path_list.keys():

            if len(self.product_storage.path_list[product_type]) != 0:
                image_path = self.product_storage.path_list[product_type]
                product = Product(product_type, image_path)
                return product.ocr()

    def barcode_detect(self):
        if len(self.product_storage.barcode['barcode']) != 0:
            barcode_info = self.product_storage.barcode['barcode']
            barcode = Product('barcode', barcode_info)
            barcodenum = barcode.barcode_detect()
            return barcode.XMLParser(barcodenum)

# Example usage
class Product_Info:
    def __init__(self):
        product_manager = ProductManager()
        self.expirydate = product_manager.save()
        self.info = product_manager.barcode_detect()


