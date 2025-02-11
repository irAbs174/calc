const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
  readFile: () => ipcRenderer.invoke('read-file')
});