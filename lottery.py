import requests
import xlsxwriter
from bs4 import BeautifulSoup

robbie_page = requests.get("http://www.robbieslottery.com/")
lands_lot_page = requests.get("http://landsloterij.org/eng/index.aspx")

robbie_soup = BeautifulSoup(robbie_page.content, 'html.parser')
lands_lot_soup = BeautifulSoup(lands_lot_page.content, 'html.parser')

print("Robbie's Lottery Winners :: " + robbie_soup.find('div', class_='title wegadnumber').text)

robbie_drawing = robbie_soup.find('div', class_='drawings four').text

robbies_winners = []

def populate_robbies_winners(list):
        for x in robbie_drawing:
                list.append(x)
        return

# remove unncecessary elements
def removeElements(list):
        for x in list:
                list.remove("\n") 
        
        list.pop(11)  
        list.pop(len(robbies_winners)-2)
        list.pop(len(robbies_winners)-1)
        return

def populate_lands_winners1(list):
        for img in images1.find_all('img'):
                list.append(img['src'])
        return

def populate_lands_winners2(list):
        for img in images2.find_all('img'):
                list.append(img['src'])
        return

def populate_lands_winners3(list):
        for img in images3.find_all('img'):
                list.append(img['src'])
        return

# bad characters
bad_chars = ['../images/black/','.jpg']

# remove bad characters
def removeBadChars(list):
        for i in bad_chars: 
                list[0] = list[0].replace(i,'')
                list[1] = list[1].replace(i,'')
                list[2] = list[2].replace(i,'')
                list[3] = list[3].replace(i,'')
                list[4] = list[4].replace(i,'')
        return

populate_robbies_winners(robbies_winners)
removeElements(robbies_winners)

print("\n1st Prize: {}".format(robbies_winners[0]+robbies_winners[1]+robbies_winners[2]+robbies_winners[3]))
print("\n2nd Prize: {}".format(robbies_winners[4]+robbies_winners[5]+robbies_winners[6]+robbies_winners[7]))
print("\n3rd Prize: {}".format(robbies_winners[8]+robbies_winners[9]+robbies_winners[10]+robbies_winners[11]))

print("---------------------------")
print("Landsloterij Winners")
images1 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning1')
images2 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning2')
images3 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning3')

Winners1 = []
Winners2 = []
Winners3 = []

populate_lands_winners1(Winners1)
populate_lands_winners2(Winners2)
populate_lands_winners3(Winners3)

removeBadChars(Winners1)
removeBadChars(Winners2)
removeBadChars(Winners3)

print("\n1st Prize: {}".format(Winners1[0]+Winners1[1]+Winners1[2]+Winners1[3]+Winners1[4]))
print("\n2nd Prize: {}".format(Winners2[0]+Winners2[1]+Winners2[2]+Winners2[3]+Winners2[4]))
print("\n2nd Prize: {}".format(Winners3[0]+Winners3[1]+Winners3[2]+Winners3[3]+Winners3[4]))

# send to .csv
workbook = xlsxwriter.Workbook('output.csv')
worksheet = workbook.add_worksheet()
row = 0
array = [["Robbie's Winners",(robbies_winners[0]+robbies_winners[1]+robbies_winners[2]+robbies_winners[3]),(robbies_winners[4]+robbies_winners[5]+robbies_winners[6]+robbies_winners[7]),(robbies_winners[8]+robbies_winners[9]+robbies_winners[10]+robbies_winners[11])],
         ['Landsloterij Winners',(Winners1[0]+Winners1[1]+Winners1[2]+Winners1[3]+Winners1[4]),(Winners2[0]+Winners2[1]+Winners2[2]+Winners2[3]+Winners2[4]),(Winners3[0]+Winners3[1]+Winners3[2]+Winners3[3]+Winners3[4])]]

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
