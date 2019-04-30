SELECT c.[company], AVG(c.[comp_benefit_stars]) as company_benifit_stars, m.[early_median_pay]
FROM [dbo].[employee_reviews] c, [dbo].[employee_numbers] m
WHERE c.[company] = m.[company_name] GROUP BY c.[company], m.[early_median_pay]