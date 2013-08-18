-- subproblem a
select count(*) from frequency where docid = '10398_txt_earn';

-- subproblem b
select count(*) from frequency where docid = '10398_txt_earn' and count=1;
