**Methods**

texts:
* `text.concordance("")` :        shows every occurrence of a given word, together with some context.
* `text.similar("")` :            shows other words appearing in a similar range of contexts.
* `text.common_contexts([""])` :  allows to examine just the contexts that are shared by two or more words.
* `text.dispersion_plot(["", "", ..])` :  allows to examine just the contexts that are shared by two or more words.
* `text.count("")`:               returns the count of how often a word occurs in a text.

lists:
* `list.index("")`:               returns the index of the (first occurency of an) item.
* `list.append("")`:              adds an item at the end of the list.

sets:
* `set(a).union(set(b))`:         returns a new set with elements from both s and t: `a | b`.
* `set(a).intersection(set(b))`:  returns a new set with elements common to a and b: `a & b`.
* `set(a).difference(set(b))`:    returns a new set with elements in a but not in b: `a - b`.

**Functions**

* `len(text)` :                   returns the length of something. (A token is the technical name for a sequence of characters.)
* `sorted(text)` :                returns a list with all occurencies.
* `set(text)` :                   returns a list with all the unique occurencies.
* `type(text)` :                  returns the type of the element.
* `enumerate(text)` :             returns a tuple containing a count and the values obtained from iterating over sequence.

* `list()` :                      instantiates a `list` object.
* `tuple()` :                     instantiates a `tuple` object.

* `all(b for x in a)` :           evaluates to `True` if all items in b are in the iterable a.
* `any(y in b for x in a)` :      evaluates to `True` if any item y in b is in the iterable a.
