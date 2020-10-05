from django.shortcuts import render,redirect
import pandas as pd
import csv
import random 
from datetime import date,datetime

html_data=[]
constituency_ID = None
voter_id = None
ndata = []
df4 = []

def login(request):
    global html_data,constituency_ID,voter_id,ndata,df4
    html_data = []
    ndata = []

    #html_data will contain the data from f4.csv
    myfile = pd.read_csv('f4.csv')
    for index,rows in myfile.iterrows():
        tdata = {
            'CID':rows['Constituency_ID'],
            'CName':rows['Constituency_Name']
        }
        html_data.append(tdata)
    msg = ""
    if request.POST:

        #input from webpage
        voter_id = int(request.POST['voter_id'])
        constituency_ID = int(request.POST['constituency_ID'])
        # print(voter_id)
        # print(constituency_ID)

        #Multiple votes checking
        chk = pd.read_csv('f3.csv')
        chk = pd.DataFrame(chk)
        chk = chk[['Voter_ID']]
        chk1 = chk.to_numpy()

        if voter_id in chk1:
            msg = "Attemp of Multiple Vote, your vote is already recorded"
            return render(request,'login.html',{'f4':html_data,'msg':msg})

        #Proper data
        else:
            df = pd.read_csv('f1.csv')
            
            df = pd.DataFrame(df)
            df1 = df[['Voter_ID','Constituency_ID']]
            df1 = pd.DataFrame(df1)
            if ((df1['Voter_ID'] == voter_id) & (df1['Constituency_ID'] == constituency_ID)).any() :
            
                # creating Member_ID and Symbol_name
                kk = pd.Series([constituency_ID]) 
                df2 = pd.DataFrame(kk , columns = ['Constituency_ID'] )

                dfk = pd.read_csv('f2.csv')
                dfk = pd.DataFrame(dfk)

                #Using Merge operation to get all member from provided constituency_ID 
                df3 = pd.merge(df2,dfk,on='Constituency_ID')
                df4 = df3[['Member_ID','Symbol_name']]

                ndata = []
                for index,rows in df4.iterrows():
                    tdata = {
                        'MID':int(rows['Member_ID']),
                        'Sname':rows['Symbol_name']
                    }
                    ndata.append(tdata)

                #successful Login, Forwarding to Voting page
                return redirect('/cast_vote/voting')
            else:
                msg = '''Entered Voter_Id and Constituency_ID not there in Database,\n 
                        Login Unsuccessful'''
                return render(request,'login.html',{'f4':html_data,'msg':msg})

    else:
        return render(request,'login.html',{'f4':html_data})

def voting(request):
    global html_data,constituency_ID,voter_id,ndata,df4
    nndata = []
    msg =""

    # Voting Page
    if request.POST:

        member_ID = int(request.POST['member_ID'])

        #date_of_registration
        today = date.today()
        date1 = today.strftime("%d/%m/%Y")

        #time_stamp_of_registration
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        #Multiple votes checking
        chk = pd.read_csv('f3.csv')
        chk = pd.DataFrame(chk)
        chk = chk[['Voter_ID']]
        chk1 = chk.to_numpy()

        
        if voter_id in chk1:
            return render(request,'multiple.html')

        else:
            
            df5 = df4[['Member_ID']]
            df5 = df5.to_numpy()

            #Checking Proper Member_ID
            if(member_ID in df5):
                with open('f3.csv', 'a+', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([voter_id,member_ID,date1,current_time])
                    # print('-->>>>>>',voter_id,member_ID,date1,current_time)
                
                #Vote is recorded successfully
                msg = "Your Vote is recorded successfully, Entering data in Database(f3.csv)"                
                ndata ={
                    'Voter_ID':voter_id,
                    'constituency_ID':constituency_ID,
                    'member_id':member_ID,
                    'Date':date1,
                    'Time_Stamp':current_time
                }
                nndata.append(ndata)

                return render(request,'voting.html',{'data' : ndata,'msg':msg, 'ndata':nndata})
            else:
                #Error Message
                msg = "Enter Proper Member_ID, your VOTE is not recorded"
                return render(request,'voting.html',{'data' : ndata,'msg':msg, 'ndata':nndata})
    else :
        return render(request,'voting.html',{'data' : ndata,'msg':msg, 'ndata':nndata})


def error(request):
    return render(request,'error.html' )