#terminal output is:


#[-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
# -1.         -1.         -1.         -1.        ]
#[-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
# -1.         -1.         -1.         -1.        ]

import numpy as np

h = 0.01*2.**(-np.arange(0, 10))

fwd_diff = (np.cos((np.pi/2)+h) - np.cos(np.pi/2))/h

ctd_diff = (np.cos((np.pi/2)+h) - np.cos((np.pi/2)-h))/(2*h)

print(fwd_diff)
print(ctd_diff)
