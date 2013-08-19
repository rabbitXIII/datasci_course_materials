-- Rohit Gopal, Data Science Assignment 2 Problem 2
-- multiply two matrices, each in a different table
-- join on a's cols to b's rows and then group by the respective rows and cols in the product matrix
select a.row_num as row, b.col_num as col, sum(a.value*b.value) as value 
	from a, b 
	where a.col_num = b.row_num 
	group by a.row_num, b.col_num;

