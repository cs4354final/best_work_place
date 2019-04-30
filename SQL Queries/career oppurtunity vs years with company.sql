SELECT c.[company], AVG(c.[carrer_opportunities_rating]) as avg_career_oppurtunity, m.[years_with_company]
FROM [dbo].[employee_reviews] c, [dbo].[employee_numbers] m
WHERE c.[company] = m.[company_name] GROUP BY c.[company], m.[years_with_company]