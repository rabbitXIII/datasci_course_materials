-- Rohit Gopal - Intro to Data Science Assignment 2 Problem 1
-- subproblem a
select count(*) from frequency where docid = '10398_txt_earn';

-- subproblem b
select count(*) from frequency where docid = '10398_txt_earn' and count=1;

-- subproblem c
select count(*) from 
	( select * 
		from frequency 
		where docid = '10398_txt_earn' and count = 1 
		UNION 
		select * 
		from frequency 
		where docid = '925_txt_trade' and count = 1 );

-- subproblem d
select count(*) from frequency where term like '%parliament%';

-- subproblem e
select count(*) from 
	( select docid, count(*) number_of_terms 
		from frequency 
		group by docid 
		having number_of_terms > 300 );


-- subproblem f
select count(*) from frequency 
	where term = 'world' 
	and docid in ( select docid from frequency where term = 'transactions' );
