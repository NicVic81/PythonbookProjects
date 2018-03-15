import pizza
# Or could use "from pizza import make_pizza" to import just that function from
# that module
# and then could call the function like normal such as
# make_pizza(16, 'pepperoni')
# Or could as also give the function an alias such as
# from pizza import make_pizza as mp and then could call it as
# mp(16, 'pepperoni')

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')