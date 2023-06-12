import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache(allow_output_mutation=True)

# Define the load_contract function
def load_contract():
    
    # Load Raffle ABI
    with open(Path('./Contracts/Compiled/raffle_abi.json')) as f:
        raffle_abi = json.load(f)


    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")


    # Get the contract using web3
    contract = w3.eth.contract(
        address=contract_address,
        abi=raffle_abi
    )



    # Return the contract from the function
    return contract



# Load the contract
contract = load_contract()


st.title("Project Raffle")
st.write("Choose an account to get started.")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Enter into Raffle
################################################################################
st.markdown("## Enter into Raffle. Payment is 0.1 ETH.")

input_payment = st.text_input("Input payment")

if st.button("Buy In"):
    tx_hash = contract.functions.EnterRaffle(
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    st.write("Congrats! You've entered the raffle.")
st.markdown("---")
