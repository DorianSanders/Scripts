import sys, socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

    # adding a banner

    print ("-" * 50)
    print ("Scanning target: "+target)
    print ("Time started: " +str(datetime.now()))
    print ("-" * 50)

    try:
        for port in range (50,85): # just looking for dns and http:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # Translete hostname to IPv4
            result = s.connect_ex((target, port))
            if result == 0:
                print (f"Port {port} is open")
                s.close
    except KeyboardInterrupt:
        print ("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("Could not connect to server.")
        sys.exit()
else:
    print ("Invalid amount of arguments.")
    print ("Syntax: python3 scanner.py <IP>")
