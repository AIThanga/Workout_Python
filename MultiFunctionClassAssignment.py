class MultipleFunctionsClassAssignment:
    def oddEven():
        num = int(input("Enter the number: ")) 
        if num % 2 == 0:
            print(num, "is Even")
            message = "Even number"
        else:
            print(num, "is Odd")
            message = "Odd number"
        return message
    
    def bmi():
        bmi_value = float(input("Enter the BMI Index: "))
        if bmi_value < 18.5:
            print("UnderWeight")
            message1 = 'UnderWeight'
        elif bmi_value < 24.9:
            print("Normal Range")
            message1 = 'Normal Range'
        elif bmi_value < 29.9:
            print("Overweight")
            message1 = 'Overweight'
        else:
            print("Very Overweight")
            message1 = 'Very Overweight'
        return message1

    def subfieldinAI():
        aiLists =['Machine Learning','Neural Neteworks', 'Robatics', 'Speech Processing','Natural Language Processing']
        print('Sub Fields in AI are:')
        for item in aiLists:
            print(item)

    def marriageEligible():
        gender = input("Your Gender")
        age = int(input("Your age")) 
        if(gender=='Male'):
            if(age<=21):
                print('Not eligible')
                message = "Not eligible"
            else:
                print('Eligible')
                message = "Eligible"
        elif(gender=='Female'):
            if(age<=18):
                print('Not eligible')
                message = "Not eligible"
            else:
                print('Eligible')
                message = "Eligible"
        else:
            print('option is wrong')
            message('option is wrong')
        return message
        
    def percentage():
        subject1 = int(input("Subject1"))
        subject2 = int(input("Subject2"))
        subject3 = int(input("Subject3"))
        subject4 = int(input("Subject4"))
        subject5 = int(input("Subject5"))
        total = subject1+subject2+subject3+subject4+subject5
        print('Total:', total)
        percentage = total/5;
        print('Percentage:',percentage)
    
    def triangle():
         height = int(input("Height"))
         breadth = int(input("Breadth"))
         areaformula = (height * breadth)/2
         print('Area of Triangle',areaformula)
         height1 = int(input("Height1"))
         height2 = int(input("Height1"))
         breadth2 = int(input("Breadth2"))
         perimiter = height1+height2+breadth2
         print('Perimeter of Triangle:',perimiter)
