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
		('Laptop'),
		('Desktop')
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
		)
		insert into Contact (Phone,Email) values
		('111-111-1111','one@email.com'),
		('222-222-2222','two@email.com'),
		('333-333-3333','three@email.com'),
		('444-444-4444','four@email.com'),
		('555-555-5555','five@email.com'),
		('666-666-6666','six@email.com'),
		('777-777-7777','seven@email.com'),
		('888-888-8888','eight@email.com'),
		('999-999-9999','nine@email.com'),
		('1010-101-1010','ten@email.com')
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
		(1000, '123 A Street','','Miami','Florida','United States','33333'),
		(1002, '3715 B Street','','Los Angeles','California','United States','55555'),
		(1003, '789 C Road','','Nashville','Tenessee','United States','77777'),
		(1004, '3185 B Street','','Los Angeles','California','United States','55555'),
		(1005, '789 C Street','','Richmond','Virginia','United States','77777'),		
		(1006, '8163 A Ln','Apt 1','Jacksonville','Florida','United States','22222'),
		(1007, '74561 B Street','','San Francisco','California','United States','55555'),
		(1008, '3595 C Street','','Knoxville','Tenessee','United States','747474'),
		(1009, '315 B Ave','','New York City','New York','United States','55555'),
		(1001, '84786 C Street','','Savanna','Georgia','United States','66666')
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
			CPU_GHz float,
			RAM_GB int,
			Storage_GB int,
			Price decimal(8,2),
			IsDefective bit
		)
end
'''

Create_Index_Product_Table = '''
if ((select count(object_id) from sys.indexes where name = 'inx_ProductID_ProductName') = 0 
	and (select count(object_id) from sys.indexes) < 999) 
	begin
		Use Electronics_Store
		create index inx_ProductID_ProductName
		on dbo.Product (ProductID,ProductName)
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

Insert_Poducts = '''
insert into Product
values(?,?,?,?,?,?,?,?)
'''

Get_Products_Data = '''
/*with Active_Products as (
select top 10 percent ProductID
from Product p
order by Price desc)
select 
c.CategoryName,
p.ProductName,
p.Price, 
p.CPU_GHz,
p.RAM_GB,
p.Storage_GB,
l.StreetName, 
--isnull(replace(l.Unit,'',null),'N/A') as Unit,
l.LocationID,
co.Email,
co.Phone
from Product p
join Active_Products ap on ap.ProductID = p.ProductID
Join Category c on p.CategoryID = c.CategoryID
join Location l on p.LocationID = l.LocationID
join Contact co on l.ContactID = co.ContactID
where p.IsDefective = 0
or p.IsDefective is null
order by p.ProductName asc*/

select
c.CategoryName,
p.ProductName,
p.Price, 
p.CPU_GHz,
p.RAM_GB,
p.Storage_GB,
l.StreetName, 
--isnull(replace(l.Unit,'',null),'N/A') as Unit,
l.LocationID,
co.Email,
co.Phone
from Product p
Join Category c on p.CategoryID = c.CategoryID
join Location l on p.LocationID = l.LocationID
join Contact co on l.ContactID = co.ContactID
where p.IsDefective = 0
or p.IsDefective is null
order by p.Price asc
'''

Refresh_Price_Per_Location = '''
if(exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'PricePerLocation'))
	begin
		drop table PricePerLocation
	end
create table PricePerLocation(
	PricePerLocationID int identity(1000,1) primary key not null,
	CategoryName nvarchar(40),
	LocationID int,
	TotalPrice decimal(14,2)
)
insert into PricePerLocation 
	(CategoryName,LocationID,TotalPrice)
	select 
	c.CategoryName,
	l.LocationID,
	sum(p.Price)
	from Product p
	left join Category c on c.CategoryID = p.CategoryID
	left join Location l on l.LocationID = p.LocationID
	group by c.CategoryName,l.LocationID
	SET IDENTITY_INSERT PricePerLocation ON 
'''

Get_Price_Per_Location='''
select * from dbo.PricePerLocation
'''

'''
--Testing
--drop index Product.inx_ProductID_ProductName 
--drop table product
--drop table location
--drop table Contact
--drop table category
--drop table Total_Inventory_Value
'''