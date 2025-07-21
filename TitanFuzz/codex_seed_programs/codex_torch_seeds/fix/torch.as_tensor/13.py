'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data, dtype=None, device=None)
print(tensor)
'\nTask 4: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import numpy as np
array = np.array([[1, 2], [3, 4]])
tensor = torch.from_numpy(array)
print(tensor)
'\nTask 5: Call the API torch.eye\ntorch.eye(n, m=None, out=None)\n'
tensor = torch.eye(2, 3)
print(tensor)
'\nTask 6: Call the API torch.zeros\ntorch.zeros(size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
tensor = torch.zeros(2, 3)
print(tensor)