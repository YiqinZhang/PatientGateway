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
    email VARCHAR(40) NOT NULL,
    gender VARCHAR(20) CHECK (gender IN ('male', 'female', 'other')) DEFAULT ('male') NOT NULL,
    role VARCHAR(20) CHECK (role IN ('doctor', 'nurse', 'patient', 'family', 'admin', 'developer','MP')) NOT NULL DEFAULT ('patient'),
    phone VARCHAR(20) CHECK (LENGTH(Phone) = 10) DEFAULT (0000000000), 
    dob DATETIME NOT NULL, 
    height_cm INT, 
    weight_kg INT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE device (
    d_id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_type TEXT NOT NULL CHECK (data_type IN ('temperature', 'weight','pulse', 'systolic blood pressure',
                                                 'diastolic blood pressure','glucose level', 'Oxygen level')) NOT NULL,
    measurement INTEGER NOT NULL,
    doctor_name VARCHAR NOT NULL,
    patient_name VARCHAR NOT NULL,
    nurse_name VARCHAR NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (doctor_name) REFERENCES user (username),
    FOREIGN KEY (patient_name) REFERENCES user (username)
    FOREIGN KEY (nurse_name) REFERENCES user (username)
);

CREATE TABLE chat (
    c_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender VARCHAR(40) NOT NULL,
    recipient VARCHAR(40) NOT NULL,
    type VARCHAR(40) CHECK( type IN ('message','image','voice','video') ) NOT NULL,
    content TEXT NOT NULL,
    transcript TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender) REFERENCES user (username),
    FOREIGN KEY (recipient) REFERENCES user (username)
);



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
    FOREIGN KEY (patient_name) REFERENCES user (username)
);