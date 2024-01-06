create database project;
use project;
CREATE TABLE Book_det (
    B_id INT NOT NULL PRIMARY KEY,
    B_name VARCHAR(255) NOT NULL,
    B_price DECIMAL(10, 2),
    available BOOLEAN
);
INSERT INTO Book_det (B_id, B_name, B_price, available)
VALUES
    (1, 'Book 1', 19.99, true),
    (2, 'Book 2', 24.99, true),
    (3, 'Book 3', 14.99, false),
    (4, 'Book 4', 29.99, true),
    (5, 'Book 5', 9.99, false);
select * from Book_det;

CREATE TABLE Students_det (
    s_roll INT NOT NULL,
    s_name VARCHAR(255) NOT NULL, s_mob VARCHAR(15),
    date_of_borrow DATE, date_of_return DATE,s_id INT,
    PRIMARY KEY (s_roll),
    FOREIGN KEY (s_id) REFERENCES Book_det(B_id)
);
INSERT INTO Students_det (s_roll, s_name, s_mob, date_of_borrow, date_of_return, s_id)
VALUES
    (1, 'John Doe', '123-456-7890', '2023-11-01', '2023-11-15', 1),
    (2, 'Jane Smith', '987-654-3210', '2023-10-15', '2023-11-05', 2),
    (3, 'Alice Johnson', '555-123-7777', '2023-11-10', '2023-11-30', 3),
    (4, 'Bob Wilson', '888-999-1111', '2023-11-05', '2023-11-25', 4),
    (5, 'Eva Davis', '777-333-2222', '2023-10-20', '2023-11-10', 5);
select * from Students_det;

CREATE TABLE book_details (
    b_id INT NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255), PRIMARY KEY (b_id),
    FOREIGN KEY (b_id) REFERENCES Book_det(B_id)
);
INSERT INTO book_details (b_id, author, publisher)
VALUES
    (1, 'Author 1', 'Publisher A'),
    (2, 'Author 2', 'Publisher B'),
    (3, 'Author 3', 'Publisher C'),
    (4, 'Author 4', 'Publisher D'),
    (5, 'Author 5', 'Publisher E');
select * from book_details;
CREATE TABLE about_std (
    roll_no INT NOT NULL, branch VARCHAR(255),
    sec VARCHAR(10), semester char(10),
    PRIMARY KEY (roll_no),
    FOREIGN KEY (roll_no) REFERENCES students_det(s_roll)
);
INSERT INTO about_std (roll_no, branch, sec, semester)
VALUES
    (1, 'Computer Science', 'A', '5'),
    (2, 'Mechanical Engineering', 'B', '6'),
    (3, 'Electrical Engineering', 'C', '3'),
    (4, 'Civil Engineering', 'A', '4'),
    (5, 'Physics', 'D', '7');
select * from about_std;


