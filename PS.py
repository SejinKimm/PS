from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

f = open("PS.txt", 'r')

for no in f:
    url = Request("https://www.acmicpc.net/problem/%s" % no.rstrip(), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    soup = BeautifulSoup(response, "html.parser")

    # 문제 이름
    value = soup.find("span", {"id": "problem_title"})
    title = str(value).split(">")[1].split("<")[0]
    print(title)

    # 문제 내용
    value = soup.find("div", {"id": "problem_description"})
    maintext = str(value).split("<p>")[1].split("</p>")[0]
    print(maintext)

    # 문제 입력 설명
    value = soup.find("div", {"id": "problem_input"})
    inputtext = str(value).split("<p>")[1].split("</p>")[0]
    print(inputtext)

    # 문제 출력 설명
    value = soup.find("div", {"id": "problem_output"})
    outputtext = str(value).split("<p>")[1].split("</p>")[0]
    print(outputtext)

    # 예제 입력 & 출력
    i = 1
    chk = 0
    while chk != 2:
        chk = 0
        value = soup.find("pre", {"id": "sample-input-%d" % i})
        if value == None:
            chk += 1
            inputsample = "없음"
        else:
            inputsample = str(value).split(">")[1].split("<")[0]

        value = soup.find("pre", {"id": "sample-output-%d" % i})
        if value == None:
            chk += 1
            outputsample = "없음"
        else:
            outputsample = str(value).split(">")[1].split("<")[0]

        if chk < 2:
            print(inputsample)
            print(outputsample)

        i += 1
    
    # 분류
    #value = soup.find("a", {"class": "spoiler-link"})
    #category = str(value).split(">")[1].split("<")[0]
    #print(category)


f.close()