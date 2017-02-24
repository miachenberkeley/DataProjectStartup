dictionnaire = {}
nb_premier = [1,3,5,11,13]
for i, word in enumerate(['{','[','(']):
    dictionnaire[word] = nb_premier[i]

for i, word in enumerate(['}',']',')']):
    dictionnaire[word] = 2 * nb_premier[i]

def is_matched(expression):
    n = len(expression)
    if n%2 != 0:
        return False
    #print(n)
    if n != 0:
        if dictionnaire[expression[0]] * 2 != dictionnaire[expression[n-1]]:
            return False
        else:
            expression = expression[1:n - 1]
            return is_matched(expression)
    else:
        return True


print(is_matched("{()}"))
print(is_matched("[{()}]"))
print(is_matched("[{()}"))
print(is_matched('{{[[(())]]}}'))
print(is_matched('{[(])}'))

print(is_matched("[{()]]"))

