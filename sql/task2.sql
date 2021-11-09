WITH group_1 AS (
SELECT home_team, away_team, COUNT(*) AS col
FROM event_entity
GROUP BY 1, 2
),
social_table AS (
SELECT t1.home_team as t1_home_team, t1.away_team as t1_away_team, t1.col as t1_col, t2.home_team as t2_home_team, t2.away_team as t2_away_team, t2.col as t2_col
FROM group_1 AS t1
LEFT JOIN group_1 AS t2 ON t1.home_team = t2.away_team AND t2.home_team = t1.away_team
),
union_data AS (
SELECT t1_home_team, t1_away_team, t1_col
FROM social_table
UNION ALL
SELECT t2_away_team, t2_home_team, t1_col
FROM social_table
)
SELECT CONCAT_WS('-',t1_home_team, t1_away_team) AS game, SUM(t1_col) AS games_count
FROM union_data
WHERE t1_home_team IS NOT NULL AND t1_away_team IS NOT NULL
GROUP BY 1
ORDER BY 2 ASC;