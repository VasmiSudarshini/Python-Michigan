file = open(r"C:\Users\vasmi\OneDrive\Documents\Python\Chap_11_Reg_Exp\sample_data.txt")
import re
#lst = list()
total = 0
for line in file:
    nums = re.findall('[0-9]+', line)
    print(nums)
    for i in nums:
        total = total + int(i)
print(total)
