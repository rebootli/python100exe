


import requests

url = "https://www.dongchedi.com/motor/pc/car/brand/get_all_brands"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.dongchedi.com/",
}

response = requests.get(url, headers=headers)
print(response.status_code)  # 查看HTTP状态码（200/404/403等）
print(response.text[:500])   # 打印前500字符，看返回的是什么


