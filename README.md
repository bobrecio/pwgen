pwgen
=====
__Formatted Password Generator__

Steps:
1. Go to PWGen site.
2. Configure formatting
3. Select word source (Upload, URL, existing word list)
4. Parse uploaded/URL word sources to create a list - one word per line.
5. Generate multiple passwords based on format.
6. Run each password through strength meter.
7. Display list passwords with strength score. (Score is hyperlink to strength details - "strength-meter")

Functions:
  * mkWordList(file) - generate the wordlist_array[]
    * Remove top 5(?) occuring words. (Show these in showFilesStats().)
    * Remove single letter words.
    * Remove numbers and words with numbers.
  * buildPW(format) - concatenates the segments of the password by calling functions to create each segment based on "format".
  * getWordOfLen(N) - returns a random word from the list with length "N". (N=null will be random length.) 
  * getNum(N) - selects a number with the N-length. (N=null will be random length.)
  * getChar(N) - returns random string of characters - length of N. (N=null will be random length.)
  * showFileStats() - Show stats of the word file - total/unique words, longest/shortest, top 5 words removed.

Form:
* Word Source: upload (text box/upload), URL (textbox), select (dropdown)



[ ] Format a single password segment using [delimiter][number of digits/chars][type of segment]: %15d = 15 digits<br>
[ ] Parse a password formatting string and produce a password<br>
[ ] Test new password strength, display strength rating.

|char|type|example|description|
|:---:|:------------:|:-----:|:---------------------------|
|%|delimiter|%2x|
|a|lower-alpha|%5a|5 random lower-alpha characters|
|A|upper-alpha|%5A|5 random upper-alpha characters|
|M|mixed-case|%3M|3 random mixed-case characters|
|d|digits|%14d|15 random digits|
|w|word from uploaded file|%3w|3-letter word from uploaded file|
|W|word with title-case|%w|one word with first letter capitalized|
|s|symbol|%1s|single symbol/special character|
|x|any characters|%14x|14 random characters of any type (%,a,A,M,d,w,W,s,x)|

NOTE: To insert a '%' in the password, use '%%'.

Usage example:
> %5W.%4d%s%5x (1 5-letter title-case word + dot + 4 digits + 1 symbol + 5 random characters)

Possible result:
> Hello.1234$eH&12

Test your passwords at http://www.passwordmeter.com/
