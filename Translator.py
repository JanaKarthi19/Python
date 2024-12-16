from translate import Translator

print("Select Your Language:")
print("1. Japanese")
print("2. Korean")
print("3. Italian")
print("4. French")

choice = int(input("Enter Your Choice: "))

if choice==1:
    sal="ja"
elif  choice==2:
    sal="ko"
elif  choice==3:
    sal ="it"
elif  choice==4:
    sal = "fr"

translatee = Translator(sal)

Text = input("Enter the text: ")
translation = translatee.translate(Text)
print(translation)