SELECT c.[company], m.[median_age]
FROM [dbo].[employee_reviews] c, [dbo].[employee_numbers] m
WHERE c.[company] = m.[company_name] GROUP BY c.[company], m.[median_age]