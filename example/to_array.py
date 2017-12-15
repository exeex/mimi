from mimi import generator
import matplotlib.pyplot as plt

# get random tab and append to midi track

tab = generator.get_random_tab(tempo=70)

array = tab.to_array()

print(array.shape)

# piano roll
plt.imshow(array[:,:,0])

# onset event
plt.imshow(array[:,:,1])