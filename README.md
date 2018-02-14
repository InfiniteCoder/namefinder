# namefinder
Find available subdomains on heroku

This script finds available subdomains on heroku(eg: example.heroku.com) which you can use for your application.
It does this by checking the validity of various words(used in domain name) which are read from a text file.

## Usage

This script requires `python3` and `requests`.  You can install `requests` using `pip` as,

    pip install requests
    
By default, the script uses `/usr/share/dict/cracklib-small` to read possible words. You may change the `word_file` variable to some other path. The `num_threads` variable sets the number of threads to be used in a thread pool, through which api requests are made. Higher the number of threads, faster will be the execution.

Execute the script using

    python3 namefinderM.py
    
The available names are printed to stdout. You will probably want to redirect the output to file and then process the file as per you wish.
