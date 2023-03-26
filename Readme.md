

Features
    1. Multiple users can create and manage multiple incidents
    2. Each incident has a unique ID in the format RMG+Random 5 digit number+Current year(2022) 
       e.g.   RMG345712022
    3. Users can create and edit incident details, including reporter name, incident details, reported date and time, priority, and status
    4. Users can view and edit only the incidents they have created
    5. Users cannot view incidents created by other users
    6. Incidents in the closed state cannot be edited
    7. The system allows for searching incidents using the unique incident ID

Functionality
    1. Creating Users
    2. The system allows  to create multiple users. Each user will have a unique username and password to log in to the system.

Creating Incidents
    Users can create incidents and fill in the incident details, including reporter name, incident details, reported date and time, priority, and status. The system will generate a unique incident ID for each new incident.

Updating Incidents
    Users can edit incidents they have created, including changing incident details, priority, and status. However, incidents in the closed state cannot be edited.

Viewing Incidents
    Users can view incidents they have created. The system will display a list of all incidents created by the user, including their status.

TODO
#Searching Incidents
#The system allows for searching incidents using the unique incident ID. Users can enter the ID in a #search field, and the system will display the incident details.

Requirements
    To run this system, you will need:
    
    Python 3.10.4 
    Sqlite or higher database
    The system files, which can be downloaded from the Github repository

Installation
    Download the necessary appication mentoned above 
    Create a virtual enviornment (recomended)
    Install the required dependencies. run the following command 

    pip install -r requirements.txt

    run the application 
    python manage.py runserver ip:port
