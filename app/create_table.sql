CREATE TABLE IF NOT EXISTS meteo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATE NOT NULL,
    temperature DECIMAL(5,2) NOT NULL,
    description VARCHAR(255),
    humidite INT,
    vent DECIMAL(5,2),
    ville VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 