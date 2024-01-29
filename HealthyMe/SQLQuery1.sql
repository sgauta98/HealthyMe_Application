UPDATE dbo.all_food_nutrition
SET saturated_fat = ISNULL(saturated_fat, 0)

UPDATE dbo.all_food_nutrition
SET name = REPLACE(name, ',', '')

SELECT TOP (1000) [column1],
      [name],
      [serving_size],
      [calories],
      [total_fat],
      --[saturated_fat]
      [cholesterol],
      [sodium],
      --[choline]
      --[folate]
      --[folic_acid]
      --[niacin]
      --[pantothenic_acid]
      --[riboflavin]
      --[thiamin]
      --[vitamin_a]
      --[vitamin_a_rae]
      --[carotene_alpha]
      --[carotene_beta]
      --[cryptoxanthin_beta]
      --[lutein_zeaxanthin]
      --[lucopene]
      --[vitamin_b12]
      --[vitamin_b6]
      --[vitamin_c]
      --[vitamin_d]
      --[vitamin_e]
      --[tocopherol_alpha]
      --[vitamin_k]
      --[calcium]
      --[copper]
      --[irom]
      --[magnesium]
      --[manganese]
      --[phosphorous]
      --[potassium]
      --[selenium]
      --[zink]
      [protein],
      --[alanine]
      --[arginine]
      --[aspartic_acid]
      --[cystine]
      --[glutamic_acid]
      --[glycine]
      [histidine],
      --[hydroxyproline]
      [isoleucine],
      [leucine],
      [lysine],
      [methionine],
      [phenylalanine],
      --[proline]
      --[serine]
      [threonine],
      --[tryptophan]
      --[tyrosine]
      [valine],
      --[carbohydrate]
      --[fiber]
      --[sugars]
      --[fructose]
      --[galactose]
      --[glucose]
      --[lactose]
      --,[maltose]
      --[sucrose]
      --[fat]
      [saturated_fatty_acids],
      --[monounsaturated_fatty_acids]
      --[polyunsaturated_fatty_acids]
      [fatty_acids_total_trans]
      --[alcohol]
      --[ash]
      --[caffeine]
      --[theobromine]
      --[water]
  FROM [allfood].[dbo].[all_food_nutrition]