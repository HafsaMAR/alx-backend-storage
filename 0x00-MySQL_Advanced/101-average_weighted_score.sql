-- stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_weight FLOAT;
    DECLARE weighted_sum FLOAT;
    DECLARE avg_weighted_score FLOAT;

    -- Declare cursor for iterating through users
    DECLARE cur_users CURSOR FOR
        SELECT id FROM users;
    
    -- Declare continue handler for cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur_users;
    
    -- Iterate through users
    users_loop: LOOP
        FETCH cur_users INTO user_id;
        
        -- Exit loop if no more users
        IF done THEN
            LEAVE users_loop;
        END IF;

        -- Reset variables
        SET total_weight = 0;
        SET weighted_sum = 0;

        -- Calculate total weight
        SELECT SUM(weight) INTO total_weight
        FROM projects;

        -- Calculate weighted sum
        SELECT SUM(score * weight) INTO weighted_sum
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Calculate average weighted score
        IF total_weight > 0 THEN
            SET avg_weighted_score = weighted_sum / total_weight;
        ELSE
            SET avg_weighted_score = 0;
        END IF;

        -- Update average weighted score in the users table
        UPDATE users
        SET average_score = avg_weighted_score
        WHERE id = user_id;
    END LOOP;

    CLOSE cur_users;
END;
//

DELIMITER ;