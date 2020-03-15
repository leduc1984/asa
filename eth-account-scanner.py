   for x in range(20):
        if x != 19:
            # First 19 addresses are concatenated with a ',' to build the final API link. Parameter string is extra entropy.
            acct = Account.create('sadkjhjwk dhkdasdlkm')
            addressList.append([acct.address + ',', acct.privateKey.hex()])
        else:
            acct = Account.create('dwqdcwejnc bcbrewrijsdn')
            addressList.append([acct.address, acct.privateKey.hex()])
    
    # Concatenate link with addresses
    for add in addressList:
        link = link + add[0]

    # Concatenate link with API key
    link = link + linkEnd

    # Send request and get JSON response
    data = requests.get(link, timeout = 10)
    jdata = json.loads(data.text)

    # Loop checks if there is a > 0 balance
    for res in jdata['result']:
        
        # If there is a account with a balance > 0 then the privat key is stored in a textfile named foundKeys.txt
        if  int(res['balance']) > 0:
            f= open("foundKeys.txt","a+")
            f.write(addressList[counter][1] + "\r\n")
            win = win + 1
            
        else:
            fail = fail + 1
        
        counter = counter + 1

    
    # Refresh link, list and counter
    link = 'https://api.etherscan.io/api?module=account&action=balancemulti&address='
    addressList = []
    counter = 0
    
    # Print stats
    print(multiprocessing.current_process().name + '  win: ' + str(win) + '   fail: ' + str(fail))
