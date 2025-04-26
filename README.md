# potential-sniffle

├── backend/                 # FastAPI + MongoDB
│   ├── app/
│   │   ├── main.py          # FastAPI app entrypoint
│   │   ├── models/          # Pydantic models & MongoDB schemas
│   │   ├── routes/          # API routes (auth, workouts, etc.)
│   │   ├── services/        # Business logic
│   │   ├── db.py            # MongoDB connection (motor/beanie)
│   │   └── config.py        # Env vars and app settings
│   ├── Dockerfile
│   └── environment.yml
│
├── client/                 # Frontend
│   ├── mobile/             # React Native with Expo
        ├── App.js
        ├── assets/
        │   ├── images/
        │   └── fonts/
        ├── components/
        │   ├── Button.js
        │   ├── Header.js
        │   └── WorkoutCard.js
        ├── navigation/
        │   ├── AppNavigator.js
        │   └── TabNavigator.js
        ├── screens/
        │   ├── HomeScreen.js
        │   ├── ProfileScreen.js
        │   ├── WorkoutsScreen.js
        │   └── LoginScreen.js
        ├── constants/
        │   ├── Colors.js
        │   └── Styles.js
        ├── services/
        │   ├── api.js       # Axios API calls (connect to your backend FastAPI later!)
        │   └── auth.js      # Auth helper functions (login/signup)
        ├── hooks/
        │   └── useAuth.js   # Custom hooks (e.g., for authentication)
        ├── context/
        │   └── AuthContext.js  # For user login/session management
        ├── utils/
        │   └── validators.js  # Utility functions like validating email/password
        ├── app.json
        ├── package.json

│   └── web/ (optional)     # React or Next.js if you want a web version too
│
├── docker-compose.yml      # To run backend + MongoDB together
└── README.md
