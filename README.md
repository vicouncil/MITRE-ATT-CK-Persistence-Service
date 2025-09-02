# MITRE-ATT-CK-Persistence-Service
Windows persistence techniques. The script illustrates MITRE ATT&amp;CK tactics including file deployment, hiding files, creating and configuring a Windows service.
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/) &nbsp;[![Platform](https://img.shields.io/badge/Windows-10/11-0078D6?logo=windows)](https://www.microsoft.com/windows)

# Deployment Flowchart
```mermaid
flowchart TD
    A([Start]) --> B{APPDATA Path?}
    B -- Yes --> C[Set save_path in APPDATA]
    B -- No --> D[Set save_path in Current Directory]
    C --> E[Download File with curl -> save_path]
    D --> E
    E --> F["Hide File (attrib +h +s)"]
    F --> G["Create Windows Service (Persistence Service)"]
    G --> H["Configure Service start=auto"]
    H --> I["Start Service"]
    I --> J([End])

    %% Error handling
    E -.-> K{Download Success?}
    K -- No --> L["Print: Failed to fetch file"]
    F -.-> M{Command Success?}
    M -- No --> N["Print: Failed attrib"]
    G -.-> O{Service Created?}
    O -- No --> P["Print: Failed service create"]
    H -.-> Q{Config Success?}
    Q -- No --> R["Print: Failed config"]
    I -.-> S{Start Success?}
    S -- No --> T["Print: Failed start"]
```
