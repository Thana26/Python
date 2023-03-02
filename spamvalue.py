def do_twice(f,a):
 f(a)
 f(a)
def print_spam(a):
 print('Spam',a)
do_twice(print_spam,'Value')
