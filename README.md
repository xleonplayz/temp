# Test Repository - Frontend Backend Connection Analyzer

A sample full-stack application for testing the code analyzer's frontend-backend connection detection.

## Structure

```
temp/
├── backend/           # FastAPI Python Server
│   ├── api/           # API Routes
│   ├── services/      # Business Logic
│   └── db/            # Database Layer
└── frontend/          # React/Next.js App
    └── src/
        ├── api/       # Axios API Clients
        └── hooks/     # React Hooks with fetch()
```

## Backend Routes

- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user

- `GET /api/users` - List all users
- `GET /api/users/{id}` - Get user by ID
- `POST /api/users` - Create user
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user

- `GET /api/posts` - List all posts
- `GET /api/posts/{id}` - Get post by ID
- `GET /api/posts/user/{id}` - Get posts by user
- `POST /api/posts` - Create post
- `PUT /api/posts/{id}` - Update post
- `DELETE /api/posts/{id}` - Delete post

## Frontend API Calls

Uses both `axios` (in `/src/api/`) and native `fetch()` (in `/src/hooks/`) to test detection of both patterns.
