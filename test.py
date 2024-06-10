# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun 10 18:05:05 2024

# @author: tlooc
# """

# import requests

# url = 'http://127.0.0.1:5000/extract_text'
# file_path = '1.jpg'

# files = {'file': open(file_path, 'rb')}
# response = requests.post(url, files=files)

# if response.status_code == 200:
#     data = response.json()
#     print("Detected text:", data['detected_text'])
#     print("Detected languages:", data['detected_languages'])
#     print("Formatted text:", data['formatted_text'])
# else:
#     print("Error:", response.status_code)
