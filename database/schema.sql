CREATE TABLE financial_data (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    revenue TEXT,
    expenses TEXT
);
-- Add more tables as needed, e.g., for users or reports