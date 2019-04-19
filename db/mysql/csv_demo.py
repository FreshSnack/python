import csv

DATA = ((9, 'Web Clients and Servers', 'base64, urllib'),
        (10, 'Web Programing CGI & WSGI', 'cgi, time, wsgiref'),
        (13, 'Web Services', 'urllib, then'),
        )
print("*** WRITING CSV DATA")
f = open("book_data.csv", 'w', newline='')
writer = csv.writer(f)
for record in DATA:
    writer.writerow(record)
f.close()

print('*** REVIEW OF SAVED DATA')
f = open("book_data.csv", 'r')
reader = csv.reader(f)
for line in reader:
    print(line)
f.close()
# for chap, title, pkg in reader:
#         print('Chapter %s: %r (featuring %s)' % (chap, title, pkg))
# f.close()
