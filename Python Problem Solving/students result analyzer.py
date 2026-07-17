


def Students_result(marks):
    #marks = [subject1,subject2,subject3]
    toralmarks = sum(marks)
    print(f"Students total marks is :",toralmarks)
    avarage = toralmarks/len(marks)
    print(f"Here is a avarage marks :",avarage)
    print(f"here is a highers number of all sublect",max(marks))
    print(f"Here is a lower number of all subject :",min(marks))
    Passed_subject = 0
    Failed_subject = 0

    for i in marks:
        if i >= 40:
            
            Passed_subject +=1
            # continue

        elif i < 40:
            
       

            Failed_subject +=1

    
    print(f"passed student number :",Passed_subject)
    print(f"failed students number:",Failed_subject)


marks = [20,40,50,10,50]
Students_result(marks)