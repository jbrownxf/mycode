#!/bin/sh
#Ask user for their lab details (50 chars or less)

echo What were the main topics in the is lab? 

read details
cd ~/mycode \
&& git add * \
&& git commit -m "$details" \
&& git push origin master

echo Done!
