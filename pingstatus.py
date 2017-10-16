# -*- coding: utf-8 -*-

"""
    Nome: pingstatus.py
    Descrizione: realizza il 'ping' utilizzando WMI
"""

import win32com.client

boold = False

wmi = win32com.client.GetObject(r"winmgmts:\\.\root\cimv2")


def ping(host, status=None):
    """
    :param host:
    :param status:
    :return: status
                0     Ok
                11010 Request timed out
                11003 Destination host unreachable
    """
    msg = ""
    col_items = wmi.ExecQuery("Select * from Win32_PingStatus Where Address = '%s'" % host)
    for item in col_items:
        status = item.StatusCode
        if boold:
            print(status)
        if item.StatusCode == 0: # success
            msg = "Host " + item.Address + "\n"
            msg = msg + "Recorded Hops: " + str(item.RecordRoute) + "\n"
            msg = msg + "Buffer Size: " + str(item.ReplySize) + "\n"
            msg = msg + "Response Time: " + str(item.ResponseTime) + "\n"
            msg = msg + "ResponseTimeToLive: " + str(item.ResponseTimeToLive) + "\n"
            msg = msg + "Timeout: " + str(item.Timeout) + "\n"
            msg = msg + "TimetoLive: " + str(item.TimetoLive)
        if boold:
            print(msg)
    return status


if __name__ == "__main__":
    if boold:
        print("Start")
    status = ping("192.168.1.23")
    print(status)
    if boold:
        print("Stop")