'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique_consecutive\ntorch.Tensor.unique_consecutive(_input_tensor, return_inverse=False, return_counts=False, dim=None)\n'
import torch
data = torch.rand(4, 3)
print(data)
print(torch.Tensor.unique_consecutive(data, return_inverse=False, return_counts=False, dim=None))