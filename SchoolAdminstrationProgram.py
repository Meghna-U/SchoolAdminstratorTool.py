import csv
def write_in_csv(list_of_info):
    with open('info_of_student','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"])
        writer.writerow(list_of_info)
if __name__=='__main__':
    i=True
    while(i):
        info_of_student=input("Enter information of the student in the following format (Name,Age,Contact Number,E-mail ID):")
        list_of_studentinfo=info_of_student.split(",")
        print("Information entered about student:\nName:{}\nAge:{}\nContact Number:{}\nE-mail ID:{}".format(list_of_studentinfo[0],list_of_studentinfo[1],list_of_studentinfo[2],list_of_studentinfo[3]))
        j=input("Is the information entered about the student affirmative (Yes/No):")
        if j=="Yes":
            write_in_csv(list_of_studentinfo)
            k=input("Do you want to enter information about another student (Yes/No):")
            if k=="Yes":
                i=True
            elif k=="No":
                i=False
        elif j=="No":
            print("Enter the information of the student again:")
    
