-- Tabla Logs nginx
CREATE TABLE IF NOT EXISTS accesslog (
  id serial NOT NULL, 
  log_line json NOT NULL, 
  created_at TIMESTAMP NOT NULL,
  PRIMARY KEY (id)
);