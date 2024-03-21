-- Triggers that fires after making order

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders

FOR EACH ROW
BEGIN
    -- update quatity
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
$$

DELIMITER ;