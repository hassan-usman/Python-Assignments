"""This code shows a result of five subjects with marks obtained,total marks,percentage of each subject
& the total percentage"""
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
student_name = "Hassan Butt"
print(student_name)
#decoration
line_2 = ("-----------")
print(line_2)
print(line_3)
#Subject,Marks,percentage headings
heading_subject = "subject"
heading_marks = "            Marks Obtained"
heading_percentage = "  Percentage"
print(heading_subject + heading_marks + "   |" + heading_percentage)
#decoration
print (line_3)
#First subject marks obtained,total marks,percentage(print)
s1_name = "Physics"
s1_marks = 45
s1_total_marks = 60
s1_percentage = (45 /60*100)
int_2 = int(s1_percentage)
print(s1_name,"\t\t\t",s1_marks,"/",s1_total_marks,"\t\t|\t",int_2,"%")
#Second subject marks obtained,total marks,percentage(print)
s2_name = "Maths"
s2_marks =    60
s2_total_marks = 75
s2_percentage = (60/75*100)
int_3 = int(s2_percentage)
print (s2_name,"\t\t\t\t",s2_marks,"/",s2_total_marks,"\t\t|\t",int_3,"%")
#Third subject marks obtained,total marks,percentage(print)
s3_name = "Pakistan Studies"
s3_marks = 45
s3_total_marks = 50
s3_percentage = 45 / 50*100
int_4 = int(s3_percentage)
print(s3_name,"\t",s3_marks,"/",s3_total_marks,"\t\t|\t",int_4,"%")
#Forth subject marks obtained,total marks,percentage(print)
s4_name = "Urdu"
s4_marks = 54
s4_total_marks = 75
s4_percentage = 54/75*100
int_5 = int(s4_percentage)
print(s4_name,"\t\t\t\t",s4_marks,"/",s4_total_marks,"\t\t|\t",int_5,"%")
#Fifth subject marks obtained,total marks,percentage(print)
s5_name = "English"
s5_marks = 70
s5_total_marks = 75
s5_percentage = 70/75*100
int_6 = int(s5_percentage)
print(s5_name,"\t\t\t",s5_marks,"/",s5_total_marks,"\t\t|\t",int_6,"%")
print(line_3)
#printing marks obtained and total marks
total = "Total Marks Obtained"
total_marks = s1_marks + s2_marks + s3_marks + s4_marks + s5_marks
print(total,total_marks)
heading_total_marks = "Total Marks"
marks_total = s1_total_marks + s2_total_marks + s3_total_marks + s4_total_marks + s5_total_marks
print(heading_total_marks,"             ",marks_total )
#printing total percentage
heading_total_percentage = "percentage"
total_percentage =  (total_marks / marks_total  * 100)
int_1 = int (total_percentage)
print(heading_total_percentage,"\t\t\t\t\t\t\t\t",int_1,"%")
print(line_3)




































