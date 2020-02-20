import requests
import xlsxwriter
from bs4 import BeautifulSoup

robbie_page = requests.get("http://www.robbieslottery.com/")
lands_lot_page = requests.get("http://landsloterij.org/eng/index.aspx")

robbie_soup = BeautifulSoup(robbie_page.content, 'html.parser')
lands_lot_soup = BeautifulSoup(lands_lot_page.content, 'html.parser')
robbie_drawing = robbie_soup.find('div', class_='drawings four').text

images1 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning1')
images2 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning2')
images3 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning3')

robbies_winners = []
lands_lot_winners1 = []
lands_lot_winners2 = []
lands_lot_winners3 = []
bad_chars = ['../images/black/','.jpg']

def populate_robbies_winners(list):
        for x in robbie_drawing:
                list.append(x)
        # remove unncecessary elements
        for x in list:
                list.remove("\n") 
        list.pop(11)  
        list.pop(len(robbies_winners)-2)
        list.pop(len(robbies_winners)-1)
        return 

def populate_lands_winners(list1,list2,list3):
        for img in images1.find_all('img'):
                list1.append(img['src'])
        for img in images2.find_all('img'):
                list2.append(img['src'])
        for img in images3.find_all('img'):
                list3.append(img['src'])
        # remove bad characters
        for i in bad_chars: 
                list1[0] = list1[0].replace(i,'')
                list1[1] = list1[1].replace(i,'')
                list1[2] = list1[2].replace(i,'')
                list1[3] = list1[3].replace(i,'')
                list1[4] = list1[4].replace(i,'')
        for i in bad_chars: 
                list2[0] = list2[0].replace(i,'')
                list2[1] = list2[1].replace(i,'')
                list2[2] = list2[2].replace(i,'')
                list2[3] = list2[3].replace(i,'')
                list2[4] = list2[4].replace(i,'')
        for i in bad_chars: 
                list3[0] = list3[0].replace(i,'')
                list3[1] = list3[1].replace(i,'')
                list3[2] = list3[2].replace(i,'')
                list3[3] = list3[3].replace(i,'')
                list3[4] = list3[4].replace(i,'')
        return  

def print_robbies_winners(winners):
        print("Robbie's Lottery Winners :: " + robbie_soup.find('div', class_='title wegadnumber').text)
        print("\n1st Prize: {}".format(winners[0]+winners[1]+winners[2]+winners[3]))
        print("\n2nd Prize: {}".format(winners[4]+winners[5]+winners[6]+winners[7]))
        print("\n3rd Prize: {}".format(winners[8]+winners[9]+winners[10]+winners[11]))
        return

def print_lands_lot_winners(winners1,winners2,winners3):
        print("---------------------------\nLandsloterij Winners")
        print("\n1st Prize: {}".format(winners1[0]+winners1[1]+winners1[2]+winners1[3]+winners1[4]))
        print("\n2nd Prize: {}".format(winners2[0]+winners2[1]+winners2[2]+winners2[3]+winners2[4]))
        print("\n3rd Prize: {}".format(winners3[0]+winners3[1]+winners3[2]+winners3[3]+winners3[4]))
        return  

populate_robbies_winners(robbies_winners)
print_robbies_winners(robbies_winners)
populate_lands_winners(lands_lot_winners1,lands_lot_winners2,lands_lot_winners3)
print_lands_lot_winners(lands_lot_winners1,lands_lot_winners2,lands_lot_winners3)

# send to .csv
workbook = xlsxwriter.Workbook('output.csv')
worksheet = workbook.add_worksheet()
row = 0
array = [["Robbie's Winners",(robbies_winners[0]+robbies_winners[1]+robbies_winners[2]+robbies_winners[3]),(robbies_winners[4]+robbies_winners[5]+robbies_winners[6]+robbies_winners[7]),(robbies_winners[8]+robbies_winners[9]+robbies_winners[10]+robbies_winners[11])],
         ['Landsloterij Winners',(lands_lot_winners1[0]+lands_lot_winners1[1]+lands_lot_winners1[2]+lands_lot_winners1[3]+lands_lot_winners1[4]),(lands_lot_winners2[0]+lands_lot_winners2[1]+lands_lot_winners2[2]+lands_lot_winners2[3]+lands_lot_winners2[4]),(lands_lot_winners3[0]+lands_lot_winners3[1]+lands_lot_winners3[2]+lands_lot_winners3[3]+lands_lot_winners3[4])]]

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()