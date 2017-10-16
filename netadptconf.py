# -*- coding: utf-8 -*-

"""
    Nome: netadptconf.py
    Descrizione: accede alla caratteristiche delle schede di rete utilizzando WMI
"""

import os
import wmi

boold = True

if __name__ == "__main__":
    var = os.environ['USERNAME']
    if boold:
        print("Hello, " + var + "\n")

    cim = wmi.WMI()

    colNetworks = cim.Win32_NetworkAdapterConfiguration()

    # ciclo per tutte le schede di rete
    for itemColNetwork in colNetworks:
        # visualizza istanze classe (le schede di rete)
            if itemColNetwork.IPEnabled:
                if boold:
                    print(itemColNetwork)

    # accesso a una singola istanza (scheda di rete)
    colNetwork = cim.Win32_NetworkAdapterConfiguration()[1]

    # visualizza informazioni su singola istanza
    if boold:
        print("\nAll Network Info - Scheda rete 1", colNetwork)
        print("IPAddress IPv4 ", colNetwork.IPAddress[0])
        print("IPAddress IPv6 ", colNetwork.IPAddress[1])
