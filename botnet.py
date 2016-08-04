#!/usr/bin/python


#list of configuration data with their place in an array
ip_addr = ["10.20.7.2", "10.20.7.3", "10.20.7.4", "10.20.7.5", "10.20.7.6", "10.20.7.7", "10.20.7.8", "10.20.7.9", "10.20.7.10"]
dest_ip = ["20.20.106.20", "20.20.106.21", "20.20.106.22", "20.20.106.23", "20.20.106.24", "20.20.106.25", "20.20.106.26", "20.20.106.27", "20.20.106.28"]
conf=[
      [
        { 'type' : 'header', 'name' : 'botnet-Rule-1', 'prompt' : {'src_ip': 'Enter the source IP for botnet rule 1'}},
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-1.json', 'src_ip' : ip_addr[0], 'message' : ' Port Scan (Single port accross multiple hosts)' },
        { 'type' : 'alert', 'name' : 'Botnet',  'id' : '5000004', 'severity' : 0, 'confidence' : 0,  'object_id' : ip_addr[0], 'wait_minutes' : 4}
      ],
      [
        { 'type' : 'header', 'name' : 'botnet-Rule-1-2-3', 'prompt' : {'src_ip': 'Enter the source IP for botnet rule 1-2-3', 'dst_ip' : 'Enter the destination IP for botnet rule 1-2-3'}},
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-1.json', 'src_ip' : ip_addr[2], 'message' : ' Port Scan (Single port accross multiple hosts)' },
	{ 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-2.json', 'src_ip' : ip_addr[2], 'message' : 'Blacklisted Web Server access (for Downloading Malware)' },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-3.json', 'src_ip' : ip_addr[2], 'dst_ip' : dest_ip[2], 'seconds_between_json' : 960, 'message' : "Anamolous connection/Application (Connection/Application that haven't been seen in the past)"  },
        { 'type' : 'alert', 'name' : 'Botnet',  'id' : '5000004', 'severity' : 50, 'confidence' : 55, 'object_id' : ip_addr[2], 'wait_minutes' : 35}
      ],
      [
        { 'type' : 'header', 'name' : 'botnet-Rule-1-3', 'prompt' : {'src_ip' : 'Enter the source IP for botnet rule 1-3', 'dst_ip' : 'Enter the desintation IP for botnet rule 1-3'}},
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-1.json', 'src_ip' : ip_addr[3], 'message' : ' Port Scan (Single port accross multiple hosts)' },
	{ 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-3.json', 'src_ip' : ip_addr[3], 'dst_ip' : dest_ip[3], 'seconds_between_json' : 960, 'message' : "Anamolous connection/Application (Connection/Application that haven't been seen in the past)" },
        { 'type' : 'alert', 'name' : 'Botnet',  'id' : '5000004', 'severity' : 35, 'confidence' : 20, 'object_id' : ip_addr[3], 'wait_minutes' : 35}
      ],
      [
        { 'type' : 'header', 'name' : 'botnet-Rule-1-2-3-4', 'prompt' : {'src_ip' : 'Enter the source IP for botnet rule 1-2-3-4'}},
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-1.json', 'src_ip' : ip_addr[5], 'message' : ' Port Scan (Single port accross multiple hosts)' },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-2.json', 'src_ip' : ip_addr[5], 'message' : 'Blacklisted Web Server access (for Downloading Malware)' },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-3.json', 'src_ip' : ip_addr[5], 'dst_ip' : dest_ip[5], 'seconds_between_json' : 960, 'message' : "Anamolous connection/Application (Connection/Application that haven't been seen in the past)"  },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-4.json', 'src_ip' : ip_addr[5], 'message' : 'IRC Server communication' },
        { 'type' : 'alert', 'name' : 'Botnet',  'id' : '5000004', 'severity' : 70, 'confidence' : 75, 'object_id' : ip_addr[5], 'wait_minutes' : 35}
      ],
      [
        { 'type' : 'header', 'name' : 'botnet-Rule-1-2-3-5', 'prompt' : {'src_ip' : 'Enter the source IP for botnet rule 1-2-3-5', 'dst_ip' : 'Enter the destination IP for botnet rule 1-2-3-5'}},
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-1.json', 'src_ip' : ip_addr[6], 'message' : ' Port Scan (Single port accross multiple hosts)' },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-2.json', 'src_ip' : ip_addr[6], 'message' : 'Blacklisted Web Server access (for Downloading Malware)' },
	{ 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-3.json', 'src_ip' : ip_addr[6], 'dst_ip' : dest_ip[6], 'seconds_between_json' : 960, 'message' : "Anamolous connection/Application (Connection/Application that haven't been seen in the past)"  },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-5.json', 'src_ip' : ip_addr[6], 'message' : 'Open DNS Connection' },
        { 'type' : 'alert', 'name' : 'Botnet',  'id' : '5000004', 'severity' : 70, 'confidence' : 75, 'object_id' : ip_addr[6], 'wait_minutes' : 35}
      ],
      [
        { 'type' : 'header', 'name' : 'botnet-Rule-1-2-3-4-5', 'prompt' : {'src_ip' : 'Enter the source IP for botnet rule 1-2-3-4-5'}},
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-1.json', 'src_ip' : ip_addr[8], 'message' : ' Port Scan (Single port accross multiple hosts)' },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-2.json', 'src_ip' : ip_addr[8], 'message' : 'Blacklisted Web Server access (for Downloading Malware)' },
	{ 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-4.json', 'src_ip' : ip_addr[8], 'message' : 'IRC Server communication' },
        { 'type' : 'netflow', 'file' : 'testcases/test_files/botnet/botnet-5.json', 'src_ip' : ip_addr[8], 'message' : 'Open DNS Connection' },
        { 'type' : 'alert', 'name' : 'Botnet',  'id' : '5000004', 'severity' : 75, 'confidence' : 75, 'object_id' : ip_addr[8], 'wait_minutes' : 20}
      ]
     ]
