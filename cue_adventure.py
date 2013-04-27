## this is solustion to http://adventure.cueup.com/
import webbrowser


####Question 1 Start####
def VAXrand(seed):
    res = ((69069 * seed + 1) % (2 ** 32))
    return res


def firstn(seed, n):
    tempseed = seed  # starting seed
    res = 0  # store result

    for i in range(n):
        res = VAXrand(tempseed)
        print "Starting seed: %d, seed mod 36: %d, result: %d, result mod 36: %d" \
            % (tempseed, tempseed % 36, res, res % 36)
        tempseed = res


def Q1():
    import time
    print '############Question 1 Start############'
    print 'will open the webpage about VAXrand in your webbrowser in 3 seconds.'
    time.sleep(3)
    webbrowser.open('http://en.wikipedia.org/wiki/Linear_congruential_generator')
    firstn(6, 10)
    print '############Question 1 End############\n'
####Question 1 End####


####Question 2 Start####
def closeBracket(openbracket):
    if openbracket == '{':
        return '}'
    elif openbracket == '(':
        return ')'
    elif openbracket == '[':
        return ']'


def unmatch_bracket_finder(testcase):
    teststack = []
    position = 0
    failed_postision = []
    for c in testcase:
        if c == '{' or c == '(' or c == '[':
            #push the open character on the stack
            teststack.append(c)

        if c == '}' or c == ')' or c == ']':
            #check first to see if the stack is empty and
            #if it is report the position
            if not teststack:
                print "Failed at position %d" % position
                break
            #it's not empty, so pop the last appended character off
            f = teststack.pop()
            #if this character is the respective close character
            #of the character that got popped off, we're good
            if closeBracket(f) == c:
                print "All good at position %d" % position
            #if the popped character isn't the respective close
            #character, then fail and report position
            elif closeBracket(f) != c:
                print "Failed at position %d" % position
                failed_postision.append(position)
        # print teststack
        position = position + 1
    print "first unmatch at position %d" % failed_postision[0]


def Q2():
    print '############Question 2 Start############'
    testcase = ('{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}')
    unmatch_bracket_finder(testcase)
    print '############Question 2 End############\n'
####Question 2 End####


if __name__ == "__main__":
#question 1
    Q1()
#question 2
    Q2()
