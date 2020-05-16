# mlbtheShow-Pack-Odds

This tool will download all of your pack history for MLB The Show 20

To get started...

1. Log in and browse to https://theshownation.com/mlb20/packs/open_pack_history
2. Open up developer tools in your browser (F12 on Windows)
3. Scroll down and select the second page
4. Click on the network tab of developer tools
5. Right click on the request that says open_pack_history?page=2&
6. Select Copy > Copy as cURL (cmd)
7. Navigate to https://curl.trillworks.com/
8. Paste the curl command into the window
9. Copy the Python request code to notepad
10. You only need the header information. Overwrite the headers dictionary and you will be good to go.
11. Make sure you update the path to the CSV file in __main__.
12. Run code!
