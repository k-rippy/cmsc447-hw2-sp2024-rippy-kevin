DROP TABLE IF EXISTS user_info;

CREATE TABLE user_info (
    Name TEXT NOT NULL,
    Id int NOT NULL PRIMARY KEY,
    Score int NOT NULL DEFAULT 0
);

INSERT INTO user_info (Name, Id, Score) 
    VALUES 
    ("Steve Smith", 211, 80), 
    ("Jian Wong", 122, 92),
    ("Chris Peterson", 213, 91),
    ("Sai Patel", 524, 94),
    ("Andrew Whitehead", 425 , 99),
    ("Lynn Roberts", 626 , 90),
    ("Robert Sanders", 287 , 75);


