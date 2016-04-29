# pynetflow & pynetflow2graphite
A library (pynetflow) for parsing Netflow v5 data and a daemon (pynetflow2graphite) for forwarding Netflow data to Graphite (or the console).

## Forwarder Usage (pynetflow2graphite.py)
    pynetflow2graphite.py [-h, --help]
                          [-i, --interface [INTERFACE]]
                          [-p, --localport [LOCALPORT]]
                          [-g, --graphiteip [GRAPHITEIP]]
                          [-f, --graphiteport [GRAPHITEPORT]]
                          [-s, --subnets [SUBNETS [SUBNETS ...]]]
                          [-v, --verbose]
                          [-n, --nographite]


    optional arguments:
      --help, -h            show this help message and exit
      
      --interface [INTERFACE], -i [INTERFACE]
                            Local listening interface IP, default=0.0.0.0
                            
      --localport [LOCALPORT], -p [LOCALPORT]
                            Local listening port, default=1514
                            
      --graphiteip [GRAPHITEIP], -g [GRAPHITEIP]
                            Graphite server IP, default=127.0.0.1
                            
      --graphiteport [GRAPHITEPORT], -f [GRAPHITEPORT]
                            Graphite server port, default=2004
                            
      --subnets [SUBNETS [SUBNETS ...]], -s [SUBNETS [SUBNETS ...]]
                            Subnets to monitor, formatted as: 192.168.0.0/24
                            
      --verbose, -v         Print NetFlow PDUs to console
      
      --nographite, -n      Don't forward to Graphite (print to console)

## Library Usage (pynetflow.py)
    #Import the pynetflow library
    import pynetflow 
    
    #Create a pynetflow object. Data should be raw bytes
    nf = pynetflow.Netflow(probe_ip_address_string, netflow_raw_data) 
    
    #Dictionary of Netflow header
    nf.header
    
    #List of Netflow data dictionaries
    nf.data 
    
    #Sensor providing contained data
    nf.sensor 
    
    #Netflow data in raw byte form
    nf.rawdata 
    
    
    
    