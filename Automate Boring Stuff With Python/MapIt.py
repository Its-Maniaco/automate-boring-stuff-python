import webbrowser, sys

# To give command line argument, import sys as they are stored in 'sys.argv' list
sys.argv #['MapIt.py', 'address part', 'address part', 'address part']

#check if command line arguments passed
if len(sys.argv) > 1:
    # we need to convert all the address part into a single address
    #['address part','address part'] -> address
    address = ' '.join(sys.argv[1:])
else:
    print("No input address")
    address = 'Null' 

'''
    https://duckduckgo.com/?t=ffab&q=870+valencia+st&atb=v314-1&ia=web&iaxm=maps
    
    Checkin to see if link also works for
    https://duckduckgo.com/?t=ffab&q=870 valencia st&atb=v314-1&ia=web&iaxm=maps
    Yes
    Therefore - https://duckduckgo.com/?t=ffab&q=,<ADDRESS>&atb=v314-1&ia=web&iaxm=maps

'''
webbrowser.open('https://duckduckgo.com/?t=ffab&q=,'+ address + '&atb=v314-1&ia=web&iaxm=maps')