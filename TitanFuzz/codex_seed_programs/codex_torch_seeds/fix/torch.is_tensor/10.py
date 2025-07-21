'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
import numpy as np
a = np.array([1, 2, 3, 4])
b = torch.tensor([1, 2, 3, 4])
c = torch.Tensor([1, 2, 3, 4])
d = torch.FloatTensor([1, 2, 3, 4])
print(torch.is_tensor(a))
print(torch.is_tensor(b))
print(torch.is_tensor(c))
print(torch.is_tensor(d))