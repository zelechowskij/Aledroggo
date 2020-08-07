# Aledroggo

> It is a python based tool designed to help people shop at Allegro, which sends an email notification when a price of certean product drops below user-defined threshold

## But how does it work?

### User input

Everything starts with user specifying what kind of product he looks for

![Recordit GIF](http://g.recordit.co/DNPIy3XFtB.gif)

As the user begins, aledroggo needs to be authorized by Allegro to gain access to its resources using *OAuth2 Client credentials flow*.
After recieving token, aledroggo can send requests to Allegro and user can search through products

Front-end and back-end are deployed on Google app engine platform. Simple user interface was built mainly on Bootstrap and CSS.

After user completes his part, an update is sent to Oracle database containing every search parameters. The DB itself is designed with usage of constraints as well as two distinctive users with different restrictions for safety measures.

![DB](/images/1.png)

Only one user can alter tables, but both can select from them.
