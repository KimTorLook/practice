'''
• Lowercase
• Lowercase letters and spaces
• No space 1st digit and last digit
• One line only
• Maximum 80 characters
'''

inputed_words = input('please input a line of word for counting')
inputed_words.strip()
inputed_words.strip("[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a=inputed_words.count(' ')

if inputed_words.count>=80:
    print('there are too many characters.')
else:
    print('Your inputed' + a + 'characters.'  )