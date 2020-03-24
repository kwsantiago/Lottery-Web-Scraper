import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def getRobbieData():
        robbie_page = requests.get("http://www.robbieslottery.com/")
        robbie_soup = BeautifulSoup(robbie_page.content, 'html.parser')
        robbie_drawing = robbie_soup.find('div', class_='drawings four').text
        return robbie_drawing

def getLandsData():
        lands_lot_page = requests.get("http://landsloterij.org/eng/index.aspx")
        lands_lot_soup = BeautifulSoup(lands_lot_page.content, 'html.parser')
        return lands_lot_soup

def getLandsWinners1():
        lands_lot_soup = getLandsData()
        images1 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning1')
        return str(images1)

def getLandsWinners2():
        lands_lot_soup = getLandsData()
        images2 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning2')
        return str(images2)

def getLandsWinners3():
        lands_lot_soup = getLandsData()
        images3 = lands_lot_soup.find('span', id='ctl00_ContentPlaceHolder1_lblWinning3')
        return str(images3)

def print_lands_winners1():
        images1 = getLandsWinners1()
        winners1 = re.sub('[a-zA-Z..<>/"=_ ]','', images1)
        print("-1st Prize: {}".format(winners1[4:9]))
        return

def print_lands_winners2():
        images2 = getLandsWinners2()
        winners2 = re.sub('[a-zA-Z..<>/"=_ ]','', images2)
        print("-1st Prize: {}".format(winners2[4:9]))
        return

def print_lands_winners3():
        images3 = getLandsWinners3()
        winners3 = re.sub('[a-zA-Z..<>/"=_ ]','', images3)
        print("-1st Prize: {}".format(winners3[4:9]))
        return

def print_robbies_winners():
        robbie_drawing = getRobbieData()
        winners = re.sub('[\n]','', robbie_drawing)
        print("Robbie's Lottery Winners")
        print("-1st Prize: {}".format(winners[0:4]))
        print("-2nd Prize: {}".format(winners[5:9]))
        print("-3rd Prize: {}".format(winners[8:12]))
        return 

def print_all_lands_winners():
        print("\nLandsloterij Winners")
        print_lands_winners1()
        print_lands_winners2()
        print_lands_winners3()
        return

def array2htmltable(data): 
    q = '<style>h1 {left: 0;line-height: 200px;margin-top: -100px;position: absolute;text-align: center;top: 50%;width: 100%; }</style><h1><table align="center" border="1">\n'
    for i in [(data[0:], 'td')]:
        q += "\n".join(
            [
                "<tr>%s</tr>" % str(_mm) 
                for _mm in [
                    "".join(
                        [
                            "<%s>%s</%s>" % (i[1], str(_q), i[1]) 
                            for _q in _m
                        ]
                    ) for _m in i[0]
                ] 
            ])+"\n"
    q += "</table></h1>"
    return q

def to_html():
        robbie_drawing = getRobbieData()
        robbies_winners = re.sub('[\n]','', robbie_drawing) # remove unnecessary characeters
        images1 = getLandsWinners1()
        lands_winners1 = re.sub('[a-zA-Z..<>/"=_ ]','', images1) # remove unnecessary characeters
        images2 = getLandsWinners2()
        lands_winners2 = re.sub('[a-zA-Z..<>/"=_ ]','', images2) # remove unnecessary characeters
        images3 = getLandsWinners3()
        lands_winners3 = re.sub('[a-zA-Z..<>/"=_ ]','', images3) # remove unnecessary characeters

        array = [["Robbie's Winners",("1: "+ robbies_winners[0:4]),("2: " + robbies_winners[5:9]),("3: " + robbies_winners[8:12])],
         ['Landsloterij Winners',("1: " + lands_winners1[4:9]),("2: " + lands_winners2[4:9]),("3: " + lands_winners3[4:9])]]
        html_str = array2htmltable(array)
        print(html_str)
        Html_file= open("/var/www/html/output.html","w") # send the output to the the html folder for PHP server
        Html_file.write(html_str)
        Html_file.close()
        return

def main():
        print_robbies_winners()
        print_all_lands_winners()
        to_html()
        return

main()

