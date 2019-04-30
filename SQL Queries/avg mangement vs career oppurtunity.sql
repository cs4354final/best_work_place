SELECT c.[company], AVG(c.[mangemnet_stars]) as avg_mngm_stars, AVG(c.[carrer_opportunities_rating]) as avg_career_opp
FROM [dbo].[employee_reviews] c, [dbo].[employee_numbers] m
WHERE c.[company] = m.[company_name] GROUP BY c.[company]