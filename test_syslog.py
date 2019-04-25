import syslog_client

if __name__ == "__main__":
    print("Start testing syslog")
    log = syslog_client.Syslog()
    log.send("Ciao mondo", syslog_client.Level.WARNING)
    print("Stopping test syslog")
