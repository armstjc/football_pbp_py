# Creation Date: 02/03/2024 05:46 PM EST
# Last Updated: 02/11/2024 11:50 AM EST
# Author: Joseph Armstrong (armstrongjoseph08@gmail.com)
# File Name: ./core/encryption/hashing.py
# Purpose: Holds code used to hash objects that need hashes.
####################################################################################################


from hashlib import sha256
from platform import system


def get_sysname_hash():
    """
    """
    system_name = system()
    system_hash = bytes(system_name,'utf-8')
    #print(system_hash)
    return sha256(system_hash).hexdigest()