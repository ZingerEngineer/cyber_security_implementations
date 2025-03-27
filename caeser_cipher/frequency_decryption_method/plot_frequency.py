import matplotlib.pyplot as plt
import sys

def plot_frequency(frequencyKeys,frequencyValues):
  plt.bar(frequencyKeys, frequencyValues)
  plt.grid(True, which='both', linestyle='--', linewidth=0.5)
  plt.show()

sys.modules[__name__] = plot_frequency