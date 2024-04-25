CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    
);

CREATE TABLE jwt_tokens (
    id SERIAL PRIMARY KEY,
    token VARCHAR(500) NOT NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    
);

CREATE TABLE revoked_tokens (
    id SERIAL PRIMARY KEY,
    token VARCHAR(500) NOT NULL,
    expiration_date TIMESTAMP NOT NULL,
);