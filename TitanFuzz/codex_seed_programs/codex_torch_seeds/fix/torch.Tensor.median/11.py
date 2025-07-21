'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
import numpy as np
input_tensor = torch.from_numpy(np.array([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]]))
print(input_tensor)
print(torch.Tensor.median(input_tensor, dim=0, keepdim=False))
print(torch.Tensor.median(input_tensor, dim=0, keepdim=True))
print(torch.Tensor.median(input_tensor, dim=1, keepdim=False))
print(torch.Tensor.median(input_tensor, dim=1, keepdim=True))