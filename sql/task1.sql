SELECT bid.client_number,  COUNT(ee.win) as Побед, COUNT(ec.lose) as Поражений
FROM bid
    LEFT JOIN (
        SELECT ev.play_id, ev.value, ev.outcome AS win
        FROM event_value AS ev
        WHERE ev.outcome = 'win'
    ) ee ON bid.play_id = ee.play_id AND  bid.coefficient = ee.value
    LEFT JOIN (
        SELECT ev.play_id, ev.value, ev.outcome AS lose
        FROM event_value AS ev
        WHERE ev.outcome = 'lose'
    ) ec ON bid.play_id = ec.play_id AND  bid.coefficient = ec.value

WHERE bid.client_number IS NOT NULL
GROUP BY bid.client_number;