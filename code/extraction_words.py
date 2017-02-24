from library import clean_text_simple, terms_to_graph
from nltk.corpus import stopwords

import xlsxwriter
from os import listdir

path_to_data = "/Users/chen/Desktop/DataProject/techcrunch data/"

stpwds = stopwords.words('english')

#extract key words
key_words_gow = {}
counter = 0

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('extraction_keywords.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,"name of file")
worksheet.write(0,1,"key words")


##########
# gow #
##########

for f in listdir('/Users/chen/Desktop/DataProject/techcrunch data/'):

    worksheet.write(counter+1, 0, f)

    file = open('/Users/chen/Desktop/DataProject/techcrunch data/' + f, "r")

    review = file.read()
    # pre-process document
    try :
        my_tokens = clean_text_simple(review)
    except :
        print "info", review
        #print "my_tokens", my_tokens
        worksheet.write_row(counter + 1, 1,  my_tokens)
        worksheet.write(counter + 1, 2,  "il y a une erreur")


    if len(my_tokens) == 0:
        pass
    elif len(my_tokens) == 1:
        keywords = my_tokens
        worksheet.write(counter + 1, 1,  keywords)

    else :

        w = min(len(my_tokens),4)
        #print "w", w
        g = terms_to_graph(my_tokens, w)

        # decompose graph-of-words
        core_numbers = dict(zip(g.vs['name'], g.coreness()))
        #print "core_numbers", core_numbers

        max_c_n = max(core_numbers.values())
        keywords = [kwd for kwd, c_n in core_numbers.iteritems() if c_n == max_c_n]
        #print(keywords)
        worksheet.write_row(counter + 1, 1, keywords)
        # save results



    counter += 1
    if counter % 100 == 0:
        print counter, 'body processed'

