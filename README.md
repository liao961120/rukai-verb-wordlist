
## English Wordlist Source

<https://github.com/felixfischer/categorized-words/blob/master/README.md>

**Clean list of ~90k english words divided into seven categories. Useful for
e.g. generation of memorable, pseudo-semantical passphrases or human-friendly
identifiers.**

### About

This package is basically just a jsonified and slightly cleaned version of the
[`2of12id.txt` wordlist](wordlist/alt12dicts/2of12id.txt) (as of 3 May 2016) from
[The Unofficial Alternate 12 Dicts Package](http://wordlist.aspell.net/12dicts/)
of the [SCOWL (Spell Checker Oriented Word Lists)](http://wordlist.aspell.net/)
project.

> The 2of12id.txt file, in the alternative version of 12Dicts, is the primary
> source of part-of-speech and inflection information, however it is limited to
> common words.

*— Description from [wordlist.aspell.net](http://wordlist.aspell.net/)*

#### Modifications

I have removed from the original file all entries that were somehow marked as
special, leaving in **only regular, non-hyphenated words consisting solely of
characters `a-z`** which should also not be totally obscure.

No censoring or other content-based cleaning has been applied. Please use this
source at your own discretion and expect it to contain profane words.

### Contents

|  Key  | Word class               | Size      |
|:-----:|:-------------------------|----------:|
| **N** | noun                     |     47004 |
| **V** | verb                     |     31232 |
| **A** | adjective                |     14903 |
| **I** | interjection             |       188 |
| **C** | conjunction/preposition  |       139 |
| **P** | pronoun                  |        78 |
| **S** | spoken contraction       |         9 |
|       | **Total of all classes** | **93553** |
