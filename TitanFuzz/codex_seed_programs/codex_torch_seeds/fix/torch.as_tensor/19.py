'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
import numpy as np
data = np.array([[1, 2], [3, 4]])
tensor = torch.as_tensor(data)
print('tensor = ', tensor)
print('tensor.dtype = ', tensor.dtype)
print('tensor.device = ', tensor.device)