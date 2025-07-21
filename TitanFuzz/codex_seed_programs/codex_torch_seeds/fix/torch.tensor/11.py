'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
data = [1, 2, 3, 4]
tensor = torch.tensor(data)
print(tensor)
'\nTask 4: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
tensor = torch.as_tensor(data)
print(tensor)
'\nTask 5: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import numpy as np
tensor = torch.from_numpy(np.array(data))
print(tensor)