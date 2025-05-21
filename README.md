# Ain Acdeamy


<br />
<div>

<h3 align="center">Ain Acdeamy</h3>

  <p align="center">
    <strong>Odoo based Eduction</strong>
  </p>
</div>

<p align="center"><strong>Made with ❤️ in <a href="https://www.shebak.com" target="_blank">Shebak</a></strong></p>


[![Watch the video](https://github.com/user-attachments/assets/bae0d29c-e86e-4067-b1db-e7c76c951db9)](https://github.com/user-attachments/assets/bae0d29c-e86e-4067-b1db-e7c76c951db9)



## About The Project
AinAcademy is an ERP module for managing training operations, built for Odoo 17. It includes instructor-led sessions, room scheduling, session attendance, and conflict validation.

## Features
- **Courses with difficulty levels and assigned instructors.**

- **Sessions with start/end time, display name, and dynamic status**

- **Student and instructor management**
  
- **Room scheduling with conflict validation**
  
- **Reservation and unreservation via wizards**


## Built With

* [![Python][Python]][Python-url]
* [![Odoo](https://img.shields.io/badge/Odoo-714B67?logo=Odoo&logoColor=fff)](#)


## Models

| Model                  | Description                          |
|-----------------------|--------------------------------------|
| ainacademy.partner   | Represents both students and instructors |
| ainacademy.course    | Defines course info and instructor   |
| ainacademy.session   | Defines session schedule and links   |
| ainacademy.room      | Represents rooms for sessions        |
| room.reservation.wizard | Used to assign a room to a session |
| room.unreserve.wizard   | Used to unassign room from a session |

## Logic 
- A session must have an instructor and a course before it can be confirmed.
- Rooms can only be assigned to one session at a time (no overlaps).
- Sessions become active only during their start–end date range.
- The display name of a session is dynamically computed as: Session Name - Course Name.
- The room's available date updates automatically based on its latest session.


### Room Un-Rresrvation

#### Case 1 session

![Image](https://github.com/user-attachments/assets/2f77f092-c98e-4fa4-a057-92e009df21f7)

#### Case All Sessions

![Image](https://github.com/user-attachments/assets/1a0cb68e-2cef-430f-ad97-4298f09befc3)


### Entity Flowcharts

1. **Partner**
 
 ![Image](https://github.com/user-attachments/assets/2bb96ed2-8580-48f4-a532-5eae26eabea6)

2. **Course**
 
 ![Course Diagram](https://github.com/user-attachments/assets/56b5016c-9cf3-4e8e-853b-28e7250cd8dd)

3. **Room**
 
 ![Room Diagram](https://github.com/user-attachments/assets/11ecbf46-4ecf-499a-9af2-eccfc236a8da)

4. **Session**
 
 ![Session Diagram](https://github.com/user-attachments/assets/294f0c2c-ce84-4b59-862c-d5e7b4e745bd)
     
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Odoo 17.0 installed and configured
- PostgreSQL server running
- Python ≤ 3.11
- Virtual environment (recommended)
- A custom addons directory set up in your Odoo configuration

### Installation Steps

1. Clone the repository into your custom addons directory:

   ```sh
   git clone https://github.com/your-username/ainacademy.git
   ```

2. Activate your Python virtual environment:

   ```sh
   source venv/bin/activate
   ```

3. Install Odoo requirements (if not already installed):

   ```sh
   pip install -r odoo/requirements.txt
   ```

4. Update module list and upgrade the module:

   ```sh
   ./odoo-bin -d your_database_name -u ainacademy --addons-path=addons,custom_addons
   ```

5. Run the Odoo server:

   ```sh
   ./odoo-bin -d your_database_name
   ```

6. Log in to Odoo, go to Apps, search for **ainacademy**
   






<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mohammed-fathi-4a08071a7/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://docs.djangoproject.com/en/3.2/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://docs.python.org/3/
