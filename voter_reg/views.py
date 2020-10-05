from django.shortcuts import render,redirect 
import pandas as pd 
import csv 
import random 
from datetime import date, datetime 

def registration(request): 
    
    #html_data will contain the data from f4.csv 
    myfile = pd.read_csv('f4.csv') 
    html_data = [] 
    for index,rows in myfile.iterrows(): 
        tdata = { 
            'CID':rows['Constituency_ID'], 
            'CName':rows['Constituency_Name'] 
        } 
        html_data.append(tdata)
    msg = ""
    nndata = []
    if request.POST:

        #Input from web-page
        name = (request.POST['name'])
        constituency_id = int(request.POST['constituency_id'])
        ph_no = (request.POST['ph_no'])
        address = request.POST['address']
        dob = str(request.POST['dob'])
        dd = dob[8:10]; dd = int(dd)
        mm = dob[5:7]; mm = int(mm)
        yy = dob[0:4]; yy = int(yy)
        #voter_id (Randomly Generated)
        voter_id = random.randint(100000,999999)
        # print(voter_id)

        #Checking age, >=18 or not
        age = 0
        born = date(yy, mm, dd)
        today = date.today() 
        try:  
            birthday = born.replace(year = today.year) 

        # raised when birth date is February 29 
        # and the current year is not a leap year 
        except ValueError:  
            birthday = born.replace(year = today.year, 
                    month = born.month + 1, day = 1) 

        if birthday > today: 
            age = today.year - born.year - 1
        else: 
            age = today.year - born.year 

        #Check for proper constituency ID
        chk = pd.read_csv('f4.csv')
        chk = pd.DataFrame(chk)
        chk = chk[['Constituency_ID']]
        chk1 = chk.to_numpy()


        #Output
        if constituency_id not in chk1:
            msg = "Incorrect Constituency_ID, No such ID in database(f4.csv)"
            return render(request,'registration.html',{'f4':html_data,'msg':msg})

        elif (age<18):
            msg = "Age is less than 18, Registration is unsuccessful"
            return render(request,'registration.html',{'f4':html_data,'msg':msg})
        
        #Everything proper
        else:
            ndata ={
                    'voter_id' : voter_id,
                    'constituency_ID':constituency_id,
                    'ph_no':ph_no,
                    'add':address,
                    'dob' : dob
                }
            nndata.append(ndata)

            msg = '''Registration is successful, Entering data in Database(f1.csv) \n
                     Please remember the Voter_ID for future reference'''
            with open('f1.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([voter_id,constituency_id,ph_no,address,dob])
                # print('-->>>>>>',voter_id,member_ID,date1,current_time)
            return render(request,'registration.html',{'f4':html_data,'data':nndata,'msg':msg})

    else:
        return render(request,'registration.html',{'f4':html_data,'msg':msg})
# def error(request):
#     return render(request,'error.html' )

