import time

questions = [
"What's the founding year of Hwa Chong Institution? (Year)",
"What programs does Hwa Chong Institution offer? (Programs, in short form, seperated by commas)",
"Size of Hwa Chong Institution? (Size)",
"Admission process for Hwa Chong Institution? (Admission methods, in dhort form, seperated by commas)",
"Student-to-faculty ratio at Hwa Chong Institution? (Ratio)",
"Alumni network of Hwa Chong Institution? (Alumni)"
]


print('Welcome to random trivia quiz about Hwa Chong Institution! (Yay)')
print('-'*70)
d = input('Firstly, do you like Hwa Chong? \n write y for yes, n for no, if you dont answer this question by typing y or n default take it as n: ')
if d == 'y':
    print('That is correct! Now here is your score:')
    count = 1
    print(count)

else:
    print('Ok thank you bye bye')
    time.sleep(2)
    print('Btw watch your back')
    exit()