# tom
TOM or The Online Machine is a python RAD framework for rich client/server applications.  It is pure python (except for QT) and plugin based on both client and server.

# Rationale
Many web client/server stacks for python already exist (e.g. Django).  However, thess frameworks are generally very complex due to their need to tame the web environment.  Creating client applications often means going outside of python code to HTML/CSS/Javascript.  This increases the compelxity of writing any rich full stack app.  Finally, deploying the apps built on these frameworks generally means configuring a complicated back end web server environment.

Tom is designed to make it easy and fast for python coders to build applications as rich as any desktop app.  All the coder need know is Python, QT and a few conventions that TOM uses.  Because TOM's functionality is all contained in pyton modules, it is easy to add client and server functionality as well as leverage functionality others have built.

I wrote this app because of my frustration at the "web tax" imposed on my time by existingtechnologies.  I hope it is useful to others.

# Acknowledgments

TOM leverages some other projects with my thanks:  

[rpyc](https://github.com/tomerfiliba-org/rpyc) is used for client/server communication

[lmdb](https://lmdb.readthedocs.io/en/release/) is used by the default data store plugin

[PyQt6](https://pypi.org/project/PyQt6/) is used for the client interface.

Full documentation at: 
https://purdue0-my.sharepoint.com/:w:/g/personal/jpkessel_purdue_edu/EajGOaQvHGZDtM9LvzWktqYBzMrMha6xWi2HejMrkC0Sog
