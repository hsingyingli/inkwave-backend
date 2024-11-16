-- migrate:up
CREATE TABLE blogs (
    id BIGSERIAL PRIMARY KEY,
    public_id UUID DEFAULT gen_random_uuid() UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    content JSON NOT NULL,
    author_id INT8 NOT NULL,
    published_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT (now()),
    updated_at timestamptz NOT NULL DEFAULT (now())
);


CREATE UNIQUE INDEX idx_blogs_id_author_id ON blogs (public_id, author_id);

ALTER TABLE blogs
ADD CONSTRAINT fk_author
FOREIGN KEY (author_id) REFERENCES users(id)
ON DELETE CASCADE;

-- migrate:down

DROP TABLE IF EXISTS blogs;
