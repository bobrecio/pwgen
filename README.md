## PWGen: Formatted Password Generator ##
---
### Steps ###
1. Go to PWGen site.
2. Select word source (Upload file, paste URL, select existing list)
2. Set the password format. (segment editor / paste format string)
5. Generate multiple passwords based on format.
6. Run each password through strength meter.
7. Display list passwords with strength score. (Score is hyperlink to strength details - "strength-meter")
---
### Functions ###
  * mkWordList(file) - generate the wordlist_array[]
    * Remove top 5(?) occuring words. (Show these in showFilesStats().)
    * Remove single letter words.
    * Remove numbers and words with numbers.
  * buildPW(format) - concatenates the segments of the password by calling functions to create each segment based on "format".
  * parseFormat(string) - returns array of format. %2W@%4d ==> ["2W","@","4d"]
  * randomFormat - returns a random password format - for i= 1 to math.random(8) {% + [1234567890] + [aAMdwWsx]}
  * getWordOfLen(N) - returns a random word from the list with length "N". (N=null will be random length.) 
  * getNum(N) - selects a number with the N-length. (N=null will be random length.)
  * getChar(N) - returns random string of characters - length of N. (N=null will be random length.)
  * showFileStats() - Show stats of the word file - total/unique words, longest/shortest, top 5 words removed.
  * pwlist[{"pwd":"","strength":""},{...},...]
Notes:
* If format=NULL, random format will be returned.
* If N=NULL, random length will be returned.

---
### Form ###
* Word Source: 
  *  upload (text box/upload), 
  *  URL (textbox), 
  *  select (dropdown)
* Display File Stats
  * Unique/Total words: 
  * 5 most common:
  * Longest/Shortest
* Select Segments: Type (dropdown), Length
* [Add segment]
* Display password format (textbox) [default: %1W%1s%3d]
* Number of choices (textbox)
* [Generate Passwords]
* List of choices: Password, Strength (Raw), Copy Icon
* [Redo] [Reset]
Notes:
* Add Segment creates properly formatted segments - %NX
---
|char|type|example|description|
|:---:|:------------:|:-----:|:---------------------------|
|%|delimiter|%2x|
|a|lower-alpha|%5a|5 random lower-alpha characters|
|A|upper-alpha|%5A|5 random upper-alpha characters|
|M|mixed-case|%3M|3 random mixed-case characters|
|d|digits|%14d|15 random digits|
|w|word from uploaded file (lower-case)|%3w|3-letter word with all lower-case letters|
|W|word from uploaded file (upper-case)|%5w|5-letter word with all upper-case letters|
|T|word from uploaded file (title-case)|%w|random length word with first letter capitalized|
|s|symbol|%1s|single symbol/special character|
| \\ |literal|%\\\%|%|
|x|any characters|%14x|14 random characters of any type (a,A,M,d,w,W,s,x)|

Notes: 
* If number is missing or 0, random length is used.
---
__ Usage example __
> %5T%\\\.%4d%s%5x (1 5-letter title-case word + dot + 4 digits + 1 symbol + 5 random characters)

__ Result (possibly) __
> Hello.1234$eH&12
---
Test your passwords at http://www.passwordmeter.com/
