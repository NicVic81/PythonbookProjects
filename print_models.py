import printing_functions as pf

printed_models = []
needs_printing = ['iphone case', 'dildo', 'anal beads']

pf.print_models(needs_printing, printed_models)
pf.show_completed_models(printed_models)

# or

import printing_functions

printed_models = []
needs_printing = ['iphone case', 'dildo', 'anal beads']

printing_functions.print_models(needs_printing, printed_models)
printing_functions.show_completed_models(printed_models)

# or

from printing_functions import print_models, show_completed_models

printed_models = []
needs_printing = ['iphone case', 'dildo', 'anal beads']

print_models(needs_printing, printed_models)
show_completed_models(printed_models)

# or

from printing_functions import print_models as pm, show_completed_models as scm

printed_models = []
needs_printing = ['iphone case', 'dildo', 'anal beads']

pm(needs_printing, printed_models)
scm(printed_models)

# or

from printing_functions import *

printed_models = []
needs_printing = ['iphone case', 'dildo', 'anal beads']

print_models(needs_printing, printed_models)
show_completed_models(printed_models)