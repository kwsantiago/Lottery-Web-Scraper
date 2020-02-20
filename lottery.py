import requests
import xlsxwriter
from bs4 import BeautifulSoup

robbie_page = requests.get("http://www.robbieslottery.com/")
lands_lot_page = requests.get("http://landsloterij.org/eng/index.aspx")

robbie_soup = BeautifulSoup(robbie_page.content, 'html.parser')
lands_lot_soup = BeautifulSoup(lands_lot_page.content, 'html.parser')

print("Robbie's Lottery Winners :: " + robbie_soup.find('div', class_='title wegadnumber').text)

robbie_drawing = robbie_soup.find('div', class_='drawings four').text

images1 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning1')
images2 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning2')
images3 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning3')

robbies_winners = []
lands_lot_winners1 = []
lands_lot_winners2 = []
lands_lot_winners3 = []

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

def print_robbies_winners(winners):
        print("\n1st Prize: {}".format(winners[0]+winners[1]+winners[2]+winners[3]))
        print("\n2nd Prize: {}".format(winners[4]+winners[5]+winners[6]+winners[7]))
        print("\n3rd Prize: {}".format(winners[8]+winners[9]+winners[10]+winners[11]))
        return

def print_lands_lot_winners(winners):
        print("\n1st Prize: {}".format(winners[0]+winners[1]+winners[2]+winners[3]+winners[4]))
        return  

populate_robbies_winners(robbies_winners)
removeElements(robbies_winners)
print_robbies_winners(robbies_winners)
print("---------------------------\nLandsloterij Winners")
populate_lands_winners1(lands_lot_winners1)
populate_lands_winners2(lands_lot_winners2)
populate_lands_winners3(lands_lot_winners3)
removeBadChars(lands_lot_winners1)
removeBadChars(lands_lot_winners2)
removeBadChars(lands_lot_winners3)      
print_lands_lot_winners(lands_lot_winners1)
print_lands_lot_winners(lands_lot_winners2)
print_lands_lot_winners(lands_lot_winners3)

# send to .csv
workbook = xlsxwriter.Workbook('output.csv')
worksheet = workbook.add_worksheet()
row = 0
array = [["Robbie's Winners",(robbies_winners[0]+robbies_winners[1]+robbies_winners[2]+robbies_winners[3]),(robbies_winners[4]+robbies_winners[5]+robbies_winners[6]+robbies_winners[7]),(robbies_winners[8]+robbies_winners[9]+robbies_winners[10]+robbies_winners[11])],
         ['Landsloterij Winners',(lands_lot_winners1[0]+lands_lot_winners1[1]+lands_lot_winners1[2]+lands_lot_winners1[3]+lands_lot_winners1[4]),(lands_lot_winners2[0]+lands_lot_winners2[1]+lands_lot_winners2[2]+lands_lot_winners2[3]+lands_lot_winners2[4]),(lands_lot_winners3[0]+lands_lot_winners3[1]+lands_lot_winners3[2]+lands_lot_winners3[3]+lands_lot_winners3[4])]]

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
