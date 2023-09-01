#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
random_value = np.random.uniform(1, 20, size=20)

reshaped_value = random_value.reshape(4, 5)
max_indices = np.argmax(reshaped_value, axis=1)
reshaped_array[np.arange(4), max_indices] = 0

print("Random Vector:")
print(random_value)

print("Reshaped Array (4x5):")
print(reshaped_array)


# In[ ]:





# In[ ]:





# In[ ]:




