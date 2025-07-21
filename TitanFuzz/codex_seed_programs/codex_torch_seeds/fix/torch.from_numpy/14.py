'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
y = torch.from_numpy(x)
print(y)