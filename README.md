# pwgen
Formatted Password Generator

[x] User uploads wordlist file (one word per line)<br>
[x] Filter words with set number of characters<br>
[x] Select a single word from the results<br>
[ ] Display the number of words in results (pool)<br>
[ ] Format a single password segment using [delimiter][number of digits/chars][type of segment]: `15d = 15 digits<br>
[] Parse a password string<br.

|char|type|example|description|
|:---:|:------------:|:-----:|:---------------------------|
|%|delimiter|%2x|
|a|lower-alpha|%5a|5 random lower-alpha characters|
|A|upper-alpha|%5A|5 random upper-alpha characters|
|M|mixed-case|%3M|3 random mixed-case characters|
|d|digits|%14d|15 random digits|
|w|word from uploaded file|%3w|3 random words from uploaded file|
|x|any characters|%14x|14 random characters of any type|
