# Patient Gateway
## Product Mission

A Remote Health Application System provides a platform where patients can manage their medical data, make appointments, and query with doctors. 
Meanwhile, medical professionals can also manage their appointments, assign examination with devices, updates patient results, and communicate with them.



## User Stories

- Administrators
  - Add users to the system and change their roles ('admin', 'doctor', 'nurse', 'patient', 'family', 'developer').
  - Add devices to the system and modify devices (add, enable, disable, remove).
  - Add data and modify data.
  - Manage events on the calendar.
- Medical professionals (nurses and doctors)
  - Browse patients data.
  - Assign devices to patients.
  - Enter medical data for patients. 
  - Chat with patients.
  - Access transcriptions of  patients' video or voice messages.
  - Manage their appointements calendar.
- Patients
  - Edit account profile.
  - Access their medical measurements.
  - Communicate with health provider via text, video or voice message.
  - Schedule appointments with their health provider and edit them.
- Developers
  - access anonymized data.



## Branches

Main branch: release ready code.

Module branches: module branches to add and implement new feature. After passing the test, merged into the main branch.



## API

| Page                | Endpoint            | Method |
| ------------------- | ------------------- | ------ |
| index               | /                   | [GET]  |
| login               | /login              | [POST] |
| register            | /register           | [POST] |
| main                | /main               | [POST] |
| user                | /user/<user_id>     | [POST] |
| add user            | /user/add/<user_id> | [POST] |
| add device data     | /device/<user_id>   | [POST] |
| send chat           | /chat/<user_id>     | [POST] |
| get chat history    | /chat/history/<>    | [GET]  |
| delete chat history | /chat/del           | [POST] |



## Components

##### Login page

![](./img/login.png)



### 1. Device Module

Define Interface for devices to ingest data into the system

##### Data Fields 

- Data types and units:
  - Temperature: ("C", "F")
  - Weight: ("kgs", "lbs")
  - Pulse:("bpm")
  - Systolic blood pressure: ("mmHg")
  - Diastolic blood pressure: ("mmHg")
  - Glucose level: ("mg/dL")
  - Oxygen level: (%)

- Error Conditions:

  - Invalid key

  - Invalid device type

  - Invalid units for device

  - Invalid measurements

##### Pull or Push mechanisms

Push mechanisms. Once the results or updates come out, they can be sent out immediately.



**Database schema**

![](./img/device_db.png)



### 2. Chat Module

The Chat Module allows patients to communicate with health providers via text, video, or voice message.

The screenshot below shows the chat module.

![](./img/send_chat.png)

The screenshot below shows the chat history, which stored in the SQLite database.

![](./img/chat_history.png)
