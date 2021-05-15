#My school name
school_name = "                Cathedral Higher Secondary School Lahore Cantt"
#Decoration
line_1 = "                ----------------------------------------------"               
print(line_1)
print(line_1)
print(school_name)
print(line_1)
print (line_1)
class_name = "Class"
class_section = "10 B"
print(class_name,class_section)
line_3 = ("-------------------------------------------------")
#My name
student_name = input("Enter student name\t\t\t")
#decoration
line_2 = ("-------------------")
print(line_2)
print(line_3)
#Subject,Marks,percentage headings
subject_name_1 = str(input("Please Enter Name of Subject 1\t\t\t"))
marks_obtained_1  = float(input("PLease Enter Marks Obtained of" + "\t" + subject_name_1 + "\t\t\t"))
maximum_marks_1 = float(input("Please Enter Maximum Marks of" + subject_name_1 + "\t\t\t"))
#printing percentag
percentage_1 = int(marks_obtained_1 /maximum_marks_1*100)
#decoration
print (line_3)
subject_name_2 = input("Please Enter Name of Subject 2\t\t\t")
marks_obtained_2  = float(input("PLease Enter Marks Obtained of"+ "\t" + subject_name_2 + "\t\t\t"))
maximum_marks_2 = float(input("Please Enter Maximum Marks of" + subject_name_2 + "\t" + "\t\t\t"))
#printing percentag
percentage_2 =int(marks_obtained_2 /maximum_marks_2*100)
#decoration
print (line_3)
subject_name_3 = input("Please Enter Name of Subject 3\t\t\t")
marks_obtained_3  = float(input("PLease Enter Marks Obtained of" + subject_name_3+ "\t" + "\t\t\t"))
maximum_marks_3 = float(input("Please Enter Maximum Marks of" + subject_name_3 + "\t" +"\t\t\t"))
#printing percentag
percentage_3 =int(marks_obtained_2 /maximum_marks_2*100)
#decoration
print (line_3)
#decoration
print (line_3)
subject_name_4 = input("Please Enter Name of Subject 4\t\t\t")
marks_obtained_4  = float(input("PLease Enter Marks Obtained of" + "\t" + subject_name_4 + "\t\t\t"))
maximum_marks_4 = float(input("Please Enter Maximum Marks of" + "\t" + subject_name_4 + "\t\t\t"))
#printing percentag 
percentage_4 =int(marks_obtained_2 /maximum_marks_2*100)
#decoration
print (line_3)
#decoration
print (line_3)
subject_name_5 = input("Please Enter Name of Subject 5\t\t\t")
marks_obtained_5  = float(input("PLease Enter Marks Obtained of" + "\t" + subject_name_5 +"\t\t\t"))
maximum_marks_5 = float(input("Please Enter Maximum Marks of" + "\t" + subject_name_5 +"\t\t\t"))
#printing percentag
percentage_5 =int(marks_obtained_2 /maximum_marks_2*100)
#decoration
print (line_3)
total_marks_obtained = int(marks_obtained_1 + marks_obtained_2 +marks_obtained_3 +marks_obtained_4 +marks_obtained_5)
total_max_marks = int(maximum_marks_1 + maximum_marks_2 + maximum_marks_3 +maximum_marks_4 + maximum_marks_5)
total_percentage = int(total_marks_obtained/total_max_marks *100)

#Output
print("Based on the data you provided following is the result card of your student")
print(line_1)
print(line_1)
print(school_name)
print(line_1)
print (line_1)
print(student_name)
print(class_name,class_section)
heading_subject = "subject"
heading_marks = "            Marks Obtained"
heading_percentage = "  Percentage"
print(heading_subject + heading_marks + "   |" + heading_percentage)
#decoration
print (line_3)
print(subject_name_1, "\t\t\t",marks_obtained_1 , "/",maximum_marks_1,"\t\t|\t",percentage_1,"%")
print(subject_name_2, "\t\t\t",marks_obtained_2 , "/",maximum_marks_2,"\t\t|\t",percentage_2,"%")
print(subject_name_3, "\t",marks_obtained_3 , "/",maximum_marks_3,"\t\t|\t",percentage_3,"%")
print(subject_name_4, "\t\t\t",marks_obtained_4 , "/",maximum_marks_4,"\t\t|\t",percentage_4,"%")
print(subject_name_5, "\t\t\t\t",marks_obtained_5 , "/",maximum_marks_5,"\t\t|\t",percentage_5,"%")
print(line_3)
print("Total Marks Obtained",total_marks_obtained,"/",total_max_marks,"\t\t|\t",total_percentage,"%")
print(line_3)
print("The information enteered has been successfully generated into Result Card above. Please press any key to end this program. ")
print(line_3)
input()