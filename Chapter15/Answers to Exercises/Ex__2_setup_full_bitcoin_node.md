__Modern Computer Architecture and Organization Second Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15, Exercise 2

Set up a full bitcoin peer node and connect it to the bitcoin network. Download the bitcoin core software from https://bitcoin.org/en/download. It is best to have a fast internet connection and at least 200 GB of free disk space.

# Answer
Download the bitcoin core installer from https://bitcoin.org/en/download and run it.

After installation completes, run the bitcoin core application. The application will begin downloading the entire bitcoin blockchain beginning with the genesis block from 2009 up to the most recently added block. This process will take several hours or days depending on your internet bandwidth.

Although bitcoin core will consume about 200 GB of disk space during the initial validation process, it will reduce its storage requirements to a disk space limit you select, which defaults to 2 GB.

After the blockchain has downloaded, the node will transition into operation as a full network peer. You can display the application's connections to network peers and monitor the addition of freshly created transactions into the pool of transactions awaiting inclusion on a future block to be added to the blockchain.

You can also create a bitcoin wallet within the application and use it to conduct your own bitcoin transactions. If you use this application to store a significant quantity of bitcoin, be certain you are enforcing best security practices for all aspects of the host computer operating system and its applications to ensure you don't get hacked and have your coins stolen.
