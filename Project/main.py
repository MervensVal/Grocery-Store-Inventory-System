import db

try:
  db.Create_Reports_Folder()
  db.Create_Tables()
  db.Extract_Products()
  db.Generate_Report1()
  db.Generate_Report2()
except Exception as e:
  print("Error occured during program execution.")
