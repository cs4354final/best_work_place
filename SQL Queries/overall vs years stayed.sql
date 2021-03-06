SELECT c.[company], AVG(c.[overall_ratings]) as average_overall_ratings, m.[years_with_company]
FROM [dbo].[employee_reviews] c, [dbo].[employee_numbers] m
WHERE c.[company] = m.[company_name] GROUP BY c.[company], m.[years_with_company]