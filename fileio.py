# use chardet to detect encoding of a file
# unicode sandwich, perform encode/decode while opening/closing the file. all the processing between open/close should be with strings.
# it's always better to explicitly mention encodings while opening the file, rather than relying on the system defaults
# often same looking strings have different byte representation in UTF, so it's better to normalize the text. There are simple ways to do the UTF normalization.
# similar concept is case folding - wherein you convert the unicode text to lowercase
# another trick is to remove diacritics(accents) so that it becomes ascii
# sorting internationalized text - use PyUCA library - else beware of the issues with sorted(fruits, key=locale.strxfrm)
# there are ways to get numeric values of Tamil/Devnagari unicode letters
# there are ways to support regexes on unicode characters
# 