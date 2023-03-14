# LifeSourceBloodBankWebsite
This is our Blood Bank website project for CS 476 at the University of Regina. 
Problem Definition: 

Blood Donation is an integral part of healthcare systems and is considered to be a medical application domain and is generic since everyone will be able to use it and is not a specific customized customer who has requested it. This project, is used in many cases, including during critical operations, or when the patient has lost blood, saving lives in the process. As Canadian Blood mentions, “Half of all Canadians will either need blood or know someone who will need blood at some point in their lives. Yet only four percent of Canadians donate. ''[1] There are many ways one can donate Blood, which can be confusing to potential donors. Our goal is to create a friendly and easy to use website where donors and blood donation services can easily connect with one another.
            A donor will easily be able to create a profile, donate blood, view history of donations, edit their profile, answer surveys/questionnaires (Eligibility quiz). Restrictions, such as a maximum of one blood donation within 3–4 months, will be automatically calculated by the website and provided to the user. The donor will easily schedule appointments at hospitals and donation sites. 
        Similarly, blood donation organizations will be able to view the donors’  history of donation, set donation schedules. Thus, our website will provide a unified service which will make blood donation and reception easier for donors and blood donation organizations. 



Admin:

Create Admin account using the following command:
python manage.py createsuperuser
After Login, can see Unit of blood of each blood group available, Number Of Donor, Number of blood request, Total Unit of blood on Dashboard.
Can Create, View, Update, Delete Events/Appointments.
Can View Donation appointments history  made by donors.
 
 
 
Donor

Donor can create an account by providing basic details.
After Login, Donor see available appointments then can book best time slot suited for them.
Donor can see previous and current appointments they have booked.  
 

HOW TO RUN THIS PROJECT

Install Python(3.9.13) (Don't Forget to Tick Add to Path while installing Python)


Download This Project Zip Folder and Extract it


Move to project folder in Terminal. Then run the following Commands:

python -m venv env


pip install -r requirements. txt


python manage.py makemigrations


python manage.py migrate


python manage.py runserver



Now enter following URL in Your Browser Installed On Your Pc
http://127.0.0.1:8000/
