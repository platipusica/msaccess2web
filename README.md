# msaccess2web

# MS Access Modernizer

Run Microsoft Access database on the Web.

Supports:
- JOIN-heavy queries
- server-side paging (OFFSET simulation)
- parameterized filters
  
No database migration required. No code needed.

Web application created with a **single command** in 1 second:

[![alt text](https://github.com/platipusica/msaccess2web/blob/main/output.gif?raw=true)](https://raw.githubusercontent.com/platipusica/msaccess2web/refs/heads/main/output.gif)


Command:

```
 python scaffold.py --db C:\Users\dba\Downloads\access_database.accdb
```



## Features

- Fixes Microsoft Access JOIN limitations
- Reliable server-side paging (TOP + window emulation)
- Works with ODBC drivers on Windows only
- Preserves Access compatibility


## Enables a Service

MS Access DB -> msaccess2web -> WEB / REST / SQL API

Then:

Web apps can use Access as backend safely. 


## Commercial support

This project is maintained for enterprise MS Access modernization projects.

Contact if:
- you are stuck on Access
- cannot migrate easily
- fear rewriting everything
- need MS Access data on the Web

