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

File on Windows:
```
(py312) C:\Users\dba\Downloads\ai>dir access_database.accdb
 Volume in drive C has no label.
 Volume Serial Number is FEBB-5BF6

 Directory of C:\Users\dba\Downloads\

08/06/2026  06:36 PM         8,388,608 access_database.accdb
               1 File(s)      8,388,608 bytes
               0 Dir(s)  40,732,401,664 bytes free

(py312) C:\Users\dba\Downloads\ai>type access_database.accdb
Standard ACE DB...
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

