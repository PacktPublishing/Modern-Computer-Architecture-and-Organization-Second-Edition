__Modern Computer Architecture and Organization Second Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 17, Exercise 2

Create a free IBM Quantum Experience account at https://quantum-computing.ibm.com/. Locate your IBM Quantum Services API token at https://quantum-computing.ibm.com/account and install it into your local environment using the instructions at https://qiskit.org/documentation/getting_started.html.

# Answer
1. Visit https://quantum-computing.ibm.com/. If you don't already have an account, click the [Create an IBMid account.](https://auth.quantum-computing.ibm.com/auth/idaas) link to get started.

2. Once you are logged in, locate **API token** on the screen. Click the button to copy your API token to the clipboard.

3. Return to the Anaconda prompt for the qiskitenv environment you created in [Exercise 1](Ex__1_install_qiskit.md).

4. Enter the following commands at the Anaconda prompt to set up your API token. You will need to replace *MY_TOKEN* with the token you copied to the clipboard in step 2:
```
python
import qiskit
from qiskit import IBMQ
IBMQ.save_account('MY_TOKEN')
```