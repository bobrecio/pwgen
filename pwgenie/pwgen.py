# %% [markdown]
# # PWGenie app
# ---
#
# ### usage: pwgen(format-string-segments)
# - Returns 3 passwords based on the format string segments
# - see Usage section below for details

# %%
import random

symbols = "!@#$%^&*-+=.?~"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
mixed_case = alpha_upper + alpha_lower
anychar = mixed_case + digits + symbols

print('anychar() > ', anychar)

# %%


def getWord(type: str = "n", word_len: str = "5"):
    types = {
            "j": "adjs.txt",
            "b": "advs.txt",
            "1": "colors.txt",
            "3": "days.txt", 
            "2": "months.txt",
            "n": "nouns.txt",
            "v": "verbs.txt",
            "w": "words.txt"
             }
    type = 'n' if type not in types else type
    file = "./words/" + types[type]
    words = open(file, "r").readlines()
    words_list = []
    for this_word in words:
        # need to remove the \n at the end of each, but not last word in file
        word = this_word[:-1] if '\n' in this_word else this_word
        if type.isdigit() == False and len(word) == int(word_len):
            words_list.append(word)
        elif type.isdigit() == True:
            words_list.append(word)
    word_pick = random.choice(words_list)
    return (word_pick)


print('getWord("1", "5") > ', getWord("1", "5"))

# %%


def spell_number(numeral: str = ""):
    n = numeral if numeral != "" else str(random.choice(range(99)))
    spelled_number = ""

    nums_list = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens_list = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
                 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    try:
        spelled_number = nums_list[int(n)] if int(n) in nums_list else tens_list[int(
            n[0])] + "-" + nums_list[int(n[1])] if n[1] != "0" else tens_list[int(n[0])]
    except:
        spell_number = ""
    return (spelled_number)


print('spell_number("0") > ', spell_number("0"))

# %%


def part_num(pnum):
    # returns the int for the length of segment
    if len(pnum) <= 0:
        # set number to 1 if it's empty
        return (1)
    elif pnum == "0":
        # set random number btwn 3 an 8, if it's 0
        return (int(random.choice("345678")))
    else:
        return (int(pnum))

print('part_num(""), part_num("0"), part_num("99") > ', part_num(""), part_num("0"), part_num("99"))

# %%

def change_word_case(this_word, this_case: str = ""):
    if this_case in "ult":
        match this_case:
            case "u":
                # upper-case word
                return (this_word.upper())
            case "l":
                # lower-case word
                return (this_word.lower())
            case "t":
                # title-case word
                return (this_word.capitalize())
    else:
        return (this_word)


print('change_word_case("heLLo", "l")', change_word_case("heLLo", "l"))


def pwgen(pattern):

    pw = ""
    try:
        pattern_parts = [part for part in pattern.split('%')[1:]]
    except:
        print('Missing pattern parameter; try "%x14"')
    else:
        for part in pattern_parts:
            match part[0]:
                case "0":
                    # spelled number
                    if len(part) > 1:
                        requested_number = part[1:] if part[1].isdigit(
                        ) else part[2:]
                        number_case = "l" if part[1].isdigit() else part[1]
                    else:
                        requested_number = ""  # if number is not specified; returns random
                        number_case = "l"
                    this_spelled_number = change_word_case(
                        spell_number(requested_number), number_case)
                    pw += this_spelled_number
                case"\\":
                    # literal
                    pw += part[1:]
                case "a" | "A" | "M" | "m" | "s" | "d" | "x":
                    # character types
                    # TODO: make sure that there is only one letter, followed by number
                    for i in range(part_num(part[1:])):
                        match part[0]:
                            case "a":
                                # lower-alpha
                                pw += random.choice(alpha_lower)
                            case "A":
                                # upper-alpha
                                pw += random.choice(alpha_upper)
                            case "m" | "M":
                                # mixed-case alpha
                                pw += random.choice(mixed_case)
                            case "s":
                                # symbol
                                pw += random.choice(symbols)
                            case "d":
                                # digit
                                pw += random.choice(digits)
                            case "x":
                                # random any character
                                pw += random.choice(anychar)

                case "w" | "n" | "v" | "j" | "b" | "c":
                    # words
                    word_type = ""
                    if (len(part) == 1):
                        word_length = 5
                        word_case = "t"
                    elif part[1].isdigit() and part[0] != "c":
                        # if no word-case indicated
                        this_num = part[1:]
                        if int(this_num) > 20:
                            # limit to 20-char words
                            this_num = "20"
                        word_length = int(part_num(this_num))
                        word_case = "t"
                    elif part[0] == "c":
                        # custom lists; ex. c1, c1u
                        word_type = part[1:-
                                         1] if part[-1].isdigit() == False else part[1]
                        word_case = part[-1] if part[-1].isdigit() == False else "l"
                        word_length = 0

                    else:
                        # limit to 20-char words
                        this_num = "20" if int(part[2:]) > 20 else part[2:]
                        word_length = int(part_num(this_num))
                        word_case = part[1]

                    word_type = word_type if part[0] == "c" else part[0]

                    this_word = getWord(
                        word_type, word_length) if part[0] != "0" else spell_number(word_length)

                    pw += change_word_case(this_word, word_case)

    return (pw)


# print(pwgen("%jt4%\ %nt0%\: (%cu1%\)%d3%\-%d4"))
# print(pwgen("%nu3"))

# %%
print(pwgen("%jt4%nt0%\@%\.%d3%c1%cu2%cl3"))
print(pwgen("%jt4%\ %nt0%\: (%0u0%\)%d3%\-%d4"))

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
# |0|spelled number (1-2 digits)|0l33, 00, 0|thirty-three (lower case), zero, (random)
# |x|any characters|%x14|14 random characters of any type|
# |wl|word (lower-case)|%wl3|3-letter word with all lower-case letters|
# |wu|word (upper-case)|%wu5|5-letter word with all upper-case letters|
# |wt|word (title-case)|%wt0|5-letter word with first letter capitalized|
# |nl, nu, nt|noun (upper-, lower-, title-case)|||
# |vl, vu, vt|verb (upper-, lower-, title-case)|||
# |jl, ju, jt|adjective (upper-, lower-, title-case)|||
# |bl, bu, bt|adverb (upper-, lower-, title-case)|||
# |cl1, cu1, ct1|custom 1: random color|%cl1|purple (lower-case)|
# |cl2, cu2, ct2|custom 2: random month word|#cu2|MARCH (upper-case)|
# |cl3, cu3, ct3|custom 3: random day word|%ct3|Wednesday (title-case)|
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
