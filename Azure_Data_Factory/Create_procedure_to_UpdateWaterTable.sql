USE [Sales_DWH]
GO

INSERT INTO [dbo].[watertable] (
    [table_name],
    [last_date]
)
VALUES
    ('crm_cust_info', '2000-01-01'),
    ('crm_prd_info', '2000-01-01'),
    ('crm_sales_details', '2000-01-01'),
    ('erp_cust_az12', '2000-01-01'),
    ('erp_loc_a101', '2000-01-01'),
    ('erp_px_cat_g1v2', '2000-01-01');

GO

CREATE OR ALTER PROCEDURE UpdateWaterTable
    @table_name VARCHAR(200),
    @last_date VARCHAR(20)
AS
BEGIN
    UPDATE watertable
    SET last_date = @last_date
    WHERE table_name = @table_name;
END;
