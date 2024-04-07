# Chart Below
<!--
U+250x	─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
U+251x	┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
U+252x	┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
U+253x	┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
U+254x	╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
U+255x	═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
U+256x	╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
U+257x	╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿
-->
```md
┌────────────────────────────────────────────────────────────────────────────────────┐
│                                   # API System                                     │
├────────────────────────────────────────────────────────────────────────────────────┘
│
└── **Authentication**
    │
    ├── **User Authentication**
    │   │
    │   ├── **Check is EXE Serial Number on White List or not, if is...**
    │   ├── **Obtain Local Info.**
    │   │   ├── EXE Hash : 315dc8f7c0a1962
    │   │   ├── Windows Product Key : TGKNY-HYP68-YVYGM-JMVQ2-V8RJW
    │   │   ├── MAC Address : 00:50:56:c0:00:08
    │   │   ├── System UUID : 29FE6B46-A5BF-11ED-8E59-70D8234874AB
    │   │   ├── BIOS Serial Number : 8CG3052S48
    │   │   ├── GPU ID : VEN_8086&DEV_46A8&SUBSYS_8A34103C&REV_0C
    │   │   ├── CPU ID : BFEBFBFF000906A4
    │   │   └── Motherboard Serial Number : PREFU1C0GHOA6L
    │   ├── **Obtain DB[Logins][exe_name] all records as a json_db.**
    │   │   └── Store in each index of json list...
    │   │       ├── EXE Hash : 315dc8f7c0a1962
    │   │       ├── Windows Product Key : TGKNY-HYP68-YVYGM-JMVQ2-V8RJW
    │   │       ├── MAC Address : 00:50:56:c0:00:08
    │   │       ├── System UUID : 29FE6B46-A5BF-11ED-8E59-70D8234874AB
    │   │       ├── BIOS Serial Number : 8CG3052S48
    │   │       ├── GPU ID : VEN_8086&DEV_46A8&SUBSYS_8A34103C&REV_0C
    │   │       ├── CPU ID : BFEBFBFF000906A4
    │   │       └── Motherboard Serial Number : PREFU1C0GHOA6L
    │   ├── **Check Software Previus Records on json_db**
    │   │   ├── if devices > limit in 'Limit' table in device[name] device
    │   │   │   ├── Alart to admin
    │   │   │   ├── Blocked = True
    │   │   │   └── Block the info all from this pc
    │   │   └── elif devices < limit in 'Limit' table in device[name] device
    │   │       ├── Alart to admin
    │   │       ├── Blocked = False
    │   │       └── Pass Bro...
    │   ├── **Genarate a Intigrity Key using EXE Hash,MAC,UUID,BIOS,CPU**
    │   │   ├── Check Software Name, Table=name
    │   │   └── Upload Login from....
    │   │       ├── Table=logins
    │   │       ├── id=exe name (secrate)
    │   │       ├── Blocked = if more then max limit
    │   │       ├── EXE Hash : 315dc8f7c0a1962 (Main Key)
    │   │       ├── Windows Product Key : TGKNY-HYP68-YVYGM-JMVQ2-V8RJW
    │   │       ├── MAC Address : 00:50:56:c0:00:08
    │   │       ├── System UUID : 29FE6B46-A5BF-11ED-8E59-70D8234874AB
    │   │       ├── BIOS Serial Number : 8CG3052S48
    │   │       ├── GPU ID : VEN_8086&DEV_46A8&SUBSYS_8A34103C&REV_0C
    │   │       ├── CPU ID : BFEBFBFF000906A4
    │   │       └── Motherboard Serial Number : PREFU1C0GHOA6L
    │   └── **if not Blocked, start device**
    │
    └── **Admin Authentication (Separate API)**
        ├──  **Signup (/signup, POST):**
        │    ├──  Checks Dose Have A Registration Key.
        │    ├──  Checks for email and password in request body.
        │    ├──  Validates email format.
        │    ├──  Checks for existing Admin with the same email.
        │    ├──  Generates a unique key for the Admin.
        │    ├──  Stores Admin data (including password) in the database.
        │    └──  Returns success message and the generated key.
        │
        └──  **Login (/login, POST):**
             ├──  Checks for credentials (email and password) in request body.
             ├──  Validates credentials against user database.
             ├──  Returns success message, key, and user data if login is successful.
             └──  Returns "Invalid credentials" message if login fails.


```
