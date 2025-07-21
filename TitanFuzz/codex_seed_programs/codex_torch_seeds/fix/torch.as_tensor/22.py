'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
data = [[1, 2], [3, 4]]
tensor_data = torch.as_tensor(data, dtype=torch.float32)
print(tensor_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
data = np.array([[1, 2], [3, 4]])
tensor_data = torch.from_numpy(data)
print(tensor_data)