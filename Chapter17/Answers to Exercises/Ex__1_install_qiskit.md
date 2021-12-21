__Modern Computer Architecture and Organization Second Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 17, Exercise 1

Install the Qiskit quantum processor software development framework by following the instructions at https://qiskit.org/documentation/install.html. The instructions suggest installation of the Anaconda (https://www.anaconda.com/) data science and machine learning tool set. After installing Anaconda, create a Conda virtual environment named *qiskitenv* to contain your work on quantum code and install Qiskit in this environment with the command **pip install qiskit**. Be sure to install the optional visualization dependencies with the command **pip install qiskit-terra[visualization]**. 

# Answer
1. Download the Anaconda installer from https://www.anaconda.com/distribution/. Select the Python 3.9 version and the appropriate 32-bit or 64-bit variant for your host computer.

2. Run the Anaconda installer and accept the defaults. Close the installer after it completes.

3. Start Anaconda from the Windows search box by typing *anaconda* and clicking on **Anaconda prompt** when it appears in the search list. A console window will appear.

4. In the Anaconda prompt, create and activate a virtual environment named *qiskitenv* with the following commands. Install any recommended packages:
```
conda create -n qiskitenv python=3.8
conda activate qiskitenv
```

5. Install Qiskit and its visualization dependencies with the following commands:
```
pip install qiskit
pip install qiskit-terra[visualization]
```

6. This completes the installation.
