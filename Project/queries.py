

Create_Category_Table = '''
if(exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'Category'))
	begin
		print 'table already exists'
	end
else
	begin
		print 'creating table Category'
		use Electronics_Store
		create table Category(			
			CategoryID int identity(1000,1) primary key not null,
			CategoryName nvarchar(40) not null
		)
		insert into Category values 
		('Phone'),
		('Laptop'),
		('Desktop'),
		('Tablet'),
		('Watch')
	end
'''


Create_Contact_Table = '''
if(exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'Contact'))
	begin
		print 'table already exists'
	end
else
	begin
		print 'creating table Contact'
		use Electronics_Store
		create table Contact(			
			ContactID int identity(1000,1) primary key not null,
			Phone nvarchar(40),
			Email nvarchar(40),
			ContactType nvarchar(40)
		)
		insert into Contact values
		('111-111-1111','one@email.com','LOC'),
		('222-222-2222','two@email.com','LOC'),
		('333-333-3333','three@email.com','EMP'),
		('444-444-4444','four@email.com','LOC'),
		('555-555-5555','five@email.com','EMP')
	end
'''

Create_Location_Table = '''
if(exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'Location'))
	begin
		print 'table already exists'
	end
else
	begin
		print 'creating table Location'
		use Electronics_Store
		create table Location(			
			LocationID int identity(1000,1) primary key not null,
			ContactID int foreign key references Contact(ContactID),
			StreetName nvarchar(100),
			Unit nvarchar(10),
			City nvarchar(100),
			State nvarchar(40),
			Country nvarchar(100),
			ZipCode nvarchar(10),
		)
		insert into Location (ContactID,StreetName,Unit,City,State,Country,ZipCode) values
		(1003, '123 A Street','Apt 1','Miami','Florida','United States','33333'),
		(1002, '315 B Street','','Los Angeles','California','United States','55555'),
		(1004, '789 C Street','','Nashville','Tenessee','United States','77777'),
		(1001, '315 B Street','','Los Angeles','California','United States','55555'),
		(1000, '789 C Street','','Nashville','Tenessee','United States','77777')
	end
'''

Create_Product_Table = '''
if(exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'Product'))
	begin
		print 'table already exists'
	end
else
	begin
		print 'creating table Product'
		use Electronics_Store
		create table Product(			
			ProductID int identity(1000,1) primary key not null,
			CategoryID int foreign key references Category(CategoryID),
			LocationID int foreign key references Location(LocationID),
			ProductName nvarchar(100),
			CPU_MB int,
			RAM_MB int,
			Storage_MB int,
			OS nvarchar(40),
			Price decimal(8,2),
			Description nvarchar(300),
			IsDefective bit
		)
end

'''

Create_Total_Inventory_Value_Table = '''
if(exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'Total_Inventory_Value'))
	begin
		print 'table already exists'
	end
else
	begin
		print 'creating table Total_Inventory_Value'
		use Electronics_Store
		create table Total_Inventory_Value(			
			Total_Inventory_ValueID int identity(1000,1) primary key not null,
			CategoryID int,
			CategoryName nvarchar(40) not null,
			TotalPrice decimal(15,2) --1,000,000,000,000
		)
end
'''

#Number of placeholders matches your table and CSV file format
Insert_Poducts = '''
insert into Product({0})
values({1})
'''

#Report 1 (Product details from all tables)


#Report 2 (Total non defective inventory value by category)
#Pull & Insert data into new table Total_Inventory_Value