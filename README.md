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
                            Local listening interface IP
                            
      --localport [LOCALPORT], -p [LOCALPORT]
                            Local listening port
                            
      --graphiteip [GRAPHITEIP], -g [GRAPHITEIP]
                            Graphite server IP
                            
      --graphiteport [GRAPHITEPORT], -f [GRAPHITEPORT]
                            Graphite server port
                            
      --subnets [SUBNETS [SUBNETS ...]], -s [SUBNETS [SUBNETS ...]]
                            Subnets to monitor, formatted as: 192.168.0.0/24
                            
      --verbose, -v         Print NetFlow PDUs to console
      
      --nographite, -n      Don't forward to Graphite (print to console)

## Library Usage (pynetflow.py)
    import pynetflow # Import the pynetflow library
    
    nf = pynetflow.Netflow(probe_ip_address_string, netflow_raw_data) # Create a pynetflow object. Data should be raw bytes
    
    nf.header # Dictionary of Netflow header
    
    nf.data # List of Netflow data dictionaries
    
    nf.rawdata # Netflow data in raw byte form
    
    nf.sensor # Sensor providing contained data
    
    
    