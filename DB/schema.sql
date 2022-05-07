DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS chat;
DROP TABLE IF EXISTS appointment;

CREATE TABLE user (
    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(40) NOT NULL,
    firstname VARCHAR(40) NOT NULL, 
    lastname VARCHAR(40) NOT NULL, 
    gender VARCHAR(20) CHECK (gender IN ('male', 'female')) DEFAULT ('male') NOT NULL, 
    role VARCHAR(20) CHECK (role IN ('doctor', 'nurse', 'patient', 'family', 'admin', 'developer')) NOT NULL DEFAULT ('patient'), 
    phone VARCHAR(20) CHECK (LENGTH(Phone) = 10) DEFAULT (0000000000), 
    dob DATETIME NOT NULL, 
    height_cm INT, 
    weight_kg INT,
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
    content TEXT,
    transcript TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES user (id),
    FOREIGN KEY (to_id) REFERENCES user (id)
);

-- CREATE TABLE appointment (
--     a_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     doctor_id INT NOT NULL,
--     patient_id INT NOT NULL,
--     appointment_date DATETIME,
--     start TIME,
--     finish TIME,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (doctor_id) REFERENCES user (id),
--     FOREIGN KEY (patient_id) REFERENCES user (id)
-- );

CREATE TABLE appointment (
    a_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name VARCHAR NOT NULL,
    patient_name VARCHAR NOT NULL,
    appointment_date VARCHAR,
    start VARCHAR,
    finish VARCHAR,
    symptom TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doctor_name) REFERENCES user (username),
    FOREIGN KEY (doctor_name) REFERENCES user (username)
);