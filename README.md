# mlbtheShow-Pack-Odds

This tool will download all of your pack history for MLB The Show 20

To get started...

1. Log in and browse to https://mlb21.theshow.com/packs/open_pack_history
2. Open up developer tools in your browser (F12 on Windows)
3. Scroll down and select the second page
4. Click on the network tab of developer tools
5. Right click on the request that says open_pack_history?page=2&
6. Select Copy > Copy as cURL (cmd)
7. Navigate to https://curl.trillworks.com/
8. Paste the curl command into the window
9. Copy the Python headers section.
10. You only need the header information. Overwrite the headers dictionary in the code and you will be good to go. This contains your authentication token and cookies
11. Make sure you update the path to the CSV file in __main__.
12. Also make sure to update the range() function in the code to make sure you have enough pages. I always add number of pages + 5
12. Run code!
