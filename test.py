def my_func(**kwargs):
    """A function that shows how powerful **kwargs is"""
    first_arg = kwargs.get('first_arg', -1)

    if isinstance(first_arg, list):
        print "first_arg is a list"

    print "First_arg: "
    print "second_arg: ", kwargs.get('second_arg',-2)
    print "third_arg: ", kwargs.get('third_arg',-3)
    print "fourth_arg: ", kwargs.get('fourth_arg',-4)

    for i in xrange(101, 0, -3):
        print i

    pass

help(my_func)

my_func(first_arg=['a','b','c'],
        second_arg={'x': 3, 'y': 2,'z': 3})
