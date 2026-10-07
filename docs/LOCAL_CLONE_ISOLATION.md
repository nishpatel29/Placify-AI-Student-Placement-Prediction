# Local Clone Isolation

If you keep several Placify AI experiments on Windows, keep every clone in its own folder with its own virtual environment and Streamlit port.

Example:

```text
C:\Users\npers\Projects\
├── Placify_AI_Main    → 8501
├── Placify_AI_Clone_1 → 8502
├── Placify_AI_Clone_2 → 8503
└── Placify_AI_Clone_3 → 8504
```

Each clone should have:

- its own `.venv`;
- its own `.streamlit/config.toml`;
- project-relative data/model paths;
- no hard-coded path to another clone.

Check active ports with:

```powershell
Get-NetTCPConnection -LocalPort 8501,8502,8503,8504 -ErrorAction SilentlyContinue |
Select-Object LocalAddress,LocalPort,State,OwningProcess |
Format-Table -AutoSize
```
