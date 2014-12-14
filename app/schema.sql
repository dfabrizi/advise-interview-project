drop table if exists Accounts;
create table accounts (
  id integer primary key autoincrement,
  email text not null,
  username text not null,
  password text not null
);

insert into accounts (email, username, password) values (" ", " ", " ");

drop table if exists jrsqldev_interview;
create table jrsqldev_interview (
id integer primary key autoincrement,
candidate text not null,
candidate_email text not null,
candidate_phone integer not null,
database_fundamentals text not null,
enterprise__years_experience integer not null,
query_optimization text not null,
facility_large_datasets text not null,
notions_n_tier_architecture text not null,
ETL_processes text not null,
why_advise text not null,
weaknesses text not null,
questions text not null
);

insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience,
query_optimization, facility_large_datasets, notions_n_tier_architecture, ETL_processes, why_advise,
weaknesses, questions) values ("John Smith", "jsmith@gmail.com", 1234567890, "Yes I know plenty about databases", 3, "run smarter queries", "I've worked with massive datasets", "I know plenty about this", 
"I know these processes", "Advise is a rapidly growing company in a great field", "I'm a perfectionist", "What are your plans for expansion in this market?");

insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience,
query_optimization, facility_large_datasets, notions_n_tier_architecture, ETL_processes, why_advise,
weaknesses, questions) values ("Samantha Stephens", "sstephens@email.com", 2126961478, "I understand the fundamentals", 5, "run less unnecessary queries", "I've worked with enormous databases", "I have these notions", "I know these processes", "It's a great company", "I work too hard", "Where are your offices?");

insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience,
query_optimization, facility_large_datasets, notions_n_tier_architecture, ETL_processes, why_advise,
weaknesses, questions) values ("Dan Brown", "dbrown@co.com", 5678453456, "I know databases well", 2, "more concise queries", "Large datbases are easy", "I know a few things", "I know about them", "It seems neat", "I have none", "What are the opportunities for growth?");

insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience,
query_optimization, facility_large_datasets, notions_n_tier_architecture, ETL_processes, why_advise,
weaknesses, questions) values ("Jessie Bolman", "jbolman@gh.com", 1938753076, "I know the basics", 1, "learn how to query better", "I'm familiar with large datasets", "I know the architecture", "I know the processes", "It's the ideal place to work", "I procrastinate", "What are employee benefits?");

insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience,
query_optimization, facility_large_datasets, notions_n_tier_architecture, ETL_processes, why_advise,
weaknesses, questions) values ("Joseph McMann", "jmcmann@aol.com", 4567892645, "I'm familiar with fundamentals", 5, "try to optimize your queries", "I work with large sets of data", "I have a few notions", "These processes interest me", "It's an interesting endeavour", "I get tired easily", "No questions");

insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience,
query_optimization, facility_large_datasets, notions_n_tier_architecture, ETL_processes, why_advise,
weaknesses, questions) values ("Brad Crawford", "bcrawford@gmail.com", 6108764589, "I have the basics down", 7, "I have strategies for optimization", "I have some facility with large data sets", "I've seen the architecture", "I'm familiar with these processes", "It seems like a great company", "I have few weaknesses", "What are health benefits?");

drop table if exists midlevel_dev_interview;
create table midlevel_dev_interview (
id integer primary key autoincrement,
candidate text not null,
candidate_email text not null,
candidate_phone integer not null,
years_experience integer not null,
c_sharp_fluency text not null,
sql_base text not null,
facility_large_datasets text not null,
weaknesses text not null,
why_advise text not null,
questions text not null
);

insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values ("Kevin Kallmyer", "kkallmyer@co.com", 6783452985, 5, "fluent", "solid base", "work with large data sets", "I'm a lefty", "It's a cool company", "Can I further my education?");

insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values ("Casey Lopez", "clopez@gmail.com", 4782963054, 3, "fluency", "good foundation", "Some facility", "I procrastinate", "It seems like a good opportunity", "No questions");

insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values ("David Cheng", "dcheng@yahoo.com", 2387490723, 4, "fluent", "solid foundation", "quality experience", "I'm a perfectionist", "Opportunities are endless", "How much will I make?");

insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values ("Arjun Gupta", "agupta@college.edu", 9872645387, 2, "near fluent", "working knowledge base", "enough experience", "I'm competitive", "It seems fun", "How much vacation time?");

insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values ("Susan Wells", "swells@webmail.org", 3957284590, 3, "fluency", "active learner", "work with corporate data sets", "No weaknesses", "It is exciting", "How is the work environment?");

insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values ("Stacey Philbin", "sphilbin@hotmail.com", 2127893456, 4, "very fluent", "solid growing knowledge base", "greate facility", "I try too hard", "It looks like a great company", "No questions");