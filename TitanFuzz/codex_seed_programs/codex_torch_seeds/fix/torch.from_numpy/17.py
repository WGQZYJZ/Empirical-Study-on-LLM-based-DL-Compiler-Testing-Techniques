'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
ndarray = np.random.rand(2, 3)
tensor = torch.from_numpy(ndarray)
print('tensor:', tensor)