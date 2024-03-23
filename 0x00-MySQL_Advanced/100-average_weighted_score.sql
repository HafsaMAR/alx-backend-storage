-- stored procedure


DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN p_user_id INT
)

BEGIN
    DECLARE total_weight FLOAT;
    DECLARE sum_weighted FLOAT;
    DECLARE weighted_average_score FLOAT;

    SELECT SUM(weight) INTO total_weight FROM projects;

    SELECT SUM(score * weight) INTO sum_weighted
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = p_user_id;

    IF total_weight > 0 THEN 
        SET weighted_average_score = sum_weighted / total_weight;
    ELSE 
        SET weighted_average_score = 0;

    END IF;
    UPDATE users
    SET average_score = weighted_average_score WHERE id = p_user_id;
END;
//