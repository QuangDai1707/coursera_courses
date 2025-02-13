CREATE TABLE MyDimDate (
    dateid INT PRIMARY KEY,
    date DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL,
    quarterName VARCHAR(2) NOT NULL,
    month INT NOT NULL,
    monthname VARCHAR(255) NOT NULL,
    day INT NOT NULL,
    weekday INT NOT NULL,
    weekdayName VARCHAR(255) NOT NULL
);

CREATE TABLE MyDimWaste (
    wasteid INT PRIMARY KEY,
    wastetype VARCHAR(255)
);

CREATE TABLE MyDimZone (
    zoneid INT PRIMARY KEY,
    zonename VARCHAR(255)
);

CREATE TABLE MyFactTrips (
	tripid INT PRIMARY KEY,
	dateid INT,
    zoneid INT,
    wasteid INT,
    wastecollected DECIMAL (10, 2),
	FOREIGN KEY (dateid) REFERENCES MyDimDate(dateid),
    FOREIGN KEY (wasteid) REFERENCES MyDimWaste(wasteid),
    FOREIGN KEY (zoneid) REFERENCES MyDimZone(zoneid)
);



