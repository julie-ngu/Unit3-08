# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This is program prints out the english alphabet in both lowercase and uppercase and shows the user its 
# corresponding unicode value

import unicodedata

for counter in range(65, 91):
    print counter, unichr(counter)
    
for counter in range(97, 123):
    print counter, unichr(counter)
