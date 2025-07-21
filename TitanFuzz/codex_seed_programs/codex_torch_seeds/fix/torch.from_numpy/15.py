'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
x_numpy = np.array([0.1, 0.2, 0.3, 0.4])
x_torch = torch.from_numpy(x_numpy)
print(x_torch)
x_numpy = np.array([0.1, 0.2, 0.3, 0.4])
x_torch = torch.from_numpy(x_numpy)
print(x_torch)