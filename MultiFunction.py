class multifunction():
    def Subfields():
        list=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for val in list:
            print(val)
    
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")
            
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age <21):
                print("NOT ELEGIBLE")
            else:
                print("ELEGIBLE")
        elif(gender=="Female"):
            if(age <18):
                print("NOT ELEGIBLE")
            else:
                print("ELEGIBLE")
                
    def percentage():
        subject1=int(input("Subject1:"))
        subject2=int(input("Subject2:"))
        subject3=int(input("Subject3:"))
        subject4=int(input("Subject4:"))
        subject5=int(input("Subject5:"))
        total=subject1+subject2+subject3+subject4+subject5
        print("Total:",total)
        print("Percentage:",(total/500)*100)
        
    def triangle():
        height=float(input("Height:"))
        breadth=float(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",(height*breadth)/2)
        
    def Perimeter():
        height1=float(input("Height1:"))
        height2=float(input("Height2:"))
        breadth=float(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",height1+height2+breadth)
    
        