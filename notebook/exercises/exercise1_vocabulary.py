from itertools import product

keyboard = {
                    "2": "[abc]",  "3": "[def]",
    "4": "[ghi]",   "5": "[jkl]",  "6": "[mno]",
    "7": "[pqrs]",  "8": "[tuv]",  "9": "[wxyz]"
}

combos = [ "".join(i) for i in product(list("23456789"), repeat=4) ]
