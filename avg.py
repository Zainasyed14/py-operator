print("Enter marks obtained")
Eng = int(input("english: "))
Maths = int(input("maths: "))
Science = int(input("Science: "))
Urdu = int(input("urdu: "))
Art = int(input("art: "))

sum = Eng+Maths+Science+Urdu+Art
percentage = sum /150*100
avg= sum/5
print("total percentage is:" , percentage)
print("your average is: " , avg)