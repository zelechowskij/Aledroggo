# Aledroggo

> It is a python based tool designed to help people shop at Allegro, which sends an email notification when a price of certain product drops below user-defined threshold

## But how does it work?

### User input

Everything starts with the user specifying what kind of product he looks for

![Recordit GIF](http://g.recordit.co/DNPIy3XFtB.gif)

As the user begins, aledroggo needs to be authorized by Allegro to gain access to its resources using *OAuth2 Client credentials flow*.
After receiving the token, aledroggo can send requests to Allegro and user can search through products

Front-end and back-end are deployed on Google app engine platform. Simple user interface was built mainly on Bootstrap and CSS.

### Database

After user completes his part, an update is sent to Oracle database containing every search parameters. The table is called "Search" and it is designed with usage of constraints as well as two distinctive users with different restrictions for safety measures.

![DB](/images/1.png)

Only one user can alter tables, but both can select from them.

### Is it cheap yet?

Independently from main app, a recurring python script is running via GCP cron jobs.
Every hour, the script selects tasks from "Search" table that are "active" and checks whether any product is cheaper than the given threshold. If so, the notification is sent and the task is marked "Inactive".

There is another table that stores every single one of the cron jobs results, thus providing possibility to e.g. draw price vs time graph of tracked product.

### It is cheap now!
![Notification](/images/2.png)
