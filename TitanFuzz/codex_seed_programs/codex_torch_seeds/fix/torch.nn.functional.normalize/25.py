'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
import numpy as np
import torch
data = np.array([[3, 4], [5, 6]])
data = torch.tensor(data, dtype=torch.float)
print(data)
torch.nn.functional.normalize(data, p=2.0, dim=1, eps=1e-12, out=None)
print(data)
torch.nn.functional.normalize(data, p=1.0, dim=1, eps=1e-12, out=None)
print(data)