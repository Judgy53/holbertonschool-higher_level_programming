-- Script that converts database hbtn_0c_0,  first_table and field name to UTF8

-- Alter hbtn_0c_0 charset to utf8
ALTER DATABASE hbtn_0c_0 
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter table first_table charset to utf8
ALTER TABLE hbtn_0c_0.first_table 
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
