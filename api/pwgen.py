# %% [markdown]
# # PWGEN app
# ---
# 
# ### usage: pwgen(format-string-segments)
# - Returns a password based on the format string segments
# - see Usage section below for details

# %%
import random

symbols = "!@#$%^&*-+=.?~"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
mixed_case = alpha_upper + alpha_lower
anychar = mixed_case + digits + symbols

print(anychar)

# %%
def getWord(type: str="n", word_len: int = 5):
    types = {"n":"nouns.txt", "v":"verbs.txt", "j":"adjs.txt", "b":"advs.txt", "w":"words.txt"}
    file = "./words/" + types[type]
    words = open(file, "r").readlines()
    words_with_len = []
    for word in words:
        if len(word[:-1]) == word_len:
            words_with_len.append(word[:-1])
    word_pick = random.choice(words_with_len)
    return(word_pick)

print(getWord("j"))

# %%
def part_num(pnum):
    if len(pnum) <= 0: 
        #set number to 1 if there is no number
        return(1)
    elif pnum == "0": 
        #set random number btwn 3 an 9, if it's 0
        return(int(random.choice("3456789")))
    else:
        return(int(pnum))

print(part_num(""), part_num("0"), part_num("99"))

# %%
def pwgen(pattern):
    
    pw = ""
    try:
        pattern_parts = [part for part in pattern.split('%')[1:]]
    except:
        print('Missing pattern parameter; try "%x14"')
    else:
        for part in pattern_parts:
            match part[0]:
                case"\\":
                    #literal
                    pw += part[1:]
                case "a"|"A"|"M"|"m"|"s"|"d"|"x":
                    # character types
                    #TODO: make sure that there is only one letter, followed by number
                    for i in range(part_num(part[1:])):
                        match part[0]:
                            case "a":
                                #lower-alpha
                                pw += random.choice(alpha_lower)
                            case "A": 
                                #upper-alpha
                                pw += random.choice(alpha_upper)
                            case "m" | "M":
                                #mixed-case alpha
                                pw += random.choice(mixed_case)
                            case "s":
                                #symbol
                                pw += random.choice(symbols)
                            case "d":
                                #digit
                                pw += random.choice(digits)
                            case "x":
                                #random any character
                                pw += random.choice(anychar)
                case "w" | "n" | "v" | "j" | "b":
                    #words
                    if (len(part) == 1):
                        word_length = 5
                        word_case = "t"
                    elif part[1].isdigit():
                        this_num = part[1:]
                        if int(this_num) > 20:
                            # limit to 20-cahr words
                            this_num = "20"
                        word_length = int(part_num(this_num))
                        word_case = "t"
                    else:
                        this_num = part[2:]
                        if int(this_num) > 20:
                            # limit to 20-char words
                            this_num = "20"
                        word_length = int(part_num(this_num))
                        word_case = part[1]

                    this_word = getWord(part[0], word_length)
                        
                    match word_case:
                        case "t":
                            #title-case word
                            pw += this_word.capitalize()
                        case "u":
                            #upper-case word
                            pw += this_word.upper()
                        case "l":
                            #lower-case word
                            pw += this_word.lower()

    return(pw)

print(pwgen("%jt4%\ %nt0%\: (%d3%\)%d3%\-%d4"))

# %%
for i in range(5):
    # words (type+case+length)
    #   type(required): n=noun; v=verb; j=adjective; b=adverb
    #   case: u=UPPER, l=lower, t=Title(default)
    #   length: 1-14, 0=random, default=5
    # characters (type+length)
    #   type(required): a=lower-letter; A=UPPER-letter; m/M=Random Mixed Case letter; d=digit; s=symbol; x=any characters (mixed + symbols + digits)
    #   length: 1-??; default=5; 0=random
    # literal (\+char/string)
    print(pwgen("%jt4%\.%nt0%\@%d3%\.%d3"))

# %% [markdown]
# ## USAGE
# pwgen(format-string-segments)
# - Format string is made up of multiple segment representing parts of the desigred password
# - `%` starts each segment
# - Words (nouns, verbs, adjectives, adverbs)
#     - Case can be designated; default is Title-case, if not given
#     - Word length can be specified; default is 5, if not given
# - Characters (letters, digits, symbols)
#     - Number of characters can be designated; default is 1, if not given
# - Literal
#     - Can be any character or string
# 
# ---
# |char|type|example|description|
# |:---:|:------------:|:-----:|:---------------------------|
# |a|lower-alpha|%a5|5 random lower-alpha characters|
# |A|upper-alpha|%A5|5 random upper-alpha characters|
# |M or m|mixed-case|%M3|3 random mixed-case characters|
# |d|digits|%d14|14 random digits|
# |s|symbol|%s|5 (default) symbol (aka special character)|
# | \\ |literal char/string|%\hello!|produces hello!|
# |x|any characters|%x14|14 random characters of any type|
# |wl|word (lower-case)|%wl3|3-letter word with all lower-case letters|
# |wu|word (upper-case)|%wu5|5-letter word with all upper-case letters|
# |wt|word (title-case)|%wt0|5-letter word with first letter capitalized|
# |nl, nu, nt|noun (upper-, lower-, title-case)|||
# |vl, vu, vt|verb (upper-, lower-, title-case)|||
# |jl, ju, jt|adjective (upper-, lower-, title-case)|||
# |bl, bu, bt|adverb (upper-, lower-, title-case)|||
# 
# ---
# __Usage example__
# > `%\wt3.%jl4%nt0%s%d3"`
# 
# |Segment|Descripton|
# |---|---|
# |%\wt3.|literal string 'wt3.'|
# |%jl4|adjective, lower-case, 4-letters long|
# |%nt0|noun, title-case, random length|
# |%s|random symbol, 1 character(default)|
# |%d3|drandom digits, 3 digits long|
# 
# __Example of results__
# 1. > `wt3.russStonks(856`
# 2. > `wt3.bentCue~570`
# 3. > `wt3.pertStubbed*699`
# 4. > `wt3.airyWaftures!570`
# 5. > `wt3.inbyPraxis~675`
# 
# 
# ---
# Test your passwords at http://www.passwordmeter.com/


