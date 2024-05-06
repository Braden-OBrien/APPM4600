import numpy as np
import matplotlib.pyplot as plt
import remez_poly as remez #credit to GitHub @DKenefake

f = lambda x: (np.e)**x

pts = np.linspace(-1, 1, 1000)