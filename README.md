# Patient Gateway
## Product Mission

Remote Health Application System



## User Stories

- I, the admin, should be able to add a patient, doctor or nurse.

- I, admin or medical professional, have a calendar that I can maintain, show when I can have appointments, and manage all aspects of my calendar.
- I, the patient, should be able to see when I can have an appointment with my doctor and should be able to edit it.
- I, the medical professional, should be able to input all my patients vitals.
- I, the medical professional, should be able to assign a set of connected devices (IoT devices) to the patient where they devices can automatically update the patient Vitals.
- I, the Admin, should be able to add devices and precure devices to be added to the system.
- I, the admin or medical professional, should be able to re-assign devices to other patients.
- I, the patient should be able to leave voice or video message to the medical professional from the web or mobile application.
- I, the patient, should be able to upload images for the medical team to review.
- I, the medical professional should be able to read transcription of the voice messages or video messages and should be able to search them.
- I, the medical professional, should be able to see in color medical terms in the message.
- I, AI developer, should be able to access the data anonymized. 

## Branches

Two branches

Main branch: release ready cody.

Develop:

A branch is created off of main to add a new feature, bug-fix, or other change. Once the work is finished and actions on this branch run succesfully, then the work should be squashed and merged into the main branch.



## Components

### Device Module

Define Interface for devices to ingest data into the system

##### Data Fields 

(including knowing how to attribute the data to a patient)

##### Error Conditions

##### Pull or Push mechanisms

Push mechanisms, Why to choose one versus the other

Make sure you include Temperature, blood pressure, pulse, oximeter, weight and Glucometer and data your system can handle





**Database schema**

![](/img/device_db.png)



### Chat Module

one-on-one chat
