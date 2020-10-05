from django.shortcuts import render,redirect
import pandas as pd
import csv
import random 
from datetime import date,datetime

def main_page(request):

    #html_data will contain the data from f4.csv
    html_data=[]
    myfile = pd.read_csv('f4.csv')
    for index,rows in myfile.iterrows():
        tdata = {
            'CID':rows['Constituency_ID'],
            'CName':rows['Constituency_Name']
        }
        html_data.append(tdata)

    if request.POST:

        ndata = []
        #Input from web-page
        member_name = request.POST['member_name'],
        constituency_ID = request.POST['constituency_ID'],
        Symbol_name = request.POST['Symbol_name'],

        img = request.FILES['symbol_img']

        #member_id (Randomly Generated)
        member_id = random.randint(100,999)

        #date_of_registration
        today = date.today()
        date1 = today.strftime("%d/%m/%Y")
        file_link ="./" + Symbol_name[0] + ".jpg"

        #time_stamp_of_registration
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        #Verification
        myfile1 = pd.read_csv('f4.csv')
        tmp = myfile1['Constituency_ID']
        tmp = list(tmp)
        for i in range(0,len(tmp)):
            tmp[i] = str(tmp[i])

        #inserting in f2.csv
        msg = ''
        nndata = []
        if(str(constituency_ID[0]) in tmp):
            with open('f2.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([member_id,constituency_ID[0],Symbol_name[0],file_link,date1,current_time])
            
            ndata = {
                'member_id':member_id,
                'constituency_ID':constituency_ID[0],
                'Symbol_name':Symbol_name[0],
                'file_link':file_link,
                'Date':date1,
                'Time_Stamp':current_time
            }
            
            nndata.append(ndata)
            msg = '''Registration is successful, Entering data in Database(f2.csv) \n
                     Please remember the Member_ID for future reference'''
        else:
            #error msg
            msg = "Enter proper Contituency ID, Data not RECORDED"

        return render(request,'main_page.html',{'data':nndata,'f4':html_data, 'message':msg} )
    else:
        return render(request,'main_page.html',{'f4':html_data})