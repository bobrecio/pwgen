# pwgen
Formatted Password Generator

[x] User uploads wordlist file (file is list of words. one word per line.)
[x] Filter words with set number of characters
[x] Select a single word from the results
[ ] Display the number of words in results ("pool")
[ ] Format a password segment using [delimiter][number of digits/chars][type of segment]: `15d = 15 digits



_Formats_
% : delimiter (%5a)
|char|type|example|description|
|:---:|:------------:|:-------:|:------------------------------------|
|a : lower alpha|%2a|2 lower-alpha characters|
|A|upper-alpha|%5A|5 upper-alpha characters|
|X|mixed case|
