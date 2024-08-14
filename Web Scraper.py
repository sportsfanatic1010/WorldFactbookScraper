import requests
from bs4 import BeautifulSoup
URL = "https://www.cia.gov/the-world-factbook/field/roadways/"
page = requests.get(URL)
nums = []
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="pb30")
for i in results:

    i2 = i.text.split(': ')
    for i in i2:
        i3 = i.split('paved')
        x = 0
        for i in i3:
            
            if len(i3) == 2:
                
                if not i3[0].endswith("un"):
                    i4 = i3[0].split(' km')[0]
                    i5 = i4.split(",")
                    i6 = ''.join(i5)
                    
                    if i6.endswith(' million'):
                        i7 = i6.split(' million')[0]
                        i8 = int(float(i7) * 1000000)
                        if x == 1:
                            print(i8)
                            try:
                                int(i8)
                                nums.append(int(i8))
                            except:
                                pass 
                        x += 1
                        
                    else:
                        if x == 1:
                            print(i6)
                            try:
                                int(i6)
                                nums.append(int(i6))
                            except:
                                pass    
                        x += 1

print(nums)
total = 0
for i in nums:
    total += i
print(f"Total: {total}")