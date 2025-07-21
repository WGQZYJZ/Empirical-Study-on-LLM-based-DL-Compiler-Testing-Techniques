'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
import numpy as np
data = np.array([1, 2, 3])
tensor_data = torch.tensor(data)
print('tensor_data:', tensor_data)
'\nTask 4: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
data = np.array([1, 2, 3])
tensor_data = torch.tensor(data, dtype=torch.float64)
print('tensor_data:', tensor_data)
'\nTask 5: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
data = np.array([1, 2, 3])