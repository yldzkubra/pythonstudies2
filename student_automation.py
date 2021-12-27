class students:
 def __init__(self):
     self.calisma=True

 def program(self):
     selection=self.menu_selection()

     if selection==1:
          self.student_registration()
     if selection==2:
          self.student_remove()
     if selection==3:
          self.student_info()
     
 def menu_selection(self):
      selection=int(input("Öğrenci otomasyonuna hoş geldiniz \n öğrenci kayıt için 1 \n öğrenci silmek için 2 \n öğrenci bilgisi görmek için 3 \n tuşlayınız: "))
      while selection<1 or selection>3 :
           selection=int(input("lütfen belirtilen seçeneklerden birini girin: "))
      return selection

 def student_registration(self): 

     name=input("öğrenci adını girin: ")
     surname=input("öğrenci soyadını girin: ")
     Class=input("öğrenci sınıfını girin: ")
     age=input("öğrenci yaşını girin: ")
     gender=input("öğrenci cinsiyetini girin: ")

     with open("student_information.txt","r",encoding="utf-8") as file :
          studentlist=file.readlines()
          if len(studentlist)==0:
               id=1
          else:
               id=len(studentlist)+1
     with open("student_information.txt","a",encoding="utf-8") as file :
          file.write(str(id)+')'+name+' '+surname+' '+Class+'.'+'sınıf'+' '+'yaş'+':'+age+' '+gender+'\n')

 def student_info(self):
     number=input("bilgilerini görmek istediğiniz öğrencinin numarasını girin: ")
     with open("student_information.txt","r",encoding="utf-8") as file:
          liste=file.readlines()  
     for i in range(len(liste)) :
          if liste[i][0:1]==number:
               print(liste[i])
          
     
 def student_remove(self):
     number=input("silmek istediğiniz öğrencinin numarasını girin: ")
     with open("student_information.txt","r",encoding="utf-8") as file :
          removelist=file.readlines()
          for i in range(len(removelist)) :
            if removelist[i][0:1]==number:
               removelist.pop(i)
          file.close()
     with open("student_information.txt","w",encoding="utf-8") as file :
          for i in removelist:
               file.write(i)


student=students()
while student.calisma:
     student.program()