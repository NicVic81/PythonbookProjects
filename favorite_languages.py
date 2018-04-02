from _collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

# Since we used the ordered dictionary class from the builtin module it will print the dictionary in the order we
# entered it.
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# You can still sort the ordered dictionary if you like.
for name, language in sorted(favorite_languages.items()):
    print(name.title() + "'s favorite language is " + language.title())
