Created by - Aditya Thakur

This text file contains some basis information about assignment :-

It contains basically three webpages : (First two for Part - 1 and third one for part - 2)
	
	(1) Voter Registration - Where a Voter Registration is done, basic checks like whether person is greater than 18 years or not, etc.
				 If all the entered data is correct, a unique voter ID is assigned to the voter
				 Also at the same time this data is entered to f1.csv
				 
				 If data is improper appropriate message is shown.
	
	
	(2) Online Voting System - Where voter can cast vote, after the successful login, person is redirected to the voting page
				   In this page, person selects the member and casts vote.
				   Also other verification is done like no attempt of multiple voting,etc.
				   The data is entered to f3.csv, after successful voting.


	(3) Administrator Pannel - This is controlled by administrator, if some new person is standing for election, his/her data is entered
				   using this web-page.
				   A unique member_id is assigned to the person after successfull registartion.
				   Also at the same time this data is entered to f2.csv

The views.py file in each of the folders contains the logic in python.
Also the templates folder contains the .html files, refer it to see the scripting part. 

***** CSV files *****

1) f1.csv - Store Voter information.
2) f2.csv - Information of candidates standing in election.
3) f3.csv - Data related to voting ( When person gives vote to a candidate )
4) f4.csv - Information related to constituency.

***** URL's ***** 

(1) Voter Registration - http://localhost:8000/voter_reg/registration
(2) Online Voting Login - http://localhost:8000/cast_vote/login
(3) Administrator Pannel - http://localhost:8000/main_project/main_page
 
If django not installed,then install it using,
pip install django

Run the Project :-

--> Open cmd, Simply reach the folder which contains the project.
--> To runserver, Type - python manage.py runserver, Server is running now.
--> Then, goto browser and enter any of the URL's mentioned above.

