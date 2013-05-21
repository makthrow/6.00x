def rem(x, a):
   """
   x: an integer argument
   a: an integer argument

   returns: integer, the remainder when x is divided by a.
   """
   if x == a:
      print "x: %r, a: %r" % (x, a)
      return 0
   elif x < a:
      print "x: %r, < a: %r" % (x, a)
      return x
   else:
      print "x:%r, a:%r" % (x, a)
      rem(x-a, a)

rem(2,5)
rem(5,5)
rem(7,5)

