--Inspect stream and chat tables
SELECT *
FROM stream
LIMIT 20;

SELECT *
FROM chat
LIMIT 20;

--Find unique games and channels in stream table
SELECT DISTINCT(game)
FROM stream;

SELECT DISTINCT(channel)
FROM stream;

--Games ordered by number of viewers, descending from highest to lowest
SELECT game, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

--Number of 'League of Legends' viewers by country, descending from highest to lowest
SELECT country, COUNT(*)
FROM stream
WHERE game = 'League of Legends' AND country IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;

--Create a genre column based on game title, show game and genre ordered by number of viewers
SELECT game,
  CASE
    WHEN game = 'League of Legends' THEN 'MOBA'
    WHEN game = 'Dota 2' THEN 'MOBA'
    WHEN game = 'Heroes of the Storm' THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive' THEN 'FPS'
    WHEN game = 'DayZ' THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved' THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

--Hourly active users in stream for each hour, listed in descending order by count
SELECT strftime('%H', time) AS 'hour', COUNT(*) AS 'viewer count'
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

--How many distinct devices in this dataset have logged onto a stream as well as a chat?
SELECT COUNT(DISTINCT(chat.device_id))
FROM chat
INNER JOIN stream 
ON chat.device_id = stream.device_id;

--At which hour of the day does each channel have the most viewers?
SELECT channel, strftime('%H', time) AS 'hour', COUNT(*) AS 'count'
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

--What are the countries in which, relatively speaking, stream viewers are most likely to log into the chat as well?
SELECT stream.country, (CAST(COUNT(chat.device_id) AS float)/CAST(COUNT(stream.device_id) AS float)) AS chat_to_stream_ratio
FROM stream
LEFT JOIN chat ON stream.device_id = chat.device_id
WHERE stream.country IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;


