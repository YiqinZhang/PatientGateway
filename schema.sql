DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS chat;
DROP TABLE IF EXISTS appointment;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    role TEXT CHECK( role IN ('admin','doctor','nurse','patient','family','developer') ) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_type TEXT NOT NULL CHECK (data_type IN ('Temperature', 'Weight','Pulse', 'Systolic_blood_pressure',
                                                 'Diastolic blood pressure','Glucose level', 'Oxygen level')),
    measurement INTEGER,
    units VARCHAR,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    nurse_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES user (id),
    FOREIGN KEY (doctor_id) REFERENCES user (id),
    FOREIGN KEY (nurse_id) REFERENCES user (id)
);

CREATE TABLE chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER NOT NULL,
    to_id INTEGER NOT NULL,
    format TEXT CHECK( format IN ('message','image','voice','video') ) NOT NULL,
    transcript VARCHAR NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES user (id),
    FOREIGN KEY (to_id) REFERENCES user (id)
);

CREATE TABLE appointment (
    a_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INT NOT NULL, 
    patient_id INT NOT NULL,
    appointment_date DATETIME, 
    start TIME,
    finish TIME,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doctor_id) REFERENCES user (id),
    FOREIGN KEY (patient_id) REFERENCES user (id)
);