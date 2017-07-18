import sqlite3 as sql

con = sql.connect('ddb.db')

with con:

    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Contacts(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name varchar(20), Surname varchar(21), Numbers  INT)')
    print('\n    !!! < For view table input ".view" > !!!')
    print('    !!! < For clear table input ".clear" > !!!')
    print('    !!! < For exit input ".exit > !!!"\n')
    new_row = ['','','']
    while True:

        s = input('    >>> ')
        if s == '.exit':
            break

        elif s == '.view':
            print('    --------------------------------------------------------------------------')
            print('    | ID |        Name        |       Surname       |      Phone number      |')
            print('    --------------------------------------------------------------------------')
            cur.execute("SELECT * FROM Contacts")
            rows = cur.fetchall()
            for row in rows:
                row0 = str(row[0])
                row1 = row[1]
                row2 = row[2]
                row3 = str(row[3])
                print ('    |', row0.center(4), '|',row1.center(20), '|', row2.center(21), '|', row3.center(24), '|', sep='')
            print('    --------------------------------------------------------------------------')
            continue

        elif s == '.clear':
            cur.execute('DROP TABLE IF EXISTS Contacts')
            cur.execute('CREATE TABLE IF NOT EXISTS Contacts(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name varchar(20), Surname varchar(20), Numbers  INT)')
            continue

        new_row[0] = input('    >>> Name: ')
        new_row[1] = input('    >>> Surname: ')
        new_row[2] = int(input('    >>> Number: '))
        cur.execute('INSERT INTO Contacts(Name, Surname, Numbers) VALUES(?,?,?)', new_row)

