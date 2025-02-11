const { app, BrowserWindow, session } = require('electron');
const path = require('path');

let mainWindow;

app.whenReady().then(() => {

  createWindow();
});

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1080,
    height: 950,
    webPreferences: {
      contextIsolation: true
    }
  });

  // چک کردن وضعیت لاگین
  session.defaultSession.cookies.get({ name: 'auth' }).then(cookies => {
    if (cookies.length === 0) {
      mainWindow.loadFile('templates/auth/login.html');
    } else {
      mainWindow.loadFile('templates/dashboard/dashboard.html');
    }
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});