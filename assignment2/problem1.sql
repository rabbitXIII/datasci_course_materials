-- Rohit Gopal - Intro to Data Science Assignment 2 Problem 1
-- subproblem a
select count(*) from frequency where docid = '10398_txt_earn';

-- subproblem b
select count(*) from frequency where docid = '10398_txt_earn' and count=1;

-- subproblem c
select count(*) from 
	( select * from frequency where docid = '10398_txt_earn' and count = 1 
		UNION 
		select * from frequency where docid = '925_txt_trade' and count = 1 );

-- subproblem d
select count(*) from frequency where term like '%parliament%';

-- subproblem e


-- subproblem f
