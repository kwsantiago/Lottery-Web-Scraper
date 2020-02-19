import requests
import xlsxwriter
from bs4 import BeautifulSoup

robbie_page = requests.get("http://www.robbieslottery.com/")
lands_lot_page = requests.get("http://landsloterij.org/eng/index.aspx")

robbie_soup = BeautifulSoup(robbie_page.content, 'html.parser')
lands_lot_soup = BeautifulSoup(lands_lot_page.content, 'html.parser')

print("Robbie's Lottery Winners :: " + robbie_soup.find('div', class_='title wegadnumber').text)
robbie_drawing = robbie_soup.find('div', class_='drawings four').text
drawingList = []
for x in robbie_drawing:
        drawingList.append(x)

# remove unncecessary elements
for x in drawingList:
         drawingList.remove("\n") 
drawingList.pop(11)  
drawingList.pop(len(drawingList)-2)
drawingList.pop(len(drawingList)-1)

print("\n1st Prize: {}".format(drawingList[0]+drawingList[1]+drawingList[2]+drawingList[3]))
print("\n2nd Prize: {}".format(drawingList[4]+drawingList[5]+drawingList[6]+drawingList[7]))
print("\n3rd Prize: {}".format(drawingList[8]+drawingList[9]+drawingList[10]+drawingList[11]))

print("---------------------------")
print("Landsloterij Winners")
images1 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning1')
images2 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning2')
images3 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning3')

# bad characters
bad_chars = ['../images/black/','.jpg']

Winners1 = []
for img in images1.find_all('img'):
        Winners1.append(img['src'])

Winners2 = []
for img in images2.find_all('img'):
        Winners2.append(img['src'])

Winners3 = []
for img in images3.find_all('img'):
        Winners3.append(img['src'])

# remove bad characters
for i in bad_chars: 
        Winners1[0] = Winners1[0].replace(i,'')
        Winners1[1] = Winners1[1].replace(i,'')
        Winners1[2] = Winners1[2].replace(i,'')
        Winners1[3] = Winners1[3].replace(i,'')
        Winners1[4] = Winners1[4].replace(i,'')

        Winners2[0] = Winners2[0].replace(i,'')
        Winners2[1] = Winners2[1].replace(i,'')
        Winners2[2] = Winners2[2].replace(i,'')
        Winners2[3] = Winners2[3].replace(i,'')
        Winners2[4] = Winners2[4].replace(i,'')

        Winners3[0] = Winners3[0].replace(i,'')
        Winners3[1] = Winners3[1].replace(i,'')
        Winners3[2] = Winners3[2].replace(i,'')
        Winners3[3] = Winners3[3].replace(i,'')
        Winners3[4] = Winners3[4].replace(i,'')

print("\n1st Prize: {}".format(Winners1[0]+Winners1[1]+Winners1[2]+Winners1[3]+Winners1[4]))
print("\n2nd Prize: {}".format(Winners2[0]+Winners2[1]+Winners2[2]+Winners2[3]+Winners2[4]))
print("\n2nd Prize: {}".format(Winners3[0]+Winners3[1]+Winners3[2]+Winners3[3]+Winners3[4]))

# send to .csv
workbook = xlsxwriter.Workbook('output.csv')
worksheet = workbook.add_worksheet()
row = 0
array = [["Robbie's Winners",(drawingList[0]+drawingList[1]+drawingList[2]+drawingList[3]),(drawingList[4]+drawingList[5]+drawingList[6]+drawingList[7]),(drawingList[8]+drawingList[9]+drawingList[10]+drawingList[11])],
         ['Landsloterij Winners',(Winners1[0]+Winners1[1]+Winners1[2]+Winners1[3]+Winners1[4]),(Winners2[0]+Winners2[1]+Winners2[2]+Winners2[3]+Winners2[4]),(Winners3[0]+Winners3[1]+Winners3[2]+Winners3[3]+Winners3[4])]]

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
