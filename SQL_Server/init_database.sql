use Sales_DWH
GO
IF OBJECT_ID('dbo.last_created_data','U') IS NOT NULL
	DROP TABLE dbo.watertable;

GO
CREATE TABLE watertable(
	table_name varchar(20),
	last_date DATE
);
