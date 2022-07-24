import requests

from bs4 import BeautifulSoup

import pandas as pd

toan = []
van = []
su = []
dia = []
ly = []
hoa = []
sinh = []
anh = []
gdcd = []
stt = []

# 15015883
start = 15007000
end = 15007100


for idx in range(start, end):
    page = requests.get("https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/{}.html".format(idx))
    if page.status_code != 404:
        print("[GET] {}/15015883".format(idx))
        soup = BeautifulSoup(page.text, "html.parser")
        parent = soup.find_all("div", {"class": "resultSearch__right"})
        elements = soup.find_all("td")
        n = 2
        elements = [elements[i:i+n] for i in range(0, len(elements), n)]

        subjects = {'Toán': '', 'Văn': '', 'Sử': '', 'Địa': '', 'Lí': '',
                    'Hoá': '', 'Sinh': '', 'Ngoại ngữ': '', 'GDCD': ''}
        for element in elements:
            for key, value in subjects.items():
                if element[0].text == key:
                    
                    subjects[key] = element[1].text
        stt.append(idx)
        toan.append(subjects["Toán"])
        van.append(subjects["Văn"])
        su.append(subjects['Sử'])
        dia.append(subjects["Địa"])
        ly.append(subjects["Lí"])
        hoa.append(subjects["Hoá"])
        sinh.append(subjects["Sinh"])
        anh.append(subjects["Ngoại ngữ"])
        gdcd.append(subjects["GDCD"])

    else:
        print("[INFO] {}/15015883: no data".format(idx))


data = pd.DataFrame({"SBD":stt,
                    "Toán":toan,
                    "Ngữ Văn":van,
                    "Tiếng Anh":anh,
                    "Lý":ly,
                    "Hóa":hoa,
                    "Sinh":sinh,
                    "Lịch Sử":su,
                    "Địa lý":dia,
                    "GDCD":gdcd,
                    })  

data.to_excel('data.xlsx', sheet_name='sheet1', index=False)


