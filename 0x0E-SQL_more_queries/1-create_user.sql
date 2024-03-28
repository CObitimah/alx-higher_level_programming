-- creates the MySQL server user user_0d_1 and grant all privilleges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED
BY 'user_0d_1_pwd';
GRANT ALL PRIVILLEGES ON * . * TO user_0d_1@localhost;
