const express = require('express');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const cors = require('cors');

const app = express();
const SECRET = 'your-secret-key';
const PORT = 3333;

let users = [];

// Critical security configuration
app.use(cors({
  origin: 'http://localhost', // Must match EXACT client origin
  credentials: true,
  exposedHeaders: ['set-cookie']
}));

app.use(express.json());
app.use(cookieParser());

// Enhanced cookie settings
const cookieConfig = {
  httpOnly: true,
  secure: false, // Allow HTTP for local development
  sameSite: 'none', // Required for cross-site cookies
  domain: 'localhost', // Explicit domain binding
  path: '/',
  maxAge: 3600000
};

// Register
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    console.log('Registration attempt:', username);
  
    if (!username || !password) {
      return res.status(400).json({ error: 'Username and password required' });
    }
  
    if (users.some(u => u.username === username)) {
      return res.status(400).json({ error: 'Username already exists' });
    }
  
    users.push({ username, password });
    console.log('Registered users:', users);
    res.json({ success: true });
  });  

app.get('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username && u.password === password);
  
  if (!user) return res.status(401).json({ error: 'Invalid credentials' });

  const token = jwt.sign({ username }, SECRET, { expiresIn: '1h' });
  res.cookie('auth', token, cookieConfig); // Apply enhanced config
  res.json({ success: true });
});

app.get('/dashboard', (req, res) => {
  const token = req.cookies.auth;
  if (!token) return res.status(200).json({ message: 'Welcome to dashboard' });
  try {
    jwt.verify(token, SECRET);
    res.json({ message: 'Welcome to dashboard' });
  } catch (err) {
    res.status(401).json({ error: 'Invalid token' });
  }
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));