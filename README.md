## PWGen: Formatted Password Generator ##
---

### Steps ###
1. Go to PWGen site.
2. Select word source (Upload file, paste URL, select existing list)
2. Set the password format. (Use the segment builder / Paste in one of your premade password formats)
5. Generate multiple passwords based on format.
6. Run each password through strength meter.
7. Display list passwords with strength score. (Score is hyperlink to strength details - "strength-meter")
---
### Functions ###
  * `mkWordList(file)` - generate the wordlist_array[]
    * Remove top 5(?) occuring words. (Show these in `showFilesStats()`.)
    * Remove single letter words.
    * Remove numbers, words with numbers, special characters and words with special characters.
  * `buildPW(format)` - concatenates the segments of the password by calling functions to create each segment based on "format".
  * `parseFormat(string)` - returns array of format. %W2%\\\@%d4 ==> ["W2","@1","d4"]
  * `randomFormat` - returns a random password format.
  * `randomPW`- returns random password.
  * `getWordOfLen(N)` - returns a random word from the list with length "N".
  * `getNum(N)` - selects a number with the N-length.
  * `getChar(N)` - returns random string of characters - length of N.
  * `showFileStats()` - Show stats of the word file - total/unique words, longest/shortest, top 5 words removed.
  * `pwlist[{"pwd":"","strength":""},{...},{...}]`

Notes:
  * If format="", random format will be returned.
  * If N=NULL, 1 is assumed.
  * If N=0, random number between 1 and 5 is used.

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
* Select Segments: Type (dropdown), Length(textbox, spinner)
* [Add segment]
* Display password format (textbox) [default: %W1%s1%d3]
* Number of choices (textbox)
* [Generate Passwords]
* List of choices: Password, Strength (Raw), Copy Icon
* [Redo] [Reset]

Notes:
  * [Add Segment] creates properly formatted segments - %NX
---
## Segment Definitions: ##
* % is the segment delimiter.
* Properly formatted segment should be % followed by number then type => % + char + length.<br>
* If no number is provided for length, length of 1 is assumed.<br>
* If number is 0, random length between 1 and 5 is used.<br>

|char|type|example|description|
|:---:|:------------:|:-----:|:---------------------------|
|a|lower-alpha|%a5|5 random lower-alpha characters|
|A|upper-alpha|%A5|5 random upper-alpha characters|
|M|mixed-case|%M3|3 random mixed-case characters|
|d|digits|%d14|14 random digits|
|w|word from uploaded file (lower-case)|%w3|3-letter word with all lower-case letters|
|W|word from uploaded file (upper-case)|%W5|5-letter word with all upper-case letters|
|T|word from uploaded file (title-case)|%T0|random-length [1-5] word with first letter capitalized|
|s|symbol|%s|one symbol (aka special character)|
| \\ |literal|%\\\%|%|
|x|any characters|%x14|14 random characters of any type (a,A,M,d,w,W,T,s,x)|

---
__Usage example__
> %5T%\\\.%d4%s%x5 (Descripton: "1 5-letter title-case word + dot + 4 digits + random number of symbols + 5 random characters")

__Result (possibly)__
> Hello.1234$eH&12
---
Test your passwords at http://www.passwordmeter.com/
