#! python3
# Given a quote, create an excerpt that is X characters long, but doesn't cut off the quote in the middle of a word. Add an ellipsis at the end so that people recognize the quote is incomplete.
# NOTE, you can use the regex in other languages, this is just a demo in python. Regex featured:
#   ----------------------
#   (\b\w+\b[\s\W]*){1,15}
#   ----------------------

import re

quote = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum, corporis quae nesciunt optio vero nihil repudiandae eligendi obcaecati earum tempora nisi, enim eos. Commodi alias beatae id rem debitis cum.

Culpa cupiditate debitis facere earum vitae ex aspernatur iusto. Neque numquam esse et hic id quas doloribus consequatur similique, sunt, adipisci vitae debitis a dolore tempora fugiat animi fuga qui.'''


def excerpt(quote):
	'''Change the number of words allowed in your excerpt by change the 15 in the range below ({1,15} gets the first to the fifteenth word)'''
	
    word_count = re.compile(
        r'(\b\w+\b[\s\W]*){1,15}'
        )

    return word_count.search(quote).group() + '...'

if __name__ == "__main__":
    # Print word-count restricted quote
    print(excerpt(quote), '\n\n\n')
